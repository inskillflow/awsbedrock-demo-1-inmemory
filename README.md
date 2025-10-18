# Système de Gestion des Employés

Un système complet de gestion des employés avec API REST FastAPI et interface web moderne.

## Fonctionnalités

- 🏢 **Gestion des employés** : Ajouter, modifier, supprimer et consulter les employés
- 🛠️ **Gestion des compétences** : Suivi des compétences techniques de chaque employé
- 📊 **Tableaux de bord** : Statistiques détaillées sur les employés et départements
- 🔍 **Filtrage avancé** : Recherche par nom, département, compétences
- 📱 **Interface responsive** : Interface web moderne et adaptative
- 🚀 **API REST** : API complète avec documentation automatique

## Structure du Projet

```
awsbedrock/
├── employee_data.py      # Module de données et fonctions utilitaires
├── server.py            # Serveur FastAPI avec tous les endpoints
├── static/              # Interface web frontend
│   ├── index.html      # Page principale
│   └── app.js          # Logic JavaScript
├── requirements.txt     # Dépendances Python
└── README.md           # Documentation
```

## Installation

1. **Cloner le projet** (ou naviguer vers le répertoire)
```bash
cd C:\03-projetsGA\awsbedrock
```

2. **Créer un environnement virtuel** (recommandé)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou source venv/bin/activate  # Linux/Mac
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

## Lancement

**Démarrer le serveur :**
```bash
python server.py
```

Le serveur sera accessible sur : http://localhost:8002

## Utilisation

### Interface Web
- Accédez à http://localhost:8002 pour l'interface graphique
- **Onglet Employés** : Gérer la liste des employés avec filtres
- **Onglet Compétences** : Voir toutes les compétences disponibles
- **Onglet Statistiques** : Tableaux de bord avec métriques

### API REST

La documentation interactive de l'API est disponible sur :
- **Swagger UI** : http://localhost:8002/api/docs
- **ReDoc** : http://localhost:8002/api/redoc

#### Endpoints principaux

```
GET    /api/employees                    # Tous les employés
GET    /api/employees/{id}               # Employé par ID
GET    /api/employees/skill/{skill}      # Employés par compétence
GET    /api/employees/department/{dept}  # Employés par département
POST   /api/employees                   # Créer un employé
PUT    /api/employees/{id}              # Modifier un employé
DELETE /api/employees/{id}              # Supprimer un employé
GET    /api/skills                      # Toutes les compétences
GET    /api/stats                       # Statistiques globales
```

#### Exemple d'utilisation de l'API

**Créer un nouvel employé :**
```bash
curl -X POST "http://localhost:8002/api/employees" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Jean Dupont",
       "email": "jean.dupont@company.com",
       "department": "IT",
       "position": "Développeur Full Stack",
       "skills": ["Python", "JavaScript", "React"],
       "experience_years": 3,
       "salary": 50000
     }'
```

**Rechercher des employés par compétence :**
```bash
curl "http://localhost:8002/api/employees/skill/Python"
```

## Données par Défaut

Le système est pré-chargé avec :
- ✅ 5 employés exemples dans différents départements
- ✅ 20+ compétences techniques variées
- ✅ Données réalistes pour démonstration

## Compétences Supportées

Le système inclut les compétences suivantes :
- **Langages** : Python, JavaScript, TypeScript, SQL
- **Frameworks** : FastAPI, React, Vue.js, Angular, Node.js
- **Cloud & DevOps** : AWS, Docker, Kubernetes, Terraform, CI/CD
- **Données** : Machine Learning, Data Analysis, MongoDB, PostgreSQL
- **Autres** : Git, GraphQL, NoSQL

## Développement

### Ajouter de nouvelles compétences
Modifiez la liste `SKILLS` dans `employee_data.py`

### Ajouter de nouveaux endpoints
Ajoutez des routes dans `server.py` suivant le pattern FastAPI

### Personnaliser l'interface
Modifiez `static/index.html` et `static/app.js`

## Technologies Utilisées

- **Backend** : FastAPI, Python, Pydantic
- **Frontend** : HTML5, JavaScript ES6+, Tailwind CSS
- **Outils** : Axios pour HTTP, Font Awesome pour icônes
- **Documentation** : Swagger/OpenAPI automatique

## Configuration

Le serveur utilise les paramètres par défaut :
- **Host** : 0.0.0.0 (toutes les interfaces)
- **Port** : 8002
- **Mode** : Development avec rechargement automatique

Pour changer la configuration, modifiez la section `uvicorn.run()` dans `server.py`.

## API Response Examples

**GET /api/employees**
```json
[
  {
    "id": 1,
    "name": "Alice Dupont",
    "email": "alice.dupont@company.com",
    "department": "Développement",
    "position": "Senior Developer",
    "skills": ["Python", "FastAPI", "AWS", "Machine Learning", "SQL"],
    "experience_years": 5,
    "salary": 65000
  }
]
```

**GET /api/stats**
```json
{
  "total_employees": 5,
  "departments": {
    "Développement": {"count": 1, "avg_salary": 65000},
    "Frontend": {"count": 1, "avg_salary": 45000}
  },
  "skills_distribution": {
    "Python": 2,
    "JavaScript": 2,
    "React": 1
  },
  "average_salary": 56000,
  "total_skills": 20
}
```

---

🚀 **Le système est maintenant prêt à être utilisé !**
