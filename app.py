from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
import os

# SQLite3

connection = sqlite3.connect("static/scoreboard.db", check_same_thread=False)
cursor = connection.cursor()

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():

    print(os.path)

    # Recent Matches
    cursor.execute('SELECT * FROM recently ORDER BY date_played DESC LIMIT 5')

    listed = []

    for a in cursor.fetchall():
        listed.append(a)

    # Leaderboard

    cursor.execute('delete from leaderboard')
    cursor.execute('insert into leaderboard (players, total_wins) select p1_name, p1_result from recently union all select p2_name, p2_result from recently;')
    connection.commit()
    cursor.execute('select players, sum(total_wins) from leaderboard group by players order by 2 desc;')

    leaderboard = []

    for i in cursor.fetchall():
        leaderboard.append(i)

    if request.method == "POST":

        if 'win-p1' in request.form:
            cursor.execute('INSERT INTO recently VALUES (?, 1, ?, 0, CURRENT_TIMESTAMP)', (request.form.get("name-p1"), request.form.get("name-p2"),))
            connection.commit()
        elif 'win-p2' in request.form:
            cursor.execute('INSERT INTO recently VALUES (?, 0, ?, 1, CURRENT_TIMESTAMP)', (request.form.get("name-p1"), request.form.get("name-p2"),))
            connection.commit()

        return redirect(url_for('index', listed=listed, leaderboard=leaderboard))
    else:
        return render_template("index.html", listed=listed, leaderboard=leaderboard)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
