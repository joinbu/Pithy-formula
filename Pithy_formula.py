import pandas as pd

#####数值输入######
# 输入数值 input words
R = pd.DataFrame([
    'ABCD',
    'DEF',
    'FG'
 ])

F = pd.DataFrame([
    'An',
    'B'
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

print('##########顺序版##########')
print(R_sequential)

print('##########自比版##########')
print(R_self_comparison)


def two_text(R,F):
    F_len = len(F)
    F_two_text = ''
    for i in range(0, F_len):
        F_two_text = ''.join([F_two_text, F[0][i]])

    l = len(R)  #获取正确数值个数 get right words'count


    #####删除错误数据 raplace faulse words in right words#####
    for j in range(0,l):
        for i in R[0][j]:
            if i in F_two_text:
                R[0][j] = R[0][j].replace(i,"")

    print("*删除错误数据*")
    print(R)

    #####将正确数值连接connet#####
    Rmix = ""
    for j in range(0,l):
        Rmix= ''.join([Rmix,R[0][j]])

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


    for j in range(0,l):
        for i in range(0,m):
            jx = Count.index[i]
            if jx in R[0][j]:
                R[0][j] = jx
                break

    print("*精简*")
    print(R)

    #####精密合并######

    Rmix2 = ""
    for j in range(0,l):
        Rmix2= ''.join([Rmix2,R[0][j]])

    ##除重##

    count2={}
    for i in Rmix2:
        count2.setdefault(i,0)
        count2[i] = count2[i] + 1

    Count2 = pd.DataFrame.from_dict(count2, orient='index', columns=['count'])

    ##除重后合并##
    l = len(Count2)
    Rmix3 = ""
    for j in range(0,l):
        Rmix3= ''.join([Rmix3,Count2.index[j]])

    print("*除重*")
    print(Rmix3)

print('##########同比版正向##########')
two_text(R,F)
print('##########同比版反向##########')
two_text(F,R)
