from .command import Command
from ..server import ChatControlServer


class Run(Command):
    """Run a new instance of chatbot"""

    name = 'run'
    arguments = [
        dict(name='--host', type=str, default='localhost', help='Serving host'),
        dict(name='--port', type=int, default=5100, help='Serving port'),
    ]

    def main(self, args):
        self.log.info(f'Started with arguments: {args}')
        chatcontrol = ChatControlServer(args.host, args.port,self.log)
        chatcontrol.run()
