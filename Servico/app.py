from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS
from common.settings import *
from common.logging import *
from resources.imagem import *

import sql
import instagram

app = Flask(__name__)

# Settings
app.config['DEBUG'] = DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
app.config['SQLALCHEMY_ECHO'] = SQLALCHEMY_ECHO
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


# Configure logging
handler = logging.FileHandler(LOGGING_LOCATION)
handler.setLevel(LOGGING_LEVEL)
formatter = logging.Formatter(LOGGING_FORMAT)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

db.init_app(app)

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/lanocentroteste/api')

# Recursos
api.add_resource(ImagensResource, '/imagens')

# Blueprints para Restful.
app.register_blueprint(api_bp)

# CORS - requisição multi-clients
cors = CORS(app, resources={r"/lanocentroteste/api/*": {"origins": "*"}})

# Iniciando estrutura do banco de dados.
@app.cli.command("create_db")
def create_db():
    sql.run()

# Carregando url das imagens do perfil do instagram.
@app.cli.command("import_profile_pic_instagram")
def import_profile_pic_instagram():
    instagram.run()

if __name__ == '__main__':
    app.run(threaded=True)
