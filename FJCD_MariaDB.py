# MariaDB [(none)]> CREATE USER 'javier'@'%' IDENTIFIED BY 'javier';
# MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'javier'@'%';

from FJCD_funciones import MariaDBmenu,MariaDB_PiezasPorAutor,MariaDB_ListarNombrePiezasAutoresQueEmpiezenPor
import mysql.connector
opcion_elegida=0

# Establece la cadena de conexión a la base de datos
conn = mysql.connector.connect(user="javier", password="javier", host="192.168.105.132", database="consultas")
# Crea un cursor para realizar consultas
cursor = conn.cursor()
# Ejecuta una consulta
# cursor.execute("SELECT * FROM clientes")
# # Lee los resultados de la consulta
# for row in cursor:
#     print(row)
# Cierra el cursor y la conexión
# cursor.close()
# conn.close()


while opcion_elegida != 6 :
    #Menu para elegir opccion
    opcion_elegida=MariaDBmenu()
    
    # 0.Introduce el codigo de una pieza para buscar a que programa pertenece una obra .
    if opcion_elegida == 0:
        MariaDB_PiezasPorAutor(cursor)
    # 1. Lista cuantas piezas a compuesto cada autor .
    elif opcion_elegida == 1:
        MariaDB_PiezasPorAutor(cursor)
        
    # 2. Lista el nombre de las piezas que ha compuesto cada autor el cual su nombre empiece por una letra introducida por el usuario .
    elif opcion_elegida == 2:
        MariaDB_ListarNombrePiezasAutoresQueEmpiezenPor(cursor)

    # 3. Inserta en la tabla autor , nuevos autores cuyo nombre sea el nombre de las obras que tienen menos de 10 letras.

    elif opcion_elegida == 3:
        print("a")
    # 4. Borra de la tabla autor los nombres que tengan mas de 10 letras;
    elif opcion_elegida == 4:
        print("a")

    # 5. Actualiza todos las piezas cuya grabacion tenga el campo nulo y pon el siguiente enlace 'https://spotify.es'
    elif opcion_elegida == 5:
        print("a")


if opcion_elegida==6:
    cursor.close()
    conn.close()

# SELECT autor.NOMBRE_AUTOR, pieza.NOMBRE_PIEZA
# FROM autor
# LEFT JOIN pieza ON autor.NOMBRE_AUTOR = pieza.NOMBRE_AUTOR
# WHERE autor.NOMBRE_AUTOR LIKE 'S%' AND pieza.NOMBRE_PIEZA IS NOT NULL
# ORDER BY autor.NOMBRE_AUTOR;

