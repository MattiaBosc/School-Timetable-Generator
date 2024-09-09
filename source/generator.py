import csv
import os
from classes import Teacher, Course, Timetable

teachers = set()
courses = set()


# Read teachers's data
with open("./teachers.csv", newline="", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        keys = list(row.keys())
        subjects = str(row[f"{keys[0]}"]).split("-")
        for subject in subjects:
            teachers.add(
                Teacher(
                    subject.strip().capitalize(),
                    str(row[f"{keys[1]}"]).strip().capitalize(),
                    str(row[f"{keys[2]}"]).strip().capitalize(),
                    int(row[f"{keys[4]}"]), #CHANGE back to 3!
                )
            )


# Read courses' data
for file in os.listdir("./courses"):
    with open(f"./courses/{file}", newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        reader.__next__()
        subjects = {}
        for row in reader:
            subjects[f"{row[0]}"] = int(row[1])
        courses.add(Course(f"{file}".split(".")[0], subjects))


timetable = Timetable(teachers, courses)
timetable.enforce_node_consistency()
timetable.revise()

print(timetable)
