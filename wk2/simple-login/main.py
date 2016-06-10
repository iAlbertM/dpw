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
            <link rel="stylesheet" type="text/css" href="css/main.css">
        </head>
        <body>
        '''
        page_form_body = '''
        <header>
            <h1>HairAttics</h1>
        </header>
            <h2>Appointments</h2>
                <form method="get">
                    <p class="input-field">
                        <label for="name">Name</label>
                        <input type="text" placeholder="name" name="name">
                    </p>
                    <p class="input-field">
                        <label for="email">Email</label>
                        <input type="email" placeholder="Email" name="email">
                    </p>
                    <p class="input-field">
                        <label for="gender">Gender</label>
                        <p class="input-field">
                            <input type="radio" name="gender" value="Male"> Male
                        </p>
                        <p class="input-field">
                            <input type="radio" name="gender" value="Female"> Female
                        </p>
                    </p>
                    <p class="input-field"> Services Wanted
                        <select name="services">
                            <p class="input-field">
                                <option value="Cut" />Cut</option>
                            </p>
                            <p class="input-field">
                                <option value="Color" />Color</option>
                            </p>
                            <p class="input-field">
                                <option value="Style" />Style</option>
                            </p>
                            <p class="input-field">
                                <option value="Extensions" />Extensions</option>
                            </p>
                        </select>
                    </p>
                    <p class="input-field">
                        <label for="hair_length">Your Hair Length</label>
                        <p class="input-field">
                            <input type="radio" name="hair_length" value="xshort"> Super Short - <br/>
                            Think Demi Moore in Ghost
                        </p>
                        <p class="input-field">
                            <input type="radio" name="hair_length" value="short"> Short - <br/>
                            Think Rihanna Bob
                        </p>
                        <p class="input-field">
                            <input type="radio" name="hair_length" value="medium"> Medium - <br/>
                            Think Cameron Diaz in The Sweetest Thing
                        </p>
                        <p class="input-field">
                            <input type="radio" name="hair_length" value="long"> Long - <br/>
                            Think current Selena Gomez
                        </p>
                    </p>
                    <input type="submit" value="submit" />
                </form>
        '''
        page_close = '''
        </body>
        </html>
        '''
        page_details = ''

        if self.request.GET:
            # store info from the form
            name = self.request.GET['name']
            email = self.request.GET['email']
            gender = self.request.GET['gender']
            services = self.request.GET['services']
            hair_length = self.request.GET['hair_length']

            # form data submitted + stored in variables I can use to populate placeholders
            page_details = '''
                   <header>
                       <h2>Request Confirmation</h2>
                       <h3>Details of your submitted request</h3>
                       <p>We recommend printing this page for your records.</p>
                   </header>
                   <div class="details">
                       <div class="detail">
                           <h4>Name</h4>
                           <p>{name}</p>
                       </div>
                       <div class="detail">
                           <h4>Email</h4>
                           <p>{email}</p>
                       </div>
                       <div class="detail">
                           <h4>Gender</h4>
                           <p>{gender}</p>
                       </div>
                       <div class="detail">
                           <h4>Services</h4>
                           <p>{services}</p>
                       </div>
                       <div class="detail">
                           <h4>Hair Length</h4>
                           <p>{hair_length}</p>
                       </div>
                   </div>
           '''
            # populate the placeholder content with data stored from the self.request.GET method
            page_details = page_details.format(**locals())
            # show page in browser with user data submitted via the form
            self.response.write(page_head + page_details + page_close)
        else:
            # otherwise show the page with a blank form
            self.response.write(page_head + page_form_body +
                                page_close)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
