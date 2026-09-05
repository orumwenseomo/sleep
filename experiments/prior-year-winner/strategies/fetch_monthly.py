#!/usr/bin/env python3
"""Downloads monthly split- and dividend-adjusted closes from Yahoo Finance for every ticker
that appears in the S&P 500 historical constituent lists (github.com/fja05680/sp500), plus
^SP500TR and ^GSPC, and writes monthly.json ({"data": {ticker: {"YYYY-MM": adjclose}}}) and
members.json ({year: [tickers at that year-end]}). Run with a shard index to parallelise:
    python3 fetch_monthly.py 0 4   # shard 0 of 4 -> monthly_0.json
Then merge the shards into monthly.json. Yahoo no longer serves ~270 delisted tickers; those
are simply absent (see README for the survivorship caveat)."""
import json, urllib.request, urllib.parse, datetime as dt, time, calendar, sys, csv, os, subprocess
k=int(sys.argv[1]) if len(sys.argv)>1 else 0; K=int(sys.argv[2]) if len(sys.argv)>2 else 1
if not os.path.exists("members.json"):
    if not os.path.exists("sp500"): subprocess.run(["git","clone","--depth","1","-q","https://github.com/fja05680/sp500","sp500"],check=True)
    rows=list(csv.DictReader(open("sp500/S&P 500 Historical Components & Changes (Updated).csv")))
    rows=sorted([(dt.date.fromisoformat(r['date']), set(r['tickers'].split(','))) for r in rows])
    ye={y:sorted([r for r in rows if r[0]<=dt.date(y,12,31)][-1][1]) for y in range(2003,2026)}
    json.dump(ye,open("members.json","w"))
M=json.load(open("members.json"))
allt=sorted(set().union(*[set(v) for v in M.values()]))+["^SP500TR","^GSPC"]
allt=[t for i,t in enumerate(allt) if i%K==k]
p1=int(calendar.timegm((2002,12,1,0,0,0))); p2=int(time.time())
data={}; err=[]
for i,t in enumerate(allt):
    yt=t.replace('.','-') if not t.startswith('^') else t
    u=f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(yt)}?period1={p1}&period2={p2}&interval=1mo&events=div,splits"
    for attempt in range(2):
        try:
            r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"})
            d=json.load(urllib.request.urlopen(r,timeout=30))["chart"]["result"][0]
            m={}
            for x,a in zip(d["timestamp"],d["indicators"]["adjclose"][0]["adjclose"]):
                if a is None or a<=0: continue
                day=dt.datetime.utcfromtimestamp(x).date(); m[f"{day.year}-{day.month:02d}"]=round(a,4)
            if m: data[t]=m
            break
        except Exception as e:
            if attempt==1: err.append((t,str(e)[:40]))
            time.sleep(0.5)
    if i%25==0: print(f"{i}/{len(allt)} {t} ok={len(data)}",flush=True)
    time.sleep(0.05)
json.dump({"data":data,"err":err},open(f"monthly_{k}.json" if K>1 else "monthly.json","w"))
print(f"DONE ok={len(data)} err={len(err)}")
