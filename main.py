import json
import os
import time

from happy_python import get_exit_code_of_cmd, HappyLog, HappyConfigBase, HappyConfigParser

hlog = HappyLog.get_instance()
website_details = []

# def main():
#     node = '/usr/bin/node '
#     js = '/home/geek/workspace/devtest/browser/browser.js'
#     chrome = '/opt/google/chrome/google-chrome'
#     url = 'https://zhiyan.cdgeekcamp.com'
#     jsonaa = '/home/geek/workspace/devtest/browser/browser.stat/2023.09_14.json'
#     jpg = '/home/geek/workspace/devtest/browser/browser.stat/2023.09_14.jpg'
#
#     node_modules_path = '/home/geek/workspace/ZhiYanModule/zhiyan-mod-browser/node_modules'
#
#     node_js_command = '%s %s %s %s %s %s' % (node, js, chrome, url, jsonaa, jpg)
#
#     os.putenv('NODE_PATH', node_modules_path)
#     code = get_exit_code_of_cmd(cmd=node_js_command, is_show_error=True, is_show_output=True)
#     os.unsetenv('NODE_PATH')
#
#     if code != 0:
#         return "error"
#
#     time.sleep(3)
#
#     with open(jsonaa) as f:
#         log_entries = json.load(f)['log']['entries']
#         for i in log_entries:
#             website_details.append(i['request']['url'])
#
#     hlog.info(website_details)
#
#     hlog.info(len(website_details))

__mod_config_file_path__ = './conf/browser.conf'


class Config(HappyConfigBase):
    def __init__(self):
        super().__init__()

        self.section = 'zymod'
        self.node_exec_path = ''
        self.node_exec_script_path = ''
        self.google_chrome_path = ''
        self.node_js_command_line_parameters = ''
        self.env_node_modules_path = ''
        self.browser_url = ''
        self.json_path = ''
        self.jpg_path = ''


def main():
    conf_path = __mod_config_file_path__
    browser_conf = Config()
    HappyConfigParser.load(conf_path, browser_conf)
    node = browser_conf.node_exec_path
    js = browser_conf.node_exec_script_path
    chrome = browser_conf.google_chrome_path
    url = browser_conf.browser_url
    jsonaa = browser_conf.json_path
    jpg = browser_conf.jpg_path
    node_modules_path = browser_conf.env_node_modules_path
    node_js_command = '%s %s %s %s %s %s' % (node, js, chrome, url, jsonaa, jpg)

    os.putenv('NODE_PATH', node_modules_path)
    code = get_exit_code_of_cmd(cmd=node_js_command, is_show_error=True, is_show_output=True)
    os.unsetenv('NODE_PATH')

    if code != 0:
        return "error"

    time.sleep(3)

    with open(jsonaa) as f:
        log_entries = json.load(f)['log']['entries']
        for i in log_entries:
            website_details.append(i['request']['url'])

    hlog.info(website_details)

    hlog.info(len(website_details))


if __name__ == "__main__":
    main()
