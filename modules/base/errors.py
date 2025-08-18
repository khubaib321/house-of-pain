class ThePain(Exception):
    pass


class NotFoundError(ThePain):
    pass


class UserNotFoundError(NotFoundError):
    pass
