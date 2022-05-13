import random
from typing import Dict

from yzcore.exceptions import UnknownError


def get_base_url(service_name: str, services_dict: Dict) -> str:
    """
    从服务列表中获取指定服务ip和port，并返回拼接的url
    :param service_name: 服务名
    :param services_dict: 依赖的服务列表信息，包含ip和port
    """
    service_info = services_dict.get(service_name)
    if not service_info:
        return ''
    if len(service_info['ip']) == 0:
        server_error = f'Could not find nacos instance of {service_name}'
        raise UnknownError(server_error)

    rand_int = random.randrange(0, len(service_info['ip']))
    subfix = '/api/v1' if service_name == 'uuid-service' else '/api/v1/'
    base_url = f"http://{service_info['ip'][rand_int]}:{service_info['port']}{subfix}"

    return base_url
