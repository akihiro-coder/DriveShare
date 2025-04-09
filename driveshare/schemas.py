from pydantic import BaseModel
from typing import List


class Location(BaseModel):
    lat: float
    lng: float


class RouteOut(BaseModel):
    id: int
    title: str
    description: str | None = None
    start_location: Location
    end_location: Location
    created_at: str
    updated_at: str