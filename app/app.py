from flask import Flask
import os
import psycopg2

app = Flask(__name__)
db_url = os.environ.get("DATABASE_URL", "")

@app.route("/")
def index():
    return f"Hello, Flask! DB URL: {db_url}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
