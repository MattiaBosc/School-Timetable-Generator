import classes_sin

teachers = classes_sin.get_teachers()
docente = []
courses = {}
docenti_assegnati = {}

for index,course in enumerate(teachers[0][4:]):
    courses[str(course)]=int(teachers[1][index+4])
    docenti_assegnati[str(course)] = []

for row in teachers[2:]:
    classes_sin.Docente(row[1], row[2], row[0], row[3], row[4])
    docente.append(classes_sin.Docente)

for course in courses.key():
    for insegnante in docente:
        if f'insegnante.{course}'!=0:
            docenti_assegnati[str(course)].append(insegnante.cognome)



