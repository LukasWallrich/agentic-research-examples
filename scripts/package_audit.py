#!/usr/bin/env python3
"""Fail on missing deliverables, unfilled numerical placeholders or broken citations."""
from pathlib import Path
import re,json,hashlib,subprocess,datetime
R=Path(__file__).resolve().parents[1]
required=['prereg/preregistration.md','prereg/provenance.json','run_all.sh','config.json','output/raw_counts.npz','output/summary.csv','output/contrasts.json','output/verification.json','output/independent_check.json','output/exploratory_checks.json','output/exploratory_grid.json','manuscript/manuscript.md','manuscript/manuscript.pdf','manuscript/manuscript.tex','manuscript/cover_letter.md','decision_log.md','novelty.md','deviations.md','review_log.md','ai_disclosure.md','weaknesses.md','manuscript/citation_check.md']
required += ['scripts/simulate.py','scripts/verify.py','scripts/independent_check.py','scripts/exploratory_checks.py','scripts/exploratory_grid.py','scripts/build_manuscript.py','scripts/render_manuscript.sh','manuscript/references.json','manuscript/reference_audit.md','output/reproducibility_check.json','reviews/coarse/r1/review_copy_r1_review.md']
required += [f'reviews/manuscript/{model}_r{n}.txt' for model in ['claude','agy'] for n in [1,2,3]]
missing=[f for f in required if not (R/f).is_file() or not (R/f).stat().st_size]
assert not missing,missing
ms=(R/'manuscript/manuscript.md').read_text();assert '{{' not in ms
refs=json.loads((R/'manuscript/references.json').read_text());ids={r['id'] for r in refs};cites=set(re.findall(r'@([a-z]+\d{4})',ms));assert cites<=ids,(cites-ids)
pro=json.loads((R/'prereg/provenance.json').read_text());p=R/'prereg/preregistration.md'
assert hashlib.sha256(p.read_bytes()).hexdigest()==pro['preregistration_sha256']
git_bytes=subprocess.check_output(['git','show',pro['commit']+':prereg/preregistration.md'],cwd=R)
assert git_bytes==p.read_bytes()
for name in ['verification','independent_check']:
    v=json.loads((R/f'output/{name}.json').read_text());assert v['passed'],name
for name in ['exploratory_checks','exploratory_grid']:
    assert json.loads((R/f'output/{name}.json').read_text())['checks_passed'],name
ledger=json.loads((R/'output/manuscript_numbers.json').read_text())
assert set(re.findall(r'\{\{(\w+)\}\}',(R/'manuscript/manuscript.template.md').read_text()))<=ledger.keys()
abstract=ms.split('# Abstract\n\n')[1].split('\n\n**Keywords')[0]
assert len(abstract.split())<=250
reproduction=json.loads((R/'output/reproducibility_check.json').read_text())
assert reproduction['passed']
for f,record in reproduction['files'].items():
    assert hashlib.sha256((R/f).read_bytes()).hexdigest()==record['after'],f
report={'passed':True,'abstract_word_count':len(abstract.split()),'manuscript_review_rounds':3,'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'required_files':required,'citation_keys':sorted(cites),'reference_count':len(refs),'unchanged_prereg_commit':pro['commit'],'numerical_ledger_entries':len(ledger),'limitations':['This checks presence, reproducibility markers, and citation identity, not human validation or novelty.','Claim support and visual layout are reviewed separately.']}
(R/'output/package_audit.json').write_text(json.dumps(report,indent=2)+'\n')
print('Package audit passed.')
