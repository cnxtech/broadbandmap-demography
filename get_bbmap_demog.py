#!/usr/bin/env python
"""
    Main method for broadband-demography: a command line tool that uses an API
    available at http://www.broadbandmap.gov and scrapes basic demographic data
    for a user-defined, comma value separated list of states. 

    This method handles command line options, basic I/O, and basic input error 
    checking.

    Detailed information on usage, required packages, and other pertinent info
    available on README.md attached to Git repository that contains this code.
"""

from broadbandmap_api import BroadbandmapAPI
from report_demog import Report_demography
import argparse
import sys

def main():
    dataset = []

    # Handle commandline arguments and options to the application
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--states", type=str, nargs="+", dest="states", 
                        required=True, help="Comma separated value list of "
                        "states. e.g., \"California,Oregon,New York\"")
    parser.add_argument("-a", "--average", help="Return mean poverty rate of input states.", 
                        action="store_true")
    parser.add_argument("-c", "--CSV", help="Output to CSV file", action="store_true")
    args = parser.parse_args()

    if not args.averages and not args.CSV:
        print("You need to choose to output a mean, CSV, or both!")
        parser.print_help()
        sys.exit()

    arg_str = ' '.join(args.states)
    states = arg_str.split(',')
    states = [state.lstrip() for state in states] # Clean up input

    # Get demographic data
    for state in states:
        api_call = BroadbandmapAPI(state=state)

        # Check for improper state
        if api_call.state_code != 0:
            dataset.append(api_call.demographics)

    # Generate output data from our dataset
    report = Report_demography(dataset)
    print("\n")
    if args.averages:
        mean = report.get_poverty_means()
        print("Mean poverty rate in input states is: %s" % mean)
    if args.CSV:
        report.create_csv(file="demographics.csv")
        print("A report with requested state demographics has been created: demographics.csv")

    print("\n")

if __name__ == '__main__':
    main()