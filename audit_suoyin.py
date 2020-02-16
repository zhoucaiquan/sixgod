import os,shutil


# 使用说明
# 首先修改path，到总目录下，然后修正即可
# 条件1. 是pdf文件 2.只有数字 例如 文件1.pdf  文件2.pdf


path = "C:/Users/s/Desktop/wika上海"
files = os.listdir(path)
# 做一个大循环，如果list_y 等于他， 继续os.listdir 然后for循环就行了


# 财务费用
for y in files:
    if y == "财务费用":
        for i in os.listdir(path+"/"+y):
            if i:
                os.renames(path+"/"+y+"/"+i,path+"/"+y+"/SF-4-"+i)


    #销售费用
    if y == "销售费用":
        for i in os.listdir(path+"/"+y):
            if i:
                os.renames(path+"/"+y+"/"+i,path+"/"+y+"/SD-4-"+i)

    #固定资产

    if y == "固定资产":
        for i in os.listdir(path+"/"+y):
            if i:
                os.renames(path+"/"+y+"/"+i,path+"/"+y+"/ZO-3-"+i)

    #管理费用
    if y == "管理费用":
        for i in os.listdir(path+"/"+y):
            if i:
                os.renames(path+"/"+y+"/"+i,path+"/"+y+"/SE-4-"+i)

    #货币资金
    if y == "货币资金":
        for i in os.listdir(path+"/"+y):
            if i:
                os.renames(path+"/"+y+"/"+i,path+"/"+y+"/ZA-3-"+i)

    #其他流动资产
    if y == "其他流动资产":
        for i in os.listdir(path+"/"+y):
            if i:
                os.renames(path+"/"+y+"/"+i,path+"/"+y+"/ZIB-3-"+i)

    #其他应付款
    if y == "其他应付款":
        for i in os.listdir(path+"/"+y):
            if i:
                os.renames(path+"/"+y+"/"+i,path+"/"+y+"/FJ-6-"+i)

    #其他应收款
    if y == "其他应收款":
        for i in os.listdir(path+"/"+y):
            if i:
                os.renames(path+"/"+y+"/"+i,path+"/"+y+"/ZU-5-"+i)

    #人员工资
    if y == "应付职工薪酬":
        for i in os.listdir(path+"/"+y):
            if i:
                os.renames(path+"/"+y+"/"+i,path+"/"+y+"/FF-6-"+i)

    #营业外收入
    if y == "营业外收入":
        for i in os.listdir(path+"/"+y):
            if i:
                os.renames(path+"/"+y+"/"+i,path+"/"+y+"/SJ-3-"+i)

    #营业外支出
    if y == "营业外支出":
        for i in os.listdir(path+"/"+y):
            if i:
                os.renames(path+"/"+y+"/"+i,path+"/"+y+"/SK-3-"+i)
