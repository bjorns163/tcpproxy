#!/usr/bin/env python3
import os.path as path


class Module:
    def __init__(self, incoming=False, verbose=False, options=None):
        # extract the file name from __file__. __file__ is proxymodules/name.py
        self.name = path.splitext(path.basename(__file__))[0]
        self.description = 'Print a hexdump of the received data'
        self.incoming = incoming  # incoming means module is on -im chain
        self.len = 16
        if options is not None:
            if 'length' in options.keys():
                self.len = int(options['length'])

    def help(self):
        return '\tlength: bytes per line (int)'

    def execute(self, data):
        # this is a pretty hex dumping function directly taken from
        # http://code.activestate.com/recipes/142812-hex-dumper/
        result = []
        digits = 4 if isinstance(data, str) else 2
        for i in range(0, len(data), self.len):
            s = data[i:i + self.len]
            hexa = " ".join(["%0*X" % (digits, ord(x)) for x in str(s)])
            text =  "".join([x if 0x20 <= ord(x) < 0x7F else "." for x in str(s)])
            result.append("%04X   %-*s   %s" % (i, self.len * (digits + 1), hexa, text))
        print("\n".join(result))
        return data


if __name__ == '__main__':
    print ('This module is not supposed to be executed alone!')
