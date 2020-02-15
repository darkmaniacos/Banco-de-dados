import dbFunctions

data = dbFunctions.DataBase(name=r"\registros.db")

data.connect()

while True:
    try:
        username = str(input("username: "))
        password = str(input("Passworld: "))

        if password != "" and username != "":
            if data.addAccount(username, password) != 0:
                continue
            print("Seus dados foram adicionados com sucesso!\nPara continuar abra o login.py!")
            break
    except Exception as error:
        print(f"Ocorreu um erro (REGISTER ERROR): {error}")

data.disconnect()