/* create database */

CREATE DATABASE 8ball_leaderboard;

/* grant database access */

GRANT ALL ON 8ball_leaderboard.* TO 'kgooding'@'%' IDENTIFIED BY "6M6@HM%VAiX27!$y7Yzf";

/* switch to database */

USE 8ball_leaderboard;

/* create database table - leaderboard */

CREATE TABLE leaderboard (
    players VARCHAR (255),
    total_wins INT
);

/* view table columns */

SHOW COLUMNS FROM leaderboard;

/* view table data */

SELECT * FROM leaderboard;

/* create database table - recently */

CREATE TABLE recently (
    p1_name VARCHAR (255),
    p1_result VARCHAR (255),
    p2_name VARCHAR (255),
    p2_result VARCHAR (255),
    date_played DATETIME,
    location VARCHAR (255)
);

/* view table columns */

SHOW COLUMNS FROM recently;

/* view table data */

SELECT * FROM recently;