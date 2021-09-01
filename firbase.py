import pyrebase 

firebaseConfig = {
    "apiKey": "AIzaSyA2YsnCNc9cAFOsIL7qNweRF7gMzRugCWo",
    "authDomain": "learningmattersprotosem.firebaseapp.com",
    "databaseURL": "https://learningmattersprotosem-default-rtdb.firebaseio.com",
    "projectId": "learningmattersprotosem",
    "storageBucket": "learningmattersprotosem.appspot.com",
    "messagingSenderId": "585768616134",
    "appId": "1:585768616134:web:4b345a33b968ad225dd7c7"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
