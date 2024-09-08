import csv
import os
from classes import Teacher, Course, Timetable

teachers = set()
courses = set()

# Read teachers
with open("./teachers.csv", newline="", encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        keys = list(row.keys())
        teachers.add(
            Teacher(
                str(row[f"{keys[0]}"]).strip().capitalize(),
                str(row[f"{keys[1]}"]).strip().capitalize(),
                str(row[f"{keys[2]}"]).strip().capitalize(),
                int(row[f"{keys[3]}"]),
            )
        )

# Read courses
for file in os.listdir("./courses"):
    with open(f"./courses/{file}", newline="", encoding="utf-8-sig") as csvfile:
        reader = csv.reader(csvfile)
        reader.__next__()
        subjects = {}
        for row in reader:
            subjects[f"{row[0]}"] = int(row[1])
        courses.add(Course(f"{file}".split(".")[0], subjects))


            