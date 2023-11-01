n = int(input("enter the first number:  ")) 
m = int(input("enter the second number:  ")) 
s1=0
i=0
j=0
s2=0
#the following lists were used in testing the algorithm, the program doesn't need them to work
TAB1=[]
TAB2=[]
for i in range(n-1,1,-1):
 if n%i==0:
  s1=s1+i
  TAB1.append(i)
for j in range(m-1,1,-1):
 if m%j==0:
  s2=s2+j
  TAB2.append(j)

if s1==m and s2==n:
 print("the two numbers are friends")
else:
 print("the two numbers aren't friends")