import xlrd
import xlwt
import pandas as pd
# from comment import striptxt
# -*- coding: utf-8 -*-
import numpy as np
import jieba
import numpy
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import lda
import lda.datasets
from nlp import striptxt
import math

data = xlrd.open_workbook(filename=r'../based/04-08Excel_xlsx/1.xlsx')
sheet1 = data.sheet_by_index(0)
summary_set = sheet1.col_values(5)
# summary_set=summary_set.pop(0)
# print(summary_set)

sentence_list = []
for sen_line in summary_set:
    sentence_output = striptxt.seg_sentence(sen_line)  # 这里的返回值是字符串
    sentence_list.append(sentence_output)
# print(comment_output)

# 将文本中的词语转换为词频矩阵 矩阵元素a[i][j] 表示j词在i类文本下的词频
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(sentence_list)
transformer = TfidfTransformer()
tfidf_matrix = transformer.fit_transform(x)
# print(x)
# analyze = vectorizer.build_analyzer()
# weight = x.toarray()
weight = tfidf_matrix.toarray()
mar = np.asarray(weight)
# print(weight)

shape = mar.shape
for x in range(0, shape[0]):
    for y in range(0, shape[1]):
        mar[x, y] = mar[x, y] + 0.49
        mar[x, y] = round(mar[x, y])
        # print()
print()
# print(shape)
