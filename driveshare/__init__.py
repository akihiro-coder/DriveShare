from flask import Flask

from driveshare.extensions import db, migrate, csrf
import config


def create_app(config_class=config.Config):
    # Flaskアプリケーションのインスタンス作成
    app = Flask(__name__)

    # アプリケーションの設定読み込み
    app.config.from_object(config_class)

    # 拡張機能の初期化
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # モデル, APIルートをFlaskに認識/登録させる。
    with app.app_context():
        # モデルをインポート（マイグレーションで必要）
        from driveshare import models

        # APIルーティングを登録
        from driveshare.api.routes import api_bp
        app.register_blueprint(api_bp)

    return app
