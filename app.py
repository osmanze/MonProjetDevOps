# -*- coding: utf-8 -*-
import os

# Lire la variable d'environnement MESSAGE avec une valeur par d�faut
message = os.getenv("MESSAGE", "Hello, DevOps World!")
print(message)
