
grades = []

def readGrade():
    grade = int(input("Ingrese una nota: "))
    grades.append(grade)

def checkGrades(grade):

    if grade < 60:
        return "Aprendizaje inicial"
    if grade < 80:
        return "Aprendizaje fundamental"
    if grade < 90: 
        return "Aprendizaje satisfactorio"
    else: 
        return "Aprendizaje Avanzado"