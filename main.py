import classes_sin

df = classes_sin.get_info()
docente = []
courses = []
docenti_assegnati = {}

#teachers.iloc[0,4:]
#teachers.columns[4:]
#teachers['last_name'].loc[teachers['1LS']!=0]
#docenti_assegnati[course]=list(df['last_name'].iloc[1:].loc[df[course]!=0])
#for row in df.values[1:]:

for index, nam_course in enumerate(df.columns[4:]):
    ore=int(df.iloc[0, 4+index])
    docenti_assegnati[nam_course]=list(df['last_name'].iloc[1:].loc[df[nam_course]!=0])
    course = classes_sin.Classe(nam_course,docenti_assegnati[nam_course],ore)
    courses.append(course)

for row in df.values[1:]:
    classi = {}
    i=4
    while i < len(row):
        if row[i]!=0:
            classi[df.columns[i]] = row[i]
        i+=1
    insegnante = classes_sin.Docente(row[1], row[2], row[0], row[3], classi)
    docente.append(insegnante)






