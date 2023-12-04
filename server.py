#!/usr/bin/env python3
"""
The main script that starts the server.
"""

import http.server
import socket
import utils

__author__ = 'Mariah Holder'
__version__ = 'Dec 2023'
__pylint__ = 'v1.8.3'

class Project2Server(http.server.BaseHTTPRequestHandler):
    """
    The subclass that listens at the HTTP socket to
    dispatch the requests to a handler
    """

    def do_GET(self): #pylint: disable=invalid-name
        """
        Overriding the do_GET() method to start the
        specified server, and ignore the pylint warning
        """
        self.log_message('path: %s', self.path)
        try:
            self.log_message('resource: %s', self.path)
            resource = self.path[1:]

            if not resource.startswith('page_hyperlinks') or resource == '':
                self.log_message('resource: %s', self.path)
                self.send_error(404, 'Expecting page_hyperlinks?args')

            website_arg = resource.split('?')[1]

            body = utils.page_hyperlinks(website_arg)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(body, 'UTF-8'))
            self.log_message('Page successfully built')

        except ValueError as exception:
            self.send_error(500, str(exception))
        except socket.error:
            pass

def main():
    """
    Launches the script and allows the server to go live.
    """
    server_address_tuple = ('localhost', 3280)
    server = http.server.HTTPServer(server_address_tuple, Project2Server)
    print('Project 2 - Extracting hyperlinks from webpage {}.'.format(server_address_tuple[1]))
    print('Type <Ctrl-C> to stop server.')
    server.serve_forever()

if __name__ == '__main__':
    main()
