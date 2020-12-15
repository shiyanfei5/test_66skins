
from config import BASE_URL


def get_url(api):
    '''
    全局方法，获取api路径
    :param api:
    :return: 返回对应的api路径
    '''
    return BASE_URL+api


# 用户登录退出
LOGIN_API = "/users/login"
LOGOUT_API = "/users/userLogout"

# 开箱
OPEN_ORDER = "/users/openOrder"

# 背包
SHOW_PACK_ORDERS = "/users/showPackOrders"

# 取回
BUY_BACK = "/users/buyBack"


