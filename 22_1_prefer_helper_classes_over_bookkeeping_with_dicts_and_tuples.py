class SimpleGradebook():
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


gradebook = SimpleGradebook()
gradebook.add_student('Panos Matsos')
gradebook.add_student('John Smith')

gradebook.report_grade('Panos Matsos', 30)
gradebook.report_grade('John Smith', 60)
gradebook.report_grade('Panos Matsos', 30)
gradebook.report_grade('John Smith', 80)

print(gradebook.average_grade('Panos Matsos'))
print(gradebook.average_grade('John Smith'))


class BySubjectGradeBook():
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, score):
        grades = self._grades[name]  # get grades of name
        subject_grades = grades.setdefault(subject, [])
        subject_grades.append(score)

    def average_grade(self, name):
        grades = self._grades[name] # returns a dictionary
        current_sum, number_of_grades = 0, 0
        for grade_values in grades.values():
            current_sum += sum(grade_values)
            number_of_grades += len(grade_values)
        return current_sum / number_of_grades


gradebook = BySubjectGradeBook()
gradebook.add_student('Panos Matsos')
gradebook.add_student('John Smith')

gradebook.report_grade('Panos Matsos', 'Maths', 30)
gradebook.report_grade('John Smith', 'Maths', 60)
gradebook.report_grade('Panos Matsos', 'History', 30)
gradebook.report_grade('Panos Matsos', 'Maths', 30)
gradebook.report_grade('John Smith', 'History', 60)
gradebook.report_grade('John Smith', 'Maths', 80)
gradebook.report_grade('Panos Matsos', 'History', 30)
gradebook.report_grade('John Smith', 'History', 80)

print(gradebook.average_grade('Panos Matsos'))
print(gradebook.average_grade('John Smith'))

import collections

Grade = collections.namedtuple('Grade', ('score', 'weight'))

