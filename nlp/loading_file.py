import xlrd
import s

dataname = r'../based/04-08Excel/14.xlsx'
# 读取地址文件名确定的excel文件
data = xlrd.open_workbook(filename=dataname)
# 读取工作sheet，（）内从0开始代表1...
sheet1 = data.sheet_by_index(0)
# 读取第（）列的信息，（）内从0开始代表1...
summary_set = sheet1.col_values(5)
# 获取user_id_set的值的数量（列表长度）
summary_len = len(summary_set)

for i in summary_set:
    print(i+'\n')

