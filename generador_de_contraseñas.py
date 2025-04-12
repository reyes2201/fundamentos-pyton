import random
import string
caracteres = string.ascii_letters + string.digits + string.punctuation
contrasena = ''.join(random.choice(caracteres)for i in range (12))
print("contraseña generada: ", contrasena)