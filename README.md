# A-Barebones-HTTP-1.1-Client
A barebones web client. Implement a function, retrieve_url, which takes a url as its only argument, and uses the HTTP protocol to retrieve and return the body's bytes.
Implements the GET method and follows the basics of the HTTP/1.1 specification.

## Usage
+ retrieve_url, which takes a url (as a str) as its only argument, and uses the HTTP protocol to retrieve and return the body's bytes.
+ Tested On: 'http://www.example.com',
    'http://accc.uic.edu/contact',
    'http://i.imgur.com/fyxDric.jpg'

## Assumptions
+ requests has been installed using
  ```
  pip install requests
  ```
  or
  ```
  pip3 install requests
  ```
+ Assume that the URL will not include a fragment, query string, or authentication credentials.
+ No redirects.

## Output
+ ```python python3 HTTP1.py http://www.example.com```
+ Return bytes when receiving a 200 OK response from the server.
+ If program cannot retrieve the resource correctly, retrieve_url will return None.
