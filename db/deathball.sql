DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS games;

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(225),
    race VARCHAR(225),
    position VARCHAR(225),
    special_ability VARCHAR(225),
    status VARCHAR(225)
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(225),
    race VARCHAR(225),
    player_id SERIAL NOT NULL REFERENCES players(id),
    total_wins INT,
    total_loses INT,
    total_fouls INT
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    home_team SERIAL NOT NULL REFERENCES teams(id),
    home_team_score INT,
    away_team SERIAL NOT NULL REFERENCES teams(id),
    away_team_score INT,
    location VARCHAR(225),
    date VARCHAR(225),
    winner VARCHAR(225)
)