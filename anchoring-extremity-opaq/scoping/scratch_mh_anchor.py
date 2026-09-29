import numpy as np
rng=np.random.default_rng(1)
def mh(z, s, t, n=20000):
    x=np.full(n, float(z))
    for _ in range(t):
        prop=x+rng.normal(0,s,n)
        acc=np.log(rng.uniform(size=n)) < (-(prop**2)+x**2)/2
        x=np.where(acc,prop,x)
    return x
for s,t in [(0.5,5),(0.3,10),(1.0,3)]:
    print(f"step {s}, t {t}")
    for z in [0.5,1,1.5,2,3,4,6,8]:
        x=mh(z,s,t); adj=z-x.mean()
        print(f"  z={z:4}: mean est {x.mean():5.2f}  adj {adj:5.2f}  adj/z {adj/z:4.2f}  sd {x.std():4.2f}")
