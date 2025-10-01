from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')
def play(num=3, color="aqua"):
    return render_template("Playground.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)