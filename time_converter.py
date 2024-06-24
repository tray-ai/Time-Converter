import time_converter_functions as tcf

def main():
    """ Main point that allows user to choose a conversion and 
    have a function perform it. """

    # Initiate a menu for the user to choose a conversion.
    menu = {
        '1' : 'seconds to minutes', 
        '2' : 'minutes to hours',
        '3' : 'hours to days',
        }
    
    while True:
        # Loop through dictionary to show user the conversion options.
        for number, convert in menu.items():
            print(number, ":", convert)
        
        # Prompt the user to choose a conversion. 
        conversion = input('\nSelect a conversion you would like to perform (1, 2, or 3): ').lower()

        if conversion == 'q':
            print("Exiting the program. Goodbye!")
            break
        # contrast if the input is not a key in the dictionary.
        elif conversion not in menu.keys():
                print('Invalid input. Please select a valid option. ')
                continue
        elif conversion == '1':
                minutes, seconds = tcf.seconds_to_minutes()
                print(f'\n{seconds} seconds converted to minutes is {minutes:.2f} minutes.\n')

        elif conversion == '2':
                hours, minutes = tcf.minutes_to_hours()
                print(f'\n{minutes} minutes converted to minutes is {hours:.2f} hours.\n')

        elif conversion == '3':
                days, hours = tcf.hours_to_days()
                print(f'\n{hours} hours converted to days is {days:.2f} days.\n')
            

if __name__ == "__main__":
    main()