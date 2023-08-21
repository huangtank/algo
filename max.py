#最大值，比較兩數誰最大，可作用於排序

#輸入
x,y=map(int,input().split())

#處理
if x>y:
    print(f'x值最大:{x}')
else:
    print(f'y值最大:{y}')

'''
也可以使用函數來做
'''

#函數
def M(x,y):
    if x>y:
        return f'x值最大:{x}'
    else:
        return f'y值最大:{y}'
print(M(x,y))

'''
亦可使用python內建函數max(),min()找出最大最小值
'''

#max(),min()
print(f'最大為{max(x,y)}')
print(f'最小為{min(x,y)}')