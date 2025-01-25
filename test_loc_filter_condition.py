# test_loc_filter_condition.py

import pandas as pd

# 建立資料框
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dennis'], 'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

# 測試：使用條件篩選資料
result = df.loc[df['Age'] > 25]
print("測試結果：")
print(result)
# 輸出：
#       Name  Age
# 1      Bob   30
# 2  Charlie   35