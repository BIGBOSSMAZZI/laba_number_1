# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print('введите первое число')
a=int(input())
print('введите операцию')
op=int(input())
print('введите второе число')
b=int(input())
if op=='+':
    print(a+b)
if op=='-':
    print(a-b)
if op=='*':
    print(a*b)
if op=='/':
    if b!=0:
        print(a/b)
    else :
        print('вселенная схлопнулась')