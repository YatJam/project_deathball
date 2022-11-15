
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(225),
    race VARCHAR(225),
    total_wins INT,
    total_loses INT,
    total_fouls INT
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(225),
    race VARCHAR(225),
    team_id INT REFERENCES teams(id),
    position VARCHAR(225),
    status VARCHAR(225),
    special VARCHAR(225)
    
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    home_team_id INT NOT NULL REFERENCES teams(id),
    home_team_score INT,
    away_team_id INT NOT NULL REFERENCES teams(id),
    away_team_score INT,
    location VARCHAR(225),
    date VARCHAR(225)
);