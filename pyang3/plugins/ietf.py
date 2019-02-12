"""IETF usage guidelines plugin
See RFC 6087
"""

import optparse
import sys

from pyang3 import plugin
from pyang3 import statements
from pyang3 import error
from pyang3.error import err_add
from pyang3.plugins import lint

def pyang_plugin_init():
    plugin.register_plugin(IETFPlugin())

class IETFPlugin(lint.LintPlugin):
    def __init__(self):
        lint.LintPlugin.__init__(self)
        self.namespace_prefixes = ['urn:ietf:params:xml:ns:yang:']
        self.modulename_prefixes = ['ietf', 'iana']

    def add_opts(self, optparser):
        optlist = [
            optparse.make_option("--ietf",
                                 dest="ietf",
                                 action="store_true",
                                 help="Validate the module(s) according to " \
                                 "IETF rules."),
            ]
        optparser.add_options(optlist)

    def setup_ctx(self, ctx):
        if not ctx.opts.ietf:
            return
        self._setup_ctx(ctx)
