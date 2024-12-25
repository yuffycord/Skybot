# Skybot Fix

APIで401が出る問題を修正したSkybotです。401エラーが出る人は試してみてください。

## 使い方

```sh
git clone https://github.com/yuffycord/Skybot
cd Skybot
pip install -r requirements.txt
python start.py
```
> [!WARNING]
> SkybotAIO のレポジトリにあるrequirements.txt使ったらpy-cordのバージョンの関係でエラー吐くのでこっち使ってください
> .envは変更するようにしてください（TOKEN=discordtoken)

## Skybotとの違い

- [x] sky.shiiyu.moe の API で 401 が出る問題を修正
- [x] value コマンド以外を削除
- [x] requirements.txt の py-cord のバージョンを修正  