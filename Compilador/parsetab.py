
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEleftCOMPARISONleftLOGICOSleftMODULOleftEXPONENTErightUMINUSCONSTANTES NAME NUMBER PLUS MINUS TIMES DIVIDE EQUALS LPAREN RPAREN WHILE EXPONENTE COMPARISON POINTS LOGICOS MODULO PRINT STRINGstatement : NAME EQUALS expressionstatement : expressionstatement : PRINT LPAREN expression RPAREN\n                  | PRINT LPAREN STRING RPARENexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression EXPONENTE expression\n                  | expression COMPARISON expression\n                  | expression LOGICOS expression\n                  | expression MODULO expressionexpression : MINUS expression %prec UMINUSexpression : CONSTANTESexpression : LPAREN expression RPARENexpression : NUMBERexpression : NAMEstatement : WHILE expression POINTS expression\n                 | WHILE expression POINTS statement'
    
_lr_action_items = {'MODULO':([4,6,7,8,10,11,12,13,25,26,27,28,29,30,31,32,33,34,36,38,39,],[-14,14,-17,-16,-13,-17,14,14,-15,-12,14,-9,14,14,14,14,14,14,14,14,-17,]),'EXPONENTE':([4,6,7,8,10,11,12,13,25,26,27,28,29,30,31,32,33,34,36,38,39,],[-14,16,-17,-16,-13,-17,16,16,-15,16,16,-9,16,16,16,16,16,16,16,16,-17,]),'MINUS':([0,2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,38,39,],[2,2,2,-14,2,18,-17,-16,-13,-17,18,18,2,2,2,2,2,2,2,2,2,2,2,-15,-12,-10,-9,-7,-6,-8,-5,-11,18,18,18,-17,]),'POINTS':([4,8,10,11,12,25,26,27,28,29,30,31,32,33,],[-14,-16,-13,-17,24,-15,-12,-10,-9,-7,-6,-8,-5,-11,]),'RPAREN':([4,8,10,11,13,25,26,27,28,29,30,31,32,33,35,36,],[-14,-16,-13,-17,25,-15,-12,-10,-9,-7,-6,-8,-5,-11,40,41,]),'DIVIDE':([4,6,7,8,10,11,12,13,25,26,27,28,29,30,31,32,33,34,36,38,39,],[-14,19,-17,-16,-13,-17,19,19,-15,-12,-10,-9,-7,19,-8,19,-11,19,19,19,-17,]),'WHILE':([0,24,],[3,3,]),'EQUALS':([7,39,],[22,22,]),'CONSTANTES':([0,2,3,5,14,15,16,17,18,19,20,21,22,23,24,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'LOGICOS':([4,6,7,8,10,11,12,13,25,26,27,28,29,30,31,32,33,34,36,38,39,],[-14,21,-17,-16,-13,-17,21,21,-15,-12,21,-9,21,21,21,21,-11,21,21,21,-17,]),'COMPARISON':([4,6,7,8,10,11,12,13,25,26,27,28,29,30,31,32,33,34,36,38,39,],[-14,15,-17,-16,-13,-17,15,15,-15,-12,-10,-9,15,15,15,15,-11,15,15,15,-17,]),'TIMES':([4,6,7,8,10,11,12,13,25,26,27,28,29,30,31,32,33,34,36,38,39,],[-14,17,-17,-16,-13,-17,17,17,-15,-12,-10,-9,-7,17,-8,17,-11,17,17,17,-17,]),'LPAREN':([0,2,3,5,9,14,15,16,17,18,19,20,21,22,23,24,],[5,5,5,5,23,5,5,5,5,5,5,5,5,5,5,5,]),'STRING':([23,],[35,]),'NAME':([0,2,3,5,14,15,16,17,18,19,20,21,22,23,24,],[7,11,11,11,11,11,11,11,11,11,11,11,11,11,39,]),'NUMBER':([0,2,3,5,14,15,16,17,18,19,20,21,22,23,24,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'$end':([1,4,6,7,8,10,11,25,26,27,28,29,30,31,32,33,34,37,38,39,40,41,],[0,-14,-2,-17,-16,-13,-17,-15,-12,-10,-9,-7,-6,-8,-5,-11,-1,-19,-2,-17,-4,-3,]),'PLUS':([4,6,7,8,10,11,12,13,25,26,27,28,29,30,31,32,33,34,36,38,39,],[-14,20,-17,-16,-13,-17,20,20,-15,-12,-10,-9,-7,-6,-8,-5,-11,20,20,20,-17,]),'PRINT':([0,24,],[9,9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,5,14,15,16,17,18,19,20,21,22,23,24,],[6,10,12,13,26,27,28,29,30,31,32,33,34,36,38,]),'statement':([0,24,],[1,37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME EQUALS expression','statement',3,'p_statement_assign','pruebaWhile.py',76),
  ('statement -> expression','statement',1,'p_statement_expr','pruebaWhile.py',80),
  ('statement -> PRINT LPAREN expression RPAREN','statement',4,'p_statement_print','pruebaWhile.py',84),
  ('statement -> PRINT LPAREN STRING RPAREN','statement',4,'p_statement_print','pruebaWhile.py',85),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','pruebaWhile.py',89),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','pruebaWhile.py',90),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','pruebaWhile.py',91),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','pruebaWhile.py',92),
  ('expression -> expression EXPONENTE expression','expression',3,'p_expression_binop','pruebaWhile.py',93),
  ('expression -> expression COMPARISON expression','expression',3,'p_expression_binop','pruebaWhile.py',94),
  ('expression -> expression LOGICOS expression','expression',3,'p_expression_binop','pruebaWhile.py',95),
  ('expression -> expression MODULO expression','expression',3,'p_expression_binop','pruebaWhile.py',96),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','pruebaWhile.py',113),
  ('expression -> CONSTANTES','expression',1,'p_expression_constant','pruebaWhile.py',117),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','pruebaWhile.py',124),
  ('expression -> NUMBER','expression',1,'p_expression_number','pruebaWhile.py',128),
  ('expression -> NAME','expression',1,'p_expression_name','pruebaWhile.py',132),
  ('statement -> WHILE expression POINTS expression','statement',4,'p_expression_while','pruebaWhile.py',140),
  ('statement -> WHILE expression POINTS statement','statement',4,'p_expression_while','pruebaWhile.py',141),
]