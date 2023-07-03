from tkinter import N


try:
    from googlesearch import search
except ImportError:
    print('import error')
query="www.google.com"
for j in search(query,tld="co.in",num=10,stop=10,pause=2):
    print(j)