#!/usr/bin/env python
def strip_func(value, delim=" "):
    return value.strip(delim)

class FilterModule(object):
    ''' A filter to fix interface's name format '''
    def filters(self):
        return {
            'strip': strip_func
        }
