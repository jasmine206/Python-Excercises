"""
A string as the following:
I completed {number_of_sessions} sessions and I rated my expert {number_of_stars} stars

while:

number_of_sessions is any number in [1, ...9]
number_of_stars is any text in [one, two, three, four, five]

Then
Convert number_of_sessions from number to text.
Convert number_of_stars from text to number.
Using dictionaries and string methods.
Expected output
For example, with number_of_sessions = 2 and number_of_stars = five, the original string will be:

I completed 2 sessions and I rated my expert five stars

The result after conversion:

I completed two sessions and I rated my expert 5 stars
"""

number_session_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}
number_star_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5
}

"""
Input is number of session (integer) and number of star (string)
Output is get number of session (string) and number of star (integer)
This method is used to get values of keys in dictionaries
"""


def conversion(number_of_sessions, number_of_stars):
    if number_of_sessions in number_session_dict and number_of_stars in number_star_dict:
        session_in_letter = number_session_dict[number_of_sessions]
        star_in_number = number_star_dict[number_of_stars]

        print('Original:\nI completed ' + str(
            number_of_sessions) + ' sessions and I rated my expert ' + number_of_stars + ' stars')
        print('Conversion:\nI completed ' + session_in_letter + ' sessions and I rated my expert ' + str(
            star_in_number) + ' stars')
    else:
        print('Please input integer for number of sessions from 1-9 and string for number of stars from 1-5!')


conversion(0, 'nine')
