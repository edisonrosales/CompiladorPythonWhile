import re

def menu_Juego():
    print("1.-Jugar\n2.-Ayuda\n3.Salir")



def logo():
    print("BIENVENIDOS AL CURSO DE WHILE")




def Ayuda():
    print("No hay ayuda")




def trampita_Salto_de_linea(texto):
    texto2 = texto
    texto = ""
    for i in range(0, len(texto2)):
        if texto2[i] == "\n":
            texto += "@"
        else:
            texto += texto2[i]
    return texto





def trampita_Tabulacion(texto):
    texto2 = texto
    texto = ""
    for i in range(0, len(texto2)):
        if texto2[i] == "\t":
            texto += "&"
        else:
            texto += texto2[i]
    return texto





def requerimiento(i):
    print("Ahora intente hacer lo mismo para completar el nivel → " + str(i))



def Descripcion_Nivel(niveles):
    if niveles==1:
        return '''Podemos generar lazos While con valores booleanos True/False acontinuacion vemos un Ejemplo:
while True:
    print("hello")'''


    elif niveles==2:
       return '''Como en el nivel anterior podemos hacer lo mismo solo que cuando tenemos 1 instruccion podemos hacerlo todo en 1 linea.
while True: print("hello")'''


    elif niveles==3:
        return '''Podemos usar instrucciones para detener la ejecucion de un lazo While mediante el comando break Ejemplo:
while True:
    print("hello")
    break'''


    elif niveles==4:
        return '''Podemos usar variables con valores booleanos(Nivel 1) para controlar un while Ejemplo:
flag= True
while flag:
    print("hello")
    flag=False'''


    elif niveles==5:
        return '''Tambien podemos hacer operaciones que devuelvan valores booleanos para controlar un while Ejemplo:
a=3
b=2
while a>b:
    print("hello")'''



    elif niveles==6:
        return '''Ademas podemos hacer mas de una operacion para controlar el while Usando logica matematica con operadores logicos como ("and" y el "or") Ejemplo:
a=3
b=2
while a>b and a!=0 or b==0:
    print("hello")'''



    elif niveles==7:
        return '''Tambien podemos hacer agrupaciones para definir prioridad de evaluaciones como en Matematicas Ejemplo:
a=3
b=2
while ((a>b or a==b) and (a!=0 or b==0)) or a==2:
    print("hello")'''



    elif niveles==8:
        return '''En caso de que la variable controladora sea False podemos controlar que hacer en ese caso con la expresion ("else") Ejeplo:
a=3
b=2
while ((a>b or a==b) and (a!=0 or b==0)) or a!=0:
    print("hello")
else:
    print("Chao")'''



    elif niveles==9:
        return '''Puede tambien usar funciones que devuelvan valores booleanos para controlar un while Ejemplo:
a=3
b=2
while funcion():
    counter=0
else:
    print("Chao")'''



    elif niveles==10:
        return '''Se conoco como while anidado cuando tienes un while dentro de otro while y asi sucesivamente Ejemplo:
a=3
b=2
while (a>b or a==b):
    counter=0
    while(counter<10):
        print("hello")
        counter=counter-1
else:
    print("Chao")'''

def regularExpresion(niveles,texto):
    if texto == None:
        return False
    if niveles == 1:
        match = re.match(r'while True:(\n\t)print\("?[a-zA-Z0-9_ +-/*]*"?\)', texto)
        return match
    elif niveles == 2:
        match = re.match(r'while True: print\("?[a-zA-Z0-9_ +-/*]*"?\)', texto)
        return match
    elif niveles == 3:
        match = re.match(r'while True:\n\tprint\("[a-zA-Z0-9_ +-/*]*"\)\n\tbreak', texto)
        return match
    elif niveles == 4:
        match = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*) *= *(True|False)\nwhile [a-zA-Z_][a-zA-Z0-9_]*:(\n\t(print\("[a-zA-Z0-9_ +-/*]*"\)|[a-zA-Z_][a-zA-Z0-9_]* *= *(True|False)))*',texto)
        return match
    elif niveles == 5:
        match = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*) *= *(\d+)\n([a-zA-Z_][a-zA-Z0-9_]*)=(\d+)\nwhile ([a-zA-Z_][a-zA-Z0-9_]*(>|<|==|!=|>=|<=)[a-zA-Z_][a-zA-Z0-9_]*):\n\tprint\("[a-zA-Z0-9_ +-/*]*"\)', texto)
        return match
    elif niveles == 6:
        match = re.match(r'(([a-zA-Z_][a-zA-Z0-9_]*) *= *(\d+)\n)+while ([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d+( *(and|or)* *([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d+|[a-zA-Z_][a-zA-Z0-9_]*)))*|[a-zA-Z_][a-zA-Z0-9_]*( *(and|or)* *([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d+|[a-zA-Z_][a-zA-Z0-9_]*)))*))+:\n\tprint\("[a-zA-Z0-9_ +-/*]*"\)',texto)
        return match
    elif niveles == 7:
        match = re.match(r'(([a-zA-Z_][a-zA-Z0-9_]*) *= *(\d+)\n)+while \(*([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d+\)*( *(and|or) *\(*([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d*|[a-zA-Z_][a-zA-Z0-9_]*))\)*)*|[a-zA-Z_][a-zA-Z0-9_]*\)*( *(and|or) *\(*([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d*|[a-zA-Z_][a-zA-Z0-9_]*))\)*)*))+\)*:\n\tprint\("[a-zA-Z0-9_ +-/*]*"\)',texto)
        return match
    elif niveles == 8:
        match = re.match(r'(([a-zA-Z_][a-zA-Z0-9_]*) *= *(\d+)\n)+while \(*([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d+\)*( *(and|or) *\(*([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d*|[a-zA-Z_][a-zA-Z0-9_]*))\)*)*|[a-zA-Z_][a-zA-Z0-9_]*\)*( *(and|or) *\(*([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d*|[a-zA-Z_][a-zA-Z0-9_]*))\)*)*))+\)*:\n\tprint\("[a-zA-Z0-9_ +-/*]*"\)\nelse:\n\tprint\("[a-zA-Z0-9_ +-/*]*"\)',texto)
        return match
    elif niveles == 9:
        match = re.match(
            r'(([a-zA-Z_][a-zA-Z0-9_]*) ?= ?(\d+)\n)*while [a-zA-Z0-9_ +-/*]*\(\)+:(\n\t(print\("[a-zA-Z0-9_ +-/*]*"\)|[a-zA-Z_][a-zA-Z0-9_]* *= *\d+))*\nelse:\n\tprint\("[a-zA-Z0-9_ +-/*]*"\)',
            texto)
        return match
    elif niveles == 10:
        match = re.match(r'(([a-zA-Z_][a-zA-Z0-9_]*) *= *(\d+)\n)+while \(*([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d+\)*( *(and|or) *\(*([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d*|[a-zA-Z_][a-zA-Z0-9_]*))\)*)*|[a-zA-Z_][a-zA-Z0-9_]*\)*( *(and|or) *\(*([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d*|[a-zA-Z_][a-zA-Z0-9_]*))\)*)*))+\)*:\n\t[a-zA-Z_][a-zA-Z0-9_]* *= *\d+\n\twhile \(*([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d+\)*( *(and|or) *\(*([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d*|[a-zA-Z_][a-zA-Z0-9_]*))\)*)*|[a-zA-Z_][a-zA-Z0-9_]*\)*( *(and|or) *\(*([a-zA-Z_][a-zA-Z0-9_]* *(>|<|==|!=|>=|<=) *(\d*|[a-zA-Z_][a-zA-Z0-9_]*))\)*)*))+\)*:(\n\t+(([a-zA-Z_][a-zA-Z0-9_]*) *= *([a-zA-Z_][a-zA-Z0-9_]* *(-|\+|/|\*) *\d+)|print\("[a-zA-Z0-9_ +-/*]*"\)))*\nelse:\n\tprint\("[a-zA-Z0-9_ +-/*]*"\)',texto)
        return match
