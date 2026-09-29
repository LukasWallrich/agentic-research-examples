"""Build the manuscript bibliography from saved registry metadata (no credentials)."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
META=ROOT/'scoping/reference_metadata'
refs=[]
items=[('pescetelli2021','10.1037/xge0000960'),('jaquiery2024','10.1371/journal.pone.0311211'),('fetchenhauer2010','10.1177/0956797609358586'),('denrell2005','10.1037/0033-295x.112.4.951'),('honeycutt2020','10.1609/hcomp.v8i1.7464'),('denrell2001','10.1287/orsc.12.5.523.10092'),('fok2024','10.1002/aaai.12182'),('gao2021','10.24963/ijcai.2021/237'),('einhorn1978','10.1037/0033-295x.85.5.395'),('mcnemar1947','10.1007/bf02295996'),('elwin2007','10.1111/j.1467-9280.2007.01856.x')]
for key,doi in items:
 m=json.loads((META/(doi.replace('/','_')+'_crossref.json')).read_text())['message']
 title=m['title'][0]
 if m.get('subtitle'): title+=' '+': '.join(m['subtitle']) if title.endswith('?') else ': '+': '.join(m['subtitle'])
 r={'id':key,'type':'paper-conference' if doi.startswith('10.24963') else 'article-journal','title':title.rstrip('.'),'author':[{k:a[k] for k in ['family','given'] if k in a} for a in m['author']],'issued':m['published'],'DOI':m['DOI'],'URL':'https://doi.org/'+m['DOI']}
 for field in ['container-title','volume','issue','page','publisher']:
  if field in m:r[field]=m[field][0] if isinstance(m[field],list) else m[field]
 if key=='honeycutt2020':
  r['author'][0]['given']='Donald R.';r['author'][2]['given']='Eric D.';r['issue']='1'
 refs.append(r)
for key,doi in [('zavattari2026','10.48550/arxiv.2607.28317'),('li2026','10.48550/arxiv.2603.22634')]:
 m=json.loads((META/(doi.replace('/','_')+'_datacite.json')).read_text())['data']['attributes']
 refs.append({'id':key,'type':'article','title':m['titles'][0]['title'].replace('$N$','N'),'author':[{'family':a['familyName'],'given':a['givenName']} for a in m['creators']],'issued':{'date-parts':[[m['publicationYear']]]},'DOI':m['doi'],'URL':m['url'],'publisher':'arXiv','genre':'Preprint','note':'Preprint; DOI registered with DataCite (Crossref query returned HTTP 404).','number':doi.split('arxiv.')[1]})
# Explicit APA display titles preserve acronyms and mathematical symbols.
# Registry titles remain unchanged in the raw source records.
display_titles = {
 'elwin2007': 'Constructivist coding: Learning from selective feedback',
 'pescetelli2021': 'The role of decision confidence in advice-taking and trust formation',
 'jaquiery2024': 'Preferences for advisor agreement and accuracy',
 'fetchenhauer2010': 'Why so cynical? Asymmetric feedback underlies misguided skepticism regarding the trustworthiness of others',
 'denrell2005': 'Why most people disapprove of me: Experience sampling in impression formation',
 'honeycutt2020': 'Soliciting human-in-the-loop user feedback for interactive machine learning reduces user trust and impressions of model accuracy',
 'denrell2001': 'Adaptation as information restriction: The hot stove effect',
 'fok2024': 'In search of verifiability: Explanations rarely enable complementary performance in AI-advised decision making',
 'gao2021': 'Human-AI collaboration with bandit feedback',
 'zavattari2026': 'One human, N agents: Audit-budget allocation for LLM agent fleets under miscalibrated, correlated confidence',
 'li2026': 'Learning to trust: How humans mentally recalibrate AI confidence signals',
 'einhorn1978': 'Confidence in judgment: Persistence of the illusion of validity',
 'mcnemar1947': 'Note on the sampling error of the difference between correlated proportions or percentages',
}
for ref in refs:
 ref['title'] = display_titles[ref['id']]
(ROOT/'manuscript/references.json').write_text(json.dumps(refs,ensure_ascii=False,indent=2)+'\n')
print('Wrote',len(refs),'CSL JSON references')
