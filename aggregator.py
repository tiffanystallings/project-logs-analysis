#!/usr/bin/env python3
#
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
from datetime import datetime


DBNAME = "news"

# Open a connection to the news database
db = psycopg2.connect(database=DBNAME)
cursor = db.cursor()


def append_to_result(result, dataset):
    """
    A helper function that takes two inputs
    Where result is the beginning of a result
    string and dataset is a list of tuples from
    the database.
    """
    for element in dataset:
        result += element[0] + " -- " + str(element[1]) + " views\n"
    return result


def top_posts(limit):
    """
    Takes limit as input, where limit is an int
    representing how many articles to print,
    and outputs a string containing that many
    top articles and their page views, sorted
    from most views to least.
    """
    result = "The current Top Articles are: \n"

    # Accessing the top_articles view from the database
    cursor.execute("select * from top_articles limit %s", (limit,))
    top_articles = cursor.fetchall()

    # Appending the data to result
    return append_to_result(result, top_articles)


def top_authors():
    """
    Takes no inputs, outputs a string containing
    all authors sorted and their page views,
    sorted from most views to least.
    """
    result = "The current Author Rankings are: \n"

    # Accessing the top_authors view from the database
    cursor.execute("select * from top_authors")
    top_authors = cursor.fetchall()

    # Appending the data to result
    return append_to_result(result, top_authors)


def high_errors():
    """
    Takes no input, outputs a string containing
    all dates where errors occured over 1% on all
    views, and the percentage of errors for that day.
    """
    result = "The days at higher than 1% error rates: \n"

    # Accessing the high_errors view from the database
    cursor.execute("select * from high_errors")
    error_dates = cursor.fetchall()

    # Formatting dates and appending to result
    for day in error_dates:
        result += day[0].strftime('%B %d, %Y') + (
            ' -- ' + str(day[1]) + '% \n')

    return result

# Print results to console
for result in [top_posts(3),
               top_authors(),
               high_errors()]:
    print(result)

# Close the database connection
cursor.close()
db.close()
