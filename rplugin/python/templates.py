import pynvim

@pynvim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @pynvim.command('Template', range='')
    def testcommand(self, args):
        self.vim.current.line = f"Command with args: {args}, range: {range}"

    # testing this autocmd thing prob should configure this to be really good
    @pynvim.autocmd('BufEnter', pattern='*.py', eval='expand("<afile>")', sync=True)
    def on_bufenter(self, filename):
        self.vim.out_write('testplugin is in ' + filename + '\n')

