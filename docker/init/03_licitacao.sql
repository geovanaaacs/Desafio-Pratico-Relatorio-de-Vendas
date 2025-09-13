SET search_path TO licitacao;

DROP TABLE IF EXISTS proposta;
DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS empresa;
DROP TABLE IF EXISTS pregao;

CREATE TABLE pregao (
    id SERIAL PRIMARY KEY,
    numero VARCHAR(20),
    data DATE
);

CREATE TABLE empresa (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(200),
    cnpj VARCHAR(20)
);

CREATE TABLE item (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(200)
);

CREATE TABLE proposta (
    id SERIAL PRIMARY KEY,
    empresa_id INT REFERENCES empresa(id),
    pregao_id INT REFERENCES pregao(id),
    item_id INT REFERENCES item(id),
    valor NUMERIC(12,2),
    quantidade INT
);
