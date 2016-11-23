import configparser
import getopt
import os
import re
import sys


def parse_config(shortopts, longopts):
    """Read options from config file, then override with command line"""
    try:
        opts, args = getopt.getopt(sys.argv[1:], shortopts, longopts)
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)

    config_ini = None

    for o, a in opts:
        if o == "--config" or o == "-c":
            config_ini = a

    if config_ini is None:
        config_ini = "config.ini"

    if not os.path.isfile(config_ini):
        print("ERROR: config file '%s' not found" % config_ini)
        sys.exit(-1)

    config = configparser.ConfigParser()
    config.read(config_ini)

    prog = re.compile("^--([^-]+)-(.*)")
    for o, a in opts:
        match = prog.match(o)
        if match:
            section = match.group(1)
            key = match.group(2)
            value = a
            config[section][key] = value

    return config
