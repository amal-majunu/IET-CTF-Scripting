# Scraping Years?

Author: Amal Majunu Vidya\
Flag: CTF{1987}

## Problem Statement
Jerry is assigned a task of finding the average of year of release of top 250 movies of Imdb within 5 mins. Can you help Jerry find the average year(floor value) of top 250 movies in imdb? The website is [here](https://www.imdb.com/chart/top/).
 The flag is CTF{avg_year}.

## Hint
### Hint1
Data too big to calculate manually?? Ever heard of web scraping? [RESOURCE](https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/)
### Hint2
Remember!! Scaped Data is string

## Solution
Use Python's BeautifulSoup Library to extract the years from the website. Then convert the strings obtained to integer and take the average of all the years.
Python solution code [here](https://github.com/amal-majunu/IET-CTF-Scripting/blob/main/index.py).