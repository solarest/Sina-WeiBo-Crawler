# -*- coding:utf8 -*-
import ConfigParser


def read_config(config_path, tag, key):
    config = ConfigParser.ConfigParser()
    config.read(config_path)
    use_value = config.get(tag, key)
    return use_value


