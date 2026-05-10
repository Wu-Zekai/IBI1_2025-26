a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
if d > e:
    print("The population growth between 2004-2014 (d) was larger than 2014-2024 (e).")
else:
    print("The population growth between 2014-2024 (e) was larger than or equal to 2004-2014 (d).")

X=True
Y=False
W=X or Y
print(W)
print("When X is " + str(X) + " and Y is " + str(Y) + ", W (X or Y) is: " + str(W))
