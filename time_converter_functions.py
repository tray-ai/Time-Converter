def seconds_to_minutes():
    """ Takes input from the user in seconds and converts it to minutes. """

    prompt = "Enter 'q' to quit the program."
    prompt += '\nEnter time in seconds, I will convert it to minutes: '

    while True:
        
        # This input will be used to convert the given seconds into minutes.
        seconds = input(prompt).lower()

        if seconds == 'q':
            print("Exiting the program. Goodbye!")
            return (0,0)
            

        try:
            seconds = float(seconds)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue
        else:
            # print(f'{input_seconds} seconds is equal to {minutes:.2f} minutes.')
            # There are 60 seconds in a minute, so we divide the input seconds by 60. 
            return seconds / 60, seconds
    

def minutes_to_hours():
    """Takes input of minutes from user and converts it to hours"""

    prompt = "Enter 'q' to quit the program."
    prompt += '\nEnter time in minutes, I will convert it to hours: '

    while True:
        
        # This input will be used to convert the given seconds into minutes.
        minutes = input(prompt).lower()

        if minutes == 'q':
            print("Exiting the program. Goodbye!")
            return (0,0)

        try:
            minutes = float(minutes)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue
        else: 
            # There are 60 minutes in a hour, so we divide the input minutes by 60.
            return minutes / 60, minutes


def hours_to_days():
    """Takes input of hours from the users and converts it to days"""

    prompt = "Enter 'q' to quit the program."
    prompt += '\nEnter time in hours, I will convert it to days: '

    while True:
        
        # This input will be used to convert the given hours into days.
        hours = input(prompt).lower()

        if hours == 'q':
            print("Exiting the program. Goodbye!")
            return (0,0)

        try:
            hours = float(hours)
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue
        else: 
            # There are 24 hours in a day, so we divide the input hours by 24.
            return hours / 24, hours