'''
Albert Martinez
06/09/16
DPW-1606
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self): # function to start it all up
        page = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        	<meta charset="UTF-8">
        	<title>Albert Martinez | Simple Form | DPW-1606 WDDBS Full Sail University</title>
        </head>
        <body>
        	<form method="get">
        		<p class="input-field">
        			<label for="name">Name</label>
        			<input type="text" placeholder="Name" id="name" name="name">
        		<p>
        		<p class="input-field">
        			<label for="email">Email</label>
        			<input type="email" placeholder="Email" id="email" name="email">
        		<p>
        		<p class="input-field">
        			<label for="gender">Gender</label>
        			<p class="input-field">
        				<input type="radio" name="gender" value="Male">
        			</p>
        			<p class="input-field">
        				<input type="radio" name="gender" value="Female">
        			</p>
        		<p>
        		<input type="submit value="submit" />
        	</form>
        </body>
        </html>
                '''
        self.response.write(page)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
