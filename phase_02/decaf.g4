grammar decaf;

program : decl+ EOF;

test: expr EOF;

decl: variableDecl | functionDecl;

variableDecl: variable';';

variable : d_type Ident;

d_type : d_type'[]'| Int | Double | Bool | String | Ident;

functionDecl : (d_type Ident '('formals')' stmtBlock) | (Void Ident '('formals')' stmtBlock);

formals : (variable+',')? ; //change

protod_type : (d_type Ident '('formals')'';' )| (Void Ident '('formals')' ';' );

stmtBlock :  '{' variableDecl*stmt* '}';

stmt : expr';' |ifStmt | whileStmt | forStmt | breakStmt | returnStmt | printStmt | stmtBlock;

ifStmt : If '('expr')'stmt (Else stmt)?;

whileStmt : While '('expr')'stmt;

forStmt : For '('expr?';'expr';'expr?')'stmt;

returnStmt : Return expr?';';

breakStmt : Break';';

printStmt : Print '('expr+','')' ';';

expr : lvalue '=' expr | constant | This | call | '('expr')' |
expr Op2 expr | expr Op1 expr | Negative expr | expr Op3 expr | expr Op4 expr | expr Logical expr |
Not expr | ReadInteger | ReadLine | NewArray '('expr','d_type')';

lvalue : Ident;

call : Ident '('actuals')';

actuals : (expr+',')? ; //change

constant : IntConstant | DoubleConstant | BoolConstant | StringConstant ;

Not: '!';
Negative: '-';
Op1: '*' | '/' | '%';
Op2: '+' | '-';
Op3: '<=' | '>=' | '<' | '>';
Op4: '==' | '!=';
Logical: '||' | '&&';

//skip
Ws: [ \t\r\n]+ -> skip;
Comment:  ('//'.*?'\n'| '/*'.*?'*/') -> skip;

//Keywords :
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
NewArray : 'newArray';
ReadInteger : 'readInteger()';
ReadLine : 'readLine()';
Void: 'void';
Null : 'null';


//Data Identifiers:
IntConstant: INT_DEC | INT_HEX; //Done
DoubleConstant: ( (IntConstant+ '.' IntConstant) | (IntConstant '.') ) EXP?;
StringConstant: ["](STR)*?["]; //Check num 1
BoolConstant: 'true' | 'false'; //Done
Ident : (UPERLETTER|LOWERLETTER)+ ('_'| DIGIT | UPERLETTER | LOWERLETTER )* {1,31} ; // Check num2


//Fragment
fragment EXP: ('e'| 'E')('+'|'-')?IntConstant+; 
fragment STR: ~('\n' | '"')*;
fragment INT_DEC: DIGIT+;
fragment INT_HEX:('0x'|'0X')[0-9a-fA-F]+;
fragment DIGIT : [0-9];
fragment UPERLETTER: [A-Z];
fragment LOWERLETTER: [a-z]; 