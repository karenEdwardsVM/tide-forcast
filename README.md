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
Wrightsville-Beach-North-Carolina:
date: 2022-09-22 time: 11:28AM  height: 0.225540993599512
date: 2022-09-23 time: 12:14PM  height: 0.173727522096922
date: 2022-09-24 time:  1:00PM  height: 0.127
date: 2022-09-25 time:  1:44PM  height: 0.08838768668089
date: 2022-09-26 time:  2:28PM  height: 0.067052727826882
```
