from driveshare.models import Route
from driveshare.schemas import RouteOut, Location
from typing import List


def get_all_routes() -> List[RouteOut]:
    routes = Route.query.all()

    return [
        RouteOut(
            id=route.id,
            title=route.title,
            description=route.description,
            start_location=Location(lat=route.start_latitude, lng=route.start_longitude),
            end_location=Location(lat=route.end_latitude, lng=route.end_longitude),
            created_at=route.created_at.isoformat(),
            updated_at=route.updated_at.isoformat()
        )
        for route in routes
    ]