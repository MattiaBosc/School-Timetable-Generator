import random


class Teacher:
    
    def __init__(self, first_name, last_name, subject, max_hours):
        self.first_name = first_name
        self.last_name = last_name
        self.subject = subject
        self.max_hours = max_hours

    def __hash__(self):
        return hash((self.first_name, self.last_name))

    def __eq__(self, other):
        if isinstance(other, Teacher):
            return self.first_name == other.first_name and self.last_name == other.last_name
        return False
        

class Course:
    
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        self.timetable = {}


class Timetable:

    def __init__(self, teachers, courses):
        self.teachers = teachers
        self.courses = courses
        self.school_timetable = {}
"""
    def genera_orario(self):
        for course in self.courses:
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
"""
