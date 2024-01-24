from flask import Flask, render_template

app = Flask(__name__)
jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru,india',
        'salary': 'Rs.10,00,000',
    },
    {
        'id': 2,
        'title': 'Data Engineer',
        'location': 'Bengaluru,india',
        'salary': 'Rs.10,00,000',
    },
    {
        'id': 3,
        'title': 'Data Scienctist',
        'location': 'Bengaluru,india',
        'salary': 'Rs.100,00,000',
    },
    {
        'id': 4,
        'title': 'Data Analyst',
        'location': 'Remote,usa',
        'salary': '$.10,00,000',
    },
]


@app.route("/")
def hello():
  return render_template("home.html",jb=jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
