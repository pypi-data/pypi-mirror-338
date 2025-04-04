from pathlib import Path

from .gsearch import gsearch
from .transform import data_to_df


def gather_leads(search_text: str, api_key: str, excel_out: Path) -> None:
    data = gsearch(search_text, api_key)
    df = data_to_df(data)
    df.to_excel(excel_out, index=False)
