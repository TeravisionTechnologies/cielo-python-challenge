import os,sys,requests,argparse


my_parser = argparse.ArgumentParser(description="Restfull client")

my_parser.add_argument('uri',metavar='uri',type=str,help='Uri to make the request')

my_parser.add_argument('method', metavar='method',type=str, help='Type of http Request method')

my_parser.add_argument('-o','--output',action='store',help='write the output')

my_parser.add_argument('-d','--data', action='store',required= False,help='data of post request in json format')

args = my_parser.parse_args()


class Request():
    global restfull
    def __init__(self):
        self.restfull = Restfull()

    def request(self,uri,method,data):
        method = method.upper()
        if method == 'GET':
            self.restfull.get(uri)
        elif method == 'POST':
            self.restfull.post(uri,data)

class Restfull():

    def post(self,uri, data):
        r = requests.post(uri,data=data)
        print(r.status_code)
    
    def get(self,uri):
        r = requests.get(uri)
        print("jeje")
        print(r.status_code)

req = Request()
req.request(args.uri,args.method,args.data)

#para probar
#python3 restful.py http://yonder.mocklab.io/thing post -d {"id":1,"value":2}