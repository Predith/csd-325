#Kristopher Kuenning
#4/6/25
#CSD325
#Module 4

import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt


# Function to display the main menu and get user's choice
def display_menu():
    print("\nMenu:")
    print("1 - View High Temperatures")
    print("2 - View Low Temperatures")
    print("3 - Exit")
    choice = input("Enter your choice (1, 2, or 3): ")
    return choice


# Function to read the weather data from the CSV file
def read_weather_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, high temperatures, and low temperatures from this file.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            low = int(row[6])
            highs.append(high)
            lows.append(low)

    return dates, highs, lows


# Function to plot high temperatures
def plot_highs(dates, highs):
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    plt.title("Daily High Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


# Function to plot low temperatures
def plot_lows(dates, lows):
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')
    plt.title("Daily Low Temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


# Main program function
def main():
    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = read_weather_data(filename)

    while True:
        user_choice = display_menu()

        if user_choice == '1':
            plot_highs(dates, highs)
        elif user_choice == '2':
            plot_lows(dates, lows)
        elif user_choice == '3':
            print("Exiting the program. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please select 1, 2, or 3.")


# Run the main function if the script is executed
if __name__ == '__main__':
    main()