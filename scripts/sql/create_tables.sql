CREATE TABLE leaderboard (
    players VARCHAR (255),
    total_wins INT
);

CREATE TABLE recently (
    p1_name VARCHAR (255),
    p1_result VARCHAR (255),
    p2_name VARCHAR (255),
    p2_result VARCHAR (255),
    date_played DATETIME,
    location VARCHAR (255) 
);