# -*- coding:utf-8 -*-
# Author: cmzz
# @Time :2019/11/21
import jieba
import csv
train_file = r'select_DISTINCT_content_score_from_jdcom.tsv'
seg_train_file = r'select_DISTINCT_content_score_from_jdcom_seg.txt'
# def generate_seg_file(input_file, out_seg_file):
#     with open(input_file, 'r', encoding='utf8') as f:
#         lines = f.readlines()
#         lines = f.readlines()
#
#     with open(out_seg_file, 'w') as f:
#         for line in lines:
#             print(line)
#             content, label = line.strip('\n').split(',')
#             word_iter = jieba.cut(content)
#             word_content = ''
#             for word in word_iter:
#                 word = word.strip(' ')
#                 if word != '':
#                     word_content += word + ' '
#             out_line = '%s\t%s\n' % (label, word_content.strip(' '))
#             f.write(out_line)
#
#
# generate_seg_file(train_file, seg_train_file)
csv_reader = csv.reader(open(train_file))
for row in csv_reader:
    print(row)
# with open(train_file, 'r') as f:
#     print(f.readlines())