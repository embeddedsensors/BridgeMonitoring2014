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
        NW = [D[0], D[1], D[2]]
        NE = [D[3], D[4], D[5]]
        SE = [D[6], D[7], D[8]]
        SW = [D[9], D[10], D[11]]
        return render.index(NW, NE, SE, SW)

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