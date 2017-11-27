# 矩形宽度
w = 100
# 矩形高度
h = 100
# 矩形y轴穿过线条数
n = 10
# 任意整数(-2,1,3,4,5,234)
random_int = 3
# 穿过y轴纵坐标最小值正数, 穿过 原点就是0
yMin = 0
# 斜率, 当其他四个变量确定时, 是确定值
k = random_int/n*h/w
# 绘制矩形
x_num = 1
y_num = 1
for i in range(x_num):
    y= w*i
for i in range(y_num):
    y = h*1
# 绘制一侧斜线,
for i in range(n):
    y = kx+(i*(h/n)+yMin)
