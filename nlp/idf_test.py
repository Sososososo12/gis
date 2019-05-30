from sklearn.feature_extraction.text import *
import xlrd
import jieba
from nlp import striptxt

dataname = r'../based/04-08Excel/14.xlsx'
# 读取地址文件名确定的excel文件
data = xlrd.open_workbook(filename=dataname)
# 读取工作sheet，（）内从0开始代表1...
sheet1 = data.sheet_by_index(0)
# 读取第（）列的信息，（）内从0开始代表1...
summary_set = sheet1.col_values(5)
    # 获取user_id_set的值的数量（列表长度）
summary_len=len(summary_set)
summary1=summary_set[1]

# content=jieba.lcut(summary1,cut_all=False)
sentence_list=[]
for sen_line in summary_set:
    sentence_list.append(striptxt.seg_sentence(sen_line))


vectorizer = CountVectorizer()
count = vectorizer.fit_transform(sentence_list)
print(vectorizer.get_feature_names())
print(vectorizer.vocabulary_)
print(count.toarray())

transformer = TfidfTransformer()
tfidf_matrix = transformer.fit_transform(count)
print(tfidf_matrix.toarray())
# print(content)