from flask import Flask, render_template

import json

with open('goals.json', encoding='utf-8') as g:
    all_goals = json.load(g)

with open('teachers.json', encoding='utf-8') as t:
    teachers = json.load(t)

links = [{'title': 'Все репетиторы', 'link': ''}, {'title': 'Заявка на подбор', 'link': 'request'}]

app = Flask(__name__)

@app.route('/')
def main():
    """
    output = render_template('index.html',
                             title=title,
                             subtitle=subtitle,
                             description=description,
                             tours=tours.items())
    """
    return 'Здесь будет главная'


@app.route('/goals/<goal>/')
def goals():
    """
    departure = departures[direction]
    output = render_template('direction.html',
                             departures=departures.items(),
                             departure=departure,
                             direction=direction,
                             tours=tours.items())
    """
    return 'Здесь будет цель goals'


@app.route('/profiles/<id>/')
def profiles(id):
    output = render_template('profile.html',
                             links=links,
                             goals=all_goals,
                             teacher=teachers[id],
                             id=id
                             )
    return output
    """
    this_tour = tours[int(id)]
    output = render_template('tour.html',
                             title=this_tour['title'],
                             stars=this_tour['stars'],
                             country=this_tour['country'],
                             dep=departures[this_tour['departure']],
                             nights=this_tour['nights'],
                             picture=this_tour['picture'],
                             desc=this_tour['description'],
                             price=str(this_tour['price']))

    return 'Здесь предлагают разместить тур, но вообще-то здесь должно быть что-то про учителя'
    """

@app.route('/search?s=aaaa')
def search():
    return 'Здесь буедт поиск'

@app.route('/request')
def reqs():
    return 'Здесь будут заявки на подбор учителя'

@app.route('/booking/<id>/<day>/<time>')
def booking(id, day, time):
    return 'Здесь будут формы бронирования'

@app.route('/message/<id>')
def message(id):
    return 'Сообщение преподу'

if __name__ == '__main__':
    app.run()
