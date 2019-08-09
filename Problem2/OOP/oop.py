"""
Problem 3
"""

import Problem2.models.session as session


class Step:
    def __init__(self, _number_of_sessions, _number_of_star):
        self.number_of_sessions = _number_of_sessions
        self.number_of_stars = _number_of_star

    def make_step(self):
        exception_message = ''
        exception = InvalidValueException(exception_message, self.number_of_sessions, self.number_of_stars)
        try:
            session_in_letter = session.NUMBER_TO_TEXT_MAP[self.number_of_sessions]
            star_in_number = session.TEXT_TO_NUMBER_MAP[self.number_of_stars]

            print('Original:\nI completed ' + str(
                self.number_of_sessions) + ' sessions and I rated my expert ' + self.number_of_stars + ' stars')
            print('Conversion:\nI completed ' + session_in_letter + ' sessions and I rated my expert ' + str(
                star_in_number) + ' stars')
        except:
            exception.exception_message()
            print(exception.message)


class InvalidValueException(Exception):

    def __init__(self, message, number_of_sessions, number_of_stars):
        self.message = message
        self.number_of_sessions = number_of_sessions,
        self.number_of_stars = number_of_stars

    def exception_message(self):
        if self.number_of_sessions not in session.NUMBER_TO_TEXT_MAP:
            self.message = 'Invalid number of sessions'
        elif self.number_of_stars not in session.TEXT_TO_NUMBER_MAP:
            self.message = 'Invalid number of stars'


Step(2, 'ten').make_step()
