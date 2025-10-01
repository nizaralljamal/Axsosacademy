from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("chekerboard.html", row=8, col=8, color1='red', color2='black')

@app.route('/<int:x>')
def row(x):
    return render_template("chekerboard.html", row=x, col=8, color1='red', color2='black')

@app.route('/<int:x>/<int:y>')
def row_col(x, y):
    return render_template("chekerboard.html", row=x, col=y, color1='red', color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>')
def row_col_color1(x, y, color1):
    return render_template("chekerboard.html", row=x, col=y, color1=color1, color2='black')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def row_col_colors(x, y, color1, color2):
    return render_template("chekerboard.html", row=x, col=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)