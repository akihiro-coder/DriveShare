from flask import Flask
from flask_migrate import Migrate
from models import db  # 既に定義してあるはず


def create_app():
    app = Flask(__name__)

    # 設定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ユーザー名:パスワード@localhost/DB名'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # DBとMigrate初期化
    db.init_app(app)
    migrate = Migrate(app, db)

    return app