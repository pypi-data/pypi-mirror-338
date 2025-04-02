#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 说明：
#    服务器批量操作
# History:
# Date          Author    Version       Modification
# --------------------------------------------------------------------------------------------------
# 2025/4/2    xiatn     V00.01.000    新建
# --------------------------------------------------------------------------------------------------
from fabric import Connection, Config
from xtn_tools_pro.utils.log import Log


class ShellPro:
    def __init__(self, server_info_list):
        self.server_info_list = server_info_list
        self.__logger = Log('shell', './xxx.log', log_level='DEBUG', is_write_to_console=True,
                            is_write_to_file=False,
                            color=True, mode='a', save_time_log_path='./logs')

        for _ in range(len(self.server_info_list)):
            ip, pwd, tips = self.server_info_list[_]["ip"], \
                            self.server_info_list[_]["pwd"], \
                            self.server_info_list[_]["tips"]
            self.__logger.info(f"{tips} 正在连接...")
            config = Config(overrides={'sudo': {'password': pwd}})
            conn = Connection(
                host=ip,
                user="root",  # 根据实际情况修改用户名
                connect_kwargs={"password": pwd},
                config=config
            )
            self.server_info_list[_]["conn"] = conn
            self.__logger.info(f"{tips} 连接成功!!!")

    def run_shell(self, conn, cmd, warn=False):
        """
            传入conn和命令执行
        :param conn:
        :param cmd:
        :return:
        """
        conn.run(cmd, warn=warn)

    def update_file(self, LOCAL_FILE, REMOTE_FILE):
        """
            覆盖远程文件
        :param LOCAL_FILE: 本地文件
        :param REMOTE_FILE: 远程文件
        :return:
        """
        for server_item in self.server_info_list:
            conn = server_item["conn"]
            conn.put(LOCAL_FILE, REMOTE_FILE)


if __name__ == '__main__':
    server_info_list = [
        {"ip": "xxx.xxx.xx.xxx", "pwd": "123456", "tips": "服务器_01"},
    ]
    sh = ShellPro(server_info_list=server_info_list)
