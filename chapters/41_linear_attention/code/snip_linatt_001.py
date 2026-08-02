from __future__ import annotations
import math,torch
def phi(x): return torch.nn.functional.elu(x)+1
def linear(q,k,v):
    S=torch.zeros(q.shape[-1],v.shape[-1],dtype=q.dtype); z=torch.zeros(q.shape[-1],dtype=q.dtype); out=[]
    for qt,kt,vt in zip(q,k,v):
        fk=phi(kt); S=S+fk[:,None]*vt[None,:]; z=z+fk; fq=phi(qt); out.append((fq@S)/(fq@z+1e-9))
    return torch.stack(out)
def delta(M,k,v,beta=.5): return M+beta*k[:,None]*(v-M.T@k)[None,:]
def demo():
    torch.manual_seed(7); q=torch.randn(5,4,dtype=torch.float64); k=torch.randn(5,4,dtype=torch.float64); v=torch.randn(5,3,dtype=torch.float64); o=linear(q,k,v); M=torch.zeros(4,3,dtype=torch.float64); before=float((M.T@phi(k[0])-v[0]).norm()); M=delta(M,phi(k[0]),v[0],.1); after=float((M.T@phi(k[0])-v[0]).norm()); return {"shape":tuple(o.shape),"before":before,"after":after}
def checks():
    d=demo(); return {"shape":d["shape"]==(5,3),"delta_reduces":d["after"]<d["before"],"finite":math.isfinite(d["after"])}
