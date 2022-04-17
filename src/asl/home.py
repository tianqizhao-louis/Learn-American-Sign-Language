from flask import (Blueprint, Flask, flash, g, redirect, render_template, request, url_for, json)

bp = Blueprint('home', __name__)


number_of_correct_answers = 0


@bp.route('/', methods=["GET"])
def index():
    return render_template('home.html')


@bp.route('/greetings/<videoId>', methods=["GET"])
def greeting(videoId):
    with open('./asl/static/learning.json') as json_file:
        data = json.load(json_file)
        lesson = {}
        for item in data:
            if item['videoId'] == int(videoId):
                lesson[item['videoId']] = item
    return render_template('greetings.html', lesson=lesson)


@bp.route('/manners/<videoId>', methods=["GET"])
def manner(videoId):
    with open('./asl/static/learning.json') as json_file:
        data = json.load(json_file)
        lesson = {}
        for item in data:
            if item['videoId'] == int(videoId):
                lesson[item['videoId']] = item
    return render_template('manners.html', lesson=lesson)


@bp.route('/learning/<videoId>', methods=["GET"])
def learning(videoId):
    with open('./asl/static/learning.json') as json_file:
        data = json.load(json_file)
        lesson = {}
        for item in data:
            if item['videoId'] == int(videoId):
                lesson[item['videoId']] = item
    return render_template('learning.html', lesson=lesson)


@bp.route('/farewell/<videoId>', methods=["GET"])
def farewell(videoId):
    with open('./asl/static/learning.json') as json_file:
        data = json.load(json_file)
        lesson = {}
        for item in data:
            if item['videoId'] == int(videoId):
                lesson[item['videoId']] = item
    return render_template('farewell.html', lesson=lesson)


# quiz starting page
@bp.route('/quiz', methods=["GET"])
def quiz():
    global number_of_correct_answers
    number_of_correct_answers = 0
    return render_template('quiz.html')


# quiz question page
@bp.route('/question/<id>')
def question(id=None):
    with open('./asl/static/quiz.json') as json_file:
        quiz_data = json.load(json_file)
    # get to correct quiz question
    return render_template('question.html', quiz_data=quiz_data, id=id)


@bp.route('/end')
def end():
    global number_of_correct_answers
    return render_template('end.html', number_of_correct_answers=number_of_correct_answers)


@bp.route('/increment', methods=['POST'])
def increment():
    global number_of_correct_answers
    number_of_correct_answers += 1

    return {"status": "success"}

# @bp.route('/greetings/<videoid>', methods=["GET"])
# def greeting_lesson(videoid):
#     return render_template('greetings.html', id=id)
