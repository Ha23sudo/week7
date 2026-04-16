print("Student Manager App") 
students = []

def add_student(name):
   students.append(name)

def remove_student(name):
   students.remove(name)

def update_student(old_name, new_name):
   index = students.index(old_name)
   students[index] = new_name