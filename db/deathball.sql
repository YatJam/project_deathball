DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(225),
    position VARCHAR(225),
    special_ability VARCHAR(225),
    status VARCHAR(225)
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(225),
    race VARCHAR(225),
    total_wins INT,
    total_loses INT,
    total_fouls INT
);