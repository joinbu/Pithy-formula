import pandas as pd

#新建一个DataFrame
R = pd.DataFrame([
    'A',
    'B',
    'C'
 ])

#使用两种不同的方式进行赋值
R_copy = R.copy()
R_noCopy = R

#修改R里面的数值
for i in range(0,3):
	R[0][i] = '修改'


print('----没有使用copy,修改R，依然会影响到R_noCopy----')
print(R_noCopy)


print('\n----使用了copy，则不会影响到R_copy----')
print(R_copy)