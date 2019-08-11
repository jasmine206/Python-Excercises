from Problem2.models.session import Session


class InvalidValueException(Exception):
    # def __init__(self, number_of_sessions, number_of_stars):
    #     super().__init__(number_of_sessions, number_of_stars)
    #     if number_of_sessions not in Session.NUMBER_TO_TEXT_MAP:
    #         self.message = 'Invalid number of sessions'
    #     if number_of_stars not in Session.TEXT_TO_NUMBER_MAP:
    #         self.message = 'Invalid number of stars'

    def __init__(self, message):
        # super.__init__(message)
        self.message = message
