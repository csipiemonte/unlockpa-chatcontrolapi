from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    def __init__(self,application, request,**kwargs):
        super(BaseHandler,self).__init__(application,request)

    def write_error(self, status_code, **kwargs):
        self.write('Error %s' % status_code)
