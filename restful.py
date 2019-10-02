#! /usr/bin/env python3

import os,sys,requests,argparse,json


my_parser = argparse.ArgumentParser(description="Restful client")

my_parser.add_argument('method', metavar='{get, post}',type=str, help='Request method')

my_parser.add_argument('uri',metavar='endpoint',type=str,help='Request endpoint URI fragment')

my_parser.add_argument('-d','--data', action='store',required=False ,help='Data to send with request')

my_parser.add_argument('-o','--output',action='store',help='Output to .json or .csv file (default: dump to stdout)')

args = my_parser.parse_args()

url_base = 'https://jsonplaceholder.typicode.com'


class Request():
    global restful
    def __init__(self):
        self.restful = Restful()

    def request(self, uri, method, data, output):
        method = method.upper()
        if method == 'GET':
            self.restful.get(url_base+uri, output)
        elif method == 'POST':
            self.restful.post(url_base+uri, data, output)

class Restful():
    global output
    def __init__(self):
        self.output = Output()

    def post(self, uri, data, output):
        r = requests.post(uri,data=data)
        response = r.json()
        self.output.write(response, output)
    
    def get(self, uri, output):
        r = requests.get(uri)
        response = r.json()
        self.output.write(response, output)
        

class Output():
    def write(self, response, output):
        if output != None and output.endswith('.json'):
            sourceFile = open(output, 'w')
            print(json.dumps(response, indent=2), file= sourceFile)
        else:
            print(json.dumps(response, indent=2))

req = Request()
req.request(args.uri, args.method, args.data, args.output)