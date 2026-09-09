#Leer n cantidad de nota decir si es aprendizaje inicial, fundamental, satisfactorio y a avanzado, mostrar todas las notas.
import principal as principal

while True:
    try: 
        principal.readGrade()
        retry = input("Quiere ingresar una nueva nota? [SI = ENTER] - NO: ").strip().upper()
        if retry == "NO":
            break

    except ValueError:
        print("Error ingrese un número entero válido")

    
print("--- Resultado de notas ---")
for grade in principal.grades:
    level = principal.checkGrades(grade)
    print(f"Nota: {grade} tiene: {level}")