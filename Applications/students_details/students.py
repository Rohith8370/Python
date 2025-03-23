"""
    students.py 
    This module contains neccessary functions to store the students details

"""
from dataclasses import dataclass, asdict


@dataclass
class student:
    """This is a data class which represents student """
    Name = str
    course = str
    email = str

# This is the memory of the applications

student_dictionary = dict()


# Locations to store the informations
 
DATASTORE_PATH = "studentsdetails.yaml"

def add_student():
    """ This functions add the student information """
    Name = input("enter the name : ")
    course = input("enter the course : ")
    email = input("enter the email id : ")
    student = student(Name,course,email)
    student_dict[email] = student

def fetch_student_details():
    """This function fetches the student information"""
    email = input("Enter the email of the student: ")
    if email in student_dict :
        student_dict[email] = student
        print(f"name = {student.Name}" )
        print(f"course = {student.course}" )
        print(f"email = {student.email}" )
    else :
        print(" Student not found ")
    
def menu():
    """ This is a menu function for the application"""
    while True:
        choice = input(
            " Enter the choice : 1 for Add the students details and 2 for Searching for Student information and 3 for exit ")
        if choice.strip == 1 :
            add_student()
        if choice.strip == 2 :
            fetch_student_details()
        else :
            break
