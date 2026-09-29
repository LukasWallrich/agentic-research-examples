#!/usr/bin/env python3
"""Build numerical prose and figures exclusively from saved simulation outputs."""
from pathlib import Path
import json,re
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator
ROOT=Path(__file__).resolve().parents[1]
O=ROOT/'output'; M=ROOT/'manuscript'
s=pd.read_csv(O/'summary.csv'); m=json.loads((O/'metadata.json').read_text()); c=m['config']
h={x['hypothesis']:x for x in json.loads((O/'contrasts.json').read_text())}
p=json.loads((ROOT/'prereg/provenance.json').read_text())
v=json.loads((O/'verification.json').read_text())
vals={}
# Values and their sources are retained as a numerical provenance ledger.
def put(key,value,source):
    vals[key]={'value':str(value),'source':source}
def f(x,d=3):return f'{x:.{d}f}'
def row(focal,schedule,n,learner):
    z=s[(s.focal==focal)&(s.schedule==schedule)&(s.n==n)&(s.learner==learner)]
    assert len(z)==1
    return z.iloc[0]
def lst(x):return ', '.join(f(a,2) for a in x)
config_values={'h_low':f(c['h_low'],2),'h_high':f(c['h_high'],2),'p_values':lst(c['p_grid']),'al_values':lst(c['a_low_grid']),'ah_values':lst(c['a_high_grid']),'r_values':lst(c['overlap_grid']),'weight_cap':int(c['weight_cap']),'tie_tolerance':str(c['tie_tolerance']),'n_values':', '.join(map(str,c['budgets'])),'k_values':', '.join(x[1:] for x in c['schedules'] if x!='random'),'replicates':f"{c['runs']:,}",'seed':c['seed'],'grid_tolerance':c['regret_tolerance']}
for k,x in config_values.items():put(k,x,'output/metadata.json:config')
put('grid_environments',m['grid_count'],'output/metadata.json:grid_count');put('total_environments',m['environment_count'],'output/metadata.json:environment_count')
put('prereg_commit',p['commit'][:7],'prereg/provenance.json:commit')
for k,x in {'interval_level':97.5,'hypothesis_count':len(h),'family_coverage':95}.items():put(k,x,'output/contrasts.json and preregistered Bonferroni rule')
z=row('crossing','d1',100,'paired'); control=row('homogeneous','d1',100,'paired')
for k,x in {'cross_a':f(z.a_low,2),'global_a':f(z.advisor_accuracy,2),'global_h':f(z.human_accuracy,2),'global_h_pct':f(100*z.human_accuracy,1),'control_al':f(control.a_low,2),'control_ah':f(control.a_high,2)}.items():put(k,x,'output/summary.csv:focal environment')
for k,which,learner,transform in [('cross_d1_accuracy','d1','absolute',lambda z:100*(z.limiting_score+z.human_accuracy)),('cross_d4_accuracy','d4','absolute',lambda z:100*(z.limiting_score+z.human_accuracy)),('cross_d1_pair','d1','paired',lambda z:z.limiting_score),('cross_d4_pair','d4','paired',lambda z:z.limiting_score),('cross_d4_ipw','d4','ipw',lambda z:z.limiting_score)]:
    put(k,f(transform(row('crossing',which,100,learner))),f'output/summary.csv:crossing/{which}/{learner}/limiting_score')
for name,x in h.items():
    low=name.lower()
    for key,val in {'verb':'reduced' if x['mean']<0 else 'increased','magnitude_pp':f(abs(x['mean'])*100),'lo_pp':f(x['ci_low']*100),'hi_pp':f(x['ci_high']*100),'n':x['n'],'k':int(x['schedule'][1:])}.items():put(low+'_'+key,val,f'output/contrasts.json:{name}')
interpretation='show that correcting selection can help or harm a finite-feedback decision' if all(x['outcome']=='supported' for x in h.values()) else 'qualify the anticipated benefit–cost tradeoff of correcting selection'
put('abstract_interpretation',interpretation,'output/contrasts.json:outcomes')
paragraphs=[]
for name,world in [('H1','crossing'),('H2','homogeneous')]:
    x=h[name]; a=row(world,x['schedule'],x['n'],'ipw'); b=row(world,x['schedule'],x['n'],'paired')
    paragraphs.append(f"{name} had the predicted direction." + f" In the {world} environment, weighted paired regret was {f(100*a.regret)} percentage points, compared with {f(100*b.regret)} for unweighted paired evaluation. The weighted-minus-paired contrast was {f(100*x['mean'])} points ({f(100*x['confidence_level'],1)}% Monte Carlo interval [{f(100*x['ci_low'])}, {f(100*x['ci_high'])}]; Monte Carlo SE = {f(100*x['mcse'],4)} points).")
put('confirmatory_text','\n\n'.join(paragraphs),'output/contrasts.json + output/summary.csv:focal rows')
table=['| Prediction | Weighted regret | Paired regret | Difference | Monte Carlo interval | Outcome |','|:--|--:|--:|--:|:--|:--|']
for name,world in [('H1','crossing'),('H2','homogeneous')]:
    x=h[name]; a=row(world,x['schedule'],x['n'],'ipw'); b=row(world,x['schedule'],x['n'],'paired')
    table.append(f"| {name} | {100*a.regret:.3f} | {100*b.regret:.3f} | {100*x['mean']:.3f} | [{100*x['ci_low']:.3f}, {100*x['ci_high']:.3f}] | {x['outcome']} |")
put('hypothesis_table','\n'.join(table),'output/contrasts.json + output/summary.csv')
table=['| Environment | Selection | Labels | Absolute | Paired | Weighted | Capped |','|:--|:--|--:|--:|--:|--:|--:|']
for world,sched,n in [('crossing','random',100),('crossing','d1',100),('crossing','d4',100),('crossing','d4',500),('homogeneous','d8',20),('homogeneous','d8',100),('homogeneous','d8',500)]:
    rates=[100*row(world,sched,n,l).adoption for l in ['absolute','paired','ipw','capped']]
    table.append('| '+ ' | '.join([world,'all cases' if sched=='random' else f'disagreements, k = {sched[1:]}',str(n)]+[f(x,1)+'%' for x in rates])+' |')
put('focal_table','\n'.join(table),'output/summary.csv:focal rows')
# Avoid implying an arbitrary grid is a population of real-world tasks.
g=s[s.grid & (s.learner=='paired') & (s.schedule=='random') & (s.n==100)]
ng=(g.delta>c['tie_tolerance']).sum(); ni=(g.delta < -c['tie_tolerance']).sum(); nt=len(g)-ng-ni
parts=[f'The scenario grid included {ng} superior-advisor environments, {ni} inferior-advisor environments, and {nt} exact marginal ties.']
for n in [20,500]:
    d=pd.read_csv(O/'descriptive_grid.csv'); d=d[(d.schedule=='d8')&(d.n==n)&(d.learner=='ipw')]
    parts.append(f"At selection ratio 8 and {n} verified outcomes, weighting had lower regret than pairing in {d.better.sum()} grid environments, higher regret in {d.worse.sum()}, and a difference within the prespecified tolerance in {d.equal.sum()}.")
rev=s[s.grid & (s.schedule=='d8')&(s.n==100)&(s.learner=='paired')].population_reversal.sum()
parts.append(f'The unweighted limiting paired sign reversed the global ordering in {rev} grid environments at that ratio. Complete results, including capped correction, all dependence settings, and lowest observed improvement budgets, are supplied in the machine-readable tables. No grid frequency is interpreted as the frequency of such environments in practice.')
put('grid_text',' '.join(parts),'output/summary.csv + output/descriptive_grid.csv')
a=row('crossing','d1',100,'paired');b=row('crossing','d4',100,'paired');d=row('homogeneous','d8',20,'paired')
put('resource_text',f'In the crossing scenario, uniform disagreement selection verified {100*a.audit_yield:.1f}% of encountered cases, requiring an expected {a.expected_opportunities:.1f} opportunities for {a.n} labels. Selection ratio {b.k} reduced yield to {100*b.audit_yield:.1f}%, requiring {b.expected_opportunities:.1f} opportunities for the same label budget. In the homogeneous control, ratio {d.k} required {d.expected_opportunities:.1f} expected opportunities for {d.n} labels. Random all-case verification requires one opportunity per label. These are expected acquisition costs under independent cases, not realised waiting times.', 'output/summary.csv:audit_yield/expected_opportunities')
put('verification_text','Numerical checks verified the joint probability tables and margins, analytic sign properties, equivalent learners under uniform weighting, and exact binomial benchmarks for the focal uniform-disagreement conditions. The saved verification report records each comparison and its prespecified Monte Carlo tolerance. No history was excluded.','output/verification.json')
put('discussion_opening',f"Within the stipulated global-adoption task, selection adjustment changed accuracy loss in opposite directions across the two focal conditions: {abs(h['H1']['mean'])*100:.2f} percentage points less loss in the crossing scenario and {h['H2']['mean']*100:.2f} points more in the homogeneous scenario. These are quantitative consequences of the model. Their practical interpretation depends on the decision being made, the feedback budget, and whether the observed cases favour the same source as future cases.",'output/contrasts.json')
put('deviation_statement','The main specification was followed; implementation clarifications and any later reviewer-requested analyses are documented in `deviations.md`.','deviations.md')
# Reviewer-requested reporting and exploratory analysis, all from saved outputs.
ind=json.loads((O/'independent_check.json').read_text()); ex=json.loads((O/'exploratory_checks.json').read_text())
put('grid_tolerance_pp',f(100*c['regret_tolerance'],2),'output/metadata.json:config.regret_tolerance')
put('cross_threshold',f(ex['misspecification_thresholds'][0]['assumed_weight_threshold'],0),'output/exploratory_checks.json:crossing sign threshold (also equal to k threshold here)')
for item in ex['conditional_oracles']:
    put('routing_cross_pct' if item['environment']=='crossing' else 'routing_control_pct',f(100*item['confidence_stratum_oracle_accuracy'],1),'output/exploratory_checks.json:conditional_oracles')
put('global_a_pct',f(100*z.advisor_accuracy,1),'output/summary.csv:advisor_accuracy')
exact={x['hypothesis']:x for x in ind['primary']}
put('confirmatory_text','Both registered contrasts had the predicted direction. Independent exact values fell inside their Monte Carlo intervals (Table 1).','output/contrasts.json + output/independent_check.json')
tab=['| Prediction | Monte Carlo difference | Exact difference | Monte Carlo interval | Direction |','|:--|--:|--:|:--|:--|']
for name,x in h.items():
    direction='weighted lower' if x['mean']<0 else 'weighted higher'
    tab.append(f"| {name} | {100*x['mean']:.3f} | {100*exact[name]['exact_contrast']:.3f} | [{100*x['ci_low']:.3f}, {100*x['ci_high']:.3f}] | {direction} |")
put('hypothesis_table','\n'.join(tab),'output/contrasts.json + output/independent_check.json')
# Grid strata preserve exact ties instead of hiding them in equal-risk counts.
q=s[s.grid & (s.schedule=='d8') & (s.n==500)].pivot(index=['env_id','delta'],columns='learner',values='regret').reset_index()
parts=[]
for label,mask in [('superior',q.delta>c['tie_tolerance']),('inferior',q.delta < -c['tie_tolerance']),('tied',q.delta.abs()<=c['tie_tolerance'])]:
    a=q[mask];diff=a.ipw-a.paired
    parts.append(f"For {label} advisors at ratio 8 and 500 labels, the lower/higher/within-tolerance regret counts for weighting versus pairing were {int((diff < -c['regret_tolerance']).sum())}/{int((diff > c['regret_tolerance']).sum())}/{int((diff.abs()<=c['regret_tolerance']).sum())} across {len(a)} environments.")
put('grid_text',vals['grid_text']['value']+' '+' '.join(parts),'output/summary.csv + output/descriptive_grid.csv; stratified by global advantage')
ties=s[s.focal.notna()][['focal','schedule','n','learner','tie_probability']]
ties.to_csv(O/'focal_tie_probabilities.csv',index=False)
put('verification_text',vals['verification_text']['value']+f" Independent exact convolution checked all {ind['focal_learner_checks']} focal learner conditions. The supplementary focal tie-probability table records ties explicitly; fair random tie-breaking is integrated into every risk.",'output/verification.json + output/independent_check.json + output/focal_tie_probabilities.csv')
pars=['The following analyses were added after seeing the registered results and are exploratory. Exact discrete score convolutions compare fixed encounter budgets and misspecified positive selection weights.']
for item in ex['focal_contrast_summaries']:
    pars.append(f"With {item['encounters']} encountered cases in the {item['environment']} environment at ratio {item['schedule'][1:]}, the expected label count was {item['expected_labels']:.1f}. Weighted and paired regret were {100*item['equal_encounter_ipw_regret']:.3f} and {100*item['equal_encounter_paired_regret']:.3f} percentage points respectively (difference {100*item['equal_encounter_ipw_minus_paired']:.3f}).")
pars.append('The contrast directions persisted at these encounter budgets, with smaller magnitudes. At fixed encounters, random all-case verification means verifying every encountered case. It has identical paired-rule risk to uniform-disagreement verification: removing agreement labels removes zero score contributions. Their label costs differ.')
pars.append('In the crossing environment, the limiting weighted ranking is correct only when the assumed low-stratum weight exceeds half the true selection ratio. Exact inverse weights need not minimise finite-feedback classification loss: an incorrect weight can emphasise a favourable stratum and improve one selected scenario while changing the target. This prevents interpreting the weighting rule as a universally optimal adoption policy.')
e2=pd.read_csv(O/'exploratory_checks.csv')
for world,sched,n in [('crossing','d4',100),('homogeneous','d8',20)]:
    a=e2[(e2.analysis=='E2_weight_misspecification')&(e2.environment==world)&(e2.schedule==sched)&(e2.budget==n)].sort_values('assumed_low_weight')
    assert len(a)==5
    weights=', '.join(str(int(w)) for w in a.assumed_low_weight)
    risks=', '.join(f(100*x) for x in a.regret)
    pars.append(f'For the {world} focal setting (true ratio {sched[1:]}, {n} labels), assumed low-stratum weights {weights} produced exact regret of {risks} percentage points, respectively.')
put('exploratory_text','\n\n'.join(pars),'output/exploratory_checks.json + output/exploratory_checks.csv:E2')
tab=['| Environment | Ratio | Labels | Paired regret | Weighted regret | Capped regret |','|:--|--:|--:|--:|--:|--:|']
for world,eid in [('crossing','e040'),('homogeneous','control')]:
    for k in [4,8]:
        for n in [20,100]:
            rates=[next(x['exact_regret'] for x in ind['checks'] if x['environment']==eid and x['schedule']==f'd{k}' and x['n']==n and x['learner']==l) for l in ['paired','ipw','capped']]
            tab.append('| '+' | '.join([world,str(k),str(n)]+[f(100*x) for x in rates])+' |')
put('matched_table','\n'.join(tab),'output/independent_check.json:matched focal cells')
ext=json.loads((O/'exploratory_grid.json').read_text())
parts=[f"A second exploratory extension crossed advisor advantages of plus or minus {abs(ext['advantage_magnitudes'][0]):.2f} in each confidence stratum with the registered stratum proportions and overlap positions. It included {ext['environment_count']} environments and {ext['rows']:,} exact learner-condition evaluations, retaining {ext['tied_environment_count']} marginal ties. All four advantage-sign patterns were represented at common ratios and budgets."]
parts.append('```{=latex}\n\\Needspace{12\\baselineskip}\n```\n')
parts.append('| Advisor advantage pattern | Minimum difference | Maximum difference |')
parts.append('|:--|--:|--:|')
for item in ext['matched_k4_n100_pattern_ranges']:
    label={'advisor_better_both':'Better in both strata','advisor_worse_both':'Worse in both strata','advisor_better_low_only':'Better only at low confidence','advisor_better_high_only':'Better only at high confidence'}[item['pattern']]
    parts.append(f"| {label} | {100*item['ipw_minus_paired_min']:.3f} | {100*item['ipw_minus_paired_max']:.3f} |")
item=ext['matched_k4_n100_pattern_ranges'][0]
parts.append(f"\n*Table 5. Exploratory ranges of weighted-minus-paired regret in percentage points at ratio {item['schedule'][1:]} and {item['n']} labels.*")
parts.append('Both crossing directions contained benefits and costs; neither same-sign pattern showed an improvement at this matched comparison. The identical minima arise at maximum-overlap environments with the same audited stratum probabilities: reversing the conditional score signs and the global superiority preserves each history’s decision loss. These exact scenario ranges are not confidence intervals and do not estimate how often each pattern occurs outside the model. The extension tests breadth over matched sign patterns while retaining a deliberately narrow advantage magnitude.')
put('extension_text',parts[0]+'\n\n'+'\n'.join(parts[1:-1])+'\n\n'+parts[-1],'output/exploratory_grid.json:matched_k4_n100_pattern_ranges + output/exploratory_grid.csv; independently verified in reviews/code/e3_minima_check.md')
# Compact reporting of the registered grid; the same-sign extension remains separate.
grid_intro=f'The registered grid included {ng} superior-advisor environments, {ni} inferior-advisor environments, and {nt} exact marginal ties. All have a positive low-confidence and nonpositive high-confidence advisor advantage. At ratio 8, the limiting paired sign reversed the global ordering in {rev} environments, all with globally superior advisors.'
tab=['| Advisor group | Labels | Lower regret | Higher regret | Within tolerance |','|:--|--:|--:|--:|--:|']
for n in [20,500]:
    d=pd.read_csv(O/'descriptive_grid.csv');d=d[(d.schedule=='d8')&(d.n==n)&(d.learner=='ipw')]
    tab.append(f"| All | {n} | {int(d.better.sum())} | {int(d.worse.sum())} | {int(d.equal.sum())} |")
for label,mask in [('Superior',q.delta>c['tie_tolerance']),('Inferior',q.delta < -c['tie_tolerance']),('Tied',q.delta.abs()<=c['tie_tolerance'])]:
    a=q[mask];diff=a.ipw-a.paired
    tab.append(f"| {label} | 500 | {int((diff < -c['regret_tolerance']).sum())} | {int((diff > c['regret_tolerance']).sum())} | {int((diff.abs()<=c['regret_tolerance']).sum())} |")
put('grid_text',grid_intro+'\n\n```{=latex}\n\\Needspace{17\\baselineskip}\n```\n\n'+'\n'.join(tab)+'\n\n*Table 3. Registered environment counts comparing weighted with paired regret at selection ratio 8. Subgroup rows partition the all-environment row at the largest registered budget; this is a finite-budget description, not an asymptotic result.*\n\nComplete results, including all capped and dependence settings, are in the machine-readable tables. Among inferior advisors, high-confidence selection supports the correct ranking; correction removes some of that support and can increase finite-label loss. No grid frequency estimates the prevalence of such environments in practice.','output/summary.csv + output/descriptive_grid.csv')
put('grid_text',vals['grid_text']['value']+f" Categories use weighted minus paired regret: below -{c['regret_tolerance']}, within the inclusive bounds ±{c['regret_tolerance']}, or above {c['regret_tolerance']} in proportion units.",'output/summary.csv + output/descriptive_grid.csv + metadata tolerance')

text=(M/'manuscript.template.md').read_text()
missing=set(re.findall(r'\{\{(\w+)\}\}',text))-vals.keys();assert not missing,missing
text=re.sub(r'\{\{(\w+)\}\}',lambda x:vals[x[1]]['value'],text)
# APA narrative citation syntax avoids repeating authors before parenthetical citations.
for author,key in [('Pescetelli and Yeung','pescetelli2021'),('Jaquiery and Yeung','jaquiery2024'),('Denrell and March','denrell2001'),('Denrell','denrell2005'),('Fetchenhauer and Dunning','fetchenhauer2010'),('Fok and Weld','fok2024'),('Honeycutt et al.','honeycutt2020'),('Gao et al.','gao2021'),('Zavattari et al.','zavattari2026'),('Li and Steyvers','li2026')]:
    text=text.replace(f'{author} [@{key}]',f'{author} [-@{key}]')
(M/'manuscript.md').write_text(text)
(O/'manuscript_numbers.json').write_text(json.dumps(vals,indent=2)+'\n')
(M/'figures').mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':150})
fig,axs=plt.subplots(1,2,figsize=(8.5,3.7),sharey=True)
colours={'absolute':'#999999','paired':'#0072B2','ipw':'#D55E00','capped':'#009E73'}
labels={'absolute':'Absolute','paired':'Paired','ipw':'Weighted','capped':'Capped'}
for ax,world,k in zip(axs,['crossing','homogeneous'],[4,8]):
    for learner in colours:
        d=s[(s.focal==world)&(s.schedule==f'd{k}')&(s.learner==learner)].sort_values('n')
        ax.errorbar(d.n,100*d.regret,yerr=100*c['contrast_z']*d.regret_mcse,marker='o',label=labels[learner],color=colours[learner],linewidth=1.7,capsize=2)
    ax.set_xscale('log');ax.xaxis.set_minor_locator(NullLocator());ax.set_xticks(c['budgets'],[str(x) for x in c['budgets']]);ax.set_xlabel('Verified outcomes');ax.set_title(f'{world.capitalize()} advantage (ratio {k})');ax.grid(axis='y',alpha=.2)
axs[0].set_ylabel('Deployment regret (percentage points)');axs[1].legend(frameon=False)
fig.tight_layout();fig.savefig(M/'figures/focal_regret.png',dpi=220);fig.savefig(M/'figures/focal_regret.pdf');plt.close(fig)
print('Built manuscript.md, numerical ledger, and focal figures.')
