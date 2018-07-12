#!/usr/bin/env python
"""
    Main method for broadband-demography: a command line tool that uses an API
    available at http://www.broadbandmap.gov and scrapes basic demographic data
    for a user-defined, comma value separated list of states. 

    This method handles command line options, basic I/O, and initial, basicl 
    input error checking.

    Detailed information on usage, required packages, and other pertinent info
    available on README.md attached to Git repository that contains this code.



"""

from broadbandmap_api import BroadbandmapAPI

def main():

    BroadbandmapAPI(state="New York")
    print("Hello world")


if __name__ == '__main__':
    main()