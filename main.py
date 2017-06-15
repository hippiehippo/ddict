import webapp2
import cgi
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
          <html>
            <body>
              <form action="/signin" method="post">
                username:<br>
                <input type="text" name="username"><br>
                Password:<br>
                <input type="password" name="password"><br>
                <div><input type="submit" value="Submit"></div>
              </form>
            </body>
          </html>""")

class PostHandler(webapp2.RequestHandler):
    def post(self):
        expected_user = "fish"
        expected_password = "sucks"
        actual_user = self.request.get('username')
        actual_password = self.request.get('password')
        self.response.content_type = 'text/plain'
        if actual_user == expected_user and actual_password == expected_password:
            self.response.out.write('good')
        else:
            self.response.out.write('bad')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/signin', PostHandler)
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == "__main__":
    main()
