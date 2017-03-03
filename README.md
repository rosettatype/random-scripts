# Random scripts

## Get all Google Fonts

A Python script/CLI that downloads all fonts from Google Fonts using the API. You will need to provide an API key. Get one [here](https://developers.google.com/fonts/docs/developer_api). The script is borrowing a lot from [this FontBakery script](https://github.com/googlefonts/fontbakery/blob/master/fontbakery-metadata-vs-api.py).

Usage:

In Terminal, in the folder with the script:

`python get_all_google_fonts.py --apikey XXXXXAPIKEYXXXX` downloads all fonts to a subfolder of the current folder. Takes a few minutes (currently it is about 320 MB of fonts)  
`python get_all_google_fonts.py --apikey XXXXXAPIKEYXXXX --subsets latin,gujarati` downloads only fonts that include `latin` and `gujarati` subsets. See the API docs for more subset options.  
`python get_all_google_fonts.py --apikey XXXXXAPIKEYXXXX --out darkfold` downloads all fonts to a folder `Darkhold`.  

For other options, see the script.

## Feedback

These scripts are provided as is. Feel free to submit an issue, but we might not have the time to fix it.