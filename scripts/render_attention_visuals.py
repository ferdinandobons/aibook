from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ROOT = Path(__file__).resolve().parents[1]
OUT1 = ROOT / 'assets/chapters/28_attention/ATT-01/candidate-v2.png'
OUT2 = ROOT / 'assets/chapters/28_attention/ATT-02/candidate-v2.png'
REG='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
MONOB='/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf'
C={'bg':'#F6F8FB','white':'#FFFFFF','ink':'#162033','muted':'#4C5A70','line':'#C7D2E0','strong':'#8797AA','blue':'#2864D7','bsoft':'#EEF5FF','green':'#238B57','gsoft':'#EDF9F1','amber':'#B77A16','asoft':'#FFF8E7','red':'#B52A35','rsoft':'#FFF1F2','purple':'#7653B5','psoft':'#F5F0FF','gray':'#F1F4F8'}

def f(n,b=False,m=False): return ImageFont.truetype(MONOB if m and b else MONO if m else BOLD if b else REG,n)
def rr(d,r,fill,outline,width=2,rad=16): d.rounded_rectangle(r,rad,fill=fill,outline=outline,width=width)
def center(d,r,t,n=24,b=False,m=False,color=None,pad=10,spacing=4):
    avail_w=r[2]-r[0]-2*pad; avail_h=r[3]-r[1]-2*pad
    for size in range(n,13,-1):
        font=f(size,b,m); bb=d.multiline_textbbox((0,0),t,font=font,spacing=spacing,align='center'); w,h=bb[2]-bb[0],bb[3]-bb[1]
        if w<=avail_w and h<=avail_h: break
    else: raise AssertionError((t,r,w,h))
    d.multiline_text(((r[0]+r[2]-w)/2,(r[1]+r[3]-h)/2),t,font=font,fill=color or C['ink'],spacing=spacing,align='center')
def left(d,p,t,n=22,b=False,color=None): d.text(p,t,font=f(n,b),fill=color or C['ink'],anchor='lm')
def pill(d,r,t,fill,outline,n=22,b=True,m=False,color=None): rr(d,r,fill,outline,2,13); center(d,r,t,n,b,m,color,pad=9)
def arrow(d,a,b,color=None,w=4,head=11):
    color=color or C['ink']; d.line([a,b],fill=color,width=w); ang=math.atan2(b[1]-a[1],b[0]-a[0])
    p1=(b[0]+head*math.cos(ang+2.55),b[1]+head*math.sin(ang+2.55)); p2=(b[0]+head*math.cos(ang-2.55),b[1]+head*math.sin(ang-2.55)); d.polygon([b,p1,p2],fill=color)
def save(im,path):
    path.parent.mkdir(parents=True,exist_ok=True); im.quantize(colors=128,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE).save(path,optimize=True)

def att01():
    im=Image.new('RGB',(1600,900),C['bg']); d=ImageDraw.Draw(im)
    pill(d,(45,36,165,88),'ATT-01',C['blue'],C['blue'],26,True,False,'white')
    left(d,(195,60),'Perché i pesi devono dipendere dalla query',42,True); left(d,(195,105),'Confronto controllato sulla stessa sequenza di value',25,False,C['muted'])
    L=(55,145,770,735); R=(830,145,1545,735); rr(d,L,C['white'],C['red'],3,22); rr(d,R,C['white'],C['blue'],3,22)
    pill(d,(75,165,750,220),'Contesto fisso',C['rsoft'],C['red'],32,True,False,C['red']); pill(d,(850,165,1525,220),'Pesi dipendenti dalla query',C['gsoft'],C['green'],30,True,False,C['green'])
    left(d,(110,255),'Stesse value disponibili',24,True)
    vals=[]
    for x,t in zip((110,255,400),('v₁','v₂','v₃')): r=(x,290,x+115,355); pill(d,r,t,C['bsoft'],C['blue'],28,True,True); vals.append(r)
    y=390; centers=[(r[0]+r[2])//2 for r in vals]
    for x,r in zip(centers,vals): d.line([(x,r[3]),(x,y)],fill=C['strong'],width=3)
    d.line([(centers[0],y),(515,y)],fill=C['strong'],width=3); arrow(d,(515,y),(545,y),C['strong'])
    rr(d,(545,335,710,430),C['psoft'],C['purple'],3,18); center(d,(545,335,710,430),'vettore fisso\nc',29,True)
    d.line([(625,430),(625,465),(252,465)],fill=C['red'],width=4); d.line([(625,465),(572,465)],fill=C['red'],width=4); arrow(d,(252,465),(252,500),C['red']); arrow(d,(572,465),(572,500),C['red'])
    pill(d,(135,500,370,590),'c per q₁\nidentico',C['rsoft'],C['red'],25); pill(d,(455,500,690,590),'c per q₂\nidentico',C['rsoft'],C['red'],25)
    rr(d,(90,620,735,700),C['rsoft'],C['red'],2,16); center(d,(90,620,735,700),'Limite: query diverse ricevono lo stesso\nriassunto.',25,True,color=C['red'])
    left(d,(885,250),'Stesse value, coefficienti diversi',24,True)
    x0=865; widths=[100,110,110,110,125]; heads=['query','v₁','v₂','v₃','output']; x=x0
    for i,(t,w) in enumerate(zip(heads,widths)):
        fill=C['gray'] if i==0 else C['bsoft'] if i<4 else C['gsoft']; out=C['strong'] if i==0 else C['blue'] if i<4 else C['green']; pill(d,(x,290,x+w,348),t,fill,out,23,True,i in (1,2,3)); x+=w+10
    for row,(q,ws,o) in enumerate((('q₁',('0,10','0,60','0,30'),'c₁'),('q₂',('0,55','0,15','0,30'),'c₂'))):
        y=365+row*120; x=x0; pill(d,(x,y,x+100,y+75),q,C['psoft'],C['purple'],28,True,True); x+=110
        for j,v in enumerate(ws): pill(d,(x,y,x+110,y+75),v,'#DCEBFF' if (row,j) in ((0,1),(1,0)) else C['bsoft'],C['blue'],26,True,True); x+=120
        pill(d,(x,y,x+125,y+75),o,C['gsoft'],C['green'],30,True,True)
    rr(d,(865,610,1510,700),C['gsoft'],C['green'],2,16); center(d,(865,610,1510,700),'Risultato: q₁ e q₂ producono combinazioni\ndiverse.',25,True,color=C['green'])
    rr(d,(150,770,1450,855),C['asoft'],C['amber'],2,18); center(d,(150,770,1450,855),'Invariante: le value non cambiano. Cambiano i coefficienti usati per combinarle.',27,True,pad=20)
    save(im,OUT1)

def att02():
    im=Image.new('RGB',(1800,1000),C['bg']); d=ImageDraw.Draw(im)
    pill(d,(45,34,165,86),'ATT-02',C['blue'],C['blue'],26,True,False,'white'); left(d,(195,60),'Una query, tre key, tre value',42,True); left(d,(195,104),'Esempio numerico illustrativo con dₖ = dᵥ = 2',25,False,C['muted'])
    widths=[260,220,220,240,360,230]; xs=[]; x=45
    for w in widths: xs.append((x,x+w)); x+=w+18
    fills=[C['white'],C['bsoft'],C['bsoft'],C['psoft'],C['gsoft'],C['white']]; outs=[C['strong'],C['blue'],C['blue'],C['purple'],C['green'],C['green']]; titles=['1  Input','2  Score','3  Scaling','4  Softmax','5  Somma pesata','6  Output']
    for i,(a,b) in enumerate(xs): rr(d,(a,155,b,785),fills[i],outs[i],2,20); pill(d,(a+14,169,b-14,227),titles[i],C['white'],outs[i],27,True,False,outs[i])
    a,b=xs[0]; left(d,(a+25,260),'query',22,True); pill(d,(a+25,285,b-25,350),'q = [1, 0]',C['white'],C['blue'],25,False,True); left(d,(a+25,400),'key e value',22,True)
    pill(d,(a+25,425,a+124,475),'key',C['gray'],C['strong'],20); pill(d,(a+136,425,b-25,475),'value',C['gray'],C['strong'],20)
    for i,(k,v) in enumerate((('k₁ =\n[1, 0]','v₁ =\n[1, 0]'),('k₂ =\n[0, 1]','v₂ =\n[0, 1]'),('k₃ =\n[1, 1]','v₃ =\n[1, 1]'))): y=490+i*78; pill(d,(a+25,y,a+124,y+62),k,C['white'],C['blue'],17,False,True); pill(d,(a+136,y,b-25,y+62),v,C['white'],C['green'],17,False,True)
    a,b=xs[1]; center(d,(a+20,250,b-20,330),'qKᵀ',34,True,True); x=a+22
    for v in ('1','0','1'): pill(d,(x,365,x+52,425),v,C['white'],C['blue'],25,True,True); x+=62
    center(d,(a+25,440,b-25,485),'shape [1×3]',20,True,True,color=C['muted']); rr(d,(a+25,520,b-25,650),C['white'],C['blue'],2,14); center(d,(a+25,520,b-25,650),'Tre prodotti\nscalari',25,True,color=C['muted'])
    a,b=xs[2]; center(d,(a+20,245,b-20,320),'÷ √2',34,True,True); x=a+13
    for v in ('0,707','0,000','0,707'): pill(d,(x,365,x+61,425),v,C['white'],C['blue'],17,True,True); x+=69
    center(d,(a+25,440,b-25,485),'shape [1×3]',20,True,True,color=C['muted']); rr(d,(a+25,520,b-25,675),C['asoft'],C['amber'],2,14); center(d,(a+25,520,b-25,675),'Lo scaling\nmodifica\ngli score,\nnon V.',23,True,color=C['amber'])
    a,b=xs[3]; center(d,(a+20,245,b-20,320),'softmax',31,True,True)
    for i,(q,v) in enumerate((('α₁','0,401'),('α₂','0,198'),('α₃','0,401'))): y=345+i*92; pill(d,(a+25,y,a+95,y+68),q,C['white'],C['purple'],24,True,True); pill(d,(a+110,y,b-25,y+68),v,C['white'],C['purple'],24,True,True)
    rr(d,(a+25,650,b-25,725),C['asoft'],C['amber'],2,14); center(d,(a+25,650,b-25,725),'Somma =\n1,000',22,True)
    a,b=xs[4]; center(d,(a+22,235,b-22,300),'o = α₁v₁ + α₂v₂ + α₃v₃',27,True,True); rr(d,(a+24,330,b-24,565),C['white'],C['green'],2,16); center(d,(a+24,330,b-24,565),'0,401 · [1, 0]\n+ 0,198 · [0, 1]\n+ 0,401 · [1, 1]',27,False,True,spacing=14); rr(d,(a+50,620,b-50,720),C['gsoft'],C['green'],3,18); center(d,(a+50,620,b-50,720),'[0,802;\n0,599]',29,True,True,color=C['green'])
    a,b=xs[5]; rr(d,(a+24,260,b-24,420),C['gsoft'],C['green'],3,18); center(d,(a+24,260,b-24,420),'output o\n[0,802;\n0,599]',27,True,True,color=C['green']); rr(d,(a+24,470,b-24,610),C['white'],C['green'],2,16); center(d,(a+24,470,b-24,610),'shape\n[dᵥ] = [2]',24,True,True); rr(d,(a+24,650,b-24,735),C['asoft'],C['amber'],2,14); center(d,(a+24,650,b-24,735),'Risultato\nillustrativo',21,True,color=C['amber'])
    for i in range(5): arrow(d,(xs[i][1]+3,470),(xs[i+1][0]-3,470),C['ink'])
    rr(d,(150,850,1650,950),C['asoft'],C['amber'],2,18); center(d,(150,850,1650,950),'Invarianti: i pesi sono non negativi e sommano a 1. L’output ha la stessa dimensione di una value.',27,True,pad=20)
    save(im,OUT2)

if __name__=='__main__': att01(); att02(); print(OUT1); print(OUT2)
