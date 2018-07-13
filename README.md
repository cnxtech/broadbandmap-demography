# broadbandmap-demography

```
usage: get_bbmap_demog.py [-h] [-s STATES [STATES ...]] [-a] [-c]

optional arguments:
  -h, --help            show this help message and exit
  -s STATES [STATES ...], --states STATES [STATES ...]
                        Comma separated value list of states. e.g.,
                        "California,Oregon,New York"
  -a, --average         Return mean poverty rate of input states.
  -c, --CSV             Output to CSV file
```
## Basics

A simple command line Python utility to scrape data from National Broadband Map API. Simply provide a comma separated value (CSV) list of states you want info on, and the application will determine the state code, and collect demographic information of the state. Info is gathered according to following URLs.

- State/territory codes: https://www.broadbandmap.gov/developer/api/census-api-by-geography-name
- State/territory demographics: https://www.broadbandmap.gov/developer/api/demographics-api-by-geography-type-and-geography-id

Examples are often the most illuminating:

```
$ python get_bbmap_demog.py -s California, New York, Oregon --CSV --average
```

Will collect demographic information on California, New York, and Oregon. This information will be outputted
to a csv file called `demographics.csv` in the directory the application was run. Additionally, with the
`--averages` option, the program will compute the weighted mean of the poverty rates in each state and output
to `stdout`. 

```
Mean poverty rate in input states is: 0.1558
A report with requested state demographics has been created: demographics.csv
```

The API only requires the first three letters of the state to work, so 'Cali' will collect data for California. Be warned, ambiguous input will just default to the first state ID so 'New' gets data for 'New Mexico'. Invalid state/territory will throw a warning and be discarded from final reports and calculations.

## Requirements

The following python libraries are required.

```
argparse
sys
requests
warnings
csv
operator
```

These should be included with most modern Python 3.6.x implementations. Please note, this has only been tested thoroughly with Python 3.6.5, although Python 3.x should work without issue. I cannot make any claims against Python 2.x!

## Unit Testing

Invoke with `py.test`:

```
$ py.test tests.py
```

## To Do, Assumptions, Caveats

- brodbandmap.gov relies on census data from several different years. This application assumes that the user will always want the latest data. A future release might make this optional.
- Very simply file handling (as in, virtually none!). The application outputs to `demographics.csv` and will simply write over it if run again. A future version will give more control over this.
- Simple error correction/detection. The application gives reasonable attempts to make sure input data is correct and to discard bad queries, however, it is quite elementary. Also, other failures such as inability to reach URLs with API calls are not handled at all. Caveat emptor: this is NOT production ready code, but fine for testing and concept.
