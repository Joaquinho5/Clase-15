import sys 

print(sys.argv)
for persona in sys.argv[1:]:
    print(f"Hola {persona} bienvendio al curso de Python")