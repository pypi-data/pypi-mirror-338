import argparse

from ._version import version
from gather_leads.main import gather_leads


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("SEARCH_TEXT", help="Input query")
    parser.add_argument("API_KEY", help="Your API key", type=str)
    parser.add_argument("OUTPUT", help="Output file")
    parser.add_argument("--version", action="version", version=version)
    args = parser.parse_args()

    gather_leads(args.SEARCH_TEXT, args.API_KEY, args.OUTPUT)
