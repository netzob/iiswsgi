#!/usr/bin/env python2.7

from pprint import pprint

if __name__ == '__main__':
    pprint(dict(
        devel_mode=__msdeploy_devel_mode__,
        db_type='__msdeploy_db_type__',
        ))
