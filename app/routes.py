from flask import Blueprint, flash, redirect, render_template, request, jsonify, send_from_directory, url_for
from sqlalchemy import and_, func, desc
main_routes = Blueprint('main_routes', __name__)


@main_routes.route('/login', methods=['GET']) 
def getIndex():
    return render_template("indexLogin.html")