import sqlite3

class DataBase:
    def __init__(self, name=r"\registros.db", path=r"BOTE O CAMINHO DO LOCAL DO 'registros.db' AQUI!"):
        self.name = name
        self.connection = name
        self.path = path 

    
    def connect(self):
        """ conecta ao database
        parametros:
        - self
        """
        try:
            self.connection = sqlite3.connect(self.path+self.name)
        except Exception as error:
            print(f"\nOcorreu um erro (CONNECT FUNCTION): {error}\n")
    

    def disconnect(self):
        """ disconecta do database
        parametros:
        - self
        """
        try:
            self.connection.close()
        except Exception as error:
            print(f"\nOcorreu um erro (DISCONNECT FUNCTION): {error}\n")
    

    def addAccount(self, username, password):
        """ adiciona uma conta no database
            parametros:
            - self
            - username
            - password
        """
        try:
            cursor = self.connection.cursor()

            rows = self.getInfo()

            for row in rows:
                if row[0] == username:
                    print("Ja existe uma conta conta com esse nome!")
                    return 1 # ja tem

            cursor.execute("INSERT INTO contas VALUES(?, ?)", (username, password))
            
            self.connection.commit()
        except Exception as error:
            print(f"\nOcorreu um erro (ADDING FUNCTION): {error}\n")
        
        return 0 # não tem
    
    
    def getInfo(self):
        """ retorna os valores do database
        parametros:
        - self
        """
        try:
            cursor = self.connection.cursor()

            rows = cursor.execute("""SELECT * FROM contas;""")

            return rows
        except Exception as error:
            print(f"\nOcorreu um erro (GETINFO FUNCTION): {error}\n")

    
    def createMainTable(self):
        """ cria a tabela do database
        parametros:
        - self
        """
        try:
            connection = sqlite3.connect(self.path+r"\registros.db")
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS contas(
                    userN TEXT,
                    passW TEXT
                    )""")
            connection.commit()
        except Exception as error:
            print(f"\nOcorreu um erro (CREATEMAINTABLE FUNCTION): {error}\n")
        finally:
            cursor.close()
            connection.close()

