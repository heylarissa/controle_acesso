#importar o pyrebase4 no pip
import pyrebase
import os
import dotenv
from pathlib import Path

def create_user(auth):
    user = input("Digite seu e-mail: ")
    password = input("Digite sua senha, com pelo menos 6 caracteres: ")
    status = auth.create_user_with_email_and_password(user,password)
    print("Resultado: ", status)


dotenv.load_dotenv(
    dotenv_path=os.path.join(Path(__file__).parent, '.env')
)

firebaseConfig = {
    "apiKey": os.environ.get("APIKEY"),
    "authDomain": os.environ.get("APIKEY"),
    "projectId": os.environ.get("APIKEY"),
    "databaseURL": os.environ.get("APIKEY"),
    "storageBucket": os.environ.get("APIKEY"),
    "messagingSenderId": os.environ.get("APIKEY"),
    "appId": os.environ.get("APIKEY"),
    "measurementId": os.environ.get("APIKEY"),
}


def main():
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    create_user(auth)


if __name__=="__main__":
    main()


