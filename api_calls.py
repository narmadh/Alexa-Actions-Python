from firbase import firebase

db = firebase.database()

def getLessonsBySubject(subject):
    lessons = []
    data = db.child("subjects").child(subject).shallow().get()
    if data.val()!=None:
        for x in data.val():
            lessons.append(x)
    return lessons

def getAllSubjects():
    subjects = []
    data = db.child("subjects").shallow().get()
    if data.val()!=None:
        for x in data.val():
            subjects.append(x)
    return subjects

def introSpeech():
    data = db.child('prompts').child('mainIntro').get().val()
    return data

def getTestContent():
    return "test content"

def teachContentSpeech():
    data = db.child('prompts').child('teachContentSpeech').get().val()
    return data

def getNumberOfLessons(subject,lesson):
    contents = []
    data = db.child("subjects").child(subject).child(lesson).get()
    if data.val()!=None:
        for x in data.val():
            contents.append(x)
    return len(contents)

def getTopicContent(subject,lesson,lesson_number):
    contents = []
    data = db.child("subjects").child(subject).child(lesson).get()
    if data.val()!=None:
        for x in data.val():
            contents.append(x)
    return contents[lesson_number]['content']

def getTopicContentRepeat(subject,lesson,lesson_number):
    contents = []
    data = db.child("subjects").child(subject).child(lesson).get()
    if data.val()!=None:
        for x in data.val():
            contents.append(x)
    return contents[lesson_number]['content']


def isSlotValid(slot,value,sub,lesson):
    if slot =='subject':
        data = getAllSubjects()
        if value in data:
            return True
        else:
            return False
    elif slot=='lesson':
        data = getLessonsBySubject(sub)
        if value in data:
            return True
        else:
            return False
    elif slot=='lesson_number':
        data = getNumberOfLessons(sub,lesson)
        if value<=data:
            return True
        else:
            return False

