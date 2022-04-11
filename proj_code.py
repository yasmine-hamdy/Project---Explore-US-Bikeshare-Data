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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # calculate the most common month
    popular_month = df['month'].value_counts().idxmax()
    # display the most common month
    print('\nMost Common Month: ', popular_month)

    # calculate the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    # display the most common day of week
    print('\nMost Common Day of the Week: ', popular_day)

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # calculate the most common hour
    popular_hour = df['hour'].mode()[0]

    # display the most common start hour
    print('\nMost Common Start Hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('\nMost Commonly Used Start Station:\n', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly Used End Station:\n', popular_end_station)

    # display most frequent combination of start station and end station trip
    popular_combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print('\nMost Frequent Combination of Start Station and End Station Trip:\n', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal Travel Time: ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean Travel Time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

