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
def index (D):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="homeContainer"> \n'])
    extend_([u'\n'])
    extend_([u'</div>\n'])
    extend_([u'<div id="data">\n'])
    extend_([escape_(D, True), u'\n'])
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
    extend_([u'    <script type="text/javascript" src="/static/Scripts/flot/jquery.js"></script>\n'])
    extend_([u'    <script type="text/javascript" src="/static/Scripts/flot/jquery.flot.js"></script>\n'])
    extend_([u'    <script type="text/javascript" src="/static/Scripts/jquery.csv-0.71.js"></script>\n'])
    extend_([u'    <script type="text/javascript" src="/static/Scripts/bridgecontrol.js"></script>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'        <!-- Define the header for the page -->\n'])
    extend_([u'        <div id="header">\n'])
    extend_([u'                <h1><a href="/">Bridge Health Control Center</a></h1>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <!-- Create the menu bar -->\n'])
    extend_([u'        <hr>\n'])
    extend_([u'        <div id="navBar" class="links">\n'])
    extend_([u'                <ul>\n'])
    extend_([u'                        <li><a href="/">Dashboard</a></li>\n'])
    extend_([u'                        <li><a href="/stats">Stats</a></li>\n'])
    extend_([u'                        <li><a href="/help">About</a></li>\n'])
    extend_([u'                </ul>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <hr>\n'])
    extend_([u'        <!-- Display the main content -->\n'])
    extend_([u'        <div id="content">\n'])
    extend_([u'                ', escape_(page, False), u'\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <!-- Define the footer for the page -->\n'])
    extend_([u'        <div id="footer">\n'])
    extend_([u'                <div id="copyright">\n'])
    extend_([u'                        <h3>Copyright 2014, Matthew Iannucci</h3>\n'])
    extend_([u'                </div>\n'])
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

