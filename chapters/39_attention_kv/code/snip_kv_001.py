from __future__ import annotations
import torch
def expand_kv(x,q_heads):
    h=x.shape[1]
    if q_heads%h: raise ValueError
    g=q_heads//h; return x[:,:,None].expand(-1,-1,g,-1,-1).reshape(x.shape[0],q_heads,x.shape[2],x.shape[3])
def cache_bytes(B,L,N,H,D,s): return 2*B*L*N*H*D*s
def demo():
    x=torch.randn(1,2,3,4); y=expand_kv(x,8); return {"shape":tuple(y.shape),"mha":cache_bytes(1,4096,32,32,128,2),"gqa":cache_bytes(1,4096,32,8,128,2),"shared":bool(torch.equal(y[:,0],y[:,1]))}
def checks():
    d=demo(); return {"shape":d["shape"]==(1,8,3,4),"cache":d["mha"]==4*d["gqa"],"sharing":d["shared"]}
