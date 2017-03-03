# Random scripts

## Get all Google Fonts

A Python script/CLI that downloads all the fonts from Google Fonts using the API. You will need to provide an API key, get one [here](https://developers.google.com/fonts/docs/developer_api). The script is borrowing a lot from [this FontBakery script](https://github.com/googlefonts/fontbakery/blob/master/fontbakery-metadata-vs-api.py).

Usage:

In Terminal, in the folder with the script you can do, for example:

`python get_all_google_fonts.py --apikey <your API key>` downloads all fonts to a subfolder of the current folder. Takes a few minutes (currently it is about 320 MB of fonts)

`python get_all_google_fonts.py --apikey <your API key> --subsets latin,gujarati` downloads only fonts that include `latin` and `gujarati` subsets. See the API docs for more subset options.

`python get_all_google_fonts.py --apikey <your API key> --out Darkfold` downloads all fonts to a folder `Darkhold`.

For other options, see the script’s own help.

Alternatively, if you did not need the most recent fonts, you could download [this archive](https://github.com/google/fonts/archive/master.zip). Note, however, that as of 3 March 2017, it has not been updated for a while and some nice new families are missing.

## Feedback

These scripts are provided as is. Feel free to submit an issue, but we might not have the time to fix it.