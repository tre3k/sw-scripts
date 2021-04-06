#!/usr/bin/env python3

class Value:
    val = 0
    err = 0   

class Fitparser:

    def __init__(self,filename="fit.log"):
        self._params = []
        self._values = dict()
        self.parse(filename)
        return

    def parse(self,filename):
        self._filename = filename
        self._fd = open(filename,'r')

        parse_param = False
        
        for line in self._fd:
            if line.find("Final set of parameters") == 0:
                parse_param = True
                continue

            if parse_param:
                if line=='\n':
                    parse_param = False

            if parse_param:
                if line[0]=='=' or line[0]=='#':
                    continue

                tmp = line.split()
                key = tmp[0]
                self._params.append(key)
                value = Value()
                value.val = float(tmp[2])
                value.err = float(tmp[4])
                self._values[key] = value
                
        return

    def getFilename(self):
        return self._filename
    
    def getParams(self):
        return self._params

    def getValues(self):
        return self._values
    
