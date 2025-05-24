def solution(text):
    text = text.lower()  # Ignora mayúsculas/minúsculas
    contador = {}
    
    for val in text:
            if val in contador:
                contador[val] += 1
            else:
                contador[val] = 1
    repetidos = 0
# Cuenta solo los caracteres que aparecen más de una vez
# Versión compacta: repetidos = sum(1 for c in contador.values() if c > 1)
    for c in contador.values():
        if c > 1:
            repetidos += 1
    return repetidos