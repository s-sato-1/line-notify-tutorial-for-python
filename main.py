import os
import sys
import time
import requests

import settings


class LineNotify(object):
    """
    """
    def __init__(self, api, token):
        """
        """
        self.api = api
        self.token= token

    def notify(self, msg):
        """
        """
        line_notify_token = self.token
        notification_message = msg
        line_notify_api = self.api
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': f'{notification_message}'}
        requests.post(line_notify_api, headers=headers, data=data)

    def notify_with_screenshot(self, msg):
        """
        """
        line_notify_token = self.token
        notification_message = msg
        line_notify_api = self.api
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': f'{notification_message}'}
        files = {'imageFile': open("screenshot/screenshot.png", "rb")}
        requests.post(line_notify_api, headers=headers, data=data, files=files)


if __name__ == "__main__":
    """
    """
    line = LineNotify(settings.line_notify_api, settings.line_notify_token)
    line.notify('hello, world.')
