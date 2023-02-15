# Neave.TV Server
# Neave.TV was made by Neave
# Server version made by TemaisgameNoobas
import cherrypy
import os

# Config
app_port = 9089
allow_outside_connections = False
app_listenip = None # Leave this as "None" if you don't know what this is

class Main(object):
	@cherrypy.expose
	def index(self):
		pass

conf = { '/':{ 'tools.staticdir.on' : True,'tools.staticdir.root' : os.path.abspath(os.path.join(os.path.dirname(__file__))),'tools.staticdir.dir' : os.path.abspath(os.path.join(os.path.dirname(__file__), 'www')),'tools.staticdir.index' : 'index.html', } }

cherrypy.config.update({'server.socket_port': app_port})
bindip = None
if app_listenip == None:
		if allow_outside_connections == True:
			bindip = '0.0.0.0'
		else:
			bindip = '127.0.0.1'
elif not app_listenip == None:
	bindip = app_listenip

cherrypy.config.update({'server.socket_host': bindip})
cherrypy.quickstart(Main(),config=conf)
