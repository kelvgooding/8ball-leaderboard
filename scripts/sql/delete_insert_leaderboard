DELETE FROM leaderboard;

INSERT INTO leaderboard (players, total_wins)
SELECT p1_name, p1_result 
FROM recently 
UNION ALL
SELECT p2_name, p2_result
FROM recently;