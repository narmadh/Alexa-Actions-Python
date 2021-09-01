import api_calls as api
import google_actions_functions as actions

response=""

def action(request):

    print(request.json)
    handler_type = request.json["handler"]["name"]    

    if(handler_type=='greeting'):
        speech = api.introSpeech()
        response = actions.prompt(request, speech)

    elif(handler_type=='teachContentScene'):
        speech = api.teachContentSpeech()
        response = actions.prompt(request, speech)

    elif(handler_type=='learnLessonSlotValidation'):
        response = actions.learnLessonSlotHandler(request)

    
    elif(handler_type=='teachContentFilled'):
        slots = request.json['scene']['slots']
        lesson=slots['lesson']['value']
        subject=slots['subject']['value']
        speech = "Awesome! You've chosen to learn lesson {} from {} subject! Let's get started! ".format(lesson,subject)
        extra = "If you wan't me to repeat the content, please say \"repeat it again\". If you have learnt the lesson then great!, say quit to exit. "
        contents = api.getTopicContent(slots['subject']['value'],slots['lesson']['value'],slots['lesson_number']['value'])
        content=""
        i=0
        for x in contents:
            i=i+1
            content=content+"Stanza {}: ".format(i)  + x  +  "  "
        response = actions.prompt(request, speech+content+extra)


    elif(handler_type=='repeatTeaching'):
        slots = request.json['scene']['slots']
        lesson=slots['lesson']['value']
        subject=slots['subject']['value']
        speech = "Ok! I will repeat it again... "
        extra = "If you wan't me to repeat the content, please say \"repeat it again\". If you have learnt the lesson then great!, say quit to exit. "
        contents = api.getTopicContent(slots['subject']['value'],slots['lesson']['value'],slots['lesson_number']['value'])
        content=""
        i=0
        for x in contents:
            i=i+1
            content="Stanza {}: ".format(i)  + x  +  "  "
        response = actions.prompt(request, speech+content+extra)

    else:
        response = actions.speakAndEndConversation(request,"Oopsies! There was a error processing your request! We will fix that soon")

    print("\nRequest data")
    print(request.data)
    print("\nHandler:")
    print(handler_type)
    print("\nResponse data")
    print(response)
    
   
    return response

