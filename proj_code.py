import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('\nWhich city would you like to explore data for? (Chicago, New York City, Washington)\n').lower()
    while city not in CITY_DATA:
        city = input('\nInvalid input. Please choose one of the following cities: Chicago, New York City, Washington\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('\nWhich month would you like to filter by, if any? (all, January, February, ... , June)\n').lower()
    while month not in months:
        month = input('\nInvalid input. Please try again.\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nWhich day would you like to filter by, if any? (all, Monday, Tuesday, ... , Sunday)\n').lower()
    #if day != 'all':
    while day not in weekdays:
        day = input('\nInvalid input. Please try again.\n').lower()

    print('-'*40)
    return city, month, day