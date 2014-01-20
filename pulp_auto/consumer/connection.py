from patchwork import Connection as PatchworkConnection

class Connection(object):
    def __init__(self, hostname='localhost', ssh_key=None):
        self.connection = PatchworkConnection(instance=hostname, key_filename=ssh_key)

    def remote(self, command):
        '''return a Plubmub bound remote command instance of a command'''
        return command(remote=self.connection.pbm)

    def __call__(self, command):
        '''return remote pulp-consumer command result'''
        return self.remote(command)()


