'''
Albert Martinez
06/09/16
DPW-1606
Simple Form
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self): # function to start it all up
        page_head = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        	<meta charset="UTF-8">
        	<title>Albert Martinez | Simple Form | DPW-1606 WDDBS Full Sail University</title>
        </head>
        <body>
        '''
        page_form_body = '''
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
		<p class="input-field">
			<label for="services">Services Wanted</label>
			<p class="input-field"><input type="checkbox" name="services" value="Cut" />Cut</p>
			<p class="input-field"><input type="checkbox" name="services" value="Color" />Color</p>
			<p class="input-field"><input type="checkbox" name="services" value="Style" />Style</p>
			<p class="input-field"><input type="checkbox" name="services" value="Extensions" />Extensions</p>
		<p>
		<p class="input-field">
			<label for="hair_length">Your Hair Length</label>
			<p class="input-field">
				<input type="radio" name="hair_length" value="Super Short-Think Demi Moore in Ghost">
			</p>
			<p class="input-field">
				<input type="radio" name="hair_length" value="Short-Think Rihanna Bob">
			</p>
			<p class="input-field">
				<input type="radio" name="hair_length" value="Medium-Think Cameron Diaz in The Sweetest Thing">
			</p>
			<p class="input-field">
				<input type="radio" name="hair_length" value="Long-Think current Selena Gomez">
			</p>
		<p>
		<input type="submit value="submit" />
	</form>
        '''
        page_results_body = '''

        '''
        page_close = '''
        </body>
        </html>
        '''
        if self.request.GET:
            # store info from the form
            user = self.request.GET['name']
            email = self.request.GET['email']
            gender = self.request.GET['gender']
            self.response.write(page_head + page_results_body + page_close)
        else:
            self.response.write(page_head + page_form_body + page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
