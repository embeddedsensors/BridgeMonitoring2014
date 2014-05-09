import web

from handleData import getNewData

# Map out the urls
urls = (
    '/', 'Index',
    '/stats', 'Stats',
    '/help', 'Help'
)
# Toggle the web debug (to test sessions)
# web.config.debug = False

# Define the web templates
t_globals = {

}
render = web.template.render('templates', base='base', globals=t_globals)

# Create the web app and the sessions
app = web.application(urls, globals())

# Start the Web page class definitions
class Index:
    """ Show the overview page """
    def GET(self):
        D = getNewData()
        return render.index(D)

class Stats:
    """ Call the stats page """
    def GET(self):
        return render.stats()

class Help:
    """ Show the help page """
    def GET(self):
        return render.help()

def notfound():
    """ Create the not found page """
    return web.notfound("Sorry, the page you were looking for was not found.")
    # You can use template result like below, either is ok:
    # return web.notfound(render.notfound())
    # return web.notfound(str(render.notfound()))

def internalerror():
    """ Create the internal error page """
    return web.internalerror("The server says: No soup for you!")

# Create the not found app
app.notfound = notfound
app.internalerror = internalerror

main = app.cgirun()