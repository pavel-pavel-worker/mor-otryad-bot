class NotCorrectMessage(Exception):
    """Некорректное сообщение в бот, которое не удалось распарсить"""
    pass


class InvalidDate(Exception):
    """Invalid date message not found in reply keyboards"""

    def __str__(self):
        return 'Invalid date message'


class CantGetDefinition(Exception):

    def __str__(self):
        return 'Cannot get definition'
