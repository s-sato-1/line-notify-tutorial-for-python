import configparser


conf = configparser.ConfigParser()
conf.read('settings.ini')

line_notify_token = conf['line']['line_notify_token']
line_notify_api = conf['line']['line_notify_api']
