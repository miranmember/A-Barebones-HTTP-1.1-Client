import logging
import socket
import sys

import requests


def retrieve_url(url):
    URL = parseUrl(url)
    if URL is None:
        return None
    return returnBody(URL)
    # returnBody(URL)
    # return b""


def parseUrl(url):
    if url.startswith("http://") or url.startswith("https://"):
        url = url[7:]
        try:
            host = url[:url.index('/')]
        except ValueError:
            host = url
        try:
            path = url[url.index('/'):]
        except ValueError:
            path = '/'
        port = 80
        if url.find(':') != -1:
            port = int(url[url.find(':') + 1: url.index('/')])
            urlWithPort = host
            host = host[:host.index(':')]
            return [host, path, port, urlWithPort]
        return [host, path, port]
    return None


def returnBody(URL):
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clientSocket.connect((URL[0], URL[2]))
        if len(URL) == 4:
            clientSocket.send(("GET " + URL[1] + " HTTP/1.1\r\n" +
                               "User-Agent: HTTPTool/1.0\r\n" +
                               "Host:" + URL[3] +
                               "\r\nConnection: close\r\n\r\n").encode())
        else:
            clientSocket.send(("GET " + URL[1] + " HTTP/1.1\r\n" +
                               "User-Agent: HTTPTool/1.0\r\n" +
                               "Host:" + URL[0] +
                               "\r\nConnection: close\r\n\r\n").encode())
    except socket.error:
        return None
    returnVal = b""
    while True:
        try:
            data = clientSocket.recv(1024)
            if data:
                returnVal += data
            else:
                break
        except socket.error:
            return None
    clientSocket.close()
    if returnVal.startswith(b"HTTP/1.1 200 OK"):
        return returnVal.split(b"\r\n\r\n", 1)[1]
        # return returnVal

if __name__ == "__main__":
    sys.stdout.buffer.write(retrieve_url(sys.argv[1]))  # pylint: disable=no-member
    # x = retrieve_url("https://www.cs.uic.edu/~ajayk")
    # response = requests.get("https://www.cs.uic.edu/~ajayk")
    # print(x)
    # print(response.content)
