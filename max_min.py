#最大值最小值，比較兩數誰最大誰最小，可作用於排序

#輸入
x,y=map(int,input().split())

#處理
if x>y:
    print(f'x值最大:{x}')
    print(f'y值最小:{y}')
else:
    print(f'x值最小:{x}')
    print(f'y值最大:{y}')

'''
也可以使用函數來做
'''

#函數
def M(x,y):
    if x>y:
        return f'x值最大:{x}, y值最小:{y}'
    else:
        return f'x值最小:{x}, y值最大:{y}'
print(M(x,y))

'''
亦可使用python內建函數max(),min()找出最大最小值
'''

#max(),min()
print(f'最大為{max(x,y)}')
print(f'最小為{min(x,y)}')

#當如果為串列時
l=[5,3,2,1,6,4]

#處理，就需要多倆個變數來存放目前讀取到的最大值，一個存放最小值
max_list=0
min_list=l[0] #設定為串列裡第一個值，以防止最小值不在串列裡
for i in l:
    if i>max_list:
        max_list=i
    if i<min_list:
        min_list=i
print(f'最大值:{max_list}')
print(f'最小值:{min_list}')

#函數
def M(x,y):
    max_list=0
    min_list=l[0] #設定為串列裡第一個值，以防止最小值不在串列裡
    for i in l:
        if i>max_list:
            max_list=i
        if i<min_list:
            min_list=i
    return f'l內最小為:{min_list}, y值最大:{max_list}'
print(M(x,y))

#串列也可以使用內建函數
print(f'最大為{max(l)}')
print(f'最小為{min(l)}')
