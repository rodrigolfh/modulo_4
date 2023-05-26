-- ¿Qué es DDL?
-- DDL es el acrónimo de Data Definition Language. Corresponde a un subset del lenguaje MySQL que
-- se utiliza para manipular los objetos de las bases de datos MySQL. Algunos de los comandos
-- más utilizados son CREATE, ALTER Y DROP.

-- ¿Cuándo se puede anular una acción DDL?
-- No es posible hacer ROLLBACK(Anular) una acción DDL(como CREATE, DROP o ALTER), ni siquiera 
-- al realizar dichos comandos dentro de una transacción. Al contrario, sí se puede realizar
-- ROLLBACK de otras acciones como las DML (DELETE, UPDATE, UNION, etc.)

-- ¿Cuando se utilizan comillas dobles en la creación de una tabla?
-- Cuando se quiere que el nombre de la tabla sea sensible a mayúsculas y minúsculas (case sensitive).

-- Parte 1: Crear entorno de trabajo
-- Crear una base de datos
CREATE DATABASE mi_app;

-- Crear un usuario con todos los privilegios para trabajar con la base de datos recién creada.
CREATE USER	'mi_app_admin'@'localhost' IDENTIFIED BY 'contraseña';
GRANT ALL PRIVILEGES ON mi_app to 'mi_app_admin'@'localhost';

-- Parte 2: Crear tres tablas.
-- - La primera almacena a los usuarios de la aplicación (id_usuario, nombre, apellido, contraseña,
-- zona horaria (por defecto UTC-3), género y teléfono de contacto).

SET GLOBAL time_zone = '-3:00';

CREATE TABLE usuarios(
id_usuario VARCHAR(12) PRIMARY KEY,
nombre 	VARCHAR(30) NOT NULL,
apellido VARCHAR(40) NOT NULL,
contraseña VARCHAR(20) NOT NULL,
género VARCHAR(20),
teléfono INT
);

-- - La segunda tabla almacena información relacionada a la fecha-hora de ingreso de los usuarios a
-- la plataforma (id_ingreso, id_usuario y la fecha-hora de ingreso -por defecto la fecha-hora actual

CREATE TABLE log_ingreso(
id_ingreso INT PRIMARY KEY AUTO_INCREMENT,
id_usuario VARCHAR(12),
fecha_hora_ingreso TIMESTAMP DEFAULT NOW(),
CONSTRAINT fk_id_usuario
FOREIGN KEY (id_usuario)
REFERENCES usuarios(id_usuario)
);



-- - La tercera tabla almacena información sobre la cantidad de veces que los usuarios han visitado la
-- aplicación. Piense en una estructura de columnas que permita entregar esta información y cree la
-- tabla.

CREATE TABLE log_conteo_usuarios (
id_usuario VARCHAR(12),
conteo INT NOT NULL,
PRIMARY KEY (id_usuario),
FOREIGN KEY (id_usuario)
REFERENCES log_ingreso (id_usuario)
ON UPDATE CASCADE
ON DELETE RESTRICT
);

-- Creo un trigger que: 1. Si es primera vez que el usuario ingresa, setea 'conteo' en 1, y 2. Si ya había
-- ingresado, suma 1 a 'conteo'

DELIMITER $$

CREATE DEFINER=`root`@`localhost` TRIGGER `log_ingreso_AFTER_INSERT` 
AFTER INSERT ON `log_ingreso` FOR EACH ROW BEGIN
IF NOT EXISTS (SELECT * FROM log_conteo_usuarios WHERE id_usuario = NEW.id_usuario)
	THEN 
	INSERT INTO log_conteo_usuarios (id_usuario, conteo)
	VALUES (NEW.id_usuario, 1);

ELSE
    UPDATE log_conteo_usuarios
    SET conteo = conteo + 1
    WHERE id_usuario = NEW.id_usuario;
END IF;
END

DELIMITER ;


-- usuarios prueba

INSERT INTO usuarios
VALUES ('11111111-1', 'Pedro', 'Pereira', 'pass', 'hombre', 99999999);
INSERT INTO usuarios
VALUES ('22222222-2', 'Juan', 'Jorquera', 'pass', 'hombre', 99999999);
INSERT INTO usuarios
VALUES ('33333333-3', 'Martina', 'Martínez', 'pass', 'mujer', 99999999);
INSERT INTO usuarios
VALUES ('44444444-4', 'Leonor', 'León', 'pass', 'mujer', 99999999);

-- log ins de usuarios de prueba

INSERT INTO log_ingreso(id_usuario)
VALUES ('11111111-1');
INSERT INTO log_ingreso(id_usuario)
VALUES ('22222222-2');
INSERT INTO log_ingreso(id_usuario)
VALUES ('33333333-3');

-- PARA REVISAR LAS TABLAS

SELECT * FROM log_ingreso;

SELECT * FROM log_conteo_usuarios;
