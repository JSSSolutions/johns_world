from flask import Flask # pip install flask

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'KEY'

	from .views import views # no need for an auth section -- normally, there'd also be a from .auth import auth, as well as a corresponding register statement
	
	app.register_blueprint(views, url_prefix='/')
	return app