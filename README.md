# Système de Gestion des Employés - Demo 1 (En Mémoire)

![Version](https://img.shields.io/badge/demo-1-blue)
![Difficulty](https://img.shields.io/badge/difficulty-easy-green)
![Status](https://img.shields.io/badge/status-learning-yellow)

Un système complet de gestion des employés avec API REST FastAPI et interface web moderne.

**Caractéristique de cette version** : Données stockées EN MÉMOIRE (non persistantes)

## Documentation

**Deux versions disponibles :**

- **Français (FR)** : `documentation-fr/` - [Version française complète](documentation-fr/README.md)
- **English (EN)** : `documentation-en/` - [Complete English version](documentation-en/README.md)

Voir les README dans chaque dossier pour la liste complète des documents.

## Position dans le Parcours

- ⬅️ **Précédent** : Aucun (première version)
- ➡️ **Suivant** : [Demo 2 - AWS Bedrock RÉEL](https://github.com/inskillflow/awsbedrock-demo-2-aws-bedrock-real) (à venir)
- 🏗️ **Architecture** : Voir [Architecture et Évolution](documentation-fr/00-ARCHITECTURE.md)
- 📚 **Tous les repos** : Voir [Index des Repositories](documentation-fr/01-INDEX_REPOSITORIES.md)
- 📖 **Plan complet** : Voir [Plan de Formation Progressive](documentation-fr/05-PLAN_DE_FORMATION_PROGRESSIVE.md)

## Fonctionnalités

- **Gestion des employés** : Ajouter, modifier, supprimer et consulter les employés
- **Gestion des compétences** : Suivi des compétences techniques de chaque employé
- **Tableaux de bord** : Statistiques détaillées sur les employés et départements
- **Filtrage avancé** : Recherche par nom, département, compétences
- **Interface responsive** : Interface web moderne et adaptative
- **API REST** : API complète avec documentation automatique

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
- 5 employés exemples dans différents départements
- 20+ compétences techniques variées
- Données réalistes pour démonstration

**IMPORTANT** : Les données sont stockées en mémoire Python (liste `EMPLOYEES` dans `employee_data.py`).
Toutes les modifications sont **perdues au redémarrage du serveur**.

### Pourquoi en mémoire ?

Cette version est conçue pour l'apprentissage :
- Pas de configuration de base de données nécessaire
- Démarrage rapide en 2 minutes
- Focus sur les concepts FastAPI et IA
- Base solide pour ajouter la persistance plus tard

**Pour la persistance** : Voir [Demo 2 - PostgreSQL](https://github.com/inskillflow/awsbedrock-demo-2-postgresql)

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

## Limitations de Demo 1

Cette version est idéale pour apprendre, mais a des limitations :

❌ **Pas de persistance** - Données perdues au redémarrage  
❌ **Pas d'authentification** - Pas de gestion utilisateurs  
❌ **Pas de fichiers** - Pas d'upload de CV/photos  
❌ **Pas de notifications** - Pas d'emails automatiques  

### Prochaines Étapes

Pour ajouter ces fonctionnalités, consultez les versions suivantes :

1. **[Demo 2 - AWS Bedrock RÉEL](https://github.com/inskillflow/awsbedrock-demo-2-aws-bedrock-real)** - Configuration AWS complète ⭐
2. **[Demo 3 - PostgreSQL](https://github.com/inskillflow/awsbedrock-demo-3-postgresql)** - Persistance des données
3. **[Demo 5 - JWT Auth](https://github.com/inskillflow/awsbedrock-demo-5-auth-jwt)** - Authentification
4. **[Demo 7 - Files S3](https://github.com/inskillflow/awsbedrock-demo-7-files-s3)** - Upload de fichiers
5. **[Demo 8 - Notifications](https://github.com/inskillflow/awsbedrock-demo-8-notifications)** - Emails

**Voir le plan complet** : [Plan de Formation Progressive](documentation-fr/05-PLAN_DE_FORMATION_PROGRESSIVE.md)

---

**Le système est maintenant prêt à être utilisé !**

Ce projet fait partie d'une série de **19 demos progressifs** pour construire un système RH complet avec IA.

**Prochaine étape importante** : [Demo 2 - Configurer AWS Bedrock RÉEL](https://github.com/inskillflow/awsbedrock-demo-2-aws-bedrock-real)
