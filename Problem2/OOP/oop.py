"""
Problem 3
"""
from Problem2.OOP.base_exception import InvalidValueException
from Problem2.models.session import Session


class Step:
    def __init__(self, _number_of_sessions, _number_of_star):
        self.number_of_sessions = _number_of_sessions
        self.number_of_stars = _number_of_star

    def make_step(self):
        # try:
        #     session_in_letter = Session.NUMBER_TO_TEXT_MAP[self.number_of_sessions]
        #     star_in_number = Session.TEXT_TO_NUMBER_MAP[self.number_of_stars]
        #
        #     print('Original:\nI completed ' + str(
        #         self.number_of_sessions) + ' sessions and I rated my expert ' + self.number_of_stars + ' stars')
        #     print('Conversion:\nI completed ' + session_in_letter + ' sessions and I rated my expert ' + str(
        #         star_in_number) + ' stars')
        #
        # except InvalidValueException as e:
        #     print(e.message)
        if self.number_of_sessions in Session.NUMBER_TO_TEXT_MAP and self.number_of_stars in Session.TEXT_TO_NUMBER_MAP:
            session_in_letter = Session.NUMBER_TO_TEXT_MAP[self.number_of_sessions]
            star_in_number = Session.TEXT_TO_NUMBER_MAP[self.number_of_stars]

            print('Original:\nI completed ' + str(
                self.number_of_sessions) + ' sessions and I rated my expert ' + self.number_of_stars + ' stars')
            print('Conversion:\nI completed ' + session_in_letter + ' sessions and I rated my expert ' + str(
                star_in_number) + ' stars')
        elif self.number_of_sessions not in Session.NUMBER_TO_TEXT_MAP:
            raise InvalidValueException('Invalid number of sessions')
        else:
            raise InvalidValueException('Invalid number of stars')


if __name__ == '__main__':
    Step(5, "hjk").make_step()
# print(InvalidValueException.__mro__)
