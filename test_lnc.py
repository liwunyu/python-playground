import pandas as pd

# 建立資料框
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# 測試：取得特定行和列的值
value = df.loc[2, 'Name']
print("測試結果：", value)
# 輸出：Charlie