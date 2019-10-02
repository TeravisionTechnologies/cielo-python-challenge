#! /usr/bin/env python3

import os,sys,requests,argparse


my_parser = argparse.ArgumentParser(description="Restful client")

my_parser.add_argument('method', metavar='{get, post}',type=str, help='Request method')

my_parser.add_argument('uri',metavar='endpoint',type=str,help='Request endpoint URI fragment')

my_parser.add_argument('-d','--data', action='store',required= False,help='Data to send with request')

my_parser.add_argument('-o','--output',action='store',help='Output to .json or .csv file (default: dump to stdout)')

args = my_parser.parse_args()

url_base = 'https://jsonplaceholder.typicode.com'


class Request():
    global restful
    def __init__(self):
        self.restful = Restful()

    def request(self,uri,method,data):
        method = method.upper()
        if method == 'GET':
            self.restful.get(url_base+uri)
        elif method == 'POST':
            self.restful.post(url_base+uri,data)

class Restful():

    def post(self,uri, data):
        r = requests.post(uri,data=data)
        print(r.status_code)
    
    def get(self,uri):
        r = requests.get(uri)
        print(r.status_code)

req = Request()
req.request(args.uri,args.method,args.data)

#para probar
#python3 restful.py /posts post -d {"id":1,"value":2}