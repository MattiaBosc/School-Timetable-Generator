from collections import deque

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
HOURS = 6

class Teacher:

    def __init__(self, subject, last_name, first_name, max_hours=0):
        self.subject = subject
        self.last_name = last_name
        self.first_name = first_name
        self.max_hours = max_hours

    def __hash__(self):
        return hash((self.first_name, self.last_name))

    def __eq__(self, other):
        if isinstance(other, Teacher):
            return self.first_name == other.first_name and self.last_name == other.last_name
        return False

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.subject})"


class Course:
    
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def __str__(self):
        return f"{self.name} {self.subjects}"

class Timetable:

    def __init__(self, teachers, courses):
        self.teachers = teachers
        self.courses = courses
        self.domains = self.initialize_domains()
        self.solution = {}

    def initialize_domains(self):
        """
        Inizialize domains for each time slot of the day
        by adding all the possible teachers
        """
        domains = {}
        for day in DAYS:
            domains[day] = [set(self.teachers) for _ in range(HOURS)]
        return domains

    def __str__(self):
        """
        Print timetable to terminal
        """
        string = ""
        for (day, timeslot), teacher in self.solution.items():
            string += f"{day} {timeslot + 1}: {teacher} \n"
        return string

    def enforce_node_consistency(self):
        """
        Enforce node consistency (unary constraint) on timetable:
        remove teacher if max number of available hours is reached
        """
        for day in self.domains.values():
            for time_slot in day:
                for teacher in self.teachers:
                    if teacher.max_hours <= 0:
                        time_slot.discard(teacher)

    def consistent(self, teacher1, teacher2):
        """
        Check for consistency of binary constraints on teachers:
            1. Physical Education requires two contiguous hours in a row

        Return True if two teachers are consistent; return False otherwise
        """
        if teacher1.subject == "MOTORIA" and teacher2.subject != "MOTORIA":
            return False
        return True

    def revise(self, day, timeslot1, timeslot2):
        """
        Make `timelot1` arc consistent with `timeslot2`.
        Remove values from the domain of timeslot1 for which there is no
        possible corresponding value in the domain of timeslot2.

        Return True if a revision was made; return False otherwise.
        """
        revised = False
        for teacher1 in set(self.domains[day][timeslot1]):
            if not any(self.consistent(teacher1, teacher2) for teacher2 in self.domains[day][timeslot2]):
                self.domains[day][timeslot1].discard(teacher1)
                revised = True
        return revised

    def ac3(self):
        """
        Update `domains` such that each variable is arc consistent.
        Begin with initial queue of all arcs in the problem.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """
        queue = deque()
        for day, slots in self.domains.items():
            for i in range(HOURS):
                if i < HOURS - 1:
                    queue.append((day, i, i + 1))

        while queue:
            day, timeslot1, timeslot2 = queue.popleft()
            if self.revise(day, timeslot1, timeslot2):
                if not self.domains[day][timeslot1]:
                    return False
                for i in range(HOURS):
                    if i != timeslot1:
                        queue.append((day, i, timeslot1))
        return True

    def complete(self, assignment):
        """
        Return True if `assignment` is complete; return False otherwise.
        """
        return len(assignment) == HOURS * len(DAYS)

    def consistent_assignment(self, day, timeslot, teacher, assignment):
        """
        Check wheter `teacher` has already been assigned for the same `timeslot` on the same `day` of the `assignment`.

        Return True if `assignment` is consistent; return False otherwise.
        """        
        for (d, t), assigned_teacher in assignment.items():
            if d == day and t == timeslot and assigned_teacher == teacher:
                return False
        return True

    def select_unassigned_variable(self, assignment):
        for day in DAYS:
            for i in range(HOURS):
                if (day, i) not in assignment:
                    return day, i
        return (None, None)

    def order_domain_values(self, day, timeslot):
        for teacher in list(self.domains[day][timeslot]):
            if teacher.max_hours <= 0:
                self.domains[day][timeslot].discard(teacher)
        return list(self.domains[day][timeslot])

    def backtrack(self, assignment={}):
        """
        Use backtrack algorithm to complete the partial input assignment, if possible to do so.
        If no assignment is possible, return None.

        `assignment` is a mapping from variables (keys) to words (values).
        """
        if self.complete(assignment):
            return assignment

        day, timeslot = self.select_unassigned_variable(assignment)

        for teacher in self.order_domain_values(day, timeslot):
            if self.consistent_assignment(day, timeslot, teacher, assignment):
                assignment[(day, timeslot)] = teacher
                teacher.max_hours -= 1
                result = self.backtrack(assignment)
                if result:
                    self.solution = result
                    return result
                del assignment[(day, timeslot)]
        return None

"""
    def subject_check(self, course):
        check = {}
        for day in self.school_timetable.values():
            for time_slot in day:
                for teacher in time_slot:
                    check[f"{teacher.subject}"] = check.get(f"{teacher.subject}", 0) + 1
        print(check)
        print(course.subjects)
        print(check == course.subjects)
"""
