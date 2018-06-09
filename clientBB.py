#!/usr/bin/env python
# import it all

import urllib2
import sys
import time


# get data from cloud
def getdata(user):
  get_str = 'http://192.168.1.6:5000/' + user
  connt_speak = urllib2.urlopen(get_str)
  response = connt_speak.read()
  #data = json.loads(response)
  print response
  connt_speak.close()

def main():
  getdata(sys.argv[1])


if __name__ == '__main__':   # std. boiler plate
  main()

