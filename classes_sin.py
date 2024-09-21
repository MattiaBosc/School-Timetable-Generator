import random
import csv
import pandas as pd
import numpy as np

TABELLA_ORARIO={'1LS':{'LUN':[i for i in range(0,6)],
                       'MAR':[i for i in range(0,6)],
                       'MER': [i for i in range(0,6)],
                       'GIO': [i for i in range(0,6)],
                       'VEN':[i for i in range(0,6)]}}


class Docente:
    def __init__(self, cognome, nome, materia, max_ore, classi):
        self.cognome = cognome
        self.nome = nome
        self.materia = materia
        self.max_ore = max_ore
        self.classi = classi
        self.ore_associate = 0
        self.orario_settimana = {'LUN':[" " for i in range(0,6)],
                  'MAR':[" " for i in range(0,9)],
                  'MER': [" " for i in range(0,6)],
                  'GIO': [" " for i in range(0,6)],
                  'VEN':[" " for i in range(0,9)]}

class Classe:
    def __init__(self, nome, docenti_assegnati, tot_ore):
        self.nome = nome
        self.docenti_assegnati = docenti_assegnati
        self.tot_ore = tot_ore
        self.orario = {}

class Orario:
    def __init__(self, docenti, classi, slot_orari):
        self.docenti = docenti
        self.classi = classi
        self.slot_orari = slot_orari
        self.orario_generato = {}

    def genera_orario(self):
        for classe in self.classi:
            #print(classe.nome)
            for ln_docente, ore in classe.docenti_assegnati.items():
                #print(docente, ore)
                for _ in range(ore):
                    #print(_)
                    slot, (day, hour) = self.trova_slot_libero(classe)
                    self.orario_generato[(classe.nome, slot)] = (ln_docente)
                    for teacher in self.docenti:
                        if teacher.cognome == ln_docente:
                            teacher.orario_settimana[day][hour] = classe.nome
                    #print(self.orario_generato[(classe.nome, slot)])
                    #print(docente.ore_associate)
                    #docente.ore_associate += 1
        #print(self.orario_generato)
        self.output()

    def trova_slot_libero(self, classe):
        # Trova uno slot libero considerando le disponibilità
        free_hour = False
        while free_hour == False:
            ora = random.randint(1, classe.tot_ore)
            ore_lun = len(self.slot_orari[classe.nome]['Lun'])
            ore_mar = len(self.slot_orari[classe.nome]['Mar'])
            ore_mer = len(self.slot_orari[classe.nome]['Mer'])
            ore_gio = len(self.slot_orari[classe.nome]['Gio'])
            ore_ven = len(self.slot_orari[classe.nome]['Ven'])
            if ora <= ore_lun:
                ora_lun = ora - 1
                #print(ora, 'Lun')
                if self.slot_orari[classe.nome]['Lun'][ora_lun] == -1:
                    self.slot_orari[classe.nome]['Lun'][ora_lun] = 0
                    #print(f"Lunedì: {ora}")
                    return ora, ('LUN', ora_lun)
                else:
                    #print(f"Lunedì - Ora occupata: {ora}")
                    #print(self.slot_orari[classe.nome]['Lun'][ora_lun])
                    continue

            elif ore_lun < ora <= (ore_lun+ore_mar):
                ora_mar = ora - ore_lun-1
                #print(ora, 'Mar')
                if self.slot_orari[classe.nome]['Mar'][ora_mar] == -1:
                    self.slot_orari[classe.nome]['Mar'][ora_mar] = 0
                    #print(f"Martedì: {ora}")
                    return ora, ('MAR', ora_mar)
                else:
                    #print(f"Martedì - Ora occupata: {ora}")
                    #print(self.slot_orari[classe.nome]['Mar'][ora_mar])
                    continue

            elif (ore_lun + ore_mar) < ora <= (ore_lun+ore_mar+ore_mer):
                ora_mer = ora - (ore_lun+ore_mar)-1
                #print(ora, 'Mer')
                if self.slot_orari[classe.nome]['Mer'][ora_mer] == -1:
                    self.slot_orari[classe.nome]['Mer'][ora_mer] = 0
                    #print(f"Mercoledì: {ora}")
                    return ora, ('MER', ora_mer)
                else:
                    #print(f"Mercoledì - Ora occupata: {ora}")
                    #print(self.slot_orari[classe.nome]['Mer'][ora_mer])
                    continue

            elif (ore_lun+ore_mar+ore_mer) < ora <= (ore_lun+ore_mar+ore_mer+ore_gio):
                ora_gio = ora - (ore_lun+ore_mar+ore_mer)-1
                #print(ora, 'Gio')
                if self.slot_orari[classe.nome]['Gio'][ora_gio] == -1:
                    self.slot_orari[classe.nome]['Gio'][ora_gio] = 0
                    #print(f"Giovedì: {ora}")
                    return ora, ('GIO', ora_gio)
                else:
                    #print(f"Giovedì - Ora occupata: {ora}")
                    #print(self.slot_orari[classe.nome]['Gio'][ora_gio])
                    continue

            elif (ore_lun+ore_mar+ore_mer+ore_gio) < ora <= (ore_lun+ore_mar+ore_mer+ore_gio+ore_ven):
                ora_ven = ora - (ore_lun+ore_mar+ore_mer+ore_gio)-1
                #print(ora, 'Ven')
                if self.slot_orari[classe.nome]['Ven'][ora_ven] == -1:
                    self.slot_orari[classe.nome]['Ven'][ora_ven] = 0
                    #print(f"Venerdì: {ora}")
                    return ora, ('VEN', ora_ven)
                else:
                    #print(f"Venerdì - Ora occupata: {ora}")
                    #print(self.slot_orari[classe.nome]['Ven'][ora_ven])
                    continue
            else:
                print(ora, "Not valid number")
                break


    def verifica_vincoli(self):
        # Controlla che ogni docente non abbia sovrapposizioni o ore extra
        # Controlla che ogni classe abbia tutte le lezioni necessarie
        pass

    def output(self):
        #print(TABELLA_ORARIO)
        list_courses = list(TABELLA_ORARIO.keys())
        nday_to_wday={0: 'LUN', 1: 'MAR', 2: 'MER', 3: 'GIO', 4: 'VEN'}
        for chiave, valore in self.orario_generato.items():
            classe, slot = chiave
            ln_docente = valore
            slot -=1
            if classe == list_courses[0]:
                nday = slot//6
                hour = slot%6
                wday=nday_to_wday[nday]
                TABELLA_ORARIO[classe][wday][hour]=ln_docente

        with open('output_orario/orario.csv', 'w') as file:
            for pr_class in TABELLA_ORARIO.keys():
                file.write(pr_class + '\n')
                for pr_day in TABELLA_ORARIO[pr_class].keys():
                    line = str(pr_day + ":")
                    file.write(line)
                    for item in TABELLA_ORARIO[pr_class][pr_day]:
                        file.writelines(item+" ")
                    file.write('\n')

            for teacher in self.docenti:
                file.write(teacher.cognome + ": ")
                for pr_day in teacher.orario_settimana.keys():
                    line = str(pr_day + ":")
                    file.write(line)
                    for item in teacher.orario_settimana[pr_day]:
                        file.write(item + " ")
                file.write('\n')
                #line_teacher=str(teacher.orario_settimana) + "\n"
                #file.write(line_teacher)
        """   
        for pr_class in TABELLA_ORARIO.keys():
            print(pr_class)
            
            for pr_day in TABELLA_ORARIO[pr_class].keys():
                print(pr_day+":", end="")
                print(TABELLA_ORARIO[pr_class][pr_day])
                    """
            #if classe==TABELLA_ORARIO.keys
            #print(f"Classe {classe} - Slot {slot}: {docente}")

def get_info(filepath='input_orario/teachers.csv'):
    """ Read a text file and return the list of
    all the teachers.
    """
    with open(filepath, 'r') as file_local:
        info = pd.read_csv(file_local)
    return info