from .command import Command
from ..server import ChatControlServer


class Run2(Command):
    """Run a new instance of chatbot"""

    name = 'run2'
    arguments = [
        dict(name='--host', type=str, default='localhost', help='Serving host'),
        dict(name='--port', type=int, default=5001, help='Serving port'),
    ]

    def main(self, args):
        self.log.info(f'Started with arguments: {args}')
        chatcontrol = ChatControlServer(args.host, args.port, args.endpoint, args.idbot, self.log)
        chatcontrol.run()
