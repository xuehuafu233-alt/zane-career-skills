#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, re, sys

def sha(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(65536),b''): h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('manifest')
    args=ap.parse_args()
    mp=pathlib.Path(args.manifest).resolve(); root=mp.parent
    data=json.loads(mp.read_text(encoding='utf-8'))
    errors=[]; warnings=[]
    website=data.get('website',{}); primary=website.get('primary','')
    if primary:
        p=(root/primary).resolve()
        if not p.exists(): errors.append(f'missing primary website: {p}')
        else:
            digest=sha(p)
            for rel in website.get('replicas',[]):
                r=(root/rel).resolve()
                if not r.exists(): errors.append(f'missing replica: {r}')
                elif sha(r)!=digest: errors.append(f'replica differs: {r}')
    patterns=[re.compile(re.escape(x),re.I) for x in data.get('sensitive_terms',[]) if x]
    scan_ext={'.html','.md','.txt','.json','.csv','.py','.js','.css'}
    for p in root.rglob('*'):
        if p.resolve()==mp:
            continue
        if p.is_file() and p.suffix.lower() in scan_ext and '.git' not in p.parts:
            try: text=p.read_text(encoding='utf-8')
            except UnicodeDecodeError: continue
            for pat in patterns:
                if pat.search(text): warnings.append(f'sensitive-term review: {p.relative_to(root)} -> {pat.pattern}')
    qa=data.get('qa',{})
    for key,val in qa.items():
        if not val: warnings.append(f'qa incomplete: {key}')
    print(json.dumps({'errors':errors,'warnings':warnings},ensure_ascii=False,indent=2))
    return 1 if errors else 0

if __name__=='__main__': sys.exit(main())
