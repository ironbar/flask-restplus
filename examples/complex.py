from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from zoo import api

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
api.init_app(app)

app.run(debug=True)
