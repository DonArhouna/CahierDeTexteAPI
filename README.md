# CahierDeTexteAPI

# 📚 Cahier de Texte API – Backend Django

Ce backend est développé avec **Django + Django REST Framework**. 
Il permet la gestion des campus, filières, classes, cours, professeurs, 
responsables, ainsi que les fonctionnalités d’émargement des profs et de cahier de texte.

## 🚀 Fonctionnalités principales

- Authentification par JWT (responsables)
- Gestion CRUD des entités :
  - Campus, Filières, Classes, Cours
  - Professeurs et Responsables
- Emargement des professeurs (via matricule)
- Suivi des cahiers de texte
- Génération de rapports mensuels et semestriels

## 🛠 Technologies

- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt
- SQLite3 / PostgreSQL (selon environnement)

## 📁 Structure
backend/ ├── gestion/ # App principale │ 
├── models.py # Modèles : Campus, Filiere, Classe... │ 
├── serializers.py # Serializers DRF │ 
├── views.py # ViewSets API │ 
 └── urls.py # Routes de l'app ├── cahier_de_texte_api/ │ 
 ├── settings.py # 
 Configuration du projet │ └── urls.py # Routes globales (token, api/) └── manage.py


## 🔐 Authentification

- `/api/token/` : login (username/password)
- `/api/token/refresh/` : refresh du JWT

## 🧪 Lancer le projet localement

```bash
cd backend
python -m venv venv
source venv/bin/activate  # sous Windows : venv\Scripts\activate
pip install -r requirements.txt

## Créer un superutilisateur
python manage.py createsuperuser
# ⚠️ Par défaut dans ce projet :

login : admin

mot de passe : admin

# Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# Lancer le serveur
python manage.py runserver

## 🔐 Schéma du flux JWT avec Django REST Framework

+----------------------+         +------------------------+          +--------------------+
|   Client Frontend    |  --->   |  Endpoint /api/token/  |  --->    |      Backend       |
| (ex: React/Angular)  |         | (Login avec username/pwd)         |   (DRF + SimpleJWT)|
+----------------------+         +------------------------+          +--------------------+
          |                                 |                                  |
          | --------- Credentials --------> |                                  |
          |                                 | -- Génère Access + Refresh Token |
          |                                 | <---------- JWT Tokens --------- |
          | <---------- 200 OK -------------|                                  |
          |                                  |
          | Utilise le **Access Token** pour les requêtes API :
          | Authorization: Bearer <access_token>
          |
          | -------------> /api/campuses/ (GET)
          | Authorization: Bearer eyJ0eXAiOiJKV...
          |
          | <----------- 200 OK -------------- Ou 401 si Token expiré/invalide
          |
          | Si le Token est expiré :
          | -------------> /api/token/refresh/ (POST)
          | Body: { "refresh": "<refresh_token>" }
          |
          | <----------- 200 OK avec nouveau access_token


