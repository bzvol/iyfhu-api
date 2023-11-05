from flask import Flask, Blueprint
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from dotenv import dotenv_values
# from os import environ as env
import stripe

env = dotenv_values('.env')

app = Flask(__name__)
CORS(app, origins=[
    'http://localhost:3000',
    'https://iyf.hu',
])
limiter = Limiter(get_remote_address, app=app)

# DEBUG MODE
stripe.api_key = env.get('STRIPE_API_KEY')

# PRODUCTION MODE
# stripe.api_key = env.get('STRIPE_API_KEY')

v1 = Blueprint('v1', __name__, template_folder='templates')

# noinspection PyUnresolvedReferences
import routes

app.register_blueprint(v1, url_prefix='/api/v1')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(env.get("PORT", 8080)))
