from flask import Flask

import api

def create_app():
	app = Flask('app', static_folder=None)

	configure_app(app)
	register_blueprints(app)

	return app

def configure_app(app):
	app.config.from_object('config')

def register_blueprints(app):
	app.register_blueprint(api.views.BLUEPRINT)

if __name__ == '__main__':
	APP = create_app()
	APP.run(
		host='0.0.0.0',
		debug=True
	)
