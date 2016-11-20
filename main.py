#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader("templates"))

class logIn(webapp2.RequestHandler):
  def get(self):
    username = 'Colleen'
    password = 'pass'

    template = JINJA_ENVIRONMENT.get_template("login.html")
    self.response.out.write(template.render())

  def post(self):
    username = self.request.get('username')
    password = self.request.get('password')
    
    if username == 'Colleen' and password == 'pass':
      template = JINJA_ENVIRONMENT.get_template("logged_in.html")
      self.response.out.write(template.render())
    else:
      msg = 'Your username or password is wrong'
    
    template = JINJA_ENVIRONMENT.get_template("login.html")
    self.response.out.write(template.render())


class loggedIn(webapp2.RequestHandler):
  def get(self):
    template = JINJA_ENVIRONMENT.get_template("logged_in.html")
    self.response.out.write(template.render())

app = webapp2.WSGIApplication([
    ('/login', logIn),
    ('/loggedin', loggedIn)
], debug=True)
