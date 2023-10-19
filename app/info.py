from flask import Blueprint

info_bp = Blueprint('info', __name__)

@info_bp.route("/info")
def getinfo():
    return "Printing info\n"