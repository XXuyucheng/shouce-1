# pandas玩转excel

## 创建读取

### 创建excel文件

- 码创建一个excel文件

```python
import pandas as pd
df = pd.DataFrame()
# 将df作为一个pd的数据表。
df.to_excel('C:/Users/子耀/Desktop/try.xlsx')
# 将df作为excel格式保存
print('done')
```

> 注意需要覆盖原数据表使在```py print('done!')```don后加一个感叹号

- 其中要给数据表家入数据如下

```py
df = pd.DataFrame({'ID':[1,2,3],'Name':['Tom','Tim','Ros']})
```

>但是注意次是索引并不是ID列要创建索引如下

```py
df = df.set_index('ID')
```

### 导入excel文件为dataframe

- read one excel to dataframe

```py
df = pd.read_excel('D:/趣加/业务收支表2023.xlsx')
```

- 常用代码

```py
print(df.shape)#计算数据行列
print(df.columns)#给出数据字段也就是每列抬头
print(df.head(1))#默认前五行
print('======================')
print(df.tail(2))#打印后两行
```

### 正确的导入（部分数据清洗）

#### header

- 脏header第一行无效

```py
df = pd.read_excel('D:/趣加/业务收支表2023.xlsx',header=1)
```

- 第一行空无影响

>`Traceback (most recent call last):
  File "d:\趣加\数据分析leaning\python pandas leaning\tyr1\try2.py", line 8, in <module>
    df = df.set_index['团队编号']个错误`提示的意思是在尝试对一个方法（method）对象进行下标操作（subscriptable），但方法对象不支持下标操作。具体来说，这里的set_index是一个方法，而不是一个可被下标索引的对象。可能是在调用set_index方法时，使用了[]而不是()，导致了此错误。为了解决这个问题，应该使用括号而不是方括号来调用set_index方法。正确的代码应该是df = df.set_index('团队编号')

- 将索引序列改为ID或编号

```py
df.set_index('团队编号',inplace=True)
```

```py
df = df.set_index('团队编号')
```

- 但是第二次读取的时候索引列还是回自动生成且导出的时候还是会有一个索引列在表格中

```py

```

### 创建数据

#### 创建序列

1. 创建序列series

```s1 = pd.Series(d)```

```py
d = {'x':1,'y':2,'z':3}#字典
s1 = pd.Series(d)
print(s1.index)
```

>这个序列会自动将py中的字典键值对的键作为index

也可以直接设置一个series的index和value

```py
L1 = [1,2,3]
L2 = ['a','s','d']
s1 = pd.Series(L1,index=L2)
```

```s1 = pd.Series([1,2,3],index=['a','s','d'])```
>直接生成
>> 注意序列没有行列之分且每个序列都有一个title也就是```name```

2. 将series放入dataframe中

- 将序列做一个列放入行列dataframe中

```py
a1 = pd.Series([1,2,3],index=['1','2','3'],name='A')
a2 = pd.Series([11,22,33],index=['1','2','3'],name='B')
a3 = pd.Series([111,222,333],index=['2','3','4'],name='C')
df = pd.DataFrame({a1.name:a1,a2.name:a2,a3.name:a3})
```

- 以list形式序列就会成为行加入
```df = pd.DataFrame([a1,a2,a3])```

> **有意思的时这里是将每个序列中index形同的对齐**
> 如果没有对应值就会成为NaN