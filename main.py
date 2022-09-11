import os
import translator

with open('main.kurwa', encoding='utf-8') as f:
    script = f.read()

script = translator.replacing(script)

f = open('test.py', 'w', encoding='utf-8')
f.write(script)
f.close()

os.system('test.py')
