# gather-leads

A minimal, proof-of-concept command-line tool to post a text query on Google's Places API and write the results in
an Excel file.

## Installation

```
$ pip install gather-leads
```

## Usage

```
usage: gather-leads [-h] [--version] SEARCH_TEXT API_KEY OUTPUT

positional arguments:
  SEARCH_TEXT  Input query
  API_KEY      Your API key
  OUTPUT       Output file

options:
  -h, --help   show this help message and exit
  --version    show program's version number and exit
```

You need to generate your own Google API key. Instructions [available here](https://support.google.com/googleapi/answer/6158862?hl=en).

Example:

```
export MY_KEY=SomeLongString
gather-leads 'spicy vegan food New York' $MY_KEY spicy.xlsx
```
