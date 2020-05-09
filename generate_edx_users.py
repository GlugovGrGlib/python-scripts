#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import rstr
from collections import deque

with open('generated_users.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['username', 'password'])
    usernames = {rstr.xeger(r'^[-a-zA-Z0-9_]{2,}\Z') for i in range(500)}
    deque(map(lambda x: spamwriter.writerow([x[1], f'edx{x[0]}']), enumerate(usernames)))
