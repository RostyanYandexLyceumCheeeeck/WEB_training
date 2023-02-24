from flask import Flask, url_for, render_template

app = Flask(__name__)
profession = {
    'врач': ['Научные симуляторы', 'img/doctor.jpg'],
    'повар': ['Научные симуляторы', 'img/chef.jpg'],
    'военный': ['Научные симуляторы', 'img/soldier.jpg'],
    'охранник': ['Инженерные тренажеры', 'img/security.jpg'],
    'физик-ядерщик': ['Научные симуляторы', 'img/nuclear physicist.jpg'],
    'электрик': ['Инженерные тренажеры', 'img/electrician.jpg'],
    'грузчик': ['Инженерные тренажеры', 'img/loader.jpg'],
    'оператор': ['Инженерные тренажеры', 'img/operator.jpg'],
    'слесарь': ['Инженерные тренажеры', 'img/plumber.jpg'],
    'программист': ['Инженерные тренажеры', 'img/programmer.jpg'],
    'растение': ['Научные симуляторы', 'img/plant.jpg'],
}


@app.route('//<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def profil(prof):
    who, name = profession[prof]
    return render_template('prof_scheme.html', prof=who, scheme=url_for('static', filename=name))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
'127.0.0.1:8080/training/врач'