import time

import requests

from gather_leads.constants import GOOGLE_PLACES_API, MASK_FIELDS


def gsearch(
    search_text: str,
    api_key: str,
    url: str = GOOGLE_PLACES_API,
    mask_fields: list[str] = MASK_FIELDS,
) -> list:
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": ",".join(mask_fields),
    }

    params = {"textQuery": search_text}

    all_results = []
    while True:
        response = requests.post(url, headers=headers, params=params)
        data = response.json()

        if "places" in data:
            all_results.extend(data["places"])

        next_page_token = data.get("nextPageToken")
        if not next_page_token:
            break  # No more pages to fetch

        params["pageToken"] = next_page_token
        time.sleep(2)  # Delay to allow API to process the next page token

    return all_results
