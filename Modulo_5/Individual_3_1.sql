-- Inserte 3 cursos nuevos.
INSERT INTO capacitación (código_curso, nombre, horario, costo, fecha) 
VALUES
(011, 'Introducción a MySQL', '09:00:00', 120000, '2023-06-10'),
(012, 'MySQL Intermedio', '09:00:00', 150000, '2023-07-10'),
(013, 'MySQL Avanzado', '09:00:00', 120000, '2023-08-10')
;

-- Inserte 3 profesores nuevos
INSERT INTO operadores (run, nombre, apellido, dirección, correo_electrónico, fecha_creación_cuenta)
VALUES
('15033894-8', 'Katina', 'Torres', 'Bruno Zavala 760', 'katinatorres@example.com', '2022-10-01'),
('15123455-4', 'Perico', 'Los Palotes', 'Calle Los Pericos 123', 'perico@example.com', '2022-11-11'),
('12345223-8', 'Juan', 'Pérez', 'Avenida Prat 1200', 'jperez@example.com', '2021-11-11')
;

-- ¿Cuál es el curso más costoso? Selecciónelo.
SELECT * FROM capacitación WHERE costo = (SELECT MAX(costo) FROM capacitación);

-- ¿Cuál es el profesor menos con menor salario? Selecciónelo.
SELECT * FROM operadores WHERE sueldo = (SELECT MIN(sueldo) FROM operadores);

-- ¿Cuál es el curso más costoso? Selecciónelo.
SELECT * FROM capacitación WHERE costo = (SELECT MAX(costo) FROM capacitación);

-- Seleccione los cursos más costosos que el promedio.
SELECT * FROM capacitación WHERE costo > (SELECT AVG(costo) FROM capacitación);


-- Cree una tabla con los cursos menos costosos que el promedio. La tabla debe tener por nombre
-- Cursos económicos públicos’. 

CREATE TABLE cursos_económicos AS SELECT * FROM capacitación WHERE costo < (SELECT AVG(costo) FROM capacitación);

-- A la tabla Cursos económicos, agrégale dos campos. ‘Cantidad mínima estudiantes’ y ‘Aportes públicos'

ALTER TABLE cursos_económicos 
ADD estudiante_mínimos INT,
ADD aportes INT;

-- La cantidad mínima de estudiantes se refiere al número mínimo de estudiantes
-- necesarios para su realización. 
-- Los aportes públicos refieren a los aportes entregados por
-- instituciones públicas para la realización del curso (tiene que ser un valor menor al costo total del
-- curso).
UPDATE cursos_económicos
SET estudiantes_mínimos = 10, aportes_públicos = 75000 WHERE código_curso = 001;
UPDATE cursos_económicos
SET estudiantes_mínimos = 8, aportes_públicos = 125000 WHERE código_curso = 002;
UPDATE cursos_económicos
SET estudiantes_mínimos = 7, aportes_públicos = 90000 WHERE código_curso = 006;
UPDATE cursos_económicos
SET estudiantes_mínimos = 6, aportes_públicos = 90000 WHERE código_curso = 11;
UPDATE cursos_económicos
SET estudiantes_mínimos = 11, aportes_públicos = 13000 WHERE código_curso = 12;
UPDATE cursos_económicos
SET estudiantes_mínimos = 12, aportes_públicos = 50000 WHERE código_curso = 13;


-- Renombre la columna “Costo realización” en la tabla Cursos económicos. El nombre nuevo debe
-- ser: Costo efectivo. En dicha columna, a cada valor se le debe restar el valor de ‘Aportes públicos’.
ALTER TABLE cursos_económicos
RENAME COLUMN costo TO costo_efectivo;

UPDATE cursos_económicos
SET costo_efectivo = costo_efectivo - aportes_públicos;

-- Por último, actualice 5 cursos...
UPDATE capacitación
SET horario = '15:00:00' WHERE código_curso = '003';
UPDATE capacitación
SET horario = '10:00:00' WHERE código_curso = '004';
UPDATE capacitación
SET horario = '14:00:00' WHERE código_curso = '005';
UPDATE capacitación
SET horario = '09:00:00' WHERE código_curso = '006';
UPDATE capacitación
SET horario = '11:00:00' WHERE código_curso = '007';

-- ... y 3 profesores.
UPDATE operadores
SET sueldo = sueldo + 100000 LIMIT 3;
