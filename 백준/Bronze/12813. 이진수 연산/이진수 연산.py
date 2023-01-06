import sys
n=(sys.stdin.readline())
f_a=len(n)-1
a=int(n,2)
m=(sys.stdin.readline())
f_b=len(m)
b=int(m,2)
mask = 2**(f_a)-1
r_and=bin(a&b)
r_or=bin(a|b)
r_xor=bin(a^b)
r_n_a=bin(a^mask)
r_n_b=bin(b^mask)


print(r_and[2:].zfill(f_a))
print(r_or[2:].zfill(f_a))
print(r_xor[2:].zfill(f_a))
print(r_n_a[2:].zfill(f_a))
print(r_n_b[2:].zfill(f_a))