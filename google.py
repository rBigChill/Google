#! /usr/local/bin/python

import webbrowser
import sys

def gSearch():
    """
        Search google from CLI
    """

    # save CLI args into variable
    query = ' '.join(sys.argv[1:])

    # open default browser with CLI query
    webbrowser.open("https://google.com/search?q=%s" % query)

if __name__ == "__main__":
    gSearch()
