
from FJCD_funciones import MariaDBmenu,MariaDB_PiezasPorAutor,MariaDB_ListarNombrePiezasAutoresQueEmpiezenPor,MariaDB_CodPiezasPrograma,MariaDBInsertar,MariaDBBorrarAutores10,MariaDBActualizarBiografia
import cx_Oracle


opcion_elegida=0

dsn_tns = cx_Oracle.makedsn('192.168.181.63', '1521', service_name='XE')
connection = cx_Oracle.connect(user='consultas', password='consultas', dsn=dsn_tns)

# conn = mysql.connector.connect(user="javier", password="javier", host="192.168.105.132", database="consultas")
cursor = connection.cursor()



while opcion_elegida != 6 :
    #Menu para elegir opccion
    opcion_elegida=MariaDBmenu()
    
    # 0. Introduce el nombre de una pieza para buscar a que programa pertenece.
    if opcion_elegida == 0:
        MariaDB_CodPiezasPrograma(cursor)
    # 1. Lista cuantas piezas a compuesto cada autor .
    elif opcion_elegida == 1:
        MariaDB_PiezasPorAutor(cursor)
        
    # 2. Lista el nombre de las piezas que ha compuesto cada autor el cual su nombre empiece por una letra introducida por el usuario .
    elif opcion_elegida == 2:
        MariaDB_ListarNombrePiezasAutoresQueEmpiezenPor(cursor)

    # 3. Inserta en la tabla autor , nuevos autores cuyo nombre sea el nombre de las obras que tienen menos de 10 letras.

    elif opcion_elegida == 3:
        MariaDBInsertar(cursor)
    # 4. Borra de la tabla autor los nombres que tengan mas de 10 letras;
    elif opcion_elegida == 4:
        MariaDBBorrarAutores10(cursor)

    # 5. Actualiza todos los autores cuya biogrfia tenga el campo 'https://null.es' y pon el siguiente enlace 'https://spotify.es'
    elif opcion_elegida == 5:
        MariaDBActualizarBiografia(cursor)


if opcion_elegida==6:
    cursor.close()
    connection.close()

# SELECT autor.NOMBRE_AUTOR, pieza.NOMBRE_PIEZA
# FROM autor
# LEFT JOIN pieza ON autor.NOMBRE_AUTOR = pieza.NOMBRE_AUTOR
# WHERE autor.NOMBRE_AUTOR LIKE 'S%' AND pieza.NOMBRE_PIEZA IS NOT NULL
# ORDER BY autor.NOMBRE_AUTOR;

# SELECT programa_pieza.CODIGO_PROGRAMA 
# FROM programa_pieza 
# INNER JOIN pieza ON programa_pieza.CODIGO_PIEZA = pieza.CODIGO_PIEZA 
# WHERE pieza.NOMBRE_PIEZA = 'Oda a Jesus';

# INSERT INTO autor (NOMBRE_AUTOR, BIOGRAFIA)
# SELECT NOMBRE_PIEZA, 'https://null.es'
# FROM pieza
# WHERE LENGTH(NOMBRE_PIEZA) < 10
# AND NOMBRE_PIEZA NOT IN (SELECT NOMBRE_AUTOR FROM autor);