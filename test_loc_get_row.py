# test_loc_get_row.py

import pandas as pd

# 建立資料框
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# 測試：根據行標籤取得資料
print("測試結果：")
print(df.loc[1])
