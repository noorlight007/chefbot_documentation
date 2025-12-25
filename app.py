from flask import Flask, render_template

app = Flask(__name__)
app.config['secret_key'] = '5800d5d9e4405020d527f0587538abbe'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/database_schema")
def database_schema():
    return render_template("db.html")

@app.route("/technologies")
def technologies():
    return render_template("technologies.html")

@app.route("/designs")
def designs():
    return render_template("designs.html")

@app.route("/gpt_instructions")
def gpt_instructions():
    return render_template("gpt_instructions.html")

@app.route("/tutorials")
def tutorials():
    return render_template("tutorials.html")

if __name__ == "__main__":
    app.run(debug=True, port=4000)
