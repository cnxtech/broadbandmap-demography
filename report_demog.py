"""
    Class to handle modifying JSON input and making clean output

"""
import csv
import operator

class Report_demography:
    """

    Generate output of data scraped from broadbandmap.com either in form
    of CSV report or with population weighted averages.

    Attributes:
        demography (list): JSON output from API request to broadbandmap.gov.
                           Gets sorted by state name.
        csvfile: csv file generated from demography data.

    """
    def __init__(self, demography):
        """
        Initialize with dataset in form of a list of JSON per state

        Args:
            demography: A list containing JSON output of a state's
                        demography
        """

        # Sort by state name so we don't have to mess with this with csv
        # creation, if required.
        self.demography = sorted(demography, key=lambda s: s[0]['geographyName'])

    def get_poverty_means(self):
        """
            Get weighted means of 'income below means' demography data

        """

        mean = 0.0
        total_pov = 0.0 # total number of people living in poverty
        total_pop = 0.0

        for data in self.demography:
            population = data[0]['population']
            incomeBelowPoverty = data[0]['incomeBelowPoverty']
            popBelowPoverty = population * incomeBelowPoverty

            total_pov += popBelowPoverty
            total_pop += population

        return(round((total_pov / total_pop), 4))

    def create_csv(self, file):
        """
        Generate csv report in alphabetical order of all states' demography

        Args:
            file: some file to accept output. If not provided, output
                  goes to stdout.

        """

        self.csvfile = file
        header = ['state', 'population', 'households', 'income below poverty',
                  'median income']

        with open(self.csvfile, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerow(header)

            for data in self.demography:
                state = data[0]['geographyName']
                population = data[0]['population']
                households = data[0]['households']
                incomeBelowPoverty = data[0]['incomeBelowPoverty']
                medianIncome = data[0]['medianIncome']
                csv_entry = [state, population, households, incomeBelowPoverty,
                             medianIncome]
                writer.writerow(csv_entry)

        
