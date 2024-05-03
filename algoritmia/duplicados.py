def eliminar_duplicados(lista: list) -> list:
    """
        Retorna una nueva lista con los elementos de `lista`, eliminando sus duplicados
        y manteniendo el orden original.
    """
    # Creamos una lista nueva que retornaremos 
    sin_duplicados = []
    # Creamos un conjunto para conocer qué elementos ya encontramos
    encontrados = set()

    # Por cada elemento en la lista...
    for elem in lista:
        # ..si ya no lo hemos encontrado...
        if elem not in encontrados:
            # ...lo agregamos a la nueva lista
            sin_duplicados.append(elem)
            # ... y al conjunto
            encontrados.add(elem)

    # Puesto que recorrimos la lista en orden, `sin_duplicados` 
    # también conserva el mismo orden.
    return sin_duplicados

assert eliminar_duplicados([1, 2, 3, 4, 4, 5, 6, 6, 7]) == [
    1, 2, 3, 4, 5, 6, 7], "El retorno de `eliminar_duplicados` no fue el esperado"
