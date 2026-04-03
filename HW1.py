#Bài 4: Viết chương trình giải phương trình bậc 1 (ax + b = 0)  
#Bài 5: Viết chương trình giải phương trình bậc 2 (ax2 + bx + c = 0)




#Bài 7: Tìm giá trị nhỏ nhất trong 4 số a, b, c, d (a, b, c, được nhập từ bàn phím).  
a,b,c,d= map(int, input().split())
if a<b and a < c and a< d: 
    print(a)
elif b<c and b<a and b<d:
    print(b)
elif c<a and c<d and c<b:
    print(c)
else:
    print(d)