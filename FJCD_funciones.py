def MariaDBmenu():
    print("---------------------------------------")
    opcion_elegida=int(input('''
    0.Introduce el codigo de una pieza para buscar a que programa pertenece una obra .
    1. Lista cuantas piezas a compuesto cada autor .
    2. Lista el nombre de las piezas que ha compuesto cada autor el cual su nombre empiece por una letra introducida por el usuario .
    3. Inserta en la tabla autor , nuevos autores cuyo nombre sea el nombre de las obras que tienen menos de 10 letras.
    4. Borra de la tabla autor los nombres que tengan mas de 10 letras;
    5. Actualiza todos las piezas cuya grabacion tenga el campo nulo y pon el siguiente enlace 'https://spotify.es'
    6. Salir
    '''))
    print("---------------------------------------")

    return opcion_elegida

def MariaDB_PiezasPorAutor(cursor):
        cursor.execute("SELECT autor.NOMBRE_AUTOR, COUNT(pieza.CODIGO_PIEZA) FROM autor LEFT OUTER JOIN pieza ON autor.NOMBRE_AUTOR = pieza.NOMBRE_AUTOR GROUP BY autor.NOMBRE_AUTOR HAVING COUNT(pieza.CODIGO_PIEZA) > 0;")
        for autor,obras in cursor:
            print("El autor ",autor," ha compuesto un total de :",obras," obras")

def MariaDB_ListarNombrePiezasAutoresQueEmpiezenPor(cursor):
    LetraAbuscar=input("Introduce una letra para mostrar las obras de los autores que empiecen por esta: ")
    consulta = f"SELECT autor.NOMBRE_AUTOR, pieza.NOMBRE_PIEZA FROM autor LEFT JOIN pieza ON autor.NOMBRE_AUTOR = pieza.NOMBRE_AUTOR WHERE autor.NOMBRE_AUTOR LIKE '{LetraAbuscar}%' AND pieza.NOMBRE_PIEZA IS NOT NULL ORDER BY autor.NOMBRE_AUTOR;"

    cursor.execute(str(consulta))
    for autor,nombreobra in cursor:
        print(autor,nombreobra)

def MariaDBInsertar(cursor):
     
