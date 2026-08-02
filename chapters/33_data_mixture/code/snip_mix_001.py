from __future__ import annotations
def mixture(counts,alpha):
    if alpha<=0: raise ValueError
    p={k:v**alpha for k,v in counts.items()}; s=sum(p.values()); return {k:v/s for k,v in p.items()}
def curriculum(step,total):
    p=min(max(step/total,0),1); return {"clean":0.8-0.3*p,"hard":0.2+0.3*p}
def demo(): return {"natural":mixture({"web":900,"code":90,"dialogue":10},1.0),"flat":mixture({"web":900,"code":90,"dialogue":10},0.5),"start":curriculum(0,100),"end":curriculum(100,100)}
def checks():
    d=demo(); return {"normalized":abs(sum(d["flat"].values())-1)<1e-12,"small_upweighted":d["flat"]["dialogue"]>d["natural"]["dialogue"],"curriculum":d["end"]["hard"]>d["start"]["hard"]}
