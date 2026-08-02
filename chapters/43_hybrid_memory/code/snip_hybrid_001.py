from __future__ import annotations
import torch
class Memory:
    def __init__(self,d,decay=.8,window=3): self.state=torch.zeros(d,dtype=torch.float64); self.decay=decay; self.window=window; self.recent=[]
    def reset(self): self.state.zero_(); self.recent.clear()
    def step(self,x): self.state=self.decay*self.state+(1-self.decay)*x; self.recent=(self.recent+[x])[-self.window:]; return torch.cat([torch.stack(self.recent).mean(0),self.state])
def demo():
    m=Memory(2,.5,2); a=m.step(torch.tensor([1.,0.],dtype=torch.float64)); b=m.step(torch.tensor([0.,1.],dtype=torch.float64)); retained=float(m.state.sum()); m.reset(); return {"shape":tuple(b.shape),"retained":retained,"reset":float(m.state.sum())}
def checks():
    d=demo(); return {"two_paths":d["shape"]==(4,),"retains":d["retained"]>0,"reset":d["reset"]==0}
