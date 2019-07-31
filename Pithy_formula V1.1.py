'''
作者：joinbu
版本号：v1.1

顺序版
自比版
二比版
（三比版）

升级思路：
1、删除同音字
2、自动分词版
	拆词
	删单字
3、三者比较版
'''

import pandas as pd

#####数值输入######
# 输入正确数值 input right words
R = pd.DataFrame([
    'True1',
    'True2',
    'True3'
 ])

#输入错误数值 input false words
F = pd.DataFrame([
    'False1',
    'False2'
 ])

R_constant = R.copy()   #必须使用.copy，否则R与R_constant会联动,We must use‘.copy’，or ‘R_constant’is always equal to ‘R’.
R_len = len(R)  #R的长度，length of R

F_constant = F.copy()
F_len = len(F)  #F的长度，length of F

R_sequential = R.copy()
R_self_comparison = R.copy()

for r in range(0,R_len):
    R_sequential_mix = ""  #用于储存顺序版中的干扰项和错误项
    R_self_comparison_mix = ""  #用于储存自比版中的干扰项和错误项

    for j in range(0,R_len):
        #####连接顺序版错误项F#####
        if j == R_len-1:
            for x in range(0,F_len):
                R_sequential_mix = ''.join([R_sequential_mix, F_constant[0][x]])

        #####连接自比版错误项F#####
        if j == R_len - 1:
            for x in range(0, F_len):
                R_self_comparison_mix = ''.join([R_self_comparison_mix, F_constant[0][x]])

        #####连接顺序版干扰项R#####
        if j > r:
            R_sequential_mix= ''.join([R_sequential_mix,R_constant[0][j]])

        #####连接自比版干扰项R#####
        if j != r:
            R_self_comparison_mix= ''.join([R_self_comparison_mix,R_constant[0][j]])


    #####删除错误数据 raplace false words in right words#####
    for i in R_sequential[0][r]:
        if i in R_sequential_mix:
            R_sequential[0][r] = R_sequential[0][r].replace(i,"")

    #####删除错误数据 raplace false words in right words#####
    for i in R_self_comparison[0][r]:
        if i in R_self_comparison_mix:
            R_self_comparison[0][r] = R_self_comparison[0][r].replace(i,"")

print('     ##########顺序版##########')
print(R_sequential)

print('     ##########自比版##########')
print(R_self_comparison)

#定义“同比版”的公式，define formula of two text sets’comparison edition
def two_text(R,F):
    R_two = R.copy()
    F_two = F.copy()

    F_len = len(F_two)
    F_two_text = ''
    for i in range(0, F_len):
        F_two_text = ''.join([F_two_text, F_two[0][i]])

    R_len = len(R_two)  #获取正确数值个数 get right words'count

    #####删除错误数据 raplace faulse words in right words#####
    for j in range(0,R_len):
        for i in R_two[0][j]:
            if i in F_two_text:
                R_two[0][j] = R_two[0][j].replace(i,"")

    print("*删除错误数据*")
    print(R_two)

    #####将正确数值连接connet#####
    Rmix = ""
    for j in range(0,R_len):
        Rmix= ''.join([Rmix,R_two[0][j]])

    #统计个数并转换为dataframe；Statistics and change into dataframe#####
    count={}
    for i in Rmix:
        count.setdefault(i,0)
        count[i] = count[i] + 1

    Count = pd.DataFrame.from_dict(count, orient='index', columns=['count'])

    #排序#####
    Count = Count.sort_values(by='count',ascending=False)

    print("*正确个数统计*")
    print(Count)

    m = len(Count)  #正确个数长度

    #####取出频率最高的单字符串取代词语#####
    for j in range(0,R_len):
        for i in range(0,m):
            jx = Count.index[i]
            if jx in R_two[0][j]:
                R_two[0][j] = jx
                break

    print("*精简*")
    print(R_two)

    #####精密合并######

    Rmix2 = ""
    for j in range(0,R_len):
        Rmix2= ''.join([Rmix2,R_two[0][j]])

    ##除重##

    count2={}
    for i in Rmix2:
        count2.setdefault(i,0)
        count2[i] = count2[i] + 1

    Count2 = pd.DataFrame.from_dict(count2, orient='index', columns=['count'])

    ##除重后合并##
    R_len = len(Count2)
    Rmix3 = ""
    for j in range(0,R_len):
        Rmix3= ''.join([Rmix3,Count2.index[j]])

    print("*除重*")
    print(Rmix3)

print('     ########同比版正向########')
two_text(R,F)
print('     ########同比版反向########')
two_text(F,R)