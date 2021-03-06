from flask import (Blueprint, Flask, flash, g, redirect, render_template, request, url_for, json)

bp = Blueprint('home', __name__)


number_of_correct_answers = 0
user_choices = []


@bp.route('/', methods=["GET"])
def index():
    return render_template('home.html')


@bp.route('/learn/<int:video_id>')
def render_test(video_id):
    item = None
    
    with open("./asl/static/learning.json", "r", encoding='utf-8') as json_file:
        data = json.load(json_file)

    for i in data:
        if i["videoId"] == video_id:
            item = i
    
    learn_type = item["videoType"]
    learn_name = item["videoName"]

    type_list = []

    for j in data:
        if j["videoType"] == learn_type:
            dict_list_type = {}
            dict_list_type["videoName"] = j["videoName"]
            dict_list_type["videoId"] = j["videoId"]
            type_list.append(dict_list_type)
    
    return render_template("learn.html", 
                                item=item,
                                learn_type=learn_type,
                                learn_name=learn_name,
                                type_list=type_list)


@bp.route('/quiz/question/<int:questionId>')
def render_questions(questionId):
    quiz_item = None

    with open('./asl/static/quiz.json') as json_file:
        quiz_data = json.load(json_file)
    
    for i in quiz_data:
        if i["questionId"] == questionId:
            quiz_item = i
    
    return render_template("question.html", quiz_item=quiz_item, quiz_data=quiz_data)


# quiz starting page
@bp.route('/quiz', methods=["GET"])
def quiz():
    global number_of_correct_answers
    number_of_correct_answers = 0

    global user_choices
    user_choices = []
    
    return render_template('quiz.html')


@bp.route('/end')
def end():
    global number_of_correct_answers
    global user_choices

    to_write = "\n".join(user_choices)

    with open('./asl/static/choices.txt', 'w', encoding='utf-8') as fwrite:
        fwrite.write(to_write)

    return render_template('end.html', number_of_correct_answers=number_of_correct_answers)



########################################################
#            AJAX methods                              #
########################################################

@bp.route('/increment', methods=['POST'])
def increment():
    global number_of_correct_answers
    number_of_correct_answers += 1

    return {"status": "success"}


@bp.route('/store', methods=['POST'])
def store_quiz_data():
    global user_choices
    content = request.json
    question_number = str(content['questionNumber'])
    choice = str(content['choice'])

    # with open('./asl/static/choices.json', 'r', encoding='utf-8') as json_file:
    #     user_data = json.load(json_file)

    # user_data['choices'][question_number] = choice

    # with open('./asl/static/choices.json', 'w', encoding='utf-8') as json_write:
    #     json.dump(user_data, json_write, sort_keys=True, indent=4)

    user_str_choice = "User chooses %s for Question %s" % (choice, question_number)

    user_choices.append(user_str_choice)

    return {
        "status": "success"
    }


@bp.route('/save-important', methods=['POST'])
def save_important():
    content = request.json
    question_number = str(content['visitTime'])

    dict_data = {"visit_time": question_number}

    with open('./asl/static/visit_time.json', 'w', encoding='utf-8') as json_write:
        json.dump(dict_data, json_write, sort_keys=True, indent=4)
    return {"status": "success"}
