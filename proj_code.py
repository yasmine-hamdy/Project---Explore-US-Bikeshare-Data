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


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        month = months.index(month) + 1
        # filter by month to create the new DataFrame
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new DataFrame
        df = df[df['day_of_week'] == day.title()]

    return df
