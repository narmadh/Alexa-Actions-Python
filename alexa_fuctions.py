from ssml_builder.core import Speech

def studyContent(type,sub,lesson,lesson_name):
    speech = Speech()
    speech.add_text("You have chosen to {} {} from {}. That is great! Lets get started...".format(type,lesson_name,sub))
    speech.audio('https://learning-matters-protosem-audio-samples.s3.ap-south-1.amazonaws.com/baba-black-sheep.mp3')
    return speech.speak()


