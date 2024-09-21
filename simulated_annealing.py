import random
import math

# Funzione per generare una soluzione iniziale casuale
def genera_soluzione_iniziale(dati):
    # Crea un orario casuale, ad esempio assegnando lezioni casualmente a slot orari
    soluzione = {}
    for classe in dati['classi']:
        for materia in dati['materie']:
            # Assegna insegnante e orario casuale
            insegnante = random.choice(dati['insegnanti'][materia])
            orario = random.choice(dati['orari_disponibili'])
            aula = random.choice(dati['aule'])
            soluzione[(classe, materia)] = (insegnante, orario, aula)
    return soluzione

# Funzione di costo (più basso è il costo, migliore è la soluzione)
def calcola_costo(soluzione, dati):
    costo = 0
    for (classe, materia), (insegnante, orario, aula) in soluzione.items():
        # Verifica disponibilità dell'insegnante
        if orario not in dati['disponibilità_insegnanti'][insegnante]:
            costo += 10  # Penalità per insegnante non disponibile
        
        # Verifica capienza dell'aula
        if dati['capacità_aule'][aula] < dati['studenti_classe'][classe]:
            costo += 5  # Penalità per aula troppo piccola
        
        # Verifica che l'insegnante non abbia due lezioni contemporaneamente
        for (alt_classe, alt_materia), (alt_insegnante, alt_orario, alt_aula) in soluzione.items():
            if insegnante == alt_insegnante and orario == alt_orario and (classe, materia) != (alt_classe, alt_materia):
                costo += 20  # Penalità per sovrapposizione insegnante
        
    return costo

# Funzione di perturbazione (effettua una piccola modifica alla soluzione corrente)
def perturba(soluzione_corrente, dati):
    nuova_soluzione = soluzione_corrente.copy()
    classe, materia = random.choice(list(soluzione_corrente.keys()))
    
    # Cambia casualmente l'orario o l'aula
    if random.random() > 0.5:
        nuovo_orario = random.choice(dati['orari_disponibili'])
        nuova_soluzione[(classe, materia)] = (soluzione_corrente[(classe, materia)][0], nuovo_orario, soluzione_corrente[(classe, materia)][2])
    else:
        nuova_aula = random.choice(dati['aule'])
        nuova_soluzione[(classe, materia)] = (soluzione_corrente[(classe, materia)][0], soluzione_corrente[(classe, materia)][1], nuova_aula)
    
    return nuova_soluzione

# Funzione di accettazione (determinata dalla temperatura)
def accetta_soluzione(costo_corrente, costo_nuovo, temperatura):
    if costo_nuovo < costo_corrente:
        return True
    else:
        # Calcola probabilità di accettazione
        probabilità = math.exp((costo_corrente - costo_nuovo) / temperatura)
        return random.random() < probabilità

# Algoritmo di Simulated Annealing
def simulated_annealing(dati, temperatura_iniziale, alpha, num_iterazioni):
    soluzione_corrente = genera_soluzione_iniziale(dati)
    costo_corrente = calcola_costo(soluzione_corrente, dati)
    temperatura = temperatura_iniziale

    soluzione_migliore = soluzione_corrente
    costo_migliore = costo_corrente

    for i in range(num_iterazioni):
        nuova_soluzione = perturba(soluzione_corrente, dati)
        costo_nuovo = calcola_costo(nuova_soluzione, dati)
        
        if accetta_soluzione(costo_corrente, costo_nuovo, temperatura):
            soluzione_corrente = nuova_soluzione
            costo_corrente = costo_nuovo
            
            if costo_nuovo < costo_migliore:
                soluzione_migliore = nuova_soluzione
                costo_migliore = costo_nuovo
        
        # Raffreddamento
        temperatura = temperatura * alpha
    
    return soluzione_migliore, costo_migliore

# Esempio di dati
dati = {
    'classi': ['1A', '1B'],
    'materie': ['Matematica', 'Italiano'],
    'insegnanti': {'Matematica': ['Anna', 'Mario'], 'Italiano': ['Paolo']},
    'aule': ['Aula1', 'Aula2'],
    'orari_disponibili': ['Lun 8-10', 'Lun 10-12', 'Mar 8-10'],
    'disponibilità_insegnanti': {'Anna': ['Lun 8-10'], 'Mario': ['Lun 10-12'], 'Paolo': ['Mar 8-10']},
    'capacità_aule': {'Aula1': 30, 'Aula2': 20},
    'studenti_classe': {'1A': 25, '1B': 20}
}

# Esegui l'algoritmo
soluzione_ottima, costo_ottimo = simulated_annealing(dati, temperatura_iniziale=1000, alpha=0.95, num_iterazioni=10000)

print("Soluzione Ottimale:", soluzione_ottima)
print("Costo Ottimale:", costo_ottimo)
