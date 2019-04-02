from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", title="The AirBnB Review Summarizer")

@app.route('/city/<city>')
def city(city):
    return render_template("city.html", title=city, city=city)

if __name__ == '__main__':
    app.run(debug=True)