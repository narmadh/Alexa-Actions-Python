from flask import Flask, request
import google_actions as actions
from flask_ask import Ask, question, session
import api_calls as api
from ssml_builder.core import Speech
from flask_ask.models import statement
import alexa_fuctions as functions


app = Flask(__name__)

ask = Ask(app,'/alexa')

@app.route('/',methods=['GET'])
def main():
    print(request)
    return {"response":"Alexa endpoint","req":request.json}

@ask.on_session_started
def new_session():
    return 'new session started'

@app.before_request
def func():
    session.modified = True

@ask.launch
def start_skill():
    print("Launched")
    welcome_message = api.introSpeech()
    set_session_attributes('intent','launch')
    return question(welcome_message)

@ask.intent("AMAZON.YesIntent")
def share_info_():
    info = "dummy"
    if get_session_attributes('intent')=='teachalphabet':
        info_message = 'Here is the information that you asked for... {}'.format(info)
    elif get_session_attributes('intent')=='selfintro':
        info_message='Great! When you are set say "I am ready to introduce myself...'
    return question(info_message)

@ask.intent("AMAZON.NoIntent")
def no_intent():
    message="Alright...Goodbye"
    return question(message)

@ask.intent("TeachAlphabetsIntent",mapping={'num':'number'})
def start_teaching_alphabets(num):
    teach_message= "Start teaching intent from Flask alexa_app...So you know the first {} alphabets! That is great..".format(num)
    set_session_attributes('intent','teachalphabets')
    return question(teach_message)

@ask.intent("IntroductionIntent",mapping={'nam':'name'})
def self_intro(nam):
    speech =Speech()
    speech.add_text("Hello {}! Here is a sample audio of a person introducting herself. Listen to it...".format(nam))
    speech.audio('https://learning-matters-protosem-audio-samples.s3.ap-south-1.amazonaws.com/intro-jencita-1.mp3')
    speech.add_text("Do you want to hear it again? Say yes to proceed...")
    set_session_attributes('intent','selfintro')
    return question(speech.speak())

@ask.intent("StudyIntent",mapping={'type':'TYPE','sub':'SUBJECT',"lesson":"LESSON","lesson_name":"LESSON_NAME"})
def study_intent(type,sub,lesson,lesson_name):
    return question(functions.studyContent(type,sub,lesson,lesson_name))
    

@ask.intent("SayAllLessonsInSubject",mapping={'sub':"SUBJECT_","lesson":"LESSON_"})
def get_contents(sub,lesson):
    speech = Speech()
    speech.add_text("There are no topics in the lesson {} in {} subject".format(lesson,sub))
    return question(speech.speak())

@ask.intent("AMAZON.CancelIntent")
def cancel():
    return statement("Goodbye!")

@ask.intent("AMAZON.StopIntent")
def cancel():
    return statement("Goodbye!")

@ask.intent("AMAZON.FallbackIntent")
def fallback():
    return question("Sorry, I don't understand. Can you please try again?")

@ask.session_ended
def session_ended():
    return"{}", 200


def set_session_attributes(name,value):
    session.attributes[name]=value

def get_session_attributes(name):
    return session.attributes[name]


###google endpoint

@app.route('/google',methods=["POST"])
def webhook():
    return actions.action(request)

   
if __name__ == '__main__ ':
    app.run()
