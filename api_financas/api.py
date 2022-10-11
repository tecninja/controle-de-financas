import psycopg2 as ps


class Api:
    
    parametros_db = {
        'host': 'localhost',
        'db_name': 'postgres',
        'user': 'teste',
        'password': '123',
        'sslmode': 'disable'
    }
    
    conexao_db = ps.extensions.connection
    
    def __init__(self) -> None:
        self.conexao_db = self.conectar()
    
    def conectar(self) -> ps.extensions.connection:
        url = f"host={self.parametros_db['host']}\
            user={self.parametros_db['user']}\
            dbname={self.parametros_db['db_name']}\
            password={self.parametros_db['password']}\
            sslmode={self.parametros_db['sslmode']}"
        return ps.connect(url)
    
    def desconectar(self):
        self.conexao_db.close()
        
        
    
    
if __name__ == '__main__':
    print(Api().conectar().__class__)
    
    