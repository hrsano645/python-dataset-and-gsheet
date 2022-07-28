# python-dataset-and-gsheet

python+dataset+gsheetでgoogle spreadsheetのデータベース化テスト

## 速度テスト

```
# 4秒ぐらい
python -m cProfile -s "tottime" ./sqlalchemy_gsheet_select.py > profile_sqlalchemy.txt

# 19秒ぐらい
python -m cProfile -s "tottime" ./dataset_gsheet_select.py > profile_dataset.txt 
```
