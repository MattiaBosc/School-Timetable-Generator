import classes_sin

teachers = classes_sin.get_teachers()
docente = []
courses = {}
docenti_assegnati = {}

#print(teachers.iloc[0,4:])
#print(teachers.columns[4:])
#print(teachers['last_name'].loc[teachers['1LS']!=0])

for index, course in enumerate(teachers.columns[4:]):
    courses[course]=int(teachers.iloc[0,4+index])
    docenti_assegnati[course]=list(teachers['last_name'].iloc[1:].loc[teachers[course]!=0])

print(courses)
print(docenti_assegnati)
print(teachers.iloc[2,0])
i_max= len(teachers['last_name'])-1
j_max= len(teachers.iloc[0,:]))
i=1
while i < i_max:
    classes_sin.Docente(teachers.iloc[0,:][1], row[2], row[0], row[3], row[4])
    docente.append(classes_sin.Docente)
for row in teachers.iloc[2:,0:4]:
    print(row)
    classes_sin.Docente(row[1], row[2], row[0], row[3], row[4])
    docente.append(classes_sin.Docente)

print(docente)

for course in courses.key():
    for insegnante in docente:
        if f'insegnante.{course}'!=0:
            docenti_assegnati[str(course)].append(insegnante.cognome)



