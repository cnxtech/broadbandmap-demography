"""
    BroadbandmapAPI class scrapes data from http://www.broadbandmap.gov, does some
    basic error checking, and returns JSON output from requests. 


"""


import requests
import json

class BroadbandmapAPI:
    url_base_get_st_code = "https://www.broadbandmap.gov/broadbandmap/census/state/"
    url_base_get_demo    = "https://www.broadbandmap.gov/broadbandmap/demographic/"\
                           "jun2014/state/ids/"


    def __init__(self, state="Oregon"):
        """
            Mostly figure out if we're getting errors from requests but otherwise move things
            along


        """
        self.state = state
        self.state_code = 0
        self.demographics = ""
        self.is_good_req = False # Is the requested state query valid?
        response_state = requests.get("%s%s?format=json" % \
                                      (BroadbandmapAPI.url_base_get_st_code, self.state)).json()
        
        if (response_state['status'] == 'OK'):
            self.is_good_req = True
            self.state_code = response_state['Results']['state'][0]['fips']

        self.demographics = requests.get("%s%s?format=json" % (BroadbandmapAPI.url_base_get_demo,
                                                               self.state_code)).json()
        print(self.demographics)

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