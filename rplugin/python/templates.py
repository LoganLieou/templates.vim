import neovim

@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.function("Template")
    def template(self, args):
        self.vim.command('echo "hello template!"')
        for arg in args:
            self.vim.command(f"echo {arg}")

