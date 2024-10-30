# esta es una función que muestra un mensaje con la función 
print(" ")
print("Cristian David Salas De LA O 3-W")
print(" ")

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
