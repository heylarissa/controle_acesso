import pyrebase
import os
import dotenv
import stat
from pathlib import Path
from datetime import datetime, date

def create_log_file (user):
    if os.path.isfile("login.txt"):
    # Modifica a permissão do arquivo para leitura, escrita e execução
        os.chmod("login.txt", stat.S_IRWXU)

    registro = datetime.now()
    hora_atual = registro.strftime("%H:%M:%S")
    data_atual = date.today()

    # Abre o arquivo para escrita
    arquivo = open("login.txt", 'w')
    # Escreve no arquivo
    arquivo.write(f"[{data_atual}, {hora_atual}] Login efetuado: {user}")
    # Fecha o arquivo
    arquivo.close()

    # Modifica o arquivo apenas para leitura
    os.chmod("login.txt", stat.S_IRUSR)

def create_user(auth, user, password):
    status = auth.create_user_with_email_and_password(user,password)
    idToken = status['idToken']
    info = auth.get_account_info(idToken)
    print("Conta criada com sucesso.")

def sign_in_user(auth, user, password):
    status = auth.sign_in_with_email_and_password(user, password)
    idToken = status['idToken']
    info = auth.get_account_info(idToken)
    
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

    print("O que deseja fazer?")
    print("1 - Criar uma conta;\n"
         "2 - Checar informações da conta;\n")
    choice = input("O que deseja fazer? (Digite um número de 1 a 3): ")
    print()

    while (choice not in [1, 2]):
        user = input("Digite seu e-mail: ")
        password = input("Digite sua senha, com pelo menos 6 caracteres: ")

        if (choice == 1):
            create_user(auth, user, password)
        elif (choice == 2):
            sign_in_user(auth, user, password)
        else:
            print("Você deve escolher 1 ou 2")

if __name__=="__main__":
    main()

