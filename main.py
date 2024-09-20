import classes_sin as cs

df = cs.get_info()
docente = []
courses = []
slot_orari={}

#teachers.iloc[0,4:]
#teachers.columns[4:]
#teachers['last_name'].loc[teachers['1LS']!=0]
#docenti_assegnati[course]=list(df['last_name'].iloc[1:].loc[df[course]!=0])
#for row in df.values[1:]:
"""
Inizialization of a list (courses) with objects Classe
In the object Classe, there is: name_course, teachers in the course, 
total hour and orario
docenti_assegnati has to be a dictionary with name of the teacher and hours in that course - done
"""

for index, nam_course in enumerate(df.columns[4:]):
    docenti_assegnati={}
    ore=int(df.iloc[0, 4+index])
    df_auxiliar = df.loc[:,['last_name', nam_course]]
    for insegnante in df_auxiliar.values[1:]:
        if insegnante[1]!=0:
            docenti_assegnati[insegnante[0]]=insegnante[1]
    course = cs.Classe(nam_course,docenti_assegnati,ore)
    courses.append(course)
"""
Inizialization of a list (docente) with objects Docente
In the object Docente, there is last_name, name, subjects, max_hours, 
courses and allocated hours (ore_associate)
"""

for row in df.values[1:]:
    classi = {}
    i=4
    while i < len(row):
        if row[i]!=0:
            classi[df.columns[i]] = row[i]
        i+=1
    insegnante = cs.Docente(row[1], row[2], row[0], row[3], classi)
    docente.append(insegnante)

"""
Inizializzation of slot_orari: each course has a timeschedule structure for the 
different days based on the name_course
"""

n_day = [-1, -1, -1, -1, -1, -1]
p1_day = [-1, -1, -1, -1, -1, 'L', -1, -1]
p2_day = [-1, -1, -1, -1, -1, 'L', -1, -1, -1]
for classe in courses:
    if ('1LS' or '2LS') in classe.nome:
        slot_orari[classe.nome]={'Lun': [-1, -1, -1, -1, -1, -1], 'Mar': [-1, -1, -1, -1, -1, -1], 'Mer': [-1, -1, -1, -1, -1, -1], 'Gio': [-1, -1, -1, -1, -1, -1], 'Ven': [-1, -1, -1, -1, -1, -1]}
    elif('3LS' or '4LS') in classe.nome:
        slot_orari[classe.nome] = {'Lun': [-1, -1, -1, -1, -1, -1], 'Mar': [-1, -1, -1, -1, -1, 'L', -1, -1, -1], 'Mer': [-1, -1, -1, -1, -1, -1], 'Gio': [-1, -1, -1, -1, -1, -1], 'Ven': [-1, -1, -1, -1, -1, 'L', -1, -1]}
    elif('5LS') in classe.nome:
        slot_orari[classe.nome] = {'Lun': [-1, -1, -1, -1, -1, -1], 'Mar': [-1, -1, -1, -1, -1, 'L', -1, -1], 'Mer': [-1, -1, -1, -1, -1, -1], 'Gio': [-1, -1, -1, -1, -1, -1], 'Ven': [-1, -1, -1, -1, -1, 'L', -1, -1]}

"""
Inizializzation object orario
"""
orario=cs.Orario(docente,courses,slot_orari)
orario.genera_orario()






