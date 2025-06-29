import pandas as pd

table_zh_cn = pd.read_csv(r"chinese/中文new.csv",encoding="gbk")
table_en = pd.read_csv(r"english/english_info.csv",encoding="gbk")

data = []

for z,e in zip(table_zh_cn.values,table_en.values):
    base_label = z[1] + ("" if pd.isna(z[3]) else z[3])
    base_name_zh = z[2]
    base_name_en = e[2]
    for i,j,k in zip(z[5::2],e[5::2],z[6::2]):
        if not pd.isna(i):
            label = base_label + ("" if pd.isna(k) else k)
            data.append({"中文名":'-'.join((base_name_zh,i)),"Engilsh Name":'-'.join((base_name_en,j)),"标签/Label":label})

data = pd.DataFrame(data)
data = data.sort_values(by="标签/Label")

print(data)

data.to_csv("Name Label Comparison.csv", index = False, encoding = "gbk")