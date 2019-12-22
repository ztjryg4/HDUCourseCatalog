# coding:utf-8
import csv, codecs
import re

# 前处理：手动替换csv中的逗号 删除上课时间 地点 合班
'''
col0 开课状态
col1 课程名称
col2 学分
col3 考核方式
col4 课程性质
col5 任课教师
col6 选课课号
col7 起止周
col8 上课时间 ele[9]
col9 上课地点 ele[10]
col10 开课学院 ele[8]
col11 合班信息 ele[11]
'''
inputfile = './data/csv/2019-2020-2_split.csv'
outputfile = './data/csv/2019-2020-2-processed.csv'

fp = open(inputfile, 'r', encoding='utf-8')
lines = fp.readlines()

new_lines = []
for ele in lines[1:]:
    ele = ele.split(",")
    # col0-6 maintain
    col0_6 = ele[0:7]
    # 7 修改 月 日
    col7 = ele[7]
    if '月' in ele[7]:
        col7 = col7.replace("月","~")
        col7 = col7.replace("日","")
    # col8 上课时间 refer to ele[9]
    col8 = ele[9]
    if 'title' in ele[9]:
        reg = re.compile(r'\=\"(.*?)\">')
        col8 = re.findall(reg,ele[9])[0]
    elif 'td' in ele[9]:
        reg = re.compile(r'<td>(.*?)</td>')
        col8 = re.findall(reg,ele[9])[0]
    # 9 refer to 13
    col9 = ele[10]
    if 'title' in ele[10]:
        reg = re.compile(r'\=\"(.*?)\">')
        col9 = re.findall(reg,ele[10])[0]
    elif 'td' in ele[10]:
        reg = re.compile(r'<td>(.*?)</td>')
        col9 = re.findall(reg,ele[10])[0]
    # 11 refer to 14
    col10 = ele[11]
    if 'title' in ele[11]:
        reg = re.compile(r'\=\"(.*?)\">')
        col11 = re.findall(reg,ele[11])[0]
    elif 'td' in ele[11]:
        reg = re.compile(r'<td>(.*?)</td>')
        col11 = re.findall(reg,ele[11])[0]
    # 10 maintain
    col10 = ele[8]
    cur_line = col0_6 + [str(col7)] + [str(col8)] + [str(col9)] + [str(col10)] + [str(col11)]
    new_lines.append(cur_line)

with open(outputfile, 'w', newline='',encoding="utf-8") as csv_file:
    csv_file.write(codecs.BOM_UTF8.decode())
    writer = csv.writer(csv_file)
    for row in new_lines:
        writer.writerow(row)

# 后处理：删除英文引号 空格重置 删除最后一行