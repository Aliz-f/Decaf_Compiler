grammar decaf;

program : decl+ EOF;

decl: t_int | t_double | t_bool | t_string | ifstmt | elsestmt | whilestmt | forstmt|
     t_return | t_break | t_print | t_this | t_new | newArray |
     readInteger | readLine | t_void | t_null | constant_bool | constant_double | 
     constant_int | constant_string | t_ID | operands | stmt | paracentesis | tools;

ifstmt : If;
elsestmt : Else;
whilestmt : While;
forstmt : For;

t_int : Int;
t_double : Double;
t_bool : Bool;
t_string : String;
t_ID : Ident;
t_void : Void;
t_break:Break;
t_return: Return;
t_print: Print;
t_this: This;
t_new: New;

constant_int : IntConstant;
constant_double : DoubleConstant;
constant_string : StringConstant;
constant_bool : BoolConstant;

newArray : NewArray;
readInteger: ReadInteger;
readLine :  ReadLine;
t_null : Null;

operands: Operands;
stmt : Stmt;
paracentesis: Paracentesis;
tools : Tools;

//skip
Ws: [ \t\r\n]+ -> skip;
Comment:  ('//'.*?'\n'| '/*'.*?'*/') -> skip;


//keywords
Int : 'int';
Double : 'double';
Bool : 'bool';
String : 'string';
If : 'if';
Else :'else';
While : 'while';
For : 'for';
Return : 'return';
Break : 'break';
Print : 'print';
This : 'this';
New : 'new';
NewArray : 'NewArray';
ReadInteger : 'ReadInteger';
ReadLine : 'ReadLine';
Void: 'void';
Null : 'null';
Operands : '!' | '-' | '*' | '/' | '%' | '+' |
        '<=' | '>=' | '<' | '>' | '||' | '&&' | '=';
Stmt : '{' | '}' | '[' | ']';
Paracentesis : '(' | ')';
Tools : ';' | ',' | '.';

//Data Identifiers:
IntConstant: INT_DEC | INT_HEX;
DoubleConstant: ( (IntConstant+ '.' IntConstant) | (IntConstant '.') ) EXP?;
StringConstant: ["].*?["];
BoolConstant: 'true' | 'false';
Ident : (LETTER)+ (DIGIT|LETTER|'_')* (DIGIT|LETTER)* ;



//Fragment
fragment EXP: ('e'| 'E')('+'|'-')?IntConstant+; 
fragment INT_DEC: DIGIT+;
fragment DIGIT : [0-9];
fragment LETTER: [Aa-zZ];
fragment INT_HEX:('0x'|'0X')[0-9a-fA-F]+;
