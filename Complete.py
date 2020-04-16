from flask import Flask, url_for, request

app = Flask('Привет, Марс!')


promotion_text = ['Человечество вырастает из детства.',
                  'Человечеству мала одна планета.',
                  'Мы сделаем обитаемыми безжизненные пока планеты.',
                  'И начнем с Марса!',
                  'Присоединяйся!']


@app.route('/')
def start():
    return '<h2>Миссия Колонизации Марса</h2>'


@app.route('/index')
def index():
    return '<h2>И на Марсе будут яблони цвести!</h2>'


@app.route('/promotion')
def promotion():
    return '''
        <h2>{}</h2>
        <h2>{}</h2>
        <h2>{}</h2>
        <h2>{}</h2>
        <h2>{}</h2>
    '''.format(*promotion_text)


@app.route('/image_mars')
def image():
    return '''
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Привет, Марс!</title>
    </head>
    <h1>Жди нас, Марс!</h1>
    <img src="{}" width="300" height="300" alt="Марс">
    <p>Вот она какая, красная планета.</p>
    '''.format(url_for('static', filename='img/Mars.png'))


@app.route('/promotion_image')
def promotion_with_image():
    return '''
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" type="text/css" href="{}" />
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
        crossorigin="anonymous">
        <title>Колонизация</title>
    </head>
    <h1>Жди нас, Марс!</h1>
    <img src="{}" width="300" height="300" alt="Марс">
    <div class="alert-dark" role="alert">
        <br><h2>{}</h2>
    </div>
    <div class="alert-success" role="alert">
        <br><h2>{}</h2>
    </div>
    <div class="alert-secondary" role="alert">
        <br><h2>{}</h2>
    </div>
    <div class="alert-warning" role="alert">
        <br><h2>{}</h2>
    </div>
    <div class="alert-danger" role="alert">
        <br><h2>{}</h2>
    </div>
    '''.format(url_for('static', filename='css/style.css'), url_for('static', filename='img/Mars.png'), *promotion_text)


@app.route('/choice')
@app.route('/choice/<planet_name>')
def choice(planet_name='Марс'):
    return '''
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
        crossorigin="anonymous">
        <title>Варианты выбора</title>
    </head>
    <h1>Жди нас, {}!</h1>
    <br><h2>{}</h2>
    <div class="alert-success" role="alert">
        <br><h2>{}</h2>
    </div>
    <div class="alert-secondary" role="alert">
        <br><h2>{}</h2>
    </div>
    <div class="alert-warning" role="alert">
        <br><h2>{}</h2>
    </div>
    <div class="alert-danger" role="alert">
        <br><h2>{}</h2>
    </div>
    '''.format(planet_name, *['Эта планета близка к земле',  'На ней много необходимых ресурсов;',
                              'На ней есть вода и атмосфера;', 'На ней есть магнитное поле;',
                              'Наконец, она просто красивая!'])


@app.route('/results')
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname='User', level=0, rating=0.0):
    return f'''
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
        crossorigin="anonymous">
        <title>Результаты</title>
    </head>
    <h1>Результаты отбора</h1>
    <h2>Претендента на участие в миссии {nickname}:</h2>
    <div class="alert-success" role="alert">
        <br><h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
    </div>
    <br><h3>составляет {rating}!</h3>
    <div class="alert-warning" role="alert">
        <br><h3>Желаем удачи!</h3>
    </div>
    '''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    file = url_for('static', filename='img/photo.jpg')
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form_style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h3 align="center">для участия в миссии</h3>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                   <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <img src="{file}" alt="Фото">
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open(f'static/img/{f.filename}', 'wb') as file:
            file.write(f.read())
        file = url_for('static', filename=f'img/{f.filename}')
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form_style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h3 align="center">для участия в миссии</h3>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                   <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <img src="{file}" alt="Фото">
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''


@app.route('/carousel', methods=['POST', 'GET'])
def carousel():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form_style.css')}" />
                            <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
                            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
                            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
                            <title>Пейзажи Марса</title>
                          </head>
                          <body>
                            <h1 align="center">Пейзажи Марса</h1>
                            <div align="center" id="carousel-example-generic" class="carousel slide" data-ride="carousel">
                              <ol class="carousel-indicators">
                                <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="1"></li>
                                <li data-target="#carousel-example-generic" data-slide-to="2"></li>
                              </ol>
                              <div class="carousel-inner" role="listbox">
                                <div class="carousel-item active">
                                  <img src="/static/img/1.jpg" alt="1" width="800" height="600">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/2.jpg" alt="2" width="800" height="600">
                                </div>
                                <div class="carousel-item">
                                  <img src="/static/img/3.jpg" alt="3" width="800" height="600">
                                </div>
                              </div>
                              <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
                                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                              </a>
                              <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
                                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                              </a>
                            </div>
                        </div>
                          </body>
                        </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/form_style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Анкета претендента</h1>
                            <h3 align="center">на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="surnamelHelp" placeholder="Введите фамилию" name="surname">

                                    <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="eduSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="edu">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Выше среднего</option>
                                          <option>Супер!</option>
                                        </select>
                                     </div>
                                        <label for="eduSelect">Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof" name="prof">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof1">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof2">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof3">
                                        <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof4">
                                        <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof5">
                                        <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof6">
                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof7">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                    </div>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['edu'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        print(request.form['prof'])
        print(request.form['prof1'])
        print(request.form['prof2'])
        print(request.form['prof3'])
        print(request.form['prof4'])
        print(request.form['prof5'])
        print(request.form['prof6'])
        print(request.form['prof7'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='localhost', debug=True)
