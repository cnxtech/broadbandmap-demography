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
from report_demog import Report_demography

import sys

def main():
    tests = []
    test1 = BroadbandmapAPI(state="Oregon")
    res1 = test1.demographics
    test2 = BroadbandmapAPI(state="New York")
    res2 = test2.demographics
    test3 = BroadbandmapAPI(state="Cali")
    res3 = test3.demographics
    test4 = BroadbandmapAPI(state="Texas")
    res4 = test4.demographics

    tests.append(res1)
    tests.append(res2)
    tests.append(res3)
    tests.append(res4)


    test_report = Report_demography(tests)
    test_report.create_csv(file="foo.csv")
    print(test_report.get_poverty_means())

if __name__ == '__main__':
    main()