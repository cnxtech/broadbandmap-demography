"""
    BroadbandmapAPI class scrapes data from http://www.broadbandmap.gov, does some
    basic error checking, and returns JSON output from requests. 


"""


import requests
import warnings

class BroadbandmapAPI:
    """
        Make API requests to Broadbandmap URLs and return a JSON datastructure
        for requested state. Will do basic error checking to handle bad input
        or connectivity issues.

    """
    url_base_get_st_code = "https://www.broadbandmap.gov/broadbandmap/census/state/"
    url_base_get_demo    = "https://www.broadbandmap.gov/broadbandmap/demographic/"\
                           "jun2014/state/ids/"


    def __init__(self, state="Oregon"):
        """
            Initialize with demographic info from URL and basic error checking.
            If the input state is valid, get an statecode from
            url_base_get_st_code via API call, then use that to get demographic
            data from url_base_get_demo.
           
            Args:
                param2: This should be the name of the state or state or
                        territory to get demographic info on. Must be at least
                        three letters according to broadbandmap.gov API.

        """
        self.state = state
        # We'll use later as test to see if request was successful.
        # 0 means no.
        self.state_code = 0
        self.demographics = ""
        response_state = requests.get("%s%s?format=json" % \
                                      (BroadbandmapAPI.url_base_get_st_code, self.state)).json()
        
        if not response_state['message']:
            self.state_code = response_state['Results']['state'][0]['fips']
            response_demo = requests.get("%s%s?format=json" % (BroadbandmapAPI.url_base_get_demo,
                                                                 self.state_code)).json()
            self.demographics = response_demo['Results']

        if self.state_code == 0:
            warnings.warn("%s is not a valid state/territory." % state)

    def test(self):
        """
        Just return base case of Oregon demographic info to make sure API call is working

        """
        state = "Oregon"
        response = requests.get("%s%s?format=json" % (BroadbandmapAPI.url_base_get_st_code, state))
        api_status = response.status_code
        #print(response.json())
        #print("Status code: ", api_status)

        response = requests.get("%s41?format=json" % (BroadbandmapAPI.url_base_get_demo))
        print(response.json())