# Table of Contents
1. [Problem](README.md#problem)
2. [Input Dataset](README.md#input-dataset)
3. [Getting Started](README.md#getting-started)
4. [Running the tests](README.md#running-the-tests)
5. [Automated tests](README.md#automated-tests)
6. [Manual tests](README.md#manual-tests)
7. [Execution](README.md#execution)
8. [Approach](README.md#approach)
9. [Built with](README.md#built-with)
10. [Author](README.md#author)

# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

Your code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code.

# Input Dataset

Raw data could be found [here](https://www.foreignlaborcert.doleta.gov/performancedata.cfm) under the __Disclosure Data__ tab (i.e., files listed in the __Disclosure File__ column with ".xlsx" extension). 
For your convenience we converted the Excel files into a semicolon separated (";") format and placed them into this Google drive [folder](https://drive.google.com/drive/folders/1Nti6ClUfibsXSQw5PUIWfVGSIrpuwyxf?usp=sharing). However, do not feel limited to test your code on only the files we've provided on the Google drive 

**Note:** Each year of data can have different columns. Check **File Structure** docs before development. 
## Getting Started

These instructions will get you a started with the project

### Prerequisites

Python 2.7 needs to be installed (https://www.python.org/getit/).
Internal packages (sys, csv, os, collections) are used in analyzing the H1B data.

### Installing

Github repository can be cloned from https://github.com/ngupta8/h1b_statistics

## Running the tests

Run 
```
cd h1b_statistics/insight_testsuite/ 
./run_tests.sh in 
```

### Automated Tests

Check for Success Cases 

Test_1 - tests to see if top10 occupations and top10 states are evaluated correctly and are sorted in correctly

Test_2 - tests to see when the columns are different for different years

Test_3 - tests when there are more than 10 distinct occupations and states. Hence, it also verifies that the percentages 
are rounded off correctly as per the requirement.

Check when problem in the data

Test_4 - When one of the required column is not in the input.  Should see error message below:
```
ERROR: Required Column Missing: 'WORKSITE_STATE' is not in list
```

# Manual Tests
1. Missing File
2. Missing Directory
3. Improper usage

## Execution

**Option 1:** Run h1b analysis
```
cd h1b_statistics
./run.sh
```
This will read the files from default directories 

`Input File`: ./input/h1b_input.csv 

`Output Files`: ./output/top_10_occupations.txt  and ./output/top_10_states.txt

**Option 2:**
```
cd h1b_statistics
python ./src/h1b_counting.py <input file path> <top occupation file path> <top states file path>
```
## Approach
1. Use DefaultDict from python collections to simplify dictionary operations. Ex: checking if key is initialized when key is used for first time. A defaultdict will never raise a KeyError 
2. Read file only once to build the result dictionary
3. Avoid intermediate storage. For example: use of readlines() and storing it into variable before iterating the file contents
4. Search for needed columns for the header of the file from **File Structure** docs
5. Cleaning the data to get rid of \" in the SOC_NAME field to avoid different keys for same values.
6. Debug_data function is available for debugging while developing
7. Reusable Method for writing to the file for the results.

## Built With

* [Python 2.7.15](https://www.python.org/getit/) - Version of Python used

## Author

* **Neha Gupta** - [ngupta8](https://github.com/ngupta8)
