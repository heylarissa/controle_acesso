#importar o pyrebase4 no pip
import pyrebase

firebaseConfig = {
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "databaseURL": "https://" + "<ID_APP>" + ".firebaseio.com",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

user = input("Digite seu e-mail: ")
password = input("Digite sua senha, com pelo menos 6 caracteres: ")
status = auth.create_user_with_email_and_password(user,password)
print("Resultado: ", status)



