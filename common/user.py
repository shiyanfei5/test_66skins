import json
import time

import requests

from common.api import get_url, LOGIN_API, LOGOUT_API
from common.bag import Bag


class User(object):

    def __init__(self, user_id, acct_id, pass_word, _requests=None):
        self.user_id = user_id
        self.account_id = acct_id
        self.pass_word = pass_word
        self.token = None
        if _requests:
            self._requests = _requests
        else:
            self._requests = requests

    def login(self):
        url = get_url(LOGIN_API)
        url_params = {
            "username": self.account_id
        }
        json_data = {
            "key": "0.1806204298780072",
            "password": self.pass_word
        }
        resp = self._requests.post(
            url,
            params=url_params,
            json=json_data
        )
        if resp.status_code == 200:
            resp_data = json.loads(resp.text)
            if resp_data["code"] == 200:
                self.token = "Bearer "+resp_data["data"]
                return
        raise Exception("用户{}登录失败" % self.account_id)

    def logout(self):
        url = get_url(LOGOUT_API)
        if self.token:
            self._requests.post(
                url,
                headers={
                    "authorization": self.token
                }
            )
            self.token = None

    def get_request_client(self):
        return self._requests


if __name__ =="__main__":
    user = User(
        "15995418002",
        "9771e4eff96cc98d97401198974ea2cfdfe9c4f97ca0b15502e6bcbdcb5f08f4e4f72e0adc54eadb635c67cc118682ae280e32c0b2b3197fc9b0504fa0665056d8bf2aa5de277745d77b0219a794f8fe3ccca73c9a5b023db663298d54f84871b6f0cacb2f38475c0c84406c593c118d9d25cab419252a6069ea6e5ea287684b"
    )
    user.login()
    time.sleep(1)
    # roll = Roll(user, 60802012111031019266)
    # resp = roll.open_roll_box(1)
    # print(resp)
    bag = Bag(user)
    resp = bag.load_all_in_bag()
    print(resp)
    resp = bag.buy_back(['202012152307220438850005'])
    print(resp)







