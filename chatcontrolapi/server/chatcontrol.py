from .server import Server
from ..webservices import Comuni
from base64 import b64decode
from tornado.web import RequestHandler, HTTPError
from tornado import gen
import queries

class ChatControlServer(Server):

    def __init__(self, host, port, log):
        """
        :param host: Serving host
        :param port: Serving port
        :param endpoint: Url of DB manager, for get the model
        :param idbot: Id of the bot to start
        """
        super().__init__(host, port, log)
        def dbget(key): return self.config.get('DB', key)
        self.querysession =  queries.TornadoSession(queries.uri(dbget('DBHOST'), dbget('DBPORT'), dbget('DATABASE'), dbget('USER'), dbget('PASSWORD')))

        

        self.add_handler(Comuni)

    
