import pymysql

class Database():
    """docstring for Database"""
    def __init__(self):
        self.conection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='cursosql'

            )

    self.cursor = self.conection.cursor()
    print("conexion Exitosa")