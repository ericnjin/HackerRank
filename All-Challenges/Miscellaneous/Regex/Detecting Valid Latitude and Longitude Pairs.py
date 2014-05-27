#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

num_tests = int(raw_input())
for n in range(num_tests):
        raw_data = raw_input()

        xy = re.findall(r'\('
                        r'([+-]?[0-9]{1,2}(?:\.[0-9]+)?)' 
                        r', '
                        r'([+-]?[0-9]{1,3}(?:\.[0-9]+)?)' 
                        r'\)',raw_data)
        if xy:
            lat, lon = xy[0]
            if -90 <= float(lat) <= 90 and -180 <= float(lon) <= 180:
                print('Valid')
                continue

        print('Invalid')
