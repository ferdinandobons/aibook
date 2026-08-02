from __future__ import annotations
import math,torch
def naive(q,k,v): return torch.softmax(q@k.T/math.sqrt(q.numel()),-1)@v
def online(q,k,v,block=2):
    m=torch.tensor(float("-inf"),dtype=q.dtype); l=torch.tensor(0.,dtype=q.dtype); o=torch.zeros(v.shape[-1],dtype=q.dtype)
    for s in range(0,len(k),block):
        score=q@k[s:s+block].T/math.sqrt(q.numel()); bm=score.max(); nm=torch.maximum(m,bm); old=torch.exp(m-nm) if torch.isfinite(m) else torch.tensor(0.,dtype=q.dtype); e=torch.exp(score-nm); o=o*old+e@v[s:s+block]; l=l*old+e.sum(); m=nm
    return o/l
def demo():
    torch.manual_seed(7); q=torch.randn(8,dtype=torch.float64); k=torch.randn(7,8,dtype=torch.float64); v=torch.randn(7,5,dtype=torch.float64); a=naive(q,k,v); b=online(q,k,v,3); return {"max_diff":float((a-b).abs().max()),"shape":tuple(b.shape)}
def checks():
    d=demo(); return {"equivalent":d["max_diff"]<1e-12,"shape":d["shape"]==(5,),"finite":math.isfinite(d["max_diff"])}
