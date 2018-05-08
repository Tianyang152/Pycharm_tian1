#2018/5/8
#用二分法求任意函数的根
import math
import matplotlib.pyplot as plt
import numpy as np

s=input('请输入方程等号右式：')                       #请试着输入2*np.sin(math.pi*x)++np.cos(math.pi*x)
a,b=map(int,input('请输入左右区间：').split())        #0 1        用空格隔开
e=float(input('请输入精度'))                           #e=0.01

def func(x):
    y=eval(s)
    return y

k=int(math.log((b-a)/e,2))+1    #k为二分法的次数
d=(b-a)/(2**k)      #d为间隔点的距离，其值小于精度e
for i in range(2**k+1):
    if func(a+i*d)==0:
        m=a+i*d
        print(m)
    if func(a+i*d)*func(a+(i+1)*d)<0:
        m=a+i*d+d/2
        print(m)

if func(b)==0:
    print(b)

x=np.linspace(a,b,2**k)
plt.plot(x,func(x),linewidth=1)
y0=x*0
plt.plot(x,y0,color='red',linewidth=1)
plt.show()