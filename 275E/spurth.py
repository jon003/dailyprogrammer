#!/usr/bin/python


'''
Write a function that, given two strings, one an element name and one a proposed symbol for that element, 
determines whether the symbol follows the rules. If you like, you may parse the program's input and output 
the result, but this is not necessary.  The symbol will have exactly two letters. Both element name and 
symbol will contain only the letters a-z. Both the element name and the symbol will have their first letter 
capitalized, with the rest lowercase. (If you find that too challenging, it's okay to instead assume that both 
will be completely lowercase.)

Rules:
1. All chemical symbols must be exactly two letters, so B is not a valid symbol for Boron.

2. Both letters in the symbol must appear in the element name, but the first letter of the element name does not necessarily need to appear in the symbol. So Hg is not valid for Mercury, but Cy is.

3. The two letters must appear in order in the element name. So Vr is valid for Silver, but Rv is not. To be clear, both Ma and Am are valid for Magnesium, because there is both an a that appears after an m, and an m that appears after an a.

4. If the two letters in the symbol are the same, it must appear twice in the element name. So Nn is valid for Xenon, but Xx and Oo are not.

'''

a, b = 'Spenglerium', 'Ee'

def check_naming(element_name, symbol):
  if len(symbol) == 2 and 
  

