import api_calls

def prompt(request,speech):
    return {
        "session": {
            "id":request.json["session"]["id"] ,
            "params": request.json["session"]["params"]
        },
        "prompt": {
            "override": False,
            "firstSimple": {
                "speech": speech,
                "text": speech
           }
        },
        "scene": {
            "name": request.json["scene"]["name"],
            "slots":request.json["scene"]["slots"]
        }
    }


def learnLessonSlotHandler(request):

    params=request.json["session"]["params"]
    slots= request.json["scene"]["slots"]
    param={}
    slot={}
    msg=''
    if len(params)==0:

        if api_calls.isSlotValid("subject",slots['subject']['value'],0,0):
            msg = "Ok in {},".format(slots["subject"]["value"])
            param=params
            param["subject"]=slots['subject'].get('value')
        else:
            slot["subject"]={"status":"INVALID"}
            msg = "Sorry, that subject is not in the syllabus."

    elif len(params)==1:

        if api_calls.isSlotValid("lesson",slots['lesson']['value'],slots['subject']['value'],0):
            msg = "Ok in {},".format(slots["lesson"]["value"])
            param=params
            param["lesson"]=slots['lesson'].get('value')
        else:
            slot["lesson"]={"status":"INVALID"}
            msg = "Sorry, that lesson is not in the syllabus."


    else:
        if api_calls.isSlotValid("lesson",slots['lesson_number']['value'],slots['subject']['value'],slots['lesson']['value']):
            msg = "Ok...".format(slots["lesson"].get("value"))
            param=params
            param["lesson_number"]=slots['lesson_number']['value']
        else:
            slots["lesson_number"]={"status":"INVALID"}
            num = api_calls.getNumberOfLessons(slots['subject']['value'],slots['lesson']['value'])
            msg = "Sorry, only {} number of lessons are available.".format(num)


    response = prompt(request, msg)
    response['session']['params']=param
    print("Slots  :")
    print(slots)
    response['scene']['slots']=slots
    return response


def speakAndEndConversation(request,speech):
    return {
        "session": {
            "id":request.json["session"]["id"] ,
            "params": request.json["session"]["params"]
        },
        "prompt": {
            "override": False,
            "firstSimple": {
                "speech": speech,
                "text": speech
            }
        },
        "scene": {
            "name": request.json["scene"]["name"],
            "slots":request.json["scene"]["slots"] ,
            "next": {
                "name": "actions.scene.END_CONVERSATION"
            }
        }
    }
