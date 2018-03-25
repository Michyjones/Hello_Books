from app import UserRegister
from app import flask_app
from app import UserLogin

flask_app.add_url_rule(
    '/api/v1/auth/register', view_func=UserRegister.as_view(
        'register'), methods=['GET', 'POST'])
flask_app.add_url_rule(
    '/api/v1/auth/login', view_func=UserLogin.as_view(
        'login'), methods=['GET', 'POST'])


if __name__ == '__main__':
    flask_app.run(debug=True)
