from flask import Flask, render_template, request

import json

with open('goals.json', encoding='utf-8') as g:
    all_goals = json.load(g)

with open('teachers.json', encoding='utf-8') as t:
    teachers = json.load(t)

links = [{'title': 'Все репетиторы', 'link': ''}, {'title': 'Заявка на подбор', 'link': 'request'}]
days = {'mo': 'Понедельник', 'tu': 'Вторник', 'we': 'Среда', 'th': 'Четверг', 'fr': 'Пятница'}

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
def goals(goal):
    goal_ru = all_goals[goal].lower()
    teachers_with_goal = []
    for teacher_id in teachers:
        if goal in teachers[teacher_id]['goals']:
            teachers_with_goal.append(teacher_id)
    teachers_with_goal.sort(key=lambda teacher_id: teachers[teacher_id]['rating'], reverse=True)

    output = render_template('goal.html',
                             links=links,
                             teachers_with_goal=teachers_with_goal,
                             teachers=teachers,
                             goal=goal,
                             goal_ru=goal_ru)
    return output

@app.route('/profiles/<id>/')
def profiles(id):
    output = render_template('profile.html',
                             links=links,
                             goals=all_goals,
                             teacher=teachers[id],
                             id=id)
    return output

@app.route('/search?s=aaaa')
def search():
    return 'Здесь буедт поиск'

@app.route('/request')
def reqs():
    return 'Здесь будут заявки на подбор учителя'

@app.route('/booking/<id>/<day>/<time>')
def booking(id, day, time):
    with open ('request.json', 'w', encoding='utf-8') as r:
        json.dump({'day': days[day], 'time': time+':00'}, r)
    output = render_template('booking.html',
                             links=links,
                             teacher=teachers[id],
                             days=days,
                             id=id,
                             day=day,
                             time=time)
    return output

@app.route('/message/<id>')
def message(id):
    return 'Сообщение преподу'

@app.route('/sent/', methods=['GET'])
def sent():
    name = request.args.get('name') # for some reason, request.form.get(item) and request.form[item] don't work.
    phone = request.args.get('phone')
    with open('request.json', encoding='utf-8') as r:
        jsonized_data = json.load(r)
    day = jsonized_data['day']
    time = jsonized_data['time']

    with open('request.json', 'w', encoding='utf-8') as r:
        json.dump({'day': day, 'time': time, 'name': name, 'phone': phone}, r)
    output = render_template('sent.html',
                             links=links,
                             name=name,
                             phone=phone,
                             day=day,
                             time=time)
    return output

if __name__ == '__main__':
    app.run(debug=True)
