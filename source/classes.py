import random
import copy

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
HOURS = 6

class Teacher:

    def __init__(self, subject, last_name, first_name, max_hours=0):
        self.subject = subject
        self.last_name = last_name
        self.first_name = first_name
        self.max_hours = max_hours

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.subject))

    def __eq__(self, other):
        if isinstance(other, Teacher):
            return self.first_name == other.first_name and self.last_name == other.last_name and self.subject == other.subject
        return False

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.subject})"


class Course:
    
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        self.timetable = {}


class Timetable:

    def __init__(self, teachers, courses):
        self.teachers = teachers
        self.courses = courses
        self.school_timetable = self.timetable_setup()

    def timetable_setup(self):
        """
        Set up an initial (completely full) timetable
        """
        school_timetable = {}
        for day in DAYS:
            school_timetable[f"{day}"] = [copy.deepcopy(self.teachers)] * HOURS
        return school_timetable

    def __str__(self):
        """
        Print timetable to terminal
        """
        string = ""
        for day, schedule in self.school_timetable.items():
            string += f"{day}:\n"
            for i, time_slot in enumerate(schedule):
                string += f"{i+1}°: "
                for teacher in time_slot:
                    string += f"{teacher}\n"
        return string

    def enforce_node_consistency(self):
        """
        Enforce node consistency (unary constraint) on timetable:
        remove teacher if max number of available hours is reached
        """
        for day in self.school_timetable.values():
            for time_slot in day:
                for teacher in self.teachers:
                    if teacher.max_hours <= 0:
                        time_slot.discard(teacher)

    def revise(self):
        """
        Enforce binary constraints on timetable:
        physical education requires two contiguous hours in a row
        """
        revised = False
        for day in self.school_timetable.values():
            for i, time_slot in enumerate(day):
                teacher = Teacher("MOTORIA", "BASILICO", "NICOLA")
                if i == 0:
                    if teacher not in day[i + 1]:
                        time_slot.discard(teacher)
                        revised = True
                elif i == HOURS - 1:
                    if teacher not in day[i - 1]:
                        time_slot.discard(teacher)
                        revised = True
                else:
                    if teacher not in day[i + 1] and teacher not in day[i - 1]:
                        time_slot.discard(teacher)
                        revised = True
        return revised


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
