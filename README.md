# Django-CyberWarcraft-Theme

```bash
django-starter-kit/
├── .github/
│   ├── workflows/
│   │   └── django-ci.yml  # Fichier GitHub Actions
│   └── FUNDING.yml        # Optionnel pour le support
├── config/
│   ├── __init__.py
│   ├── settings.py        # Config modulaire
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html      # Template master
│   │   └── index.html     # Page d'accueil stylée
│   └── views.py
├── static/
│   ├── css/
│   │   ├── bootstrap.min.css  # Bootstrap 5
│   │   └── neon-theme.css     # CSS personnalisé
│   └── js/
│       └── custom.js
├── .env.sample            # Variables d'environnement
├── .gitignore
├── Dockerfile             # Optionnel
├── manage.py
├── README.md              # Instructions
└── requirements.txt
```

# 1. Clique sur "Use this template" sur GitHub
# 2. Clone ton nouveau repo
git clone https://github.com/ton_user/ton-nouveau-projet.git

# 3. Initialise l'environnement
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 4. Crée ton .env
cp .env.sample .env
# Edite le .env avec tes valeurs

# 5. Lance le serveur !
python manage.py runserver

## ✨ Features Included

- [x] Configuration CI/CD avec GitHub Actions
- [x] Bootstrap 5 + Thème Néon
- [x] Structure modulaire (settings/ séparé)
- [x] Dockerfile préconfiguré
- [x] Page d'accueil exemple avec animations
- [x] Gestion sécurisée des secrets (.env)
