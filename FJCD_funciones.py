def MariaDBmenu():
    print("---------------------------------------")
    opcion_elegida=int(input('''
    0. Introduce el nombre de una pieza para buscar a que programa pertenece  .
    1. Lista cuantas piezas a compuesto cada autor .
    2. Lista el nombre de las piezas que ha compuesto cada autor el cual su nombre empiece por una letra introducida por el usuario .
    3. Inserta en la tabla autor , nuevos autores cuyo nombre sea el nombre de las obras que tienen menos de 10 letras.
    4. Borra de la tabla autor los nombres que tengan mas de 10 letras;
    5. Actualiza todos los autores cuya biogrfia tenga el campo 'https://null.es' y pon el siguiente enlace 'https://spotify.es'
    6. Salir
    '''))
    print("---------------------------------------")

    return opcion_elegida

# 0. Introduce el nombre de una pieza para buscar a que programa pertenece.
def MariaDB_CodPiezasPrograma(cursor):
    NombreObra=input("Introduce el nombre de una pieza para buscar a que programa pertenece :")
    consulta = f"SELECT programa_pieza.CODIGO_PROGRAMA FROM programa_pieza INNER JOIN pieza ON programa_pieza.CODIGO_PIEZA = pieza.CODIGO_PIEZA WHERE pieza.NOMBRE_PIEZA = '{NombreObra}';"
    try:
        cursor.execute(consulta)
        for CodigoPrograma in cursor:
            print(CodigoPrograma)
    except:
        print("Error al insertar")
        cursor.rollback()
# 1. Lista cuantas piezas a compuesto cada autor .
def MariaDB_PiezasPorAutor(cursor):
        try:
            cursor.execute("SELECT autor.NOMBRE_AUTOR, COUNT(pieza.CODIGO_PIEZA) FROM autor LEFT OUTER JOIN pieza ON autor.NOMBRE_AUTOR = pieza.NOMBRE_AUTOR GROUP BY autor.NOMBRE_AUTOR HAVING COUNT(pieza.CODIGO_PIEZA) > 0;")
            for autor,obras in cursor:
                print("El autor ",autor," ha compuesto un total de :",obras," obras")
        except:
            print("Error al insertar")
            cursor.rollback()
# 2. Lista el nombre de las piezas que ha compuesto cada autor el cual su nombre empiece por una letra introducida por el usuario .
def MariaDB_ListarNombrePiezasAutoresQueEmpiezenPor(cursor):
    LetraAbuscar=input("Introduce una letra para mostrar las obras de los autores que empiecen por esta: ")
    consulta = f"SELECT autor.NOMBRE_AUTOR, pieza.NOMBRE_PIEZA FROM autor LEFT JOIN pieza ON autor.NOMBRE_AUTOR = pieza.NOMBRE_AUTOR WHERE autor.NOMBRE_AUTOR LIKE '{LetraAbuscar}%' AND pieza.NOMBRE_PIEZA IS NOT NULL ORDER BY autor.NOMBRE_AUTOR;"
    try:
        cursor.execute(str(consulta))
        for autor,nombreobra in cursor:
            print(autor,nombreobra)
    except:
        print("Error al insertar")
        cursor.rollback()
# 3. Inserta en la tabla autor , nuevos autores cuyo nombre sea el nombre de las obras que tienen menos de 10 letras.
def MariaDBInsertar(cursor):
    try:
        cursor.execute("INSERT INTO autor (NOMBRE_AUTOR, BIOGRAFIA) SELECT NOMBRE_PIEZA, 'https://null.es' FROM pieza WHERE LENGTH(NOMBRE_PIEZA) < 10 AND NOMBRE_PIEZA NOT IN (SELECT NOMBRE_AUTOR FROM autor);")
        print("Se han insertado" ,cursor.rowcount, "filas.")
    except:
        print("Error al insertar")
        cursor.rollback()
# 4. Borra de la tabla autor los nombres que tengan mas de 10 letras;
def MariaDBBorrarAutores10(cursor):
    try:
        cursor.execute("DELETE FROM autor WHERE LENGTH(NOMBRE_AUTOR) > 10;")
        print("Se han eliminado" ,cursor.rowcount, "filas.")
    except:
        print("Error al insertar")
        cursor.rollback()

# 5. Actualiza todos los autores cuya biogrfia tenga el campo 'https://null.es' y pon el siguiente enlace 'https://spotify.es'
def MariaDBActualizarBiografia(cursor):
    try:
        cursor.execute("UPDATE autor SET BIOGRAFIA = 'https://spotify.es' WHERE BIOGRAFIA = 'https://null.es';")
        print("Se han actualizado" ,cursor.rowcount, "filas.")
    except:
        print("Error al insertar")
        cursor.rollback()


#POSTGREE
# 3. Inserta en la tabla autor , nuevos autores cuyo nombre sea el nombre de las obras que tienen menos de 10 letras.
def PostgreInsertar(cursor):
    try:
        cursor.execute("INSERT INTO autor (NOMBRE_AUTOR, BIOGRAFIA) SELECT NOMBRE_PIEZA, 'https://null.es' FROM pieza WHERE LENGTH(NOMBRE_PIEZA) < 10 AND NOMBRE_PIEZA NOT IN (SELECT NOMBRE_AUTOR FROM autor) ON CONFLICT DO NOTHING;")
        print("Se han insertado" ,cursor.rowcount, "filas.")
    except:
        print("Error al insertar")
        cursor.rollback()
