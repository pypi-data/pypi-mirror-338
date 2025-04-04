from dataclasses import dataclass


@dataclass
class Place:
    id: str
    display_name_text: str
    rating: float | None
    user_rating_count: float | None
    website_uri: str | None
    international_phone_number: str | None

    @classmethod
    def from_json_entry(cls, json: dict):
        place = cls(
            json["id"],
            json["displayName"]["text"],
            json.get("rating", None),
            json.get("userRatingCount", None),
            json.get("websiteUri", None),
            json.get("internationalPhoneNumber", None),
        )
        return place
