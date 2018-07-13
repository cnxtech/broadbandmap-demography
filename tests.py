"""
    Unit tests for broadbandmap-demography application

"""

from broadbandmap_api import BroadbandmapAPI
from report_demog import Report_demography
import csv
import os

def test_BroadbandmapAPI_statecode():
    """ 
    Known Oregon state code is 41

    """
    api_call = BroadbandmapAPI(state='Oregon')
    assert int(api_call.state_code) == 41

def test_BroadbandmapAPI_bad_statecode():
    """
    Invalid state entry should give 0 statecode
    """
    api_call = BroadbandmapAPI(state="Pluto")
    assert api_call.state_code == 0

def test_Report_demography_get_poverty_means_single():
    """
    Expected weighted poverty mean of Oregon is just its poverty rate.
    """
    dataset = []
    api_call_OR = BroadbandmapAPI(state="Oregon")
    poverty_rate_OR = api_call_OR.demographics[0]['incomeBelowPoverty']
    dataset.append(api_call_OR.demographics)
    report = Report_demography(dataset)
    mean = report.get_poverty_means()

    assert mean == poverty_rate_OR

def test_Report_demography_get_poverty_means_multi():
    """
    Expected weighted poverty mean of New York, California, and Oregon is 0.1558
    """
    dataset = []
    api_call_NY = BroadbandmapAPI(state="New York")
    api_call_OR = BroadbandmapAPI(state="Oregon")
    api_call_CA = BroadbandmapAPI(state="California")

    dataset.append(api_call_CA.demographics)
    dataset.append(api_call_OR.demographics)
    dataset.append(api_call_NY.demographics)

    report = Report_demography(dataset)
    mean = report.get_poverty_means()

    assert mean == 0.1558

def test_Report_demography_create_csv():
    """
    Generated CSV file should contain Oregon population of 3996309
    """
    dataset = []
    test_file = 'demographics-unittest.csv'
    api_call_OR = BroadbandmapAPI(state="Oregon")
    poverty_rate_OR = api_call_OR.demographics[0]['incomeBelowPoverty']
    dataset.append(api_call_OR.demographics)
    report = Report_demography(dataset)
    report.create_csv(file=test_file)
    population = 0

    with open(test_file, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for line in reader:
            population = line[1]

    os.remove(test_file)
    assert int(population) == 3996309
