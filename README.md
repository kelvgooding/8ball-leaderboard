# 8-Ball Leaderboard

**What is 8-Ball Leaderboard?**

8-Ball Leaderboard is a web application based on the Flask framework. The purpose of this web application, is to have a central place to store match results and total scores per player for the Pool matches in either a location or company.
**Features:**

New Match:

2 Players can input their names and the winner will use the relevent button to mark themselves as the winner.

Leaderboard:

The leaderboard will update to show the player who has the highest win count. This will also show all players who have participated.

Recent Results:

This section will show the last 5 matches played, with the details of the 2 players, the winner and a timestamp.

## Running app using Docker

Clone the repository:

```
git clone git@github.com:kelvgooding/8ball-leaderboard.git
```

Navigate to the cloned repository directory

Run the following command to build the Docker image

```
sudo docker build -t 8ball-leaderboard .
```

Run the following command to create and start the container:

```
sudo docker run -itd -p 3001:3001 8ball-leaderboard
```

This can now be accessed via web browser - http://localhost:3001