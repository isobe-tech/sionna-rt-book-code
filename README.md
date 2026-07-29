# Sionna RTによる電波伝搬レイトレーシング入門 サンプルコード

書籍『Sionna RTによる電波伝搬レイトレーシング入門』に対応する、章別Jupyter Notebookと補助シーンを公開するリポジトリです。

## 対象環境

- Python 3.11
- Sionna RT 2.0.1
- Jupyter Notebook / JupyterLab

Sionna RTのAPIは更新で変わる可能性があります。本書と同じ手順を再現する場合は、付属の`environment.yml`を使用してください。最新環境へ移行する場合は、[Sionna公式ドキュメント](https://nvlabs.github.io/sionna/)も確認してください。

## セットアップ

```bash
git clone https://github.com/isobe-tech/sionna-rt-book-code.git
cd sionna-rt-book-code
conda env create -f environment.yml
conda activate sionna-rt-book
jupyter lab
```

Notebookは**リポジトリのルートを作業ディレクトリとして**実行してください。本書のコードは`scenes/indoor_apartment/scene.xml`や`figs/ch06/`のように、ルートからの相対パスで書かれています。生成した図は`figs/chXX/`へ保存されます。

## Notebookの構成

各Notebookは、本書に印刷したコードを**掲載順にそのまま**並べたものです。コードセルの中身は書籍の本文と一字一句同じで、節見出しがそのまま Markdown セルの見出しになっています。

先頭の「準備」セルだけは本文に印刷していません。本文のコードが前提にしている import とシーンの読み込みをここでまとめて済ませてあり、これを実行すれば以降は上から順に実行できます。

本書が説明のために示している断片（自分で作ったシーンのパスや、そのシーンには無い物体名を使う例）はそのままでは動きません。該当するセルの前に注記を置いてあります。

Notebookは、本文の掲載コードと対応するように管理しています。

## 章別Notebook

| 章 | 内容 | Notebook |
|---:|---|---|
| 2 | 環境構築と動作確認 | `ch02_install_check.ipynb` |
| 3 | 基礎的なレイトレーシング | `ch03_basic_ray_tracing.ipynb` |
| 4 | CIR、CFR、チャネルタップ、到来角 | `ch04_cir_cfr_taps.ipynb` |
| 5 | 電波マップ | `ch05_radio_map_basic.ipynb` |
| 6 | シーンと可視化 | `ch06_visualization.ipynb` |
| 7 | 材料モデルと反射・透過 | `ch07_materials.ipynb` |
| 8 | 回折 | `ch08_diffraction.ipynb` |
| 9 | 散乱 | `ch09_scattering.ipynb` |
| 10 | 移動体チャネルとドップラー | `ch10_mobility_doppler.ipynb` |
| 11 | シーンの作成と編集 | `ch11_scene_editing.ipynb` |
| 13 | アンテナと偏波 | `ch13_antenna_polarization.ipynb` |
| 14 | アレーアンテナとビーム制御 | `ch14_array_beam_control.ipynb` |
| 15 | 屋内Wi-Fi | `ch15_indoor_wifi.ipynb` |
| 16 | 都市部5G・ミリ波 | `ch16_urban_5g_mmwave.ipynb` |
| 17 | 道路環境とV2X | `ch17_v2x_road_environment.ipynb` |
| 18 | 計算速度・精度・検証 | `ch18_validation.ipynb` |

第12章はBlender、OpenStreetMap、外部3Dデータの変換手順を扱うため、対応Notebookはありません。

## 実行上の注意

- 電波マップの計算時間とメモリ使用量は、シーン、セルサイズ、送信サンプル数、最大反射回数に依存します。
- 最初はセルを粗くし、送信サンプル数を減らして動作確認してください。
- GPUは必須ではありません。実際に選択されたMitsuba variantは`mitsuba.variant()`で確認できます。
- 第15章は`scenes/indoor_apartment/`の自作シーンを使用します。間仕切りを足した派生シーンはNotebookの実行時に生成されます。
- 出力セルは保存していません。実行して結果を得てください。

## 誤植・問題の報告

コードの不具合、書籍との不一致、実行環境に関する情報は[Issues](https://github.com/isobe-tech/sionna-rt-book-code/issues)へ登録してください。報告時はPython、Sionna RT、Mitsuba、Dr.Jitのバージョンと、使用OSを記載してください。

## ライセンス

このリポジトリのコードは[MIT License](LICENSE)で公開します。Sionna RTおよび同梱シーン・外部データには、それぞれのライセンスが適用されます。

本リポジトリはNVIDIAによる公式リポジトリではありません。
