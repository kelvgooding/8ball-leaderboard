from flask import Flask, render_template, request, redirect
import sqlite3

# SQLite3 configuration

connection = sqlite3.connect("static/db/8B_DB_PROD.db", check_same_thread=False)
cursor = connection.cursor()

# Flask configuration

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():

    # All Players

    players = []

    for i in cursor.execute('SELECT DISTINCT(PLAYERS) FROM LEADERBOARD'):
        players.append(i[0])

    company = []

    for i in cursor.execute('SELECT * FROM COMPANY'):
        company.append(i[0])

    # Recent Matches - List

    listed = []

    # Recent Matches - SQL Query

    for values in cursor.execute('SELECT * FROM recently ORDER BY date_played DESC LIMIT 5'):
        listed.append(values)

    # Leaderboard - List

    leaderboard = []

    # Leaderboard - SQL Delete / Insert

    cursor.execute('DELETE FROM leaderboard')
    cursor.execute('INSERT INTO leaderboard (players, company, total_wins) SELECT p1_name, p1_company, p1_result FROM recently UNION ALL SELECT p2_name, p2_company, p2_result FROM recently;')
    connection.commit()

    # Leaderboard - SQL Query

    for values in cursor.execute('SELECT players, SUM(total_wins) AS total_wins, COUNT(players) AS matches_played, ROUND(SUM(total_wins) * 100.0 / COUNT(players), 1) as win_perc, company FROM leaderboard GROUP BY players ORDER BY 2 DESC;'):
        leaderboard.append(values)

    # SQL Insert - Input Player Name / Win

    if request.method == "POST":
        if 'win-p1' in request.form:
            cursor.execute('INSERT INTO recently VALUES (?, ?, 1, ?, ?, 0, CURRENT_TIMESTAMP)', (request.form.get("name-p1"), request.form.get("company-p1"), request.form.get("name-p2"), request.form.get("company-p2"),))
            connection.commit()
        elif 'win-p2' in request.form:
            cursor.execute('INSERT INTO recently VALUES (?, ?, 0, ?, ?, 1, CURRENT_TIMESTAMP)', (request.form.get("name-p1"), request.form.get("company-p1"), request.form.get("name-p2"), request.form.get("company-p2"),))
            connection.commit()
        return redirect('/')
    else:
        return render_template("index.html", listed=listed, leaderboard=leaderboard, players=players, company=company)

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5010)
