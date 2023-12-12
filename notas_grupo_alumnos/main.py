alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guardar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")
    calificaciones = []
    calificacion = float(input("Dame una calificación del alumno (negativo para terminar):"))
    while calificacion > 0:
        if calificacion > 0 and calificacion <= 10:  # validar calificacion
            calificaciones.append(calificacion)
        else:
            print("Ingrese una calificación válida, entre 0 y 10")
        calificacion = float(input("Dame una calificación del alumno (negativo para terminar):"))
        alumnos[alumno] = calificaciones.copy()  # copia de la lista

#imprimir media de calificaciones

for alumno, calificaciones in alumnos.items():
    print(f"El alumno {alumno} tiene las siguientes calificaciones: {calificaciones}")
    print(f"El promedio es: {sum(calificaciones)/len(calificaciones)}")
