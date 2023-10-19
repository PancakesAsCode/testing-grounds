from flask import Flask
from flask_restful import Api
from info import info_bp
from hit import Hit
from users import Users, User
from metrics import Health, Ready


app = Flask(__name__)
api = Api(app)
apihit = 0

#move this version / info
version = 1.0

# Register blueprints
app.register_blueprint(info_bp)


def apiCount(num):
    return num + 1

@app.route("/count")
def count():
    global apihit
    apihit = apiCount(apihit)
    return "API count: {}\n".format(apihit)

@app.route("/version")
def getVersion():
    global version
    return "Version: {}\n".format(version)


# Define API routes
api.add_resource(Hit, '/hit')
api.add_resource(Users, '/users')
api.add_resource(User, '/users/<int:user_id>')
api.add_resource(Health, '/healthz')
api.add_resource(Ready, '/readyz')

# Program run
if __name__ == "__main__":
    app.run()