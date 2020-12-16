# Generated from decaf.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .decafParser import decafParser
else:
    from decafParser import decafParser

fin = open('output.txt' , 'a')

# This class defines a complete listener for a parse tree produced by decafParser.
class decafListener(ParseTreeListener):

    # Enter a parse tree produced by decafParser#program.
    def enterProgram(self, ctx:decafParser.ProgramContext):
        pass

    # Exit a parse tree produced by decafParser#program.
    def exitProgram(self, ctx:decafParser.ProgramContext):
        pass


    # Enter a parse tree produced by decafParser#decl.
    def enterDecl(self, ctx:decafParser.DeclContext):
        pass

    # Exit a parse tree produced by decafParser#decl.
    def exitDecl(self, ctx:decafParser.DeclContext):
        pass


    # Enter a parse tree produced by decafParser#ifstmt.
    def enterIfstmt(self, ctx:decafParser.IfstmtContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#ifstmt.
    def exitIfstmt(self, ctx:decafParser.IfstmtContext):
        pass


    # Enter a parse tree produced by decafParser#elsestmt.
    def enterElsestmt(self, ctx:decafParser.ElsestmtContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#elsestmt.
    def exitElsestmt(self, ctx:decafParser.ElsestmtContext):
        pass


    # Enter a parse tree produced by decafParser#whilestmt.
    def enterWhilestmt(self, ctx:decafParser.WhilestmtContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#whilestmt.
    def exitWhilestmt(self, ctx:decafParser.WhilestmtContext):
        pass


    # Enter a parse tree produced by decafParser#forstmt.
    def enterForstmt(self, ctx:decafParser.ForstmtContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#forstmt.
    def exitForstmt(self, ctx:decafParser.ForstmtContext):
        pass


    # Enter a parse tree produced by decafParser#t_int.
    def enterT_int(self, ctx:decafParser.T_intContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#t_int.
    def exitT_int(self, ctx:decafParser.T_intContext):
        pass


    # Enter a parse tree produced by decafParser#t_double.
    def enterT_double(self, ctx:decafParser.T_doubleContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#t_double.
    def exitT_double(self, ctx:decafParser.T_doubleContext):
        pass


    # Enter a parse tree produced by decafParser#t_bool.
    def enterT_bool(self, ctx:decafParser.T_boolContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#t_bool.
    def exitT_bool(self, ctx:decafParser.T_boolContext):
        pass


    # Enter a parse tree produced by decafParser#t_string.
    def enterT_string(self, ctx:decafParser.T_stringContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#t_string.
    def exitT_string(self, ctx:decafParser.T_stringContext):
        pass


    # Enter a parse tree produced by decafParser#t_ID.
    def enterT_ID(self, ctx:decafParser.T_IDContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_ID {item}\n')

    # Exit a parse tree produced by decafParser#t_ID.
    def exitT_ID(self, ctx:decafParser.T_IDContext):
        pass


    # Enter a parse tree produced by decafParser#t_void.
    def enterT_void(self, ctx:decafParser.T_voidContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#t_void.
    def exitT_void(self, ctx:decafParser.T_voidContext):
        pass


    # Enter a parse tree produced by decafParser#t_break.
    def enterT_break(self, ctx:decafParser.T_breakContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#t_break.
    def exitT_break(self, ctx:decafParser.T_breakContext):
        pass


    # Enter a parse tree produced by decafParser#t_return.
    def enterT_return(self, ctx:decafParser.T_returnContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#t_return.
    def exitT_return(self, ctx:decafParser.T_returnContext):
        pass


    # Enter a parse tree produced by decafParser#t_print.
    def enterT_print(self, ctx:decafParser.T_printContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#t_print.
    def exitT_print(self, ctx:decafParser.T_printContext):
        pass


    # Enter a parse tree produced by decafParser#t_this.
    def enterT_this(self, ctx:decafParser.T_thisContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#t_this.
    def exitT_this(self, ctx:decafParser.T_thisContext):
        pass


    # Enter a parse tree produced by decafParser#t_new.
    def enterT_new(self, ctx:decafParser.T_newContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#t_new.
    def exitT_new(self, ctx:decafParser.T_newContext):
        pass


    # Enter a parse tree produced by decafParser#constant_int.
    def enterConstant_int(self, ctx:decafParser.Constant_intContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_INT {item}\n')

    # Exit a parse tree produced by decafParser#constant_int.
    def exitConstant_int(self, ctx:decafParser.Constant_intContext):
        pass


    # Enter a parse tree produced by decafParser#constant_double.
    def enterConstant_double(self, ctx:decafParser.Constant_doubleContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_DOUBLE {item}\n')

    # Exit a parse tree produced by decafParser#constant_double.
    def exitConstant_double(self, ctx:decafParser.Constant_doubleContext):
        pass


    # Enter a parse tree produced by decafParser#constant_string.
    def enterConstant_string(self, ctx:decafParser.Constant_stringContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_STRING{item}\n')

    # Exit a parse tree produced by decafParser#constant_string.
    def exitConstant_string(self, ctx:decafParser.Constant_stringContext):
        pass


    # Enter a parse tree produced by decafParser#constant_bool.
    def enterConstant_bool(self, ctx:decafParser.Constant_boolContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_BOOL {item}\n')

    # Exit a parse tree produced by decafParser#constant_bool.
    def exitConstant_bool(self, ctx:decafParser.Constant_boolContext):
        pass


    # Enter a parse tree produced by decafParser#newArray.
    def enterNewArray(self, ctx:decafParser.NewArrayContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#newArray.
    def exitNewArray(self, ctx:decafParser.NewArrayContext):
        pass


    # Enter a parse tree produced by decafParser#readInteger.
    def enterReadInteger(self, ctx:decafParser.ReadIntegerContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#readInteger.
    def exitReadInteger(self, ctx:decafParser.ReadIntegerContext):
        pass


    # Enter a parse tree produced by decafParser#readLine.
    def enterReadLine(self, ctx:decafParser.ReadLineContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#readLine.
    def exitReadLine(self, ctx:decafParser.ReadLineContext):
        pass


    # Enter a parse tree produced by decafParser#t_null.
    def enterT_null(self, ctx:decafParser.T_nullContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'T_{item}\n')

    # Exit a parse tree produced by decafParser#t_null.
    def exitT_null(self, ctx:decafParser.T_nullContext):
        pass


    # Enter a parse tree produced by decafParser#operands.
    def enterOperands(self, ctx:decafParser.OperandsContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'{item}\n')

    # Exit a parse tree produced by decafParser#operands.
    def exitOperands(self, ctx:decafParser.OperandsContext):
        pass


    # Enter a parse tree produced by decafParser#stmt.
    def enterStmt(self, ctx:decafParser.StmtContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'{item}\n')

    # Exit a parse tree produced by decafParser#stmt.
    def exitStmt(self, ctx:decafParser.StmtContext):
        pass


    # Enter a parse tree produced by decafParser#paracentesis.
    def enterParacentesis(self, ctx:decafParser.ParacentesisContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'{item}\n')

    # Exit a parse tree produced by decafParser#paracentesis.
    def exitParacentesis(self, ctx:decafParser.ParacentesisContext):
        pass


    # Enter a parse tree produced by decafParser#tools.
    def enterTools(self, ctx:decafParser.ToolsContext):
        my_list = list(ctx.getChildren())
        for item in my_list:
            fin.writelines(f'{item}\n')

    # Exit a parse tree produced by decafParser#tools.
    def exitTools(self, ctx:decafParser.ToolsContext):
        pass



del decafParser