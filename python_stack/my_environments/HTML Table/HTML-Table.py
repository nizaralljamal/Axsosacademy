from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    people = [
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Jane', 'last_name': 'Doe'},
        {'first_name': 'Jill', 'last_name': 'Doe'},
        {'first_name': 'Joe', 'last_name': 'Doe'},
    ]
    return render_template("Html-Table.html", people=people)

if __name__ == "__main__":
    app.run(debug=True)
