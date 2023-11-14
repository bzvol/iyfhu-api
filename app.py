from flask import Flask, Blueprint
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from dotenv import dotenv_values
# from os import environ as env
import stripe_config
import routes

env = dotenv_values('.env')

app = Flask(__name__)
CORS(app, origins=[
    'http://localhost:3000',
    'https://iyf.hu',
])
limiter = Limiter(get_remote_address, app=app)

stripe_config.init()

v1 = Blueprint('v1', __name__, template_folder='templates')
routes.register_routes()
app.register_blueprint(v1, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(env.get("PORT", 8080)))
