#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Downloads all the fonts from Google Fonts using the API (you will need an API key).

The script is borrowing a lot from: https://github.com/googlefonts/fontbakery/blob/master/fontbakery-metadata-vs-api.py
"""

import json
import optparse
import os
import sys
import urllib
import urlparse


# Mapping weights to numbers
# using the intended postscript name might have been nicer
# but this is easier than having fontTools as a requirement
weight_numbers = {
    "Thin": "100",
    "ExtraLight": "200",
    "Light": "300",
    "Regular": "400",
    "Medium": "500",
    "SemiBold": "600",
    "Bold": "700",
    "ExtraBold": "800",
    "Black": "900",
}


def parseOptions():
    usage = "usage: %prog [options]"
    parser = optparse.OptionParser(formatter=optparse.TitledHelpFormatter(), usage=usage,
        description="%prog")

    parser.add_option("-a", "--apikey",
        action="store", dest="apikey", type="string", default="",
        help="required, the API key, get yours at https://developers.google.com/fonts/docs/developer_api")
    parser.add_option("-o", "--out",
        action="store", dest="out", type="string", default="downloaded_google_fonts",
        help="target directory")
    parser.add_option("-s", "--subsets",
        action="store", dest="subsets", type="string", default="",
        help="optional, comma-separated list of subsets the fonts have to support (e.g. latin,latin-ext,gujarati). When empty, all fonts get downloaded. When used, only fonts with these subsets are downloaded.")
    parser.add_option("-t", "--test",
        action="store_true", dest="test", default=False,
        help="just report, do not download anything")
    return parser.parse_args()


def getVariantName(code):

    variant_name = code.replace("italic", "Italic").replace("regular", "Regular")
    for name, number in weight_numbers.items():
        variant_name = variant_name.replace(number, name)

    return variant_name


def main():
    (options, args) = parseOptions()

    if options.subsets:
        options.subsets = set(options.subsets.split(","))
    else:
        options.subsets = set()

    if options.apikey:
        response = urllib.urlopen("https://www.googleapis.com/webfonts/v1/webfonts?key={}".format(options.apikey))
        try:
            font_list = json.loads(response.read())["items"]
            family_names = [item["family"] for item in font_list]
        except (ValueError, KeyError):
            sys.exit(1)

        downloaded_fonts = 0
        downloaded_families = []
        for font_item in font_list:
            family_name = font_item["family"]
            for variant_code, font_url in font_item["files"].items():
                urlparts = urlparse.urlparse(font_url)
                extension = os.path.splitext(urlparts.path)[1]
                font_name = "%s-%s%s" % (family_name, getVariantName(variant_code), extension)
                cache_font_path = os.path.join(options.out, family_name, font_name)
                cache_dir = os.path.dirname(cache_font_path)
                if options.subsets.issubset(set(font_item["subsets"])):
                    downloaded_fonts += 1
                    if family_name not in downloaded_families:
                        downloaded_families.append(family_name)
                    if not options.test:
                        if not os.path.exists(cache_dir):
                            os.makedirs(cache_dir)
                        with open(cache_font_path, "w") as fp:
                            fp.write(urllib.urlopen(font_url).read())
                    print("Downloading: {}".format(font_name))
        print("Downloaded {} families, {} fonts in total.".format(downloaded_fonts, len(downloaded_families)))
    else:
        print("Add -h for help")

if __name__ == "__main__":
  main()
