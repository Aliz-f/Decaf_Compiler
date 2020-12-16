import sys
from antlr4 import *
from decafLexer import decafLexer
from decafParser import decafParser
from decafListener import decafListener


def main(argv):
    inpu = FileStream(argv[1])
    lexer = decafLexer(inpu)
    stream = CommonTokenStream(lexer)
    parser = decafParser(stream)
    tree = parser.program()
    compiler_listeners = decafListener()
    walker = ParseTreeWalker()
    walker.walk(compiler_listeners,tree)
    # output = open("output.txt","w")
    # output.close()
    # print(tree.toStringTree())

if __name__ == '__main__':
    main(sys.argv)
