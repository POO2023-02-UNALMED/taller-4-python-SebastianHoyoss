from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        if asignaturas == None:
            self._asignaturas=[]
        self.listadoAlumnos = estudiantes
        if estudiantes == None:
            self.listadoAlumnos=[]

    def listadoAsignaturas(self, kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista == None:
            lista=[]
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        return "Grupo de estudiantes:" + {self._grupo}

    @ classmethod
    def asignarNombre(cls, nombre=None):
        if nombre==None:
            cls.grado="Grado 6"
            return
        cls.grado=nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre
