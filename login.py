import dbFunctions

data = dbFunctions.DataBase(name=r"\registros.db")

data.connect()

logado = False

while True:
    try:
        username = str(input("username: "))
        password = str(input("Passworld: "))

        rows = data.getInfo()

        for row in rows:
            if row[0] == username and row[1] == password:
                logado = True
                break
        if logado == True:
            print("Logado com sucesso!")
            break
        else:
            print("Nome/senha incorretos!")
    except Exception as error:
        print(f"Ocorreu um erro (LOGGIN ERROR): {error}")

data.disconnect()