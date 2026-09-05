#!/usr/bin/env python3
"""Backtest of selection rules on the S&P 500, 2006-2025 purchase years.
Inputs: monthly.json (Yahoo monthly adjusted closes per ticker), members.json (year-end
constituents). Selection at the start of year y uses data through Dec y-1 and the
constituent list at year-end y-1. Two evaluations per rule: hold one year (Dec y-1 -> Dec y)
and hold to Aug 2026 (the reel's framing), each vs the S&P 500 total-return index."""
import json, math, statistics as st, sys, random
D=json.load(open("monthly.json"))["data"]; M=json.load(open("members.json"))
I="^SP500TR"; YEARS=list(range(2006,2026)); END="2026-08"
def a(t,y,m): return D.get(t,{}).get(f"{y}-{m:02d}")
def dec(t,y): return a(t,y,12)
def ret(t,y):
    p,q=dec(t,y-1),dec(t,y); return None if not p or not q else q/p-1
def multi(t,y,n):
    p,q=dec(t,y-n),dec(t,y); return None if not p or not q else q/p-1
def m121(t,y):  # Dec y-1 -> Nov y (skip last month)
    p,q=dec(t,y-1),a(t,y,11); return None if not p or not q else q/p-1
def vol(t,y):
    xs=[a(t,y,m) for m in range(1,13)]; xs=[dec(t,y-1)]+xs
    if any(x is None for x in xs): return None
    lr=[math.log(xs[i]/xs[i-1]) for i in range(1,len(xs))]; return st.pstdev(lr)*math.sqrt(12)
def hold_end(t,y):
    p=dec(t,y-1); m=D.get(t,{})
    if not p or not m: return None
    q=m.get(END)
    if q is None:  # delisted after Dec y-1: value at the last available month
        ks=[k for k in m if k<=END and k>f"{y-1}-12"]
        if not ks: return None
        q=m[max(ks)]
    return q/p
UNI={}
for y in YEARS:
    UNI[y]=[t for t in M[str(y-1)] if t in D and ret(t,y-1) is not None and not t.startswith('^')]
JUNK={"UVN","CBE","PBG","TIE","MEE","GR","EP"}
for y in YEARS: UNI[y]=[t for t in UNI[y] if t not in JUNK]
def ranked(y,key=lambda t,y: ret(t,y-1)):
    xs=[(key(t,y),t) for t in UNI[y]]; xs=[(v,t) for v,t in xs if v is not None]; xs.sort(reverse=True); return [t for v,t in xs]
# ---- rules: each returns a list of tickers for purchase year y
def rank(k): return lambda y: ranked(y)[k-1:k]
def top(n): return lambda y: ranked(y)[:n]
def bucket(lo,hi): return lambda y: ranked(y)[lo-1:hi]
def bottom(n): return lambda y: ranked(y)[-n:]
def mid(n): return lambda y: (lambda r: r[len(r)//2-n//2:len(r)//2+n//2])(ranked(y))
def mom(nyr,n): return lambda y: ranked(y,lambda t,y: multi(t,y-1,nyr))[:n]
def m121top(n): return lambda y: ranked(y,lambda t,y: m121(t,y-1))[:n]
def lowvol(n): return lambda y: ranked(y,lambda t,y: (lambda v: None if v is None else -v)(vol(t,y-1)))[:n]
def highvol(n): return lambda y: ranked(y,lambda t,y: vol(t,y-1))[:n]
def mom_lowvol(k,n):
    def f(y):
        cand=ranked(y)[:k]; xs=[(vol(t,y-1),t) for t in cand]; xs=[(v,t) for v,t in xs if v is not None]; xs.sort(); return [t for v,t in xs[:n]]
    return f
def consistent(n,yrs=3):
    def f(y):
        ok=[t for t in UNI[y] if all((ret(t,y-1-i) or -1)>0 for i in range(yrs))]
        xs=sorted([(ret(t,y-1),t) for t in ok],reverse=True); return [t for v,t in xs[:n]]
    return f
def steady(n,yrs=3):  # best 3-year return among stocks positive in each of the last 3 years, low vol tie-break
    def f(y):
        ok=[t for t in UNI[y] if all((ret(t,y-1-i) or -1)>0 for i in range(yrs))]
        xs=sorted([(multi(t,y-1,yrs) or -9,t) for t in ok],reverse=True); return [t for v,t in xs[:n]]
    return f
def beat_idx_lowvol(n):  # beat the index last year, then lowest vol
    def f(y):
        ri=ret(I,y-1); cand=[t for t in UNI[y] if ret(t,y-1)>ri]
        xs=sorted([(vol(t,y-1) or 9,t) for t in cand]); return [t for v,t in xs[:n]]
    return f
def allew(): return lambda y: UNI[y]
RULES=[
 ("Reel: #1 of prior year",rank(1)),("#2 of prior year",rank(2)),("#3",rank(3)),("#5",rank(5)),("#10",rank(10)),
 ("Top 3 equal-weight",top(3)),("Top 5",top(5)),("Top 10",top(10)),("Top 25",top(25)),("Top 50 (decile)",top(50)),
 ("Ranks 2-5",bucket(2,5)),("Ranks 6-10",bucket(6,10)),("Ranks 11-25",bucket(11,25)),("Ranks 26-50",bucket(26,50)),
 ("Ranks 51-100",bucket(51,100)),("Ranks 101-200",bucket(101,200)),("Middle 50",mid(50)),
 ("Bottom 50",bottom(50)),("Bottom 10",bottom(10)),("Worst 1",bottom(1)),
 ("3-yr momentum #1",mom(3,1)),("3-yr momentum top 10",mom(3,10)),("5-yr momentum top 10",mom(5,10)),
 ("12-1 momentum #1",m121top(1)),("12-1 momentum top 10",m121top(10)),("12-1 momentum top 50",m121top(50)),
 ("Lowest vol 10",lowvol(10)),("Lowest vol 50",lowvol(50)),("Highest vol 10",highvol(10)),
 ("Top 50 by return, lowest-vol 10",mom_lowvol(50,10)),("Top 100 by return, lowest-vol 25",mom_lowvol(100,25)),
 ("Up 3 yrs running, top 10 last yr",consistent(10)),("Up 3 yrs running, top 25 last yr",consistent(25)),
 ("Up 3 yrs running, best 3-yr top 10",steady(10)),("Beat index last yr, lowest-vol 10",beat_idx_lowvol(10)),("Beat index last yr, lowest-vol 25",beat_idx_lowvol(25)),
 ("Top 3 by 12-1 momentum",m121top(3)),("Up 3 yrs running, top 3 last yr",consistent(3)),("Up 3 yrs running, top 5 last yr",consistent(5)),("All constituents equal-weight",allew()),
]
def evaluate(rule):
    r1=[];rI=[];g=[];gI=[];sizes=[];miss=0;picks={}
    for y in YEARS:
        sel=rule(y); picks[y]=sel[:3]
        xs=[ret(t,y) for t in sel]; xs=[x for x in xs if x is not None]
        if not xs: continue
        miss+=len(sel)-len(xs); sizes.append(len(xs))
        r1.append(st.mean(xs)); rI.append(ret(I,y))
        hs=[hold_end(t,y) for t in sel]; hs=[h for h in hs if h is not None]
        g.append(st.mean(hs)*1000); gI.append(hold_end(I,y)*1000)
    ex=[x-i for x,i in zip(r1,rI)]
    cum=math.prod(1+x for x in r1); cumI=math.prod(1+x for x in rI); n=len(r1)
    return dict(n=n,wins=sum(e>0 for e in ex),med=st.median(ex),mean=st.mean(ex),cagr=cum**(1/n)-1,cagrI=cumI**(1/n)-1,
                hold=sum(g),holdI=sum(gI),hwins=sum(x>i for x,i in zip(g,gI)),size=st.mean(sizes),miss=miss,ex=ex,r1=r1,picks=picks)
if __name__=="__main__":
    base=[st.mean(1 if ret(t,y)>ret(I,y) else 0 for t in UNI[y]) for y in YEARS]
    print(f"universe sizes {min(len(UNI[y]) for y in YEARS)}-{max(len(UNI[y]) for y in YEARS)}; share of stocks beating index each year: median {st.median(base)*100:.0f}%, range {min(base)*100:.0f}-{max(base)*100:.0f}%")
    print("index 1y returns: "+" ".join(f"{y}:{ret(I,y)*100:+.0f}" for y in YEARS))
    print(f"\n{'rule':<38}{'yrs':>4}{'1y wins':>8}{'med exc':>9}{'mean exc':>9}{'CAGR':>7}{'idx':>7}{'hold-end $':>11}{'idx $':>9}{'h wins':>7}{'size':>6}{'miss':>5}")
    out={}
    for name,rule in RULES:
        e=evaluate(rule); out[name]=e
        print(f"{name:<38}{e['n']:>4}{e['wins']:>8}{e['med']*100:>8.1f}%{e['mean']*100:>8.1f}%{e['cagr']*100:>6.1f}%{e['cagrI']*100:>6.1f}%{e['hold']:>11,.0f}{e['holdI']:>9,.0f}{e['hwins']:>7}{e['size']:>6.1f}{e['miss']:>5}")
    print("\nPer-year excess (1y hold) for selected rules:")
    for name in ["Reel: #1 of prior year","#3","Top 3 equal-weight","Top 5","Top 10","Ranks 26-50","Lowest vol 50","Beat index last yr, lowest-vol 25","Up 3 yrs running, top 25 last yr","12-1 momentum top 50","All constituents equal-weight"]:
        e=out[name]; print(f"{name:<38}"+" ".join(f"{x*100:+.0f}" for x in e['ex']))
    print("\nTop-3 picks by year for #1 and a few rules:")
    for name in ["Reel: #1 of prior year","#3","Top 3 equal-weight","Beat index last yr, lowest-vol 10","Up 3 yrs running, top 10 last yr","Lowest vol 10"]:
        e=out[name]; print(name+": "+" ".join(f"{y}:{','.join(e['picks'][y])}" for y in YEARS))
    json.dump({k:{kk:vv for kk,vv in v.items() if kk!='picks'} for k,v in out.items()},open("strat_results.json","w"))
