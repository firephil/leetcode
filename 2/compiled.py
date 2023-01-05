# compile and run another python file on the fly

with open('addtwo.py', 'r') as f:
    src = f.read()
# Converting above source code to an executable
code = compile(src, 'mulstring', 'exec')

# Running the executable code.
exec(code)