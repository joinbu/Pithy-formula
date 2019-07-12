import pandas as pd

#####数值输入######
# 输入数值 input words
R = pd.DataFrame([
    '合同协议书',
    '中标通知书',
    '投标函及投标函附录',
    '项目专用合同条款',
    '公路工程专用合同条款',
    '通用合同条款',
    '工程量清单计量规则',
    '技术规范',
    '图纸',
    '已标价工程量清单',
    '.承包人有关人员、设备投入的承诺及投标文件中的施工组织设计',
    '其他合同文件'
 ])

R_constant = R.copy()   #必须使用.copy，否则R与R_constant会联动
R_len = len(R)  #3, R的长度

for r in range(0,R_len):
    #####将其他连接connet#####
    R_mix = ""
    for j in range(0,R_len):

        if j <= r:
            continue
        R_mix= ''.join([R_mix,R_constant[0][j]])

    #####删除错误数据 raplace faulse words in right words#####
    for i in R[0][r]:
        if i in R_mix:
            R[0][r] = R[0][r].replace(i,"")

print(R)
