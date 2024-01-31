import pynvim

## need a way to modify templates and config
templates_dir = "~/.config/nvim/templates/"

@pynvim.plugin
class Main(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('TestCommand', nargs='*', range='')
    def testcommand(self, args, range):
        self.nvim.current.line = ('Command with args: {}, range: {}'
                                  .format(args, range))

    # in-line template i.e. some data structure or something that you need to implement
    @pynvim.command('TemplateCommand')
    def template(self, args):
        self.nvim.command(f'echo "args: {args}"')
        self.nvim.current.buffer.append("Hello world")
