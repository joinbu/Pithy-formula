import pandas as pd

#####数值输入######
# 输入数值 input words
R = pd.DataFrame([
    'ABCD',
    'DEF',
    'FG'
 ])

F = pd.DataFrame([
    'A',
    '2'
 ])

R_constant = R.copy()   #必须使用.copy，否则R与R_constant会联动
R_sequential = R.copy()
R_self_comparison = R.copy()

R_len = len(R)  #3, R的长度

F_constant = F.copy()   #必须使用.copy，否则R与R_constant会联动
F_len = len(F)  #3, R的长度


for r in range(0,R_len):
    #####将其他连接connet#####
    R_sequential_mix = ""
    R_self_comparison_mix = ""

    for j in range(0,R_len):
        #####连接错误项#####
        if j == R_len-1:
            for x in range(0,F_len):
                R_sequential_mix = ''.join([R_sequential_mix, F_constant[0][x]])

        #####连接错误项#####
        if j == R_len - 1:
            for x in range(0, F_len):
                R_self_comparison_mix = ''.join([R_self_comparison_mix, F_constant[0][x]])


        if j > r:
            R_sequential_mix= ''.join([R_sequential_mix,R_constant[0][j]])

        if j != r:
            R_self_comparison_mix= ''.join([R_self_comparison_mix,R_constant[0][j]])


    #####删除错误数据 raplace faulse words in right words#####
    for i in R_sequential[0][r]:
        if i in R_sequential_mix:
            R_sequential[0][r] = R_sequential[0][r].replace(i,"")

    #####删除错误数据 raplace faulse words in right words#####
    for i in R_self_comparison[0][r]:
        if i in R_self_comparison_mix:
            R_self_comparison[0][r] = R_self_comparison[0][r].replace(i,"")

print('#####顺序版#####')
print(R_sequential)

print('#####自比版#####')
print(R_self_comparison)
