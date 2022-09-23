# Tide Forcast
This is code which pulls tide forcasts for the following cities:
```
  Half Moon Bay, California
  Huntington Beach, California
  Providence, Rhode Island
  Wrightsville Beach, North Carolina
```
and uses https://www.tide-forecast.com/ to pull tide information for low tides in those cities.

### Installation and Execution
Made with Python version 3, uses Beautiful Soup
```
pip3 install beautifulsoup4
python3 tide-forcast.py
```

You will see a printout of the tides after sunrise and before sunset for each city in the following formatting:
```
date  time  height
```
