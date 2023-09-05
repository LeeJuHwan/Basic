import symbol
import token
import parser
from pprint import pprint
from typing import List



def lex(expression: str):
    symbols = {v: k for k, v in symbol.__dict__.items() if isinstance(v, int)}
    tokens =  {v: k for k, v in token.__dict__.items() if isinstance(v, int)}
    lexicon = {**symbols, **tokens}

    st = parser.expr(expression)
    st_list = parser.st2list(st)
    
    def replace(li: List):
        r = []
        for i in li:
            if isinstance(i, list):
                r.append(replace(i))
            else:
                if i in lexicon:
                    r.append(lexicon[i])
                else:
                    r.append(i)
        return r
    return replace(st_list)


if __name__ == "__main__":
    pprint(lex("a+1"))


cst = ['eval_input',
 ['testlist',
  ['test',
   ['or_test',
    ['and_test',
     ['not_test',
      ['comparison',
       ['expr',
        ['xor_expr',
         ['and_expr',
          ['shift_expr',
           ['arith_expr',
            ['term',
             ['factor', ['power', ['atom_expr', ['atom', ['NAME', 'a']]]]]],
            ['PLUS', '+'],
            ['term',
             ['factor',
              ['power', ['atom_expr', ['atom', ['NUMBER', '1']]]]]]]]]]]]]]]]],
 ['NEWLINE', ''],
 ['ENDMARKER', '']]

