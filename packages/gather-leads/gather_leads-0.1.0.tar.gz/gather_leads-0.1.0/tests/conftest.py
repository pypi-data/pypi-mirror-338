import pytest


@pytest.fixture
def json_data():
    entries = [
        {
            "id": "asdf",
            "displayName": {
                "text": "human readable",
                "language": "en",
            },
            "websiteUri": "https://example.com",
            "internationalPhoneNumber": "+00 0000 00",
            "rating": 4.1,
            "userRatingCount": 125,
        },
        {
            "id": "zxcv",
            "displayName": {
                "text": "other name",
                "language": "en",
            },
            "websiteUri": "https://example2.com",
            "internationalPhoneNumber": "+00 0000 01",
            "rating": 3.8,
            "userRatingCount": 99,
        },
        {
            "id": "id_3",
            "displayName": {
                "text": "weird name",
                "language": "en",
            },
            "websiteUri": None,
            "internationalPhoneNumber": "+00 0000 02",
            "rating": None,
            "userRatingCount": None,
        },
    ]
    return entries
