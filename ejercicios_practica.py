#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('secundaria.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS estudiante;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE estudiante(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER NOT NULL,
                [grade] INTEGER,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()



def fill():
    print('Completemos esta tablita!')
    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia INSERT.
    # Observar que hay campos como "grade" y "tutor" que no son obligatorios
    # en el schema creado, puede obivar en algunos casos completar esos campos
    valuesDB = []
    rep = False
    records = ["name", "age", "grade", "tutor"]
    transform = True

    #Bucle para crear alumnos
    while True:    
        for alumn in range(len(records)):
            #Bucle de validación
            while True:
                
                records_inp = str(input(f"Ingrese el dato para el campo {records[alumn]}: "))
                #Para evitar la transformación de str a int cuando no es necesario
                if records[alumn] == "name" or records[alumn] == "tutor":
                    transform = False
                else:
                    transform = True

                #Verificar si en los campos "age" y "grade" los datos son numéricos
                while transform:
                    if (records[alumn] == "age" or records[alumn] == "grade") and records_inp.isdigit():
                        break
                    else:
                        print(f"-El campo {records[alumn]} no puede llevar carácteres alfabéticos...")
                        rep = True
                        break
                #Volver al inicio del bucle si age o grade son alfanuméricos
                if rep:
                    rep = False
                    continue
                else:
                    break
            #Agrego valores
            valuesDB.append(records_inp)
        #Agregar registro a la tabla

        #Agregar los datos a la DB
        conn = sqlite3.connect('secundaria.db')
        c = conn.cursor()
        c.execute("""
                INSERT INTO estudiante(name,age,grade,tutor)
                VALUES(?,?,?,?);""",(valuesDB))
        #Guardar y cerrar
        conn.commit()
        conn.close()
        #Reset de la matriz valuesDB para volver a generar un nuevo registro
        valuesDB.clear()

        #Crear más registros de alumnos:
        alumn_record = str(input("Desea agregar otro registro de estudiante?: ")).capitalize()
        if alumn_record == "Si":
            print("**Creando otro registro**\n")
        elif alumn_record == "No":
            break
        #Realizado


def fetch():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # todas las filas con todas sus columnas
    # Utilizar fetchone para imprimir de una fila a la vez

    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    c.execute('SELECT * FROM estudiante;')
    while True:
        fetch_one = c.fetchone()
        if fetch_one is None:
            break
        print(fetch_one)

    #Guardar y cerrar
    conn.commit()
    conn.close()
    #Realizado


def search_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # aquellos estudiantes que se encuentra en el año "grade"

    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # id / name / age
    conn = sqlite3.connect('secundaria.db')
    c_grade = conn.cursor()
    c_2 = conn.cursor()
    c_name = conn.cursor()
    #Querys
    c_grade.execute(f'SELECT grade FROM estudiante WHERE grade = {grade};')
    c_2.execute('SELECT id, name, age FROM estudiante;')
    c_name.execute(f'SELECT name FROM estudiante WHERE grade = {grade};')

    while True:
        
        fetch_grade = c_grade.fetchone()
        fetch_two = c_2.fetchone()
        fetch_name = c_name.fetchone()

        if (fetch_grade is None) or (fetch_two is None) or (fetch_name is None):
            break
        print(f"El estudiante {fetch_name} está en el grado {fetch_grade}")
        print(fetch_two)
    #Cerrando sesión
    conn.close()
    #Realizado


def insert(new_student):
    print('Nuevos ingresos!')
    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    c.execute(""" INSERT INTO estudiante(name, age)
              VALUES(?,?)""",(new_student))

    #Guardar y cerrar
    conn.commit()
    conn.close()
    #Realizado


def modify(id, name):
    print('Modificando la tabla')
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" pasado como parámetro
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    c.execute('UPDATE estudiante SET name = ? WHERE id = ?;',(name,id))

    #Guardar y cerrar
    conn.commit()
    conn.close()
    #Realizado


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #create_schema()   # create and reset database (DB)
    #fill()
    #fetch()

    grade = 3
    #search_by_grade(grade)

    new_student = ['You', 16]
    #insert(new_student)

    name = '¿Inove?'
    id = 2
    #modify(id, name)
