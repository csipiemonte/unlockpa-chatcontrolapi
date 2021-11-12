from .basehandler import BaseHandler
from datetime import datetime
import json
import queries


class ComuniObj:

        
    def __init__(self, dictionary):
        """Constructor"""
        for key in dictionary:
            setattr(self, key, dictionary[key])
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True)


class Comuni(BaseHandler):

    def __init__(self, application, request, server):
        super().__init__(application, request)
        self.server = server

    name = 'comuni'
    path = '/comuni'



    async def get(self):
        domain = self.get_argument("domain")
        if (not domain):
           self.set_status(400) 
           return self.finish("Invalid key")
        domain.replace(" ", "")
        
        qu = self.server.queries.get('SQL_READ', 'sql_read_comune')
        sqlanswer = await self.server.querysession.query(qu, [domain])
        if not isinstance(sqlanswer, queries.Results) or sqlanswer.count()<=0:
            self.send_error(status_code=404)
        else:
            self.write(ComuniObj(sqlanswer.as_dict()).toJSON())
            
        sqlanswer.free()
