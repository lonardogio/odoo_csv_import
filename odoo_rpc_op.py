#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser as ConfigParser
import argparse
from odoo_rpc_op import jsonrpc

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Use JSONRPC Operation')
    parser.add_argument('-c', '--config', dest='config', default="conf/connection.conf",
                        help='Configuration File that contains connection parameters', required=True)
    parser.add_argument('--model', dest='model', help='Model to import', required=True)

    args = parser.parse_args()
    args.config

    jsonrpc.operation(args.config, args.model)
