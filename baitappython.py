from sympy import FiniteSet
#Bai 1
A = set([x for x in range(-20,20) if (x-2)*(x-7)*(x-6) == 0])
print("A=",A)
B = set([x for x in range(-20,20) if x**2 - 7*x + 6 == 0])
print("B=",B)
C = set([x for x in range(-20,20) if x**2 - 8*x + 7 == 0])
print("C=",C)
#kiem tra C la con cua A hay khong ?
def tapcon(A,C):
    kq = True
    for x in A:
        if x not in C:
            kq = False
    return kq
print("Kiem tra C con A la:",    
      tapcon(A,C))
#Bai 2
n = 8
for x in range(1,n+1):
    for y in range(1,n+1):
        for z in range(1,n+1):
            for i in range(1,n+1):
                if x!=y and y!=z and z!=i and x!=z and x!=i and y!=i and i%2==1:
                    print(x,y,z,i)















    
