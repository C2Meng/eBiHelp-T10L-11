from flask import Blueprint

quiz = Blueprint('quiz', __name__)

@quiz.route('/quest')
def quest():
    return "<p>Quest</p>"

@quiz.route('/result')
def result():
    return "<p>Result</p>"

@quiz.route('/create-quiz')
def create_quiz():
    return "<p>Create Quiz</p."