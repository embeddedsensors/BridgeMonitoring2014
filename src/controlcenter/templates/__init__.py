from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def help():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])

    return self

help = CompiledTemplate(help, 'templates/help.html')
join_ = help._join; escape_ = help._escape

# coding: utf-8
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="homeContainer"> \n'])
    extend_([u'\n'])
    extend_([u'</div>\n'])

    return self

index = CompiledTemplate(index, 'templates/index.html')
join_ = index._join; escape_ = index._escape

# coding: utf-8
def base (page):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<html>\n'])
    extend_([u'<head>\n'])
    extend_([u'    <title>Bridge Health Monitoring Control Center</title>\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" href="/static/Styles/mobile.css" media="only screen and (max-device-width: 767px)" />\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" href="/static/Styles/screen.css" media="only screen and (min-device-width: 768px)" />\n'])
    extend_([u'    <link rel="shortcut icon" type="image/x-icon" href="/static/favicon.ico" />\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'        <!-- Define the header for the page -->\n'])
    extend_([u'        <div id="header">\n'])
    extend_([u'                <h1><a href="/">Bridge Health Control Center</a></h1>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <!-- Create the three coloumn layout.-->\n'])
    extend_([u'        <div class="colmask threecol">\n'])
    extend_([u'                <div class="colmid">\n'])
    extend_([u'                        <div class="colleft">\n'])
    extend_([u'                                <div class="col1">\n'])
    extend_([u'                                        <!-- Column 1 start -->\n'])
    extend_([u'                                        <!-- Get the page data as declared in code.py -->\n'])
    extend_([u'                                        ', escape_(page, False), u'\n'])
    extend_([u'                                        <!-- Column 1 end -->\n'])
    extend_([u'                                </div>\n'])
    extend_([u'                                <div class="col2">\n'])
    extend_([u'                                        <!-- Column 2 start -->\n'])
    extend_([u'                        <div id="menu">\n'])
    extend_([u'                                <h2><a href="/">Dashboard</a></h2>\n'])
    extend_([u'                                <h2><a href="/stats">Stats</a></h2>\n'])
    extend_([u'                                <h2><a href="/help">Help</a></h2>\n'])
    extend_([u'                            </div>\n'])
    extend_([u'                                        <!-- Column 2 end -->\n'])
    extend_([u'                                </div>\n'])
    extend_([u'                                <div class="col3">\n'])
    extend_([u'                                        <!-- Column 3 start -->\n'])
    extend_([u'                                        <!-- Column 3 end -->\n'])
    extend_([u'                                </div>\n'])
    extend_([u'                        </div>\n'])
    extend_([u'                </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <!-- Ends the three column layout-->\n'])
    extend_([u'        <!-- Define the footer for the page -->\n'])
    extend_([u'        <div id="footer">\n'])
    extend_([u'                <center>        \n'])
    extend_([u'                        <div id="copyright">\n'])
    extend_([u'                                <h3>Copyright 2014, Matthew Iannucci</h3>\n'])
    extend_([u'                        </div>\n'])
    extend_([u'                </center>\n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<!-- End the page layout -->\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

base = CompiledTemplate(base, 'templates/base.html')
join_ = base._join; escape_ = base._escape

# coding: utf-8
def stats():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])

    return self

stats = CompiledTemplate(stats, 'templates/stats.html')
join_ = stats._join; escape_ = stats._escape

