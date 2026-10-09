
import os
from getpass import getpass
from flask import Flask, request, redirect, url_for, render_template_string
import mysql.connector

app = Flask(__name__)

# Enter database settings privately when the app starts.
DB_CONFIG = {
    "host": os.environ.get("MYSQL_HOST"),
    "port": int(os.environ.get("MYSQL_PORT", "3306")),
    "database": os.environ.get("MYSQL_DATABASE"),
    "user": os.environ.get("MYSQL_USER"),
    "password": os.environ.get("MYSQL_PASSWORD"),
    "ssl_disabled": False,
}
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

PAGE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>MovieWatch</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 700px;
               margin: 40px auto; padding: 0 20px; }
        input, select, button { padding: 10px; margin: 6px 0;
                                width: 100%; box-sizing: border-box; }
        button { cursor: pointer; }
        .message { padding: 10px; background: #f1f1f1; }
        li { margin: 12px 0; }
    </style>
</head>
<body>
    <h1>MovieWatch</h1>
    <h2>Add a Movie to Your Watchlist</h2>

    {% if message %}
        <p class="message">{{ message }}</p>
    {% endif %}

    <form method="POST">
        <label for="title">Movie Title</label>
        <input id="title" name="title" required maxlength="255">

        <label for="genre">Genre</label>
        <input id="genre" name="genre" required maxlength="100">

        <label for="release_year">Release Year</label>
        <input id="release_year" name="release_year"
               type="number" min="1888" max="2100" required>

        <label for="viewing_status">Viewing Status</label>
        <select id="viewing_status" name="viewing_status">
            <option>Want to Watch</option>
            <option>Watched</option>
        </select>

        <button type="submit">Add Movie</button>
    </form>

    <h2>My Movies</h2>
    {% if movies %}
        <ul>
        {% for movie in movies %}
            <li>
                <strong>{{ movie[1] }}</strong> —
                {{ movie[2] }}, {{ movie[3] }} · {{ movie[4] }}
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No movies have been added yet.</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        genre = request.form.get("genre", "").strip()
        year_text = request.form.get("release_year", "").strip()
        status = request.form.get("viewing_status", "Want to Watch")

        if not title or not genre or not year_text:
            message = "Please complete all movie fields."
        elif status not in ("Watched", "Want to Watch"):
            message = "Please select a valid viewing status."
        else:
            try:
                year = int(year_text)
                if year < 1888 or year > 2100:
                    message = "Please enter a valid release year."
                else:
                    connection = get_db_connection()
                    try:
                        cursor = connection.cursor()
                        cursor.execute(
                            """INSERT INTO movies
                               (title, genre, releaseYear, viewingStatus)
                               VALUES (%s, %s, %s, %s)""",
                            (title, genre, year, status),
                        )
                        connection.commit()
                        message = f"Successfully added: {title}"
                        cursor.close()
                    finally:
                        connection.close()
            except ValueError:
                message = "Please enter a valid release year."
            except mysql.connector.Error:
                app.logger.exception("Database operation failed")
                message = "Could not save the movie. Check the database connection."

    connection = get_db_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            """SELECT movieID, title, genre, releaseYear, viewingStatus
               FROM movies ORDER BY movieID DESC"""
        )
        movies = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    return render_template_string(PAGE, message=message, movies=movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)