import pynvim

@pynvim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @pynvim.function("Hello")
    def helloPy(self, args):
        self.vim.command('echo "Hello, world!\n"')
