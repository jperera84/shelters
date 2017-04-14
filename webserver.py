""" Web server """
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import cgi

class WebServerHandler(BaseHTTPRequestHandler):
    """ Web server handler """
    def do_GET(self):
        """ Handler Get Methods """
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                output = "<html><body>Hello World!"
                output += """ <form method='POST' enctype='multipart/form-data' action='/hello'>
                                <h2>What do like me to say?</h2>
                                <input name='message' type='text'>
                                <input type='submit' value='Submit'>
                              </form> """
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                output = "<html><body>Hola! <a href='/hello'>Go Back Hello</a>"
                output += """ <form method='POST' enctype='multipart/form-data' action='/hello'>
                                <h2>What do like me to say?</h2>
                                <input name='message' type='text'>
                                <input type='submit' value='Submit'>
                              </form> """
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
        except IOError:
            self.send_error(404, "File not found %s" %(self.path))

    def do_POST(self):
        """ Handle Post Request """
        try:
            self.send_response(301)
            self.end_headers()
            ctype, pdict = cgi.parse_header(self.headers.getheader("content-type"))
            if ctype == "multipart/form-data":
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get("message")
                output = "<html><body><h2>Okay, how about this:</h2><h1>%s</h1>" %(messagecontent[0])
                output += """ <form method='POST' enctype='multipart/form-data' action='/hello'>
                                <h2>What do like me to say?</h2>
                                <input name='message' type='text'>
                                <input type='submit' value='Submit'>
                              </form> """
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
        except:
            pass


def main():
    """ Main Function """
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Web server is running on port: %s" %(port)
        server.serve_forever()
    except KeyboardInterrupt:
        print "^C entered, stopping web server..."
        server.socket.close()

if __name__ == "__main__":
    main()
