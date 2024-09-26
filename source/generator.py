import csv
import os
from classes import Teacher, Course, Timetable

teachers = set()
courses = set()


# Read teachers's data
with open("./teachers.csv", newline="", encoding="utf-8-sig") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        teachers.add(
            Teacher(
                [subject.strip().capitalize() for subject in row[0].split("-")],
                row[1].strip().capitalize(),
                row[2].strip().capitalize(),
                int(row[4]) #change back to 3
            )
        )
        

# Read courses' data
for file in os.listdir("./courses"):
    with open(f"./courses/{file}", newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        reader.__next__()
        subjects = {}
        for row in reader:
            subjects[f"{row[0]}".capitalize()] = int(row[1])
        courses.add(Course(f"{file}".split(".")[0], subjects))


timetable = Timetable(courses, teachers)

if timetable.ac3():
    if timetable.backtrack():
        print(timetable)
    else:
        print("NO SOLUTION")
