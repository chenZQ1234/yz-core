"""
nacos sdk 支持版本为Python 2.7 Python 3.6 Python 3.7
"""
import nacos
import logging
from typing import List,Dict
from requests.exceptions import HTTPError

class BaseNacosClient:
    def __init__(self,nacos_url:str,username:str,password:str,service_name:str,nacos_ip:str=None,nacos_port:int=None,namespace:str=None,**kwargs):
        """
        param: url (url of nacos)
        param: namespace
        param: username (username of nacos)
        param: password (password of nacos)
        param: service_name
        param: ip (ip of nacos)
        param: port (port of nacos)
        """
        self.url = nacos_url
        self.namespace = namespace
        self.username = username
        self.password = password
        self.service_name = service_name
        self.nacos_ip = nacos_ip
        self.nacos_port = nacos_port
        self.client = nacos.NacosClient(nacos_url,namespace=namespace,username=username,password=password)

    async def send_heartbeat(self):
        """向nacos发送心跳"""
        try:
            self.client.send_heartbeat(
                self.service_name,
                ip=self.nacos_ip,
                port=self.nacos_port
                )
        except Exception:
            # 如果没有收到心跳返回信息则重新注册
            self.client.add_naming_instance(
                service_name=self.service_name,
                ip=self.nacos_ip,
                port=self.nacos_port
            )


    def register_nacos(self):
        """微服务注册nacos"""
        try:
            self.client.add_naming_instance(
                service_name=self.service_name,
                ip=self.nacos_ip,
                port=self.nacos_port
            )
        except Exception as ex:
            logging.error("Failed to register to nacos : %s", ex)

    async def list_services(self,server_list: List,callback_return)->Dict:
        """获取服务列表"""
        res=dict()
        for service in server_list:
            res.update({service:{"ip":[],"port":""}})
            try:
                resp=self.client.list_naming_instance(service,namespace_id="public",healthy_only=True)
                # print(resp)
            except HTTPError:
                continue

            for host in resp.get('hosts'):
                res[service]["ip"].append(host.get('ip'))
                res[service]['port']=host.get('port')
                
        if callback_return:
            callback_return(res)

    
