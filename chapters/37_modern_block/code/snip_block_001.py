from __future__ import annotations
import torch
from torch import nn
class RMSNorm(nn.Module):
    def __init__(self,d,eps=1e-6): super().__init__(); self.weight=nn.Parameter(torch.ones(d)); self.eps=eps
    def forward(self,x): return x*torch.rsqrt(x.pow(2).mean(-1,keepdim=True)+self.eps)*self.weight
class Block(nn.Module):
    def __init__(self,d,h): super().__init__(); self.norm=RMSNorm(d); self.g=nn.Linear(d,h,bias=False); self.u=nn.Linear(d,h,bias=False); self.d=nn.Linear(h,d,bias=False)
    def forward(self,x): return x+self.d(torch.nn.functional.silu(self.g(self.norm(x)))*self.u(self.norm(x)))
def demo():
    torch.manual_seed(7); b=Block(8,16); x=torch.randn(2,4,8,requires_grad=True); y=b(x); y.mean().backward(); return {"shape":tuple(y.shape),"finite":bool(torch.isfinite(y).all()),"grad":float(x.grad.norm())}
def checks():
    d=demo(); return {"shape":d["shape"]==(2,4,8),"finite":d["finite"],"grad":d["grad"]>0}
