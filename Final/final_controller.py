# [START imports]
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

# session code from this example:
# url: http://webapp-improved.appspot.com/api/webapp2_extras/sessions.html

import jinja2
import webapp2
from webapp2_extras import sessions

# import your mastermind functions
import finalFuncs

# boiler plate code for sessions
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]

# more boiler plate code, just leave it as is
class BaseHandler(webapp2.RequestHandler):  # Copied from Google's doc
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

# [START main_page]
class MainPage(BaseHandler):

    def get(self):
        District= self.request.get("district")
        Income= self.request.get("income")
        Persons = self.request.get("persons")
        User = finalFuncs.User(District, Income, Persons)
        Cost = finalFuncs.Cost()
        total = finalFuncs.totalCost(Cost, User)
        
        
        template_values= {'District':District, 'Income':Income, "Persons":Persons, "User":User, "Cost":total}
        
        template = JINJA_ENVIRONMENT.get_template('finalproject.html')
        self.response.write(template.render(template_values))
# [END main_page]



# boiler plate, leave as is
config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}


# here is where you map your url requests to handlers
app = webapp2.WSGIApplication([
    ('/', MainPage),
], config=config, debug=True)
