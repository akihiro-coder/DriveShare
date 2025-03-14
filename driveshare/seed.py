from driveshare import create_app, db
from driveshare.models import Route, Waypoint, Photo
from datetime import datetime


def seed_data():
    app = create_app()

    # アプリケーションコンテキストに入る（これがないとDB操作ができない）
    with app.app_context():
        print("🚀 Seeding database with initial data...")

        # 既存データ削除（リセット）
        db.session.query(Waypoint).delete()
        db.session.query(Photo).delete()
        db.session.query(Route).delete()
        db.session.commit()

        # --------------------------
        # 1件目のルート（箱根ドライブ）
        # --------------------------
        hakone_route = Route(
            title="箱根ターンパイクドライブ",
            description="絶景を楽しみながら走れるルート",
            start_latitude=35.232,
            start_longitude=139.112,
            end_latitude=35.349,
            end_longitude=139.154,
            route_path=[
                {"latitude": 35.232, "longitude": 139.112},
                {"latitude": 35.280, "longitude": 139.130},
                {"latitude": 35.349, "longitude": 139.154}
            ],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        # Waypoints
        hakone_wp1 = Waypoint(
            route=hakone_route,
            sequence=1,
            latitude=35.280,
            longitude=139.130
        )
        hakone_wp2 = Waypoint(
            route=hakone_route,
            sequence=2,
            latitude=35.310,
            longitude=139.140
        )

        # Photos
        hakone_photo1 = Photo(
            route=hakone_route,
            photo_path="photos/hakone_turnpike.jpg",
            caption="ターンパイクから見た絶景ポイント"
        )
        hakone_photo2 = Photo(
            route=hakone_route,
            photo_path="photos/hakone_cafe.jpg",
            caption="途中に立ち寄ったカフェ"
        )

        # --------------------------
        # 2件目のルート（伊豆スカイライン）
        # --------------------------
        izu_route = Route(
            title="伊豆スカイラインツーリング",
            description="海と山を楽しむ伊豆半島縦断ルート",
            start_latitude=35.032,
            start_longitude=138.926,
            end_latitude=35.088,
            end_longitude=139.012,
            route_path=[
                {"latitude": 35.032, "longitude": 138.926},
                {"latitude": 35.060, "longitude": 138.970},
                {"latitude": 35.088, "longitude": 139.012}
            ],
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

        # Waypoints
        izu_wp1 = Waypoint(
            route=izu_route,
            sequence=1,
            latitude=35.060,
            longitude=138.970
        )
        izu_wp2 = Waypoint(
            route=izu_route,
            sequence=2,
            latitude=35.075,
            longitude=138.990
        )

        # Photos
        izu_photo1 = Photo(
            route=izu_route,
            photo_path="photos/izu_ocean_view.jpg",
            caption="伊豆スカイラインからの海の眺め"
        )
        izu_photo2 = Photo(
            route=izu_route,
            photo_path="photos/izu_rest_stop.jpg",
            caption="休憩ポイントで食べたソフトクリーム"
        )

        # データをセッションに追加
        db.session.add_all([
            hakone_route, hakone_wp1, hakone_wp2, hakone_photo1, hakone_photo2,
            izu_route, izu_wp1, izu_wp2, izu_photo1, izu_photo2
        ])

        # コミット！
        db.session.commit()

        print("✅ Database seeded successfully!")


if __name__ == "__main__":
    seed_data()
