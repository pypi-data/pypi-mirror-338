import pandas as pd
from gather_leads.transform import data_to_df


def test_data_to_df(json_data):
    expected_df = pd.DataFrame(
        {
            "id": ["asdf", "zxcv", "id_3"],
            "display_name_text": ["human readable", "other name", "weird name"],
            "rating": [4.1, 3.8, None],
            "user_rating_count": [125, 99, None],
            "website_uri": ["https://example.com", "https://example2.com", None],
            "international_phone_number": ["+00 0000 00", "+00 0000 01", "+00 0000 02"],
        }
    )

    transformed_df = data_to_df(json_data)

    assert transformed_df.equals(expected_df)
