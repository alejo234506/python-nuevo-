def area_rectangulo(
        x:float ,
        y:float
)-> float:
    """
    funcion qu calcula el area de un rectangulo 

    ---params---
    - x (float): es la base de mi rectangulo
    - y (float): es la altura  de mi rectangulo

    ---return---
    -area (float) : es el area de mi rectangulo 

    """
    return x * y

altura = float(input('introduce la altura del rectangulo:'))
base=float(input('introduce el base  del rectangulo:'))
result=area_rectangulo(base,altura)
print(f'el area el rectangulo es {result}')
