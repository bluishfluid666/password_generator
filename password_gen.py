import random
import pyperclip

def passwordGenerator(password_len, incl_symbol=False, incl_ambiguous=False):
  """generate random string of password of preference per user's request"""
  
  raw = "B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, X, Z, W, Y, A, E, I, O, U"
  rawambiguous = "{ } [ ] ( ) / \ ' \" ` ~ , ; : . < >"
  rawsymbol = "@#$%"
  
  numbers = list(range(10))
  capitalized = raw.split(sep=', ')
  lower = list(map(lambda x: x.lower(), capitalized))
  symbols = list(rawsymbol)
  ambiguous = rawambiguous.split(sep=' ')
  chars = password_len
  pw, sym, ambi, num, cap = [], [], [], [], []
  not_spec = capitalized+lower+numbers
  num.append(random.choice(numbers))
  cap.append(random.choice(capitalized))
  chars -= (1+1)
  if incl_symbol:
    sym.append(random.choice(symbols))
    chars -= 1
  if incl_ambiguous:
    ambi.append(random.choice(ambiguous))
    chars -= 1
  processed = random.sample(not_spec, k=chars)
  pw = processed+num+cap+sym+ambi
  return ''.join([str(item) for item in random.sample(pw, k=len(pw))])
while True:
  password_length = int(input('Your password length: '))
  include_symbol = input(f'Include symbols like (@ # $ %)? (y/n) ')
  include_ambiguous = input("Include ambiguous characters like { } [ ] ( ) / \ ' \" ` ~ , ; : . < >? (y/n) ")
  symbol_flag = False
  ambiguous_flag = False
  if include_symbol == 'y':
    symbol_flag = True
  if include_ambiguous == 'y':
    ambiguous_flag = True

  result = passwordGenerator(password_length, symbol_flag, ambiguous_flag)
  print("--------Your password: "+ result+"--------")
  pyperclip.copy(result)
  print('Your password is ready to be pasted. Thank you for using our service.')
  cont = input('Continue using? (y/n) ')
  if cont != 'y':
    break