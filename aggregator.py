# aggregator.py
# News Data Analysis
#
# Works on the news database to provide an
# analysis of the collected data that:
# - Provides the top Articles and their views
# - Shows which authors have the most views
# - Provides dates with high occurances of
#   HTTP errors.

import psycopg2

DBNAME = "news"

# Open a connection to the news database
db = psycopg2.connect(database=DBNAME)
cursor = db.cursor()

def top_posts(limit):
	"""
	Takes limit as input, where limit is an int
	representing how many articles to print, 
	and outputs a string containing that many
	top articles and their page views, sorted
	from most views to least.
	"""

	return limit

def top_authors():
	"""
	Takes no inputs, outputs a string containing
	all authors sorted and their page views,
	sorted from most views to least.
	"""

	return 0

def high_errors(percent):
	"""
	Takes percent as input, where percent is an int
	representing the error occurance percentage
	to check for, and outputs a string containing
	all dates where errors occured over at a
	higher percent than the input, and the percentage
	of errors for that day.
	"""

	return percent

# Print results to console
for result in [top_posts(3), 
			   top_authors(), 
			   high_errors(1)]:
	print(result)

cursor.close()
db.close()