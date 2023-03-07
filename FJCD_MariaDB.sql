create table autor ( NOMBRE_AUTOR VARCHAR(20), BIOGRAFIA VARCHAR(100), constraint PK_NOMBRE_AUTOR primary key (NOMBRE_AUTOR), );
create table pieza( CODIGO_PIEZA VARCHAR(20), NOMBRE_PIEZA VARCHAR(30), GRABACION VARCHAR(100), NOMBRE_AUTOR VARCHAR(20), constraint PK_CODIGO_PIEZA primary key (CODIGO_PIEZA), constraint FK_NOMBRE_AUTOR foreign key (NOMBRE_AUTOR) references autor(NOMBRE_AUTOR) on delete cascade );
create table programa_pieza ( CODIGO_PROGRAMA VARCHAR(20), CODIGO_PIEZA VARCHAR(20), ORDEN TINYINT, constraint PK_PROGRAMA_PIEZA primary key (CODIGO_PIEZA,CODIGO_PROGRAMA), constraint FK_CODIGO_PROGRAMA foreign key (CODIGO_PROGRAMA) references programa(CODIGO_PROGRAMA) on delete cascade, constraint FK_CODIGO_PIEZA foreign key (CODIGO_PIEZA) references pieza(CODIGO_PIEZA) on delete cascade );
--Autor
INSERT INTO autor VALUES('Leonardo','https://es.wikipedia.org/wiki/Autor/leonardo.es');
INSERT INTO autor VALUES('Javi','https://javi.es');
INSERT INTO autor VALUES('Juan','https://juan.es');
INSERT INTO autor VALUES('Lola','https://Lola.es');
INSERT INTO autor VALUES('Maria','https://maria.es');
INSERT INTO autor VALUES('Pedro','https://pedro.es');
INSERT INTO autor VALUES('Ana','https://ana.es');
INSERT INTO autor VALUES('Sara','https://sara.es');
INSERT INTO autor VALUES('Jorge','https://jorge.es');
INSERT INTO autor VALUES('Ricardo','https://ricardo.es');
INSERT INTO autor VALUES('Isabel','https://isabel.es');
INSERT INTO autor VALUES('Diego','https://diego.es');
INSERT INTO autor VALUES('Sofia','https://sofia.es');
INSERT INTO autor VALUES('Carlos','https://carlos.es');
-- PIEZAS
INSERT INTO pieza VALUES ('P01','Oda a Jesus','CPO1.M4A','Leonardo');
INSERT INTO pieza VALUES ('P02','Ayabamarda','CPO2.M4A','Javi');
INSERT INTO pieza VALUES ('P03','El trol del puente','CPO3.M4A','Juan');
INSERT INTO pieza VALUES ('P04','Lepisma','CPO4.M4A','Leonardo');
INSERT INTO pieza VALUES ('P05','El zombie que bailaba','CPO5.M4A','Javi');
INSERT INTO pieza VALUES ('P06','Wilirex juega tactico','CPO6.M4A','Juan');
INSERT INTO pieza VALUES ('P07','Alergico al polen','CPO7.M4A','Lola');
INSERT INTO pieza VALUES ('P08','Mi estrella blanca','CPO8.M4A','Leonardo');
INSERT INTO pieza VALUES ('P09','La real ale','CPO9.M4A','Javi');
INSERT INTO pieza VALUES ('P10','O rey Juanmiguel','CPO10.M4A','Juan');
INSERT INTO pieza VALUES ('P11','La cebada','CPO11.M4A','Lola');
INSERT INTO pieza VALUES ('P12','Cristo rey vive','CPO12.M4A','Leonardo');
INSERT INTO pieza VALUES ('P13','Los templarios','CPO13.M4A','Javi');

-- PROGRAMA_PIEZA
INSERT INTO programa_pieza VALUES ('CP01','P01',01);
INSERT INTO programa_pieza VALUES ('CP02','P02',02);
INSERT INTO programa_pieza VALUES ('CP03','P03',03);
INSERT INTO programa_pieza VALUES ('CP04','P04',04);
INSERT INTO programa_pieza VALUES ('CP05','P05',05);
INSERT INTO programa_pieza VALUES ('CP06','P06',06);
INSERT INTO programa_pieza VALUES ('CP07','P07',07);
INSERT INTO programa_pieza VALUES ('CP08','P08',08);
INSERT INTO programa_pieza VALUES ('CP09','P09',09);
INSERT INTO programa_pieza VALUES ('CP10','P10',10);
INSERT INTO programa_pieza VALUES ('CP11','P11',11);
INSERT INTO programa_pieza VALUES ('CP12','P12',12);
INSERT INTO programa_pieza VALUES ('CP13','P13',13);

INSERT INTO programa_pieza VALUES ('CP01','CPO1.M4A',01);
INSERT INTO programa_pieza VALUES ('CP01','CPO2.M4A',02);
INSERT INTO programa_pieza VALUES ('CP01','CPO3.M4A',03);
INSERT INTO programa_pieza VALUES ('CP01','CPO4.M4A',04);