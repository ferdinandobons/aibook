from __future__ import annotations
import math,torch
from torch import nn
class MoE(nn.Module):
    def __init__(self,d,e,capacity): super().__init__(); self.router=nn.Linear(d,e,bias=False); self.experts=nn.ModuleList([nn.Linear(d,d,bias=False) for _ in range(e)]); self.capacity=capacity
    def forward(self,x):
        p=self.router(x).softmax(-1); routes=p.argmax(-1); out=torch.zeros_like(x); load=torch.zeros(len(self.experts),dtype=torch.int64); dropped=torch.zeros(len(x),dtype=torch.bool)
        for i,r in enumerate(routes.tolist()):
            if load[r]>=self.capacity: dropped[i]=True; continue
            out[i]=self.experts[r](x[i])*p[i,r]; load[r]+=1
        aux=len(self.experts)*torch.sum(p.mean(0)*(load.to(x.dtype)/len(x))); return out,routes,load,dropped,aux
def demo():
    torch.manual_seed(7); m=MoE(4,3,2); o,r,l,d,a=m(torch.randn(8,4)); return {"shape":tuple(o.shape),"load":l.tolist(),"dropped":int(d.sum()),"aux":float(a)}
def checks():
    d=demo(); return {"shape":d["shape"]==(8,4),"capacity":max(d["load"])<=2,"accounting":sum(d["load"])+d["dropped"]==8,"finite":math.isfinite(d["aux"])}
