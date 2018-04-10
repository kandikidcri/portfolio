from flask import Flask
app = Flask(__name__)

"""
@function setRoute

@description Allow the ability for a client sent request to be served with the provided file 
             from the servers filesystem in the form of a response of the file's contents specified in the {file} param.

@param file           {String} File with relative path to resource being sent back on valid 
                               request.

@param routeName      {String} The part of the URL following where route name is 
                               like cristinarossie.com/{routeName}.

@param alternateRoute {String} The part of the URL following where route name is 
                               like cristinarossie.com/{routeName}.

"""
def setRoute(
    file = None, 
    routeName = None, 
    alternateRoute = None):
        def requestHandler(file): 
            return open(file, 'r').read()
        noFileErrorMsg = "You must provide the file to link to the route you are trying to set."
        
        if file is None:
            return noFileErrorMsg

        if alternateRoute is None:
            @app.route(routeName)
            def handlePrimaryRequest():
                return requestHandler(file)
        else:
            @app.route(routeName)
            @app.route(alternateRoute)
            def handleAlternateRequests(): 
                return requestHandler(file)
            
        
"""
Route URL request from http://cristinarossie.com or http://cristinarossie.com/main
to the file contents of main.html. Route requests from http://cristinarossie.com/about to about.html.
"""
def servePortfolioResources():
    setRoute("/html/main.html", "/main", "/")
    setRoute("about.html", "/about")
    app.run()

servePortfolioResources()