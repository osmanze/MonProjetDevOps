# -*- coding: utf-8 -*-
import os

# Lire la variable d'environnement MESSAGE avec une valeur par défaut
message = os.getenv("MESSAGE", "Hello, DevOps World!")
print(message)
