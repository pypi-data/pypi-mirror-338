import pandas as pd

from .models import Place


def data_to_df(json_entries: list[dict]) -> pd.DataFrame:
    places_data = [Place.from_json_entry(entry) for entry in json_entries]
    places_df = pd.DataFrame(places_data)
    return places_df
