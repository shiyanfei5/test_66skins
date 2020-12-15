import requests

from common.api import OPEN_ORDER, get_url


class Roll(object):

    def __init__(self, user, box_id):
        self.user = user
        self.box_id = box_id

    def open_roll_box(self, num):
        _requests = self.user.get_request_client()
        url = get_url(OPEN_ORDER)
        url_params = {
            "boxId": self.box_id,
            "num": num
        }
        return _requests.post(
            url,
            params=url_params,
            headers={"authorization": self.user.token}
        )















