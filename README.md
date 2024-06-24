# Time-Converter
 This Python script provides a user-friendly interface to perform basic time unit conversions, such as converting seconds to minutes, minutes to hours, and hours to days.

The time_converter.py script is the main point of interaction for users. It serves as the interface that guides users through selecting various time conversions. Upon execution, this script presents a menu of conversion options, including converting seconds to minutes, minutes to hours, and hours to days. It continuously runs in a loop, allowing users to choose a conversion or exit the program by inputting their choice. Based on the user's selection, the script calls specific functions from the time_converter_functions.py module to perform the necessary calculations. The results of these conversions are then displayed back to the user in a clear and formatted manner.

On the other hand, time_converter_functions.py is a dedicated module that encapsulates the core logic required for the time conversions. This file contains the actual mathematical functions for converting time units. Each function in this module focuses on a particular conversion, such as converting seconds to minutes, minutes to hours, or hours to days. When called by time_converter.py, these functions receive the necessary input, perform the conversions, and return the results to be displayed.

