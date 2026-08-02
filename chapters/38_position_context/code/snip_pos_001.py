from __future__ import annotations
import math,torch
def rotate(x,angle):
    R=torch.tensor([[math.cos(angle),-math.sin(angle)],[math.sin(angle),math.cos(angle)]],dtype=x.dtype); return x@R.T
def rope(x,pos,base=0.2):
    pairs=x.reshape(-1,2); return torch.stack([rotate(p,pos*base*(i+1)) for i,p in enumerate(pairs)]).reshape_as(x)
def alibi(n,slope):
    p=torch.arange(n); return -slope*(p[:,None]-p[None,:]).abs().to(torch.float64)
def demo():
    x=torch.tensor([1.,2.,3.,4.],dtype=torch.float64); return {"norm_before":float(x.norm()),"norm_after":float(rope(x,7).norm()),"bias":alibi(4,0.5).tolist()}
def checks():
    d=demo(); b=alibi(4,1.0); return {"norm":abs(d["norm_before"]-d["norm_after"])<1e-12,"diagonal":bool(torch.all(torch.diag(b)==0)),"distance":float(b[0,3])<float(b[0,1])}
