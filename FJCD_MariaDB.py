# MariaDB [(none)]> CREATE USER 'javier'@'%' IDENTIFIED BY 'javier';
# MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'javier'@'%';

from FJCD_funciones import MariaDBmenu,MariaDB_PiezasPorAutor,MariaDB_ListarNombrePiezasAutoresQueEmpiezenPor,MariaDB_CodPiezasPrograma,MariaDBInsertar,MariaDBBorrarAutores10,MariaDBActualizarBiografia
import mysql.connector

opcion_elegida=0
conn = mysql.connector.connect(user="javier", password="javier", host="192.168.105.132", database="consultas")
cursor = conn.cursor()



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
    conn.close()

