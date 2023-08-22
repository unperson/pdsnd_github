import time
import math
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAYS_OF_WEEK = ['all', 'monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']


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
    city = ''
    while city not in CITIES:
        city = input(
            'Please enter one of the following cities to analyze: Chicago, New York City, Washington: ').strip().lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month not in MONTHS:
        month = input(
            'Please enter one of the following months to analyze: all, January, February, March, April, May, June: ').strip().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in DAYS_OF_WEEK:
        day = input(
            'Please enter the day of week to analyze, e.g. all, Monday, Tuesday, Wednesday, ...: ').strip().lower()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month of travel: ' +
          MONTHS[df['month'].mode()[0]].title())
    print('-'*20)

    # TO DO: display the most common day of week
    print('The most common day of travel: ' + df['day_of_week'].mode()[0])
    print('-'*20)

    # TO DO: display the most common start hour
    print('The most common start hour of travel: ' +
          str(df['Start Time'].dt.hour.mode()[0]))
    print('-'*20)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station was: ' +
          df['Start Station'].mode()[0])
    print('-'*20)

    # TO DO: display most commonly used end station
    print('The most commonly used end station: ' + df['End Station'].mode()[0])
    print('-'*20)

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip:")
    print(df.groupby(['Start Station', 'End Station']).size().nlargest(1))
    print('-'*20)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_time_in_seconds = df['Trip Duration'].values.sum()
    print(f"The total travel time: {total_trip_time_in_seconds} seconds")
    days = total_trip_time_in_seconds // 86400
    total_trip_time_in_seconds = total_trip_time_in_seconds % 86400
    hours = total_trip_time_in_seconds // 3600
    total_trip_time_in_seconds = total_trip_time_in_seconds % 3600
    minutes = total_trip_time_in_seconds // 60
    total_trip_time_in_seconds = total_trip_time_in_seconds % 60
    seconds = total_trip_time_in_seconds
    print(
        f"The total travel time in days, hours, minutes, seconds: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(math.floor(seconds))} seconds")
    print('-'*20)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].values.mean()
    print(f"The mean travel time was: {mean_travel_time} seconds")
    days = mean_travel_time // 86400
    mean_travel_time = mean_travel_time % 86400
    hours = mean_travel_time // 3600
    mean_travel_time = mean_travel_time % 3600
    minutes = mean_travel_time // 60
    mean_travel_time = mean_travel_time % 60
    seconds = mean_travel_time
    print(
        f"The mean travel time in days, hours, minutes, seconds: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, {int(math.floor(seconds))} seconds")
    print('-'*20)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Counts:')
    print(df['User Type'].value_counts())
    print('-'*20)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('Gender Counts:')
        print(df['Gender'].value_counts())
        print('-'*20)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print(f"Earliest year of birth: {int(df['Birth Year'].min())}")
        print(f"Most recent year of birth: {int(df['Birth Year'].max())}")
        print(f"Most common year of birth: {int(df['Birth Year'].mode()[0])}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    index = 0
    response = input(
        'Do you want to see 5 lines of raw data (yes/no)? ').strip().lower()
    while response == 'yes' and index < df.shape[0]:
        print(df.iloc[index:index + 5])
        index += 5
        response = input(
            'Do you want to see 5 more lines of raw data (yes/no)? ').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

# Thank you, Udacity