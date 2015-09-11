#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

def main():
    id_regex = re.compile(r'/questions/([0-9]+)/')
    question_regex = re.compile(r'class="question-hyperlink">(.*?)</a>')
    passed_time_regex = re.compile(r'class="relativetime">(.*?)</span>')

    data = sys.stdin.read()
    ids = id_regex.findall(data)
    question = question_regex.findall(data)
    passed_time = passed_time_regex.findall(data)

    for i, q, p in zip(ids, question, passed_time):
        print(';'.join([i, q, p]))

if __name__ == '__main__':
    main()
