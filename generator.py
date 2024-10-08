import random


class Docente:
    def __init__(self, nome, materie, max_ore, disponibilita):
        self.nome = nome
        self.materie = materie
        self.max_ore = max_ore
        self.disponibilita = disponibilita
        self.ore_associate = 0


class Classe:
    def __init__(self, nome, materie_assegnate):
        self.nome = nome
        self.materie_assegnate = materie_assegnate
        self.orario = {}


class Orario:
    def __init__(self, docenti, classi, slot_orari):
        self.docenti = docenti
        self.classi = classi
        self.slot_orari = slot_orari
        self.orario_generato = {}

    def genera_orario(self):
        for classe in self.classi:
            for materia, ore in classe.materie_assegnate.items():
                for _ in range(ore):
                    docente = self.trova_docente(materia)
                    if docente and docente.ore_associate < docente.max_ore:
                        slot = self.trova_slot_libero(classe, docente)
                        if slot:
                            self.orario_generato[(classe.nome, slot)] = (
                                materia,
                                docente.nome,
                            )
                            docente.ore_associate += 1

    def trova_docente(self, materia):
        docenti_possibili = [
            docente for docente in self.docenti if materia in docente.materie
        ]
        return random.choice(docenti_possibili) if docenti_possibili else None

    def trova_slot_libero(self, classe, docente):
        # Trova uno slot libero considerando le disponibilità
        pass

    def verifica_vincoli(self):
        # Controlla che ogni docente non abbia sovrapposizioni o ore extra
        # Controlla che ogni classe abbia tutte le lezioni necessarie
        pass

    def output(self):
        for chiave, valore in self.orario_generato.items():
            classe, slot = chiave
            materia, docente = valore
            print(f"Classe {classe} - Slot {slot}: {materia} con {docente}")
