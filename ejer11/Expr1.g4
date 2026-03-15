grammar Expr1;

expr: expr '+' NUM
    | NUM
    ;

NUM: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;