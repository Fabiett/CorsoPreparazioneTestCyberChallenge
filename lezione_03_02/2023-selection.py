from argparse import ArgumentParser
from os.path import exists
from collections import defaultdict

# --- 

def calculate_max_global_score(N, M, S, required_skills, candidates):
    skill_to_candidates = defaultdict(list)
    # Riempi il dizionario con i candidati valutati in base alle loro competenze
    for candidate_id, skills in candidates.items():
        for skill_name, skill_score in skills:
            skill_to_candidates[skill_name].append(skill_score)
    # Ordina i candidati per ogni skill in ordine decrescente di punteggi
    for skill in skill_to_candidates:
        skill_to_candidates[skill].sort(reverse=True)
    # Assegna i candidati migliori disponibili alle rispettive skills necessarie
    global_score = 0
    for skill_name in required_skills:
        if skill_to_candidates[skill_name]:
            # Se c'è un candidato disponibile con la skill necessaria, aggiungi il suo punteggio globale
            global_score += skill_to_candidates[skill_name].pop(0)
    return global_score

# --- 

def process_input(input_lines):
    # Crea un oggetto iteratore con le linee del file di input
    input_lines = iter(input_lines)
    # Estrai il numero di casi di test
    T = int(next(input_lines))
    results = []
    for _ in range(T):
        # Estrai i parametri del caso di test
        N, M, S = map(int, next(input_lines).split())
        # Estrai le skills necessarie
        required_skills = next(input_lines).split()        
        candidates = {}
        # Estrai i candidati e le loro skills
        for _ in range(N):
            candidate_id = int(next(input_lines))
            candidate_skills = []
            for _ in range(S):
                # Estrai la skill e il punteggio del candidato
                skill, score = next(input_lines).split()
                candidate_skills.append((skill, int(score)))
                candidates[candidate_id] = candidate_skills

        # Calcola il punteggio massimo globale
        max_score = calculate_max_global_score(N, M, S, required_skills, candidates)
        results.append(max_score)
        return results

# ---

argsp = ArgumentParser()
argsp.add_argument('input', help='Input file')

filename = argsp.parse_args().input

if not exists(filename):
    print('File not found')
    exit(1)

with open(filename) as f:
    lines = [l.strip() for l in f.readlines()]

for score in process_input(lines):
    print(score)