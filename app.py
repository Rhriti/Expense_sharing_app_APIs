from flask import Flask
from routes.user_routes import user_bp
from routes.expense_routes import expense_bp
from routes.balance_sheet import bp


app = Flask(__name__)
app.config.from_object('config.Config')


app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(expense_bp, url_prefix='/api')
app.register_blueprint(bp, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)
