#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A module about printing time"""

import datetime

CURDATE = None

def get_current_date():
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
