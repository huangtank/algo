a,b=map(int,input("輸入a和b值(a先b後)").split())#輸入a,b兩數

#互換
t=a
a=b
b=t
 
#輸出
print(f'a值變成了{a}')
print(f'b值變成了{b}')

'''
python能夠以a,b=b,a的方式做交換
'''

#互換
a,b=b,a

#輸出
print(f'a值變成了{a}')
print(f'b值變成了{b}')