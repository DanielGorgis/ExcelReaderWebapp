import pandas as pd
import xlrd
import xlsxwriter
import numpy as np


df = pd.read_excel('dummy dummy dummy.xlsx', sheet_name='Sheet1')

some_List = df['Blueprint']

some_stringList = []

for i in some_List:
    some_stringList.append(str(i))



if '22222' in some_stringList[556]:
    print('It is in the list')