import random, time, bisect
import statistics as stats

# ---------------- ALGORITMOS ----------------

def linear_search(a, x):
    for i,v in enumerate(a):
        if v==x: return i
    return -1

def binary_search(a, x):
    i = bisect.bisect_left(a, x)
    return i if i<len(a) and a[i]==x else -1

def exponential_search(a, x):
    if not a: return -1
    if a[0]==x: return 0
    i=1
    n=len(a)
    while i<n and a[i]<x:
        i <<= 1
    lo, hi = i>>1, min(i, n-1)
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==x: return m
        if a[m]<x: lo=m+1
        else: hi=m-1
    return -1

def interpolation_search(a, x):
    lo, hi = 0, len(a)-1
    while lo<=hi and a[lo]<=x<=a[hi]:
        if a[lo]==a[hi]:
            return lo if a[lo]==x else -1
        pos = lo + int((x-a[lo])*(hi-lo)/(a[hi]-a[lo]))
        if pos<lo or pos>hi: break
        if a[pos]==x: return pos
        if a[pos]<x: lo=pos+1
        else: hi=pos-1
    return -1

# ---------------- BENCHMARK ----------------

def bench(a, queries, fn):
    t0=time.perf_counter()
    for x in queries:
        fn(a,x)
    t1=time.perf_counter()
    return (t1-t0)/len(queries)*1000  # ms por búsqueda

# ---------------- DATA ----------------

def make_data(n, kind):
    if kind=="uniform":
        a=list(range(n))
    elif kind=="biased":
        a=[]
        for _ in range(n):
            if random.random()<0.8:
                a.append(random.randint(0, int(0.1*n)))
            else:
                a.append(random.randint(int(0.1*n), 5*n))
        a.sort()
    elif kind=="shuffled":
        a=list(range(n))
        random.shuffle(a)
    return a

def make_queries(a):
    q=[]
    for _ in range(700):
        q.append(random.choice(a))
    for i in range(300):
        q.append(len(a)*10+i)
    random.shuffle(q)
    return q

# ---------------- MAIN ----------------

random.seed(123)
sizes=[10000, 100000, 500000]

for n in sizes:
    print(f"\n===== n={n} =====")

    for kind in ["uniform","biased","shuffled"]:
        a=make_data(n, kind)
        q=make_queries(a)

        print(f"\nDataset: {kind}")

        print("Lineal:", bench(a,q,linear_search))

        if kind!="shuffled":
            print("Binaria:", bench(a,q,binary_search))
            print("Exponencial:", bench(a,q,exponential_search))
            print("Interpolación:", bench(a,q,interpolation_search))
        else:
            print("Solo aplica lineal (no ordenado)")