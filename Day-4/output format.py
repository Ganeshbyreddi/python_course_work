Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
>>> b=10.3
>>> c='codegnan'
>>> print(a,b,c)
10 10.3 codegnan
>>> print("a value is",a)
a value is 10
>>> print("a value is",a,"| b value is",b,'| c value is',c)
a value is 10 | b value is 10.3 | c value is codegnan
>>> print(a,b,c)
10 10.3 codegnan
>>> print(a,b,c,sep='')
1010.3codegnan
>>> print(a,b,c,sep='\n')
10
10.3
codegnan
>>> print(a,b,c,sep='\t')
10	10.3	codegnan
>>> print(a,b,c,sep='\t',end='@')
10	10.3	codegnan@
>>> print(a,b,c,sep='\t',end='\n\n')
10	10.3	codegnan

>>> print(f'a={a} b={b} c={c}')
a=10 b=10.3 c=codegnan
>>> print(f'a value is {a} | bvalue is {b} | c value is {c}")
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"a value is {a} | bvalue is {b} | c value is {c}")
...       
a value is 10 | bvalue is 10.3 | c value is codegnan
>>> print('a=%d b=%f c=%s'%(a,b,c))
...       
a=10 b=10.300000 c=codegnan
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
...       
a=10 b=10.30 c=codegnan
>>> print('a = {} | b = {} | c = {}'.format(a,b,c))
...       
a = 10 | b = 10.3 | c = codegnan
>>> print('a = {} | b = {} | c = {}'.format(c,a,b))
...       
a = codegnan | b = 10 | c = 10.3
>>> print('a = {1} | b = {2} | c = {0}'.format(a,b,c))
...       
a = 10.3 | b = codegnan | c = 10
