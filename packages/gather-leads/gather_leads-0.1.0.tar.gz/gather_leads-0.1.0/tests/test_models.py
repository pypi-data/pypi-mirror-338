from gather_leads.models import Place


def test_initializes():
    place = Place(
        "asdf", "human readable", 3, 123, "https://example.com", "+00 000 0000"
    )
    assert place.rating == 3.0


def test_from_json_returns_place_with_all_data():
    json_data = {
        "id": "asdf",
        "displayName": {
            "text": "human readable",
            "language": "en",
        },
        "websiteUri": "https://example.com",
        "internationalPhoneNumber": "+00 0000 00",
        "rating": 4.1,
        "userRatingCount": 125,
    }
    place = Place.from_json_entry(json_data)
    assert place.display_name_text == "human readable"
    assert place.rating == 4.1


def test_from_json_returns_place_with_nones():
    json_data = {
        "id": "asdf",
        "displayName": {
            "text": "human readable",
            "language": "en",
        },
        "websiteUri": None,
        "internationalPhoneNumber": "+00 0000 00",
        "rating": None,
        "userRatingCount": 125,
    }
    place = Place.from_json_entry(json_data)
    assert place.display_name_text == "human readable"
    assert place.website_uri is None
    assert place.rating is None
