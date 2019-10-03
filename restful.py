#! /usr/bin/env python3

import os
import sys
import requests
import argparse
import json
import csv

challenge_parser = argparse.ArgumentParser(description="Restful client")

challenge_parser.add_argument('method', metavar='{get, post}',type=str, help='Request method')

challenge_parser.add_argument('uri',metavar='endpoint',type=str,help='Request endpoint URI fragment')

challenge_parser.add_argument('-d','--data', action='store',required=False ,help='Data to send with request')

challenge_parser.add_argument('-o','--output',action='store',help='Output to .json or .csv file (default: dump to stdout)')

args = challenge_parser.parse_args()

url_base = 'https://jsonplaceholder.typicode.com'


class Request():
    global restful
    def __init__(self):
        self.restful = Restful()

    def request(self, uri, method, data, output):
        method = method.upper()
        if method == 'GET':
            self.restful.get(url_base + uri, output)
        elif method == 'POST':
            self.restful.post(url_base + uri, data, output)

class Restful():
    global output
    def __init__(self):
        self.output = Output()

    def post(self, uri, data, output):
        try:
            r = requests.post(uri,data = data)
            r.raise_for_status()
            self.output.write(r, output)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
    
    def get(self, uri, output):
        try:
            r = requests.get(uri)
            r.raise_for_status()
            self.output.write(r, output)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        

class Output():
    def write(self, resp, output):
        if output != None and output.endswith('.json'):
            response = resp.json()
            sourceFile = open(output, 'w')
            print(resp.status_code)
            print(json.dumps(response, indent = 2), file = sourceFile)
        elif output != None and output.endswith('.csv'):
            response = resp.json()
            data = []
            if type(response).__name__ == 'dict':
                data.append(response.keys())
                values = response.values()
                filtered = (element if type(element).__name__ != 'str' else element.replace('\n', ' ') for element in values)
                data.append(filtered)
            elif type(response).__name__ == 'list':
                for index, element in enumerate(response):
                    if index == 0:
                        data.append(element.keys())
                    values = element.values()
                    filtered = (row if type(row).__name__ != 'str' else row.replace('\n', ' ') for row in values)
                    data.append(filtered)
                with open(output, 'w') as csvFile:
                    writer = csv.writer(csvFile, lineterminator='\n')
                    
                    writer.writerows(data)
                csvFile.close()
                print(resp.status_code)
            else:
                print(resp.status_code)
                print('Empty response')
                sys.exit(1)
        else:
            print(resp.status_code)
            print(resp.text)

req = Request()
req.request(args.uri, args.method, args.data, args.output)