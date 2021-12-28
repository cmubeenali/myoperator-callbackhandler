from werkzeug.wrappers import Request,Response
from werkzeug.routing import Map,Rule
from datetime import datetime
import json,logging,requests,uuid

MAX_GREENLETE_COUNT=20

class App(object):
    def __init__(self):
        self.url_map = Map([
            Rule('/store-data',endpoint='handle_callback')
        ])            

    def handle_callback(self, req, args):
        print("IF_PARAMS_INURL : ",args)
        print("IF_PARAMS_DATA : ",req.data)
        print("IF_PARAMS_FORM : ",req.form)
        return Response("OK",status=200,mimetype='text/html')

    def dispatch_request(self, req):
        adapter = self.url_map.bind_to_environ(req.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, endpoint)(req, values)
        except Exception:
            return self.not_found(req, req.args)

    def wsgi_app(self, env, start_resp):
        try:
            request = Request(env)
            resp = self.dispatch_request(request)
            return resp(env,start_resp)
        except:
            pass
    def __call__(self, env, start_resp):
        return self.wsgi_app(env, start_resp)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app=App()
    run_simple('127.0.0.1', 6000, app, use_reloader=True,threaded=True)