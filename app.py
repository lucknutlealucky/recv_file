#docker run -it --rm --name file_rcv --network="proxy" -v /home/kang_parkir/python/upload:/usr/src/myapp -v /home/kang_parkir/python/upload/file:/shared -w /usr/src/myapp python:3 python app.py

import subprocess
import sys
import os


try:
    os.mkdir("/shared")
except:
    pass

subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])

import socket
IP1 = socket.gethostbyname(socket.gethostname())




path = "/shared"
dir_list = os.listdir(path)

from flask import Flask
from flask import request

    
app = Flask(__name__)
    # The route() function of the Flask class is a decorator, 
    # which tells the application which URL should call 
    # the associated function.
@app.route('/')
    # ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'sorry you not suposed to be here'

@app.route('/post', methods=['POST'])
def process_json():
    data = request.get_json()
    to_reply = []
    # print(data['file_list'])
    for i in data['file_list']:
        if i not in dir_list:
            to_reply.append(i)
    
    to_send_back = {"files": to_reply}
            
    return str(to_send_back)

    # main driver function
if __name__ == '__main__':
        
        # run() method of Flask class runs the application 
        # on the local development server.
    app.run(host=IP1, port=80)
