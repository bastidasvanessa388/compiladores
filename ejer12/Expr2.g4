grammar Expr2;

expr: expr '+' expr
    | expr '*' expr
    | NUM
    ;

NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;