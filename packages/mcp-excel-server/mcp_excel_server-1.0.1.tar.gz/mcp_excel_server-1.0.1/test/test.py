import pandas as pd
import numpy as np

# 创建一个示例数据集
np.random.seed(42)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 75000, 90000, 100000],
    'Department': ['HR', 'Sales', 'IT', 'Marketing', 'Finance']
}

df = pd.DataFrame(data)
df.to_excel('sample_data.xlsx', index=False)