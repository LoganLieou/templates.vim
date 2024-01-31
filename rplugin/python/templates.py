import neovim

@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.function("Template")
    def template(self, args):
        self.vim.command("echo hello template!")
        # args are not valid
        if (args):
            self.vim.command("echo args exist!")
        else:
            self.vim.command("echo no args passed!")
