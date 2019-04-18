#
import csv
dicfile = 'dic.csv'
content=[]
recc=[]
with open("dicS.csv","r",encoding='UTF-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        print(reader)
        content.append(line)
    print(content)

data = content
# cur当前列数
# str:当前生成句子
def solve(cur,str):
    if cur ==2:
        recc.append(str)
        return
    for i in range(10):
        solve(cur +1,str + data[cur][i])

solve(0,"")
csv_file=csv.writer(open('result.csv','a',newline=''),dialect='excel')
csv_file.writerow(recc)