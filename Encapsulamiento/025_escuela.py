class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad
        self.cursos = []

    def agregar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Especialidad: {self.especialidad}")
        print("Cursos que dicta:")
        for curso in self.cursos:
            print(f"- {curso.nombre}")


class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def listar_estudiantes(self):
        print(f"Estudiantes en el curso {self.nombre}:")
        for est in self.estudiantes:
            print(f"- {est.nombre}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Curso: {self.curso.nombre}")
        print(f"Profesor del curso: {self.curso.profesor.nombre}")


# ----------- DEMO COMPLETA -----------
# Creamos un profesor
profesor1 = Profesor("Carlos Navarrete", 35, "Inteligencia Artificial")

# Creamos cursos
curso1 = Curso("Python Pro", profesor1)
curso2 = Curso("Machine Learning", profesor1)

# Asignamos cursos al profesor
profesor1.agregar_curso(curso1)
profesor1.agregar_curso(curso2)

# Creamos estudiantes
estudiante1 = Estudiante("Andrés López", 30, curso1)
estudiante2 = Estudiante("Valentina Ruiz", 28, curso2)

# Agregamos estudiantes a los cursos
curso1.agregar_estudiante(estudiante1)
curso2.agregar_estudiante(estudiante2)

# Lista de personas (polimorfismo en acción 🔥)
personas = [profesor1, estudiante1, estudiante2]

for persona in personas:
    persona.mostrar_info()
    print("------")
