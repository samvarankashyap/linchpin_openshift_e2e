#!/usr/bin/env python
def get_char(value, no_of_char):
    return value[0:no_of_char]

class FilterModule(object):
    ''' A filter to fix interface's name format '''
    def filters(self):
        return {
            'get_char': get_char
        }
