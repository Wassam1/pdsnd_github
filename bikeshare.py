import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    print('Please select a city from the following: 1-chicago 2-new york city 3-washington\n')
    print('Please make sure your input is in lower case matching the options above\n')
    
    city = input('City selection: ')
    
    while city not in CITY_DATA.keys():
        
        print('Please make sure your input is in lower case matching the provided options\n')
        
        city = input('City selection: ')
        
        if city not in CITY_DATA.keys():
            print('Invalid input!\n')
    
    print('\nYou have selected "{}" as your choice.\n'.format(city.title())) 

    # TO DO: get user input for month (all, january, february, ... , june)
    Months = {'january': 1,
              'february': 2,
              'march': 3,
              'april': 4,
              'may': 5,
              'june': 6,
              'all': 13}
    
    print('!Month Filter!\n')
    print('You can filter data by months (from january to june). Your input should be full month name in lower case.\n')
    print('If you DO NOT want to apply this filter type "all".')
    
    month = input('\nMonth Selection: ')
    
    while month not in Months.keys():
        
        print('Please make sure your input is in lower case & full month name.\n')
        
        month = input('Month selection: ')
        
        if month not in Months.keys():
            print('\nInvalid input!\n')
    
    print('\nYou have selected "{}" for your month filter.'.format(month))
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    Days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
            
    
    print('\n!Day Filter!\n')
    print('You can filter data by days of the week. Your input should be full day name in lower case.\n')
    print('If you DO NOT want to apply this filter type "all".')
    
    day = input('\nDay selection: ')
    
    while day not in Days:
        
        print('Please make sure your input is in lower case & full day name.\n')
        
        day = input('Day selection: ')
        
        if day not in Days:
            print('\nInvalid input!\n')
    
    print('You have selected "{}" for your day filter'.format(day))


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
    #reading the csv file for the selected city (similart to practice3 question)
    df = pd.read_csv(CITY_DATA[city])
    
    #creating the required filters by month and day if selected. To do so we first
    #need to convert start time to datetime and then extract month and day into new columns and then apply filters.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    #Month filter
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        #creating our month filtered dataframe
        df = df[df['month'] == month]
        
        
    #Day filter
    if day != 'all':
        
        #creating day filtered dataframe
        df = df[df['day_of_week'] == day.title()] #our input was lower so we need 'title' to match dataframe
        

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    
    Returns:
        Nothing
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time() #capture start time for computation duration

    # TO DO: display the most common month
    # 'mode' method is used to display most common month (from practice questions)
    common_month = df['month'].mode()[0]
    
    print('The most common month is: {}\n'.format(common_month))


    # TO DO: display the most common day of week
    #'mode' method is used to display most common day (from practice questions)
    common_day = df['day_of_week'].mode()[0]
    
    print('The most common day is: {}\n'.format(common_day))


    # TO DO: display the most common start hour
    #first need to creat an hour column, then use mode to find most common hour
    df['hour'] = df['Start Time'].dt.hour
    
    common_hour = df['hour'].mode()[0]
    
    print('The most common hour is: {}\n'.format(common_hour))

    #computation duration
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        
    Returns:
        Nothing
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()#capture start time for computation duration

    # TO DO: display most commonly used start station
    # 'mode' method is used for the most common start station
    strt_station = df['Start Station'].mode()[0]
    
    print('The most common start station is: {}.\n'.format(strt_station))

    # TO DO: display most commonly used end station
    # 'mode' method is used for the most common end station
    end_station = df['End Station'].mode()[0]
    
    print('The most common end station is: {}.\n'.format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    # 'str.cat' will be used to concat all combos of start-end into a new column then find
    # the most popular combo with 'mode'
    df['Start-End'] = df['Start Station'].str.cat(df['End Station'], sep = ' - ')
    
    combo = df['Start-End'].mode()[0]
    
    print('The most frequent combination of start-end station for trips is: {}. \n'.format(combo))
    
    #computation duration
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        
    Returns:
        nothing
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()#computation duration start time

    # TO DO: display total travel time
    # Trip duration is displayed in seconds. For any meaningful data we will display in hours,
    # minutes and seconds using 'divmod'
    tot_duration = df['Trip Duration'].sum()
    
    mins, secs = divmod(tot_duration, 60)
    
    hrs, mins = divmod(mins, 60)
    
    print('Total travel time is {} hrs, {} mins, {} secs.\n'.format(hrs, mins, secs))
    

    # TO DO: display mean travel time
    #for mean we use'mean' method then 'divmod' again to get average trips length in minutes
    avg_duration = df['Trip Duration'].mean()
    
    minutes, seconds = divmod(avg_duration, 60)
    
    print('Average trip durations in minutes is: {}\n'.format(minutes))
    #I don't need to use the seconds as it will be too much details
    #the variable is created to make sure divmod runs ok

    #computation duration
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
        
    Returns:
        noting
        
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()#capture computation duration start time

    # TO DO: Display counts of user types
    # here we use 'value_counts' method as per example
    user_type = df['User Type'].value_counts()
    
    print('Counts of User Types: \n{}'.format(user_type))


    # TO DO: Display counts of gender
    # to display genders we will apply a try clause as
    # some dataframe will not have a gender feed
    try:
        gen = df['Gender'].value_counts()
        print('\nCounts of users\' genders are shown below: \n{}'.format(gen))
        
    except:
        print('Genders were not provided by users\n')


    # TO DO: Display earliest, most recent, and most common year of birth
    # we will need another try clause for birthdate as not all dataframes will have birth dates
    try:
        min_year = int(df['Birth Year'].min())
        max_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        
        print('\nThe earliest year of birth is {} while the most recent one is {} and the most common year is {}\n'.format(min_year, max_year, common_year))
    
    except:
        print('Birth dates were not provided by users\n')
        
    #computation duration
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    #this function is created to meet the rubric's criteria of displaying raw data upon user's request.
def sample_data(df):
    """
    Displays 5 sample rows of the filtered selected dataframe.
    
    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    
    Returns:
        nothing
    """
    #request user input
    print('\nWould you like to view a smaple list of the raw data?')
    print('please type "yes" or "no"')
    
    #creat list for our while loop responses
    responses = ['yes', 'no']
    
    response = input().lower()
    
    #initialize our counter to ensure printing different set of lines from the dataframe.
    line = 0
    
    if response == 'yes':
            print(df.head())
        
    elif response not in responses:
        print('Invalid input!\n')
    
    
    while response not in responses:
        
        print('Please make sure you only type "yes" or "no".\n')
        
        response = input()

    
    #second while loop to check if mroe data is required
    while response.lower() == 'yes':
        print('\nWould you like to view more data?')
        line += 5
        response = input().lower()
        
        if response == 'yes':
            print(df[line:line+5])
        
        elif response != 'yes':
            break
    
    print('-'*40)
        
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        sample_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
