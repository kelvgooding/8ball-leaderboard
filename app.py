"""
Author: Kelvin Gooding
Created: 2023-03-01
Updated: 2023-08-05
Version: 1.3
"""

# Modules

from flask import Flask, render_template, request, redirect
import sqlite3

# SQLite3 Variables

connection = sqlite3.connect("8ball_leaderboard.db", check_same_thread=False)
cursor = connection.cursor()

# Flask Variables

app = Flask(__name__)

# SOS - Start of Script

@app.route("/", methods=["POST", "GET"])
def index():

    # Empty list to hold distinct players from the database

    location = []

    for i in cursor.execute('SELECT DISTINCT(LOCATION) FROM RECENTLY'):
        location.append(i[0])

    players = []

    for i in cursor.execute('SELECT DISTINCT(PLAYERS) FROM LEADERBOARD'):
        players.append(i[0])

    # Empty list to hold recent matches from the database

    listed = []

    for values in cursor.execute('SELECT * FROM recently ORDER BY date_played DESC LIMIT 5'):
        listed.append(values)

    # SQL - Cleardown the leaderboard table before inserting new data

    cursor.execute('DELETE FROM leaderboard')
    cursor.execute('INSERT INTO leaderboard (players, total_wins) SELECT p1_name, p1_result FROM recently UNION ALL SELECT p2_name, p2_result FROM recently;')
    connection.commit()

    # Empty list to hold recent match data from the database

    leaderboard = []

    for values in cursor.execute('SELECT players, SUM(total_wins) AS total_wins, COUNT(players) AS matches_played, ROUND(SUM(total_wins) * 100.0 / COUNT(players), 1) as win_perc FROM leaderboard GROUP BY players ORDER BY 2 DESC;'):
        leaderboard.append(values)

    # Insert player name and win into recently table

    if request.method == "POST":
        if 'win-p1' in request.form:
            cursor.execute('INSERT INTO recently VALUES (?, 1, ?, 0, CURRENT_TIMESTAMP, ?)', (request.form.get("name-p1"), request.form.get("name-p2"), request.form.get("loc_comp"),))
            connection.commit()
        elif 'win-p2' in request.form:
            cursor.execute('INSERT INTO recently VALUES (?, 0, ?, 1, CURRENT_TIMESTAMP, ?)', (request.form.get("name-p1"), request.form.get("name-p2"), request.form.get("loc_comp"),))
            connection.commit()
        return redirect('/')
    else:
        return render_template("index.html", location=location, players=players, leaderboard=leaderboard, listed=listed)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=3001)
