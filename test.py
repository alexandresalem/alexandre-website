import os

print(os.environ)
for k,v in os.environ.items():
    print(f'A chave {k} possui valor {v}')
