#! /usr/bin/env python

'''
    Command Line Utility to return a details for the selected VM
'''


import requests
import json
from ucsd_library import vm_details

if __name__ == '__main__':

    import sys
    from pprint import pprint
    from argparse import ArgumentParser, FileType

    p = ArgumentParser()
    p.add_argument('vmid',                          # Name stored in namespace
                   metavar = 'Virtual Machine ID',            # Arguement name displayed to user
                   help = 'The UCSD  vmid to return details for.',
                   type = str
                    )
    p.add_argument('-f',                          # Name stored in namespace
                   metavar = 'A field to return',            # Arguement name displayed to user
                   help = 'Which detail fields to return.  Can be used multiple times.',
                   type = str, action="append", default = []
                    )
    p.add_argument('-k',
                   metavar = "The field to search.  ",
                   help = "Which detail field to search for.",
                   type = str
                   )
    p.add_argument('-v',
                   metavar = "The value to search for.  ",
                   help = "What value to search the detail field for.",
                   type = str
                   )
    ns = p.parse_args()
    if (ns.k and ns.v): rf = {ns.k:ns.v}
    else: rf = {}

    result = vm_details(ns.vmid, key_filter=ns.f, result_filter = rf)

    pprint (result)

