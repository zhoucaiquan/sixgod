import os,shutil



path = "C:/Users/s/Desktop/yy"# 当前路径
files = os.listdir(path)

# 财务费用

for i in files:
    if i:
        os.renames(path+"/"+i,path+"/SF-4-"+i)


#销售费用
for i in files:
    if i:
        os.renames(path+"/"+i,path+"/SD-4-"+i)

#固定资产

for i in files:
    if i:
        os.renames(path+"/"+i,path+"/ZO-3-"+i)

#管理费用

for i in files:
    if i:
        os.renames(path+"/"+i,path+"/SE-4-"+i)

#货币资金

for i in files:
    if i:
        os.renames(path+"/"+i,path+"/ZA-3-"+i)

#其他流动资产

for i in files:
    if i:
        os.renames(path+"/"+i,path+"/ZIB-3-"+i)

#其他应付款
for i in files:
    if i:
        os.renames(path+"/"+i,path+"/FJ-6-"+i)

#其他应收款
for i in files:
    if i:
        os.renames(path+"/"+i,path+"/ZU-5-"+i)

#人员工资
for i in files:
    if i:
        os.renames(path+"/"+i,path+"/FF-6-"+i)

#营业外收入
for i in files:
    if i:
        os.renames(path+"/"+i,path+"/SJ-3-"+i)

#营业外支出
for i in files:
    if i:
        os.renames(path+"/"+i,path+"/SK-3-"+i)
