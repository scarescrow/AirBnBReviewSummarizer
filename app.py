from flask import Flask, render_template
import sqlite3
import os
import unicodedata

app = Flask(__name__)

cities = ["Seattle", "Chicago", "New York"]
DB_PATH = os.path.join("./assets/", "summary.db")

@app.route('/')
def home():
    return render_template("index.html", title="The AirBnB Review Summarizer")

@app.route('/city/<city>')
def city(city):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT words FROM topwords WHERE city = ?", (city,))
    words = cursor.fetchone()[0]#.encode('ascii', 'ignore')
    print(words)
    cursor.execute("SELECT positive, negative, neutral FROM sentiment WHERE city = ?", (city,))
    sentiments = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("city.html", title=city, city=city, sentiments=sentiments, words=words)

if __name__ == '__main__':
    app.run(debug=True)