import string

# Función para modificar la lista del abecedario
def modify_alphabet():
    # Almacenar el abecedario en una lista
    alphabet = list(string.ascii_lowercase)  # ['a', 'b', 'c', 'd', ..., 'z']
    
    # Eliminar las letras en posiciones múltiplos de 3 (índices 2, 5, 8, ...)
    alphabet = [letter for index, letter in enumerate(alphabet) if (index + 1) % 3 != 0]
    
    return alphabet
