import os

credentials_auth = {
    'username' : os.getenv('CREDENTIALS_USER'),
    'password' : os.getenv('CREDENTIALS_PASSWORD'),
    }

smtp_auth = {
    'server' : os.getenv('SMTP_SERVER'),
    'port' : os.getenv('SMTP_PORT'),
    'email' : os.getenv('SMTP_EMAIL'),
    'password' : os.getenv('SMTP_PASSWORD'),
    }

mysql_db_auth = {
    'username' : os.getenv('MYSQL_DB_USER'),
    'password' : os.getenv('MYSQL_DB_PASSWORD'),
    'host' : os.getenv('MYSQL_DB_HOST'),
    'port' : '3306',
    'database' : '8ball_leaderboard',
    }
