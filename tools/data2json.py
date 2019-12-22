import json
import csv

inputfile = './data/csv/2019-2020-2-processed.csv'
outputfile = './data/json/2019-2020-2_split.json'

fp = open(inputfile, 'r', encoding='utf-8')
lines = fp.readlines()
# col0 开课状态
# col1 课程名称
# col2 学分
# col3 考核方式
# col4 课程性质
# col5 任课教师
# col6 选课课号
# col7 起止周
# col8 上课时间 ele[9]
# col9 上课地点 ele[10]
# col10 开课学院 ele[8]
# col11 合班信息 ele[11]
rows = []
for line in lines:
    line = line.split(",")
    currow = {
        'status' : line[0],
        'coursename' : line[1],
        'credit' : line[2],
        'assessment' : line[3],
        'coursetype' : line[4],
        'teacher' : line[5],
        'coursecode' : line[6],
        'duration' : line[7],
        'time' : line[8],
        'place' : line[9],
        'school' : line[10],
        'arrangement' : line[11]
    }
    # currow_json = json.dumps(currow, ensure_ascii=False)
    # print(currow_json)
    rows.append(currow)
    # exit(0)

# print(rows)
# exit(0)
main_struc = {'total': len(lines)-1, 'rows': rows}

main_json = json.dumps(main_struc, ensure_ascii=False)
# print(main_json)
outfp = open(outputfile,"w",encoding="utf-8")
outfp.write(main_json)