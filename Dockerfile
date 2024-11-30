# Utilise une image de base de Python
FROM python:3.8-slim

# D�finit le r�pertoire de travail
WORKDIR /app

# Copie le fichier app.py dans le conteneur
COPY app.py .

# D�finit une variable d'environnement
ENV MESSAGE="Bonjour, monde DevOps!"

# Commande pour ex�cuter le script Python
CMD ["python", "app.py"]
