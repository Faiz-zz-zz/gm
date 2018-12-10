import brml.*
load diseaseNet

Symptoms = 40
Diseases = 20

[pot_jt sep meta] = jtree(pot)

pot_jt = absorption(pot_jt, sep, meta)

for symptom=1:Symptoms
    pot_number = whichpot(pot_jt, 20 + symptom, 1)
    pot_symptom(symptom) = sumpot(pot_jt{pot_number}, 20 + symptom, 0).table(1)
end

%efficient

DAG = dag(pot)
for symptom=1:Symptoms
    parents_pots = pot(parents(DAG, symptom+20)) % a, b, c
    potentials = [pot(20+symptom) parents_pots] % p(d) * p(a) * p(b) * p(c)
    pot_symptom_eff(symptom) = sumpot(multpots(potentials), symptom + 20, 0).table(1)
end

% set new states
given_states = [1 1 1 1 1 2 2 2 2 2]
[pot_jt_assigned sep] = jtassignpot(setpot(pot, (1:10) + 20, given_states), meta)
pot_jt_assigned = absorption(pot_jt_assigned, sep, meta) % run absorption algo again on the modified data.

for diseas=1:Diseases
    pot_number = whichpot(pot_jt_assigned, diseas, 1)
    pot_disease(diseas) = condpot(sumpot(pot_jt_assigned{pot_number}, diseas, 0)).table(1) % normalised IPF.m
end