import os
from flask import Flask, render_template, request
from flask import make_response, jsonify, session
from models import User

from flask.views import MethodView

flask_app = Flask(__name__)

users_data = {}

flask_app.secret_key = os.urandom(24)
# print(flask_app.secret_key)


class UserRegister(User, MethodView):
    def get(self):
        return render_template('register.html')

    def post(self):
        # getting a dictonary from flask request form
        data = request.form.to_dict()
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        if email is None:
            return make_response(jsonify(
                {'error': 'Fill in the details'}), 400)

        if password is None:
            return make_response(jsonify(
                {
                    'error': 'Fill in the details'
                }), 400)

        if (role != 'user') and (role != 'admin'):
            return make_response(jsonify(
                {'error': 'Role can only be user or admin'}), 400)

        if len(password) < 8:

            return make_response(jsonify(
                {'message': 'password should be more than 8 character'}), 400)
        if email in users_data.keys():
            return make_response(jsonify(
                {'message': 'user already exist'}), 409)

        new_user = User(email=email, password=password, role=role)
        users_data[email] = new_user
        session['user'] = email
        return make_response(jsonify({
            "message": "user_created successfully"
        }), 201)


class UserLogin(MethodView):
    def get(self):
        return render_template('login.html')

    def post(self):
        data = request.form.to_dict()
        email = data.get('email')
        password = data.get('password')

        if email is None:
            return make_response(jsonify(
                {"error": "Email required"}), 400)

        if password is None:
            return make_response(jsonify(
                {"error": "password required"}), 400)

        if email in users_data.keys():
            user_data = users_data[email]
            if password == user_data.password:
                session['user'] = user_data.email
                if user_data.role == 'user':
                    return make_response(jsonify({
                        "message": "student login successfully"
                    }), 200)
                else:
                    return make_response(jsonify({
                        "message": "Admin logged in"
                    }), 200)
        return make_response(jsonify({
            "error": "invalid credentials"
        }), 401)
