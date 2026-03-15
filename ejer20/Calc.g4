grammar Calc;

prog: stat+ ;

stat
    : ID IGUAL expr
    | PRINT expr
    ;

expr: term ((MAS | MENOS) term)* ;

term: factor ((MUL | DIV) factor)* ;

factor
    : NUM
    | ID
    | PARI expr PARD
    ;

PRINT: 'print';
IGUAL: '=';
MAS: '+';
MENOS: '-';
MUL: '*';
DIV: '/';
PARI: '(';
PARD: ')';

ID: [a-zA-Z]+ ;
NUM: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;