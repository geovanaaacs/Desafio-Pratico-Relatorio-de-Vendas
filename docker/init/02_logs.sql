SET search_path TO logs;

DROP TABLE IF EXISTS logs;

CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    data_hora TIMESTAMP,
    usuario VARCHAR(50),
    ip VARCHAR(50),
    status INT
);
