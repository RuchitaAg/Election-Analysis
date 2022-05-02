# Election-Analysis

## Overview of this excercise-

The purpose of this analysis was to assist a Colorado Board of Election employee Tom in the election audit of the tabulated results of US Congressional precinct for Colorado. I was tasked to generate a vote count report to testify the election results. 

As part of this audit report the requirement was to capture below highlights with the help of python automation to enable adoption at scale: 
- Total # of votes cast. 
- Total # of votes by each candidate, 
- Percentage of votes for each candidate and 
- Identify the winner of election

However, as part of additional request following analysis was also included:
- Breakdown of the number of votes and the percentage of total votes for each county in the precinct
- Identify the county that had the largest number of votes


## Election Audit Results -

As part of the analysis using automated script run on a CSV file, it was identified that a total of 369,711 votes were casted in this election across 3 counties: Arapahoe, Denver and Jefferson. **Denver was the largest county in terms of vote turnout.**

On the candidate list were 3 candidates; Charles Casper Stockham, Raymon Anthony Doane and Diana DeGette. 
**Diana DeGette won the elections with clear majority holding 73.8% of the overall votes casted in her favor.**
 
 Below snapshot provides detailed split of votes for each county and candidate:
 
![image](https://user-images.githubusercontent.com/102870991/166193043-290d4fcb-f031-4ddf-a0ac-7496cf769f61.png)



This summary was created using a Python script that generated the same output in Visual Code Auditor, shown below to offer validation of above output:

![image](https://user-images.githubusercontent.com/102870991/166193284-7b9a5eef-cb10-4b50-ab08-a1c4bfd58208.png)



## Election Audit Summary:

The python script renders analysis with minimal time-investment or human intervention making the audit report free of manual errors. 
It can be easily deployed for other congressional districts as well as senatorial districts and local elections with small modfications:

The script is capable of reading any number of rows with mutliple candidates without requiring any alterations. 

If type of file to be read is different, _we can modify the dependencies_. In our case we inported a CSV file.

We can _modify the path_ where our dependencies are stored by pointing to relevant folders in line # 9 referenced in code snapshot below:

![image](https://user-images.githubusercontent.com/102870991/166194940-c9d0cffe-4b6c-468e-8519-cf479795e27d.png)


Hope you find the audit finding and my python script useful.


Thanks and Regards,

Ruchita Agarwal






