from matplotlib import pyplot as plt

n=1000000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
#print(primes)

q=[]
w=[]
e=[]
r=[]
t=[]
y=[]
for i in range(len(primes)):
    if 0<primes[i]<10:
        q.append(primes[i])
    if 10<primes[i]<100:
        w.append(primes[i])
    if 100<primes[i]<1000:
        e.append(primes[i])
    if 1000<primes[i]<10000:
        r.append(primes[i])
    if 10000<primes[i]<100000:
        t.append(primes[i])
    if 100000<primes[i]<1000000:
        y.append(primes[i])
# print(len(q))
# print(len(w))
# print(len(e))
# print(len(r))


total=[]
a=0
for i in range(len(primes)-1):
    a=primes[i+1]-primes[i]
    total.append(a)
print(total)
del primes[len(primes)-1]  

print(len(primes))
print(len(total))

plt.plot(primes, total)
plt.show()