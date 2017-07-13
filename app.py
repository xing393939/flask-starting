# coding: utf-8
import os.path
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)

def register_blueprints(app):
    # Prevents circular imports
    from views import posts
    from views import reply
    from views import user
    app.register_blueprint(posts)
    app.register_blueprint(reply)
    app.register_blueprint(user)

register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)
