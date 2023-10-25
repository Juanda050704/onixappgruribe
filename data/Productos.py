import random
Productos = []
nombresProdructos=['id','nombre', 'costo_unitario', 'iva']
    
for _ in range(3000):
    
    id=random.randint(0,50000)
    nombre=random.choice(['Smartphone',
    'Laptop',
    'Televisor',
    'Cámara digital',
    'Auriculares inalámbricos',
    'Refrigeradora',
    'Micrófono USB',
    'Tablet',
    'Impresora láser',
    'Aspiradora robot'])
    costo_unitario = random.randint(150000, 600000)
    iva = 0.19
    orden = [id, nombre, costo_unitario, iva]
    Productos.append(orden)
    