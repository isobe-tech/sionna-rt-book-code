#!/usr/bin/env python3
"""Notebook の JSON 妥当性・構文・未定義名を検査する。

各 Notebook は「準備セル → 本文の掲載コード」の順に並んでいる。上から順に実行
できることを保証したいので、コードセルを順に連結したうえで、トップレベルで
未定義のまま使われる名前が無いかまで見る。実行はしない（Sionna RT と
LLVM/CUDA バックエンドが要るため）。
"""

import ast
import builtins
import json
import sys
from pathlib import Path

BUILTIN = set(dir(builtins)) | {"__file__", "get_ipython"}


class Scope(ast.NodeVisitor):
    """トップレベルで未定義のまま使われる名前を集める。"""

    def __init__(self):
        self.bound = set()
        self.free = []

    def _bind(self, node):
        for t in ast.walk(node):
            if isinstance(t, ast.Name):
                self.bound.add(t.id)

    def visit_Import(self, n):
        for a in n.names:
            self.bound.add((a.asname or a.name).split(".")[0])

    def visit_ImportFrom(self, n):
        for a in n.names:
            self.bound.add(a.asname or a.name)

    def visit_FunctionDef(self, n):
        self.bound.add(n.name)
        for a in n.args.args + n.args.kwonlyargs:
            self.bound.add(a.arg)
        self.generic_visit(n)

    def visit_ClassDef(self, n):
        self.bound.add(n.name)
        self.generic_visit(n)

    def visit_Lambda(self, n):
        for a in n.args.args:
            self.bound.add(a.arg)
        self.generic_visit(n)

    def visit_arg(self, n):
        self.bound.add(n.arg)

    def visit_ExceptHandler(self, n):
        if n.name:
            self.bound.add(n.name)
        self.generic_visit(n)

    def visit_comprehension(self, n):
        self.visit(n.iter)
        self._bind(n.target)
        for f in n.ifs:
            self.visit(f)

    def visit_For(self, n):
        self.visit(n.iter)
        self._bind(n.target)
        for b in n.body + n.orelse:
            self.visit(b)

    def visit_With(self, n):
        for item in n.items:
            self.visit(item.context_expr)
            if item.optional_vars:
                self._bind(item.optional_vars)
        for b in n.body:
            self.visit(b)

    def visit_Name(self, n):
        if isinstance(n.ctx, ast.Store):
            self.bound.add(n.id)
        elif n.id not in self.bound and n.id not in BUILTIN:
            self.free.append(n.id)


# Both editions live in this repository. Check them both, so the English
# notebooks do not slip past CI.
NOTEBOOK_DIRS = ("notebooks", "notebooks_en")


def main() -> None:
    notebooks = []
    for directory in NOTEBOOK_DIRS:
        notebooks.extend(sorted(Path(directory).glob("*.ipynb")))
    if not notebooks:
        raise SystemExit("No notebooks found")

    failed = 0
    for path in notebooks:
        with path.open(encoding="utf-8") as stream:
            notebook = json.load(stream)

        cells = []
        for index, cell in enumerate(notebook.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            source = cell.get("source", "")
            if isinstance(source, list):
                source = "".join(source)
            compile(source, f"{path}:cell-{index}", "exec")
            cells.append(source)

        if not cells:
            print(f"ng: {path}: コードセルが無い")
            failed += 1
            continue

        scope = Scope()
        for node in ast.parse("\n".join(cells)).body:
            scope.visit(node)
        if scope.free:
            print(f"ng: {path}: 未定義の名前 {sorted(set(scope.free))}")
            failed += 1
            continue

        print(f"ok: {path} ({len(cells)} code cells)")

    if failed:
        raise SystemExit(f"{failed} notebook(s) failed")


if __name__ == "__main__":
    main()
