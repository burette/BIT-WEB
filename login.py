#!/usr/bin/env python
# encoding: utf-8
import requests


class Loginer():
    def __init__(self, username, password, user_ip):
        self.loginUrl = 'http://10.0.0.55/srun_portal_pc.php?ac_id=8&'
        self.username = username
        self.password = password
        self.user_ip = user_ip

    def login(self):
        postdata = {'username': self.username,
                    'password': self.password,
                    'action': 'login',
                    'ipv6': '',
                    'ac_id': '8',
                    'user_ip': self.user_ip,
                    'nas_ip': '',
                    'user_mac': '',
                    'url': ''}

        z = requests.post(self.loginUrl, data=postdata)


def main():
    # 以下输入自己的账号密码以及服务器分配的IP
    username = '322018XXXX'
    password = 'XXXXXX'
    user_ip = '10.4.20.XXX'
    if username and password and user_ip:
        l = Loginer(username, password, user_ip)
        l.login()
        print('done')
    else:
        print('检查用户名、密码、IP')


if __name__ == '__main__':
    main()
