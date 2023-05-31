DELIMITER //

CREATE TRIGGER before_insert_transacciones
BEFORE INSERT ON transacciones
FOR EACH ROW
BEGIN
    DECLARE saldo_origen INT;
    DECLARE saldo_destino INT;

    -- Verificar si monto > cuentas.saldo donde id_usuario = id_usuario_origen
    SELECT saldo INTO saldo_origen
    FROM cuentas
    WHERE id_usuario = NEW.id_usuario_origen;

    IF NEW.monto > saldo_origen THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Monto mayor que el saldo de la cuenta origen.';
    END IF;

    -- Verificar si monto <= 0
    IF NEW.monto <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Monto debe ser mayor que 0.';
    END IF;

    -- Verificar si id_usuario_origen existe en la tabla 'cuentas'
    SELECT COUNT(*) INTO @count_origen
    FROM cuentas
    WHERE id_usuario = NEW.id_usuario_origen;

    IF @count_origen = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: El id_usuario_origen no existe en la tabla cuentas.';
    END IF;

    -- Verificar si id_usuario_destino existe en la tabla 'cuentas'
    SELECT COUNT(*) INTO @count_destino
    FROM cuentas
    WHERE id_usuario = NEW.id_usuario_destino;

    IF @count_destino = 0 THEN
        -- Insertar usuario en tabla 'cuentas' con saldo = 0
        INSERT INTO cuentas (id_usuario, saldo) VALUES (NEW.id_usuario_destino, 0);
    END IF;

    -- Actualizar saldos en tabla 'cuentas' para id_usuario_origen y id_usuario_destino
    UPDATE cuentas
    SET saldo = saldo + NEW.monto
    WHERE id_usuario = NEW.id_usuario_destino;

    UPDATE cuentas
    SET saldo = saldo - NEW.monto
    WHERE id_usuario = NEW.id_usuario_origen;
END;
//

DELIMITER ;
select * from usuarios;
SELECT * FROM cuentas;
select * from transacciones;

-- darle saldo inicial de luca
INSERT INTO cuentas VALUES (
1, 1000);

-- pasar 200 del 1 al 2
INSERT INTO transacciones (id_usuario_origen, id_usuario_destino, monto)
VALUES(
1,
2,
200
);

-- pasar del 2 al 1 más de lo que tiene 
INSERT INTO transacciones (id_usuario_origen, id_usuario_destino, monto)
VALUES(
2,
1,
300
);

-- pasar un número negativo

INSERT INTO transacciones (id_usuario_origen, id_usuario_destino, monto)
VALUES(
1,
2,
200
);