import datetime
from time import sleep


def log(message, when=None):
    """
    Log a message with a timestamp. Timestamp is optional. If not given, the current datetime will be used.

    :param message: the message to log
    :param when: the datetime to log message at
    :return: None
    """
    print('%s: %s' % (datetime.datetime.now() if when is None else when, message))


log('foo')
log('foo bar', datetime.datetime.now() + datetime.timedelta(days=2))
sleep(1)
log('foo bar final')

