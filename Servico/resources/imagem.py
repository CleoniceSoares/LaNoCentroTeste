from flask_restful import Resource, marshal_with, reqparse, current_app, abort, marshal
from common.database import db
from sqlalchemy import exc
from models.imagem import ImagemModel, imagem_campos


class ImagensResource(Resource):

    def insert_Imagem(nome):
        query = "INSERT INTO tb_imagem(nome) " \
                "VALUES(%s)"
        args = (nome)

        try:
            db_config = read_db_config()
            conn = MySQLConnection(**db_config)

            cursor = conn.cursor()
            cursor.execute(query, args)

            if cursor.lastrowid:
                print('last insert id', cursor.lastrowid)
            else:
                print('last insert id not found')

            conn.commit()
        except Error as error:
            print(error)

        finally:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    main()
