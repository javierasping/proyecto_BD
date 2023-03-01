El proyecto consiste en realizar tres programas en Python que realice operaciones DML sobre una base de datos. Deberá realizar el mismo programa Python pero sobre cada uno de los SGBD relaciones trabajados en clase (Oracle, MySQL/MariaDB y PostgreSQL).

Las tablas que voy a seleccionar para mi enunciado son "autor" ,"pieza" y "programa_pieza" .

Enunciado :
1. Introduce el nombre de una pieza para buscar a que programa pertenece.
2. Lista cuantas piezas a compuesto cada autor .
3. Lista el nombre de las piezas que ha compuesto cada autor el cual su nombre empiece por una letra introducida por el usuario
4. Inserta en la tabla autor , nuevos autores cuyo nombre sea el nombre de las obras que tienen menos de 10 letras.
5. Borra de la tabla autor los nombres que tengan mas de 10 letras;
6. Actualiza todos los autores cuya biogrfia tenga el campo 'https://null.es' y pon el siguiente enlace 'https://spotify.es'





**ESQUEMA CREACION DE TABLAS PARA ORACLE**

 create table autor (
    NOMBRE_AUTOR        VARCHAR2(20),
    BIOGRAFIA           VARCHAR2(100),
    constraint PK_NOMBRE_AUTOR   primary key (NOMBRE_AUTOR),
    );

 create table pieza(
   CODIGO_PIEZA         VARCHAR2(20),
   NOMBRE_PIEZA         VARCHAR2(30),
   GRABACION            VARCHAR2(100),
   NOMBRE_AUTOR         VARCHAR2(20),
   constraint PK_CODIGO_PIEZA   primary key (CODIGO_PIEZA),
   constraint FK_NOMBRE_AUTOR foreign key (NOMBRE_AUTOR) references autor(NOMBRE_AUTOR) on delete cascade
   );
 
 create table programa_pieza (
   CODIGO_PROGRAMA      VARCHAR2(20),
   CODIGO_PIEZA         VARCHAR2(20),
   ORDEN                NUMBER(2),
   constraint PK_PROGRAMA_PIEZA   primary key (CODIGO_PIEZA,CODIGO_PROGRAMA),
   constraint FK_CODIGO_PROGRAMA foreign key (CODIGO_PROGRAMA) references programa(CODIGO_PROGRAMA) on delete cascade,
   constraint FK_CODIGO_PIEZA foreign key (CODIGO_PIEZA) references pieza(CODIGO_PIEZA) on delete cascade
   );

**ESQUEMA CREACION DE TABLAS PARA MARIADB**

 create table autor (
    NOMBRE_AUTOR        VARCHAR(20),
    BIOGRAFIA           VARCHAR(100),
    constraint PK_NOMBRE_AUTOR   primary key (NOMBRE_AUTOR),
    );

create table pieza(
   CODIGO_PIEZA         VARCHAR(20),
   NOMBRE_PIEZA         VARCHAR(30),
   GRABACION            VARCHAR(100),
   NOMBRE_AUTOR         VARCHAR(20),
   constraint PK_CODIGO_PIEZA   primary key (CODIGO_PIEZA),
   constraint FK_NOMBRE_AUTOR foreign key (NOMBRE_AUTOR) references autor(NOMBRE_AUTOR) on delete cascade
   );
 
create table programa_pieza (
   CODIGO_PROGRAMA      VARCHAR(20),
   CODIGO_PIEZA         VARCHAR(20),
   ORDEN                TINYINT,
   constraint PK_PROGRAMA_PIEZA   primary key (CODIGO_PIEZA,CODIGO_PROGRAMA),
   constraint FK_CODIGO_PROGRAMA foreign key (CODIGO_PROGRAMA) references programa(CODIGO_PROGRAMA) on delete cascade,
   constraint FK_CODIGO_PIEZA foreign key (CODIGO_PIEZA) references pieza(CODIGO_PIEZA) on delete cascade
   );

**ESQUEMA CREACION DE TABLAS PARA POSTGRE**

create table autor (
    NOMBRE_AUTOR        VARCHAR(20),
    BIOGRAFIA           VARCHAR(100),
    constraint PK_NOMBRE_AUTOR   primary key (NOMBRE_AUTOR));

create table pieza(
   CODIGO_PIEZA         VARCHAR(20),
   NOMBRE_PIEZA         VARCHAR(30),
   GRABACION            VARCHAR(100),
   NOMBRE_AUTOR         VARCHAR(20),
   constraint PK_CODIGO_PIEZA   primary key (CODIGO_PIEZA),
   constraint FK_NOMBRE_AUTOR_P foreign key (NOMBRE_AUTOR) references autor(NOMBRE_AUTOR) on delete cascade);
 
create table programa_pieza (
   CODIGO_PROGRAMA      VARCHAR(20),
   CODIGO_PIEZA         VARCHAR(20),
   ORDEN                SMALLINT,
   constraint PK_PROGRAMA_PIEZA   primary key (CODIGO_PIEZA,CODIGO_PROGRAMA),
   constraint FK_CODIGO_PROGRAMA foreign key (CODIGO_PROGRAMA) references programa(CODIGO_PROGRAMA) on delete cascade,
   constraint FK_CODIGO_PIEZA foreign key (CODIGO_PIEZA) references pieza(CODIGO_PIEZA) on delete cascade);
