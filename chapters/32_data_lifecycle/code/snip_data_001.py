from __future__ import annotations
import hashlib,re
def normalize(text): return re.sub(r"\s+"," ",text.casefold()).strip()
def digest(text): return hashlib.sha256(normalize(text).encode()).hexdigest()
def deduplicate(records):
    out=[]; seen=set()
    for key,text in records:
        h=digest(text)
        if h not in seen: seen.add(h); out.append((key,text))
    return out
def split(key):
    value=int(hashlib.sha256(key.encode()).hexdigest()[:8],16)%100
    return "train" if value<80 else "validation" if value<90 else "test"
def demo():
    rows=[("a","Pacco non arrivato"),("b"," PACCO non arrivato "),("c","Carta rifiutata")]; unique=deduplicate(rows); return {"raw":len(rows),"unique":len(unique),"splits":[split(k) for k,_ in unique]}
def checks():
    d=demo(); return {"dedup":d["unique"]==2,"deterministic":split("a")==split("a"),"hash_changes":digest("a")!=digest("b")}
