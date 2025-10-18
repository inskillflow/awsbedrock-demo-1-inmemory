# Plan de Formation Progressive - Système RH avec IA

Ce document présente une approche d'apprentissage progressive pour construire un système de gestion des employés complet. Chaque étape ajoute une nouvelle couche de complexité et correspond à un repository GitHub distinct.

---

## Philosophie d'Apprentissage

Au lieu de tout construire d'un coup, nous procédons par **couches successives**. Chaque version :
- Ajoute UNE nouvelle technologie ou fonctionnalité majeure
- Est autonome et fonctionnelle
- Peut être déployée indépendamment
- Sert de base pour la version suivante

**Avantage** : Apprentissage progressif, debuggage plus facile, compréhension approfondie.

---

## Roadmap des Versions

### Niveau 1 : Fondations

#### Demo 1 : En Mémoire (ACTUEL)
**Repository** : `awsbedrock-demo-1-inmemory`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-1-inmemory

**Description** :
- API REST FastAPI complète
- Interface web moderne
- Agent IA AWS Bedrock avec mode local
- **DONNÉES EN MÉMOIRE** (perdues au redémarrage)

**Technologies** :
- FastAPI + Uvicorn
- JavaScript Vanilla + Tailwind CSS
- AWS Bedrock (Claude 3 Sonnet)
- Données Python in-memory

**Ce qu'on apprend** :
- Bases de FastAPI
- Architecture API REST
- Intégration IA AWS Bedrock
- Interface web responsive

**Limitations** :
- Pas de persistance
- Pas d'authentification
- Pas de gestion de fichiers

**Temps d'apprentissage** : 1-2 semaines

---

### Niveau 2 : Configuration AWS Réelle

#### Demo 2 : AWS Bedrock Réel Configuré
**Repository** : `awsbedrock-demo-2-aws-bedrock-real`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-2-aws-bedrock-real

**Description** :
- Tout de Demo 1
- **AJOUT** : Configuration complète AWS Bedrock
- Compte AWS créé et configuré
- Credentials AWS fonctionnels
- Test avec Claude 3 Sonnet RÉEL
- Documentation détaillée du setup AWS

**Nouvelles technologies** :
- AWS IAM (gestion des permissions)
- AWS Bedrock activé
- AWS CLI configuré
- python-dotenv (variables d'environnement)

**Ce qu'on apprend** :
- Créer un compte AWS
- Configurer IAM et permissions
- Activer AWS Bedrock
- Gérer les credentials AWS
- Tester l'IA réelle
- Comprendre les coûts AWS

**Nouveaux fichiers** :
```
├── .env.example        # Template AWS credentials
├── aws_setup.md        # Guide setup AWS complet
├── test_bedrock.py     # Script de test AWS
└── requirements.txt    # Identique Demo 1
```

**Guide inclus** :
- Configuration pas-à-pas du compte AWS
- Capture d'écran de chaque étape
- Script de vérification des credentials
- Estimation des coûts réels
- Comment surveiller la facturation

**Temps d'apprentissage** : 2-3 jours

---

### Niveau 3 : Persistance des Données

#### Demo 3 : PostgreSQL + Neon
**Repository** : `awsbedrock-demo-3-postgresql`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-3-postgresql

**Description** :
- Base de Demo 2 (AWS réel)
- **AJOUT** : Base de données PostgreSQL via Neon (serverless)
- Persistance des données
- Migrations de schéma avec Alembic

**Nouvelles technologies** :
- SQLAlchemy (ORM)
- Alembic (migrations)
- Neon.tech (PostgreSQL serverless)

**Ce qu'on apprend** :
- Modèles de données relationnelles
- ORM (Object-Relational Mapping)
- Migrations de base de données
- Combiner AWS Bedrock + PostgreSQL

**Nouveaux fichiers** :
```
├── database.py          # Configuration DB
├── models.py           # Modèles SQLAlchemy
├── alembic/            # Migrations
│   ├── versions/
│   └── env.py
└── requirements.txt    # + sqlalchemy, alembic, psycopg2
```

**Temps d'apprentissage** : 1 semaine

---

#### Demo 4 : Xata (PostgreSQL Moderne)
**Repository** : `awsbedrock-demo-4-xata`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-4-xata

**Description** :
- Alternative à Demo 3
- Base de Demo 2 (AWS réel)
- **AJOUT** : Base de données Xata
- Recherche full-text intégrée
- UI admin pour la base de données

**Nouvelles technologies** :
- Xata SDK Python
- Recherche full-text sans Elasticsearch
- File attachments (préparation)

**Ce qu'on apprend** :
- Bases de données modernes
- Recherche full-text
- API moderne vs SQL classique
- Branching de base de données

**Temps d'apprentissage** : 3-5 jours

---

### Niveau 4 : Authentification et Sécurité

#### Demo 5A : Clerk Authentication (Rapide)
**Repository** : `awsbedrock-demo-5a-auth-clerk`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-5a-auth-clerk

**Description** :
- Base de Demo 3 (PostgreSQL)
- **AJOUT** : Authentification avec Clerk (service)
- Setup en 15 minutes
- OAuth social inclus (Google, GitHub)
- 2FA automatique

**Nouvelles technologies** :
- Clerk Python SDK
- Webhooks Clerk
- Session management automatique

**Ce qu'on apprend** :
- Intégration service d'auth tiers
- OAuth social
- Webhooks
- Production-ready en quelques minutes

**Nouveaux fichiers** :
```
├── auth/
│   ├── __init__.py
│   ├── clerk_client.py  # Client Clerk
│   └── dependencies.py  # Middleware Clerk
├── webhooks/
│   └── clerk.py        # Webhooks handlers
└── .env.example        # + CLERK_SECRET_KEY
```

**Avantages** :
- **Ultra rapide** (15 min vs 1 semaine)
- UI préfabriquée élégante
- Sécurité gérée par des experts
- OAuth social inclus
- 2FA/MFA automatique

**Limitations** :
- Dépendance externe
- Coûts après free tier
- Moins de contrôle

**Free Tier Clerk** :
- 5,000 utilisateurs actifs mensuels gratuits
- Toutes les fonctionnalités incluses
- Parfait pour démarrer

**Temps d'apprentissage** : 1 jour

---

#### Demo 5B : JWT Authentication Custom (Apprentissage)
**Repository** : `awsbedrock-demo-5b-auth-jwt-custom`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-5b-auth-jwt-custom

**Description** :
- Base de Demo 3 (PostgreSQL)
- **AJOUT** : Authentification JWT codée from scratch
- Inscription / Connexion custom
- Tokens d'accès et refresh
- Tout codé manuellement

**Nouvelles technologies** :
- python-jose (JWT)
- passlib (hachage mot de passe)
- OAuth2 avec FastAPI

**Ce qu'on apprend** :
- **Comment fonctionne l'authentification** (en profondeur)
- JWT (JSON Web Tokens)
- Hachage et sécurité des mots de passe
- Protection des endpoints
- Refresh tokens
- Gestion des sessions

**Nouveaux fichiers** :
```
├── auth/
│   ├── __init__.py
│   ├── jwt.py          # Gestion JWT
│   ├── password.py     # Hachage bcrypt
│   ├── schemas.py      # Pydantic models
│   └── dependencies.py # Middleware auth
├── models.py           # + User model
└── routers/
    └── auth.py         # Routes auth
```

**Avantages** :
- **Apprentissage complet**
- Contrôle total
- Gratuit (pas de service)
- Personnalisable à 100%

**Limitations** :
- Temps de développement (1 semaine)
- Plus de bugs potentiels
- Sécurité à gérer soi-même
- Pas d'OAuth social par défaut

**Temps d'apprentissage** : 1 semaine

---

#### Quelle Version Choisir ?

**Choisissez Demo 5A (Clerk) si** :
- Vous voulez aller vite en production
- Vous avez besoin d'OAuth social
- Vous voulez une UI moderne sans effort
- Vous préférez déléguer la sécurité

**Choisissez Demo 5B (JWT Custom) si** :
- Vous voulez comprendre l'authentification en profondeur
- Vous préparez un entretien technique
- Vous voulez le contrôle total
- Vous n'avez pas de budget pour des services

**Recommandation** :
1. Commencez par **Demo 5A (Clerk)** pour avoir un système fonctionnel rapidement
2. Puis faites **Demo 5B (JWT Custom)** pour apprendre comment ça marche vraiment

---

#### Demo 6 : Roles & Permissions (RBAC)
**Repository** : `awsbedrock-demo-6-rbac`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-6-rbac

**Description** :
- Base de Demo 5A ou 5B (Auth)
- **AJOUT** : Gestion des rôles
- Permissions granulaires
- Role-Based Access Control (RBAC)

**Rôles implémentés** :
- **Admin** : Accès complet
- **HR Manager** : Gestion complète des employés
- **Department Manager** : Gestion de son département
- **Employee** : Lecture seule de son profil

**Ce qu'on apprend** :
- RBAC (Role-Based Access Control)
- Permissions granulaires
- Middleware de validation
- Gestion avancée des accès

**Nouveaux fichiers** :
```
├── auth/
│   ├── roles.py        # Définition des rôles
│   └── permissions.py  # Vérification permissions
└── models.py           # + Role model
```

**Temps d'apprentissage** : 3-5 jours

---

### Niveau 5 : Fonctionnalités Avancées

#### Demo 7 : File Uploads + S3
**Repository** : `awsbedrock-demo-7-files-s3`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-7-files-s3

**Description** :
- Base de Demo 6 (RBAC)
- **AJOUT** : Upload de fichiers
- Stockage AWS S3
- Photos de profil, CV, documents

**Nouvelles technologies** :
- boto3 (AWS S3)
- Pillow (traitement images)
- python-multipart (upload)

**Ce qu'on apprend** :
- Upload de fichiers avec FastAPI
- Stockage cloud (AWS S3)
- Traitement d'images
- Validation de fichiers

**Nouveaux fichiers** :
```
├── services/
│   ├── storage.py      # Gestion S3
│   └── images.py       # Traitement images
└── models.py           # + FileAttachment model
```

**Temps d'apprentissage** : 1 semaine

---

#### Demo 8 : Notifications + Email
**Repository** : `awsbedrock-demo-8-notifications`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-7-notifications

**Description** :
- Base de Demo 6 (Files)
- **AJOUT** : Système de notifications
- Emails transactionnels
- Alertes RH automatiques

**Nouvelles technologies** :
- AWS SES (emails)
- ou SendGrid (alternative)
- Celery (tâches asynchrones)
- Redis (file d'attente)

**Ce qu'on apprend** :
- Envoi d'emails
- Tâches asynchrones
- Files de messages
- Cron jobs avec FastAPI

**Nouveaux fichiers** :
```
├── services/
│   ├── email.py        # Service email
│   └── notifications.py # Gestion notifications
├── tasks/
│   └── celery_app.py   # Configuration Celery
└── templates/
    └── emails/         # Templates HTML emails
```

**Temps d'apprentissage** : 1 semaine

---

#### Demo 9A : Stripe Payments & Subscriptions
**Repository** : `awsbedrock-demo-9a-stripe`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-9a-stripe

**Description** :
- Base de Demo 8 (Notifications)
- **AJOUT** : Système d'abonnements avec Stripe
- Plans tarifaires (Free, Pro, Enterprise)
- Webhooks Stripe
- Gestion de la facturation

**Nouvelles technologies** :
- Stripe Python SDK
- Stripe Webhooks
- Gestion des plans
- Facturation automatique

**Ce qu'on apprend** :
- Intégration Stripe
- Gestion d'abonnements SaaS
- Webhooks de paiement
- Facturation récurrente
- Gestion des essais gratuits
- Upgrade/downgrade de plans

**Nouveaux fichiers** :
```
├── payments/
│   ├── __init__.py
│   ├── stripe_client.py  # Client Stripe
│   ├── plans.py          # Définition des plans
│   └── subscriptions.py  # Gestion abonnements
├── webhooks/
│   └── stripe.py         # Webhooks Stripe
├── models.py             # + Subscription model
└── .env.example          # + STRIPE_SECRET_KEY
```

**Plans tarifaires implémentés** :
```python
PLANS = {
    "free": {
        "price": 0,
        "max_employees": 10,
        "ai_requests_per_month": 100,
        "features": ["basic_features"]
    },
    "pro": {
        "price": 29,  # $/mois
        "max_employees": 100,
        "ai_requests_per_month": 1000,
        "features": ["all_features", "priority_support"]
    },
    "enterprise": {
        "price": 99,  # $/mois
        "max_employees": "unlimited",
        "ai_requests_per_month": "unlimited",
        "features": ["all_features", "dedicated_support", "sla"]
    }
}
```

**Fonctionnalités** :
- Checkout Stripe intégré
- Gestion des webhooks (payment_succeeded, subscription_cancelled, etc.)
- Portail client Stripe (gestion abonnement)
- Quotas par plan
- Facturation automatique

**Temps d'apprentissage** : 1 semaine

---

#### Demo 9B : Exports & Reports
**Repository** : `awsbedrock-demo-9b-exports`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-9b-exports

**Description** :
- Base de Demo 9A (Stripe)
- **AJOUT** : Exports de données
- Génération de rapports
- PDF, Excel, CSV

**Nouvelles technologies** :
- reportlab (PDF)
- openpyxl (Excel)
- pandas (manipulation données)

**Ce qu'on apprend** :
- Génération de PDF
- Export Excel
- Rapports automatiques
- Graphiques dans les PDF

**Nouveaux fichiers** :
```
├── services/
│   ├── exports.py      # Service exports
│   └── reports.py      # Génération rapports
└── templates/
    └── reports/        # Templates rapports
```

**Temps d'apprentissage** : 3-5 jours

---

### Niveau 6 : IA Avancée

#### Demo 10 : RAG + pgvector (Recherche Sémantique)
**Repository** : `awsbedrock-demo-10-rag-pgvector`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-10-rag-pgvector

**Description** :
- Base de Demo 9B (Exports)
- **AJOUT** : RAG (Retrieval Augmented Generation)
- **pgvector** pour PostgreSQL
- Base vectorielle des employés
- Recherche sémantique avancée

**Nouvelles technologies** :
- LangChain
- **pgvector** (extension PostgreSQL)
- Embeddings AWS Bedrock Titan
- Recherche vectorielle dans PostgreSQL

**Ce qu'on apprend** :
- Retrieval Augmented Generation (RAG)
- Bases vectorielles avec **pgvector**
- Embeddings (conversion texte → vecteurs)
- Recherche sémantique (similarité cosinus)
- Combiner SQL classique + recherche vectorielle

**Nouveaux fichiers** :
```
├── ai/
│   ├── embeddings.py      # Génération embeddings
│   ├── vectorstore.py     # Gestion pgvector
│   ├── rag_agent.py       # Agent RAG
│   └── semantic_search.py # Recherche sémantique
├── alembic/versions/
│   └── xxx_add_pgvector.py # Migration pgvector
└── requirements.txt       # + langchain, pgvector
```

**Configuration pgvector** :
```sql
-- Migration pour activer pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- Ajouter colonne vector aux employés
ALTER TABLE employees 
ADD COLUMN embedding vector(1536);

-- Index pour recherche rapide
CREATE INDEX ON employees 
USING ivfflat (embedding vector_cosine_ops);
```

**Exemple d'utilisation** :
```python
# Recherche sémantique d'employés
question = "Qui a de l'expérience en IA et cloud computing?"
results = semantic_search(question, top_k=5)
# Retourne les 5 employés les plus pertinents
```

**Avantages pgvector** :
- ✅ Tout dans PostgreSQL (pas de base séparée)
- ✅ Transactions ACID
- ✅ Recherche vectorielle + SQL classique
- ✅ Performance excellente
- ✅ Gratuit et open-source

**Temps d'apprentissage** : 1-2 semaines

---

#### Demo 11 : Conversation History
**Repository** : `awsbedrock-demo-11-chat-history`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-11-chat-history

**Description** :
- Base de Demo 10 (RAG)
- **AJOUT** : Historique des conversations
- Contexte multi-tours
- Conversations sauvegardées

**Ce qu'on apprend** :
- Gestion de l'historique conversationnel
- Contexte multi-tours
- Personnalisation des réponses

**Nouveaux modèles** :
```python
class Conversation(Base):
    id: int
    user_id: int
    created_at: datetime
    
class Message(Base):
    id: int
    conversation_id: int
    role: str  # user/assistant
    content: str
    timestamp: datetime
```

**Temps d'apprentissage** : 3-5 jours

---

#### Demo 11B : Agentic AI (Multi-Agent System)
**Repository** : `awsbedrock-demo-11b-agentic-ai`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-11b-agentic-ai

**Description** :
- Base de Demo 11 (Chat History)
- **AJOUT** : Système multi-agents IA
- Agents spécialisés qui collaborent
- Orchestration intelligente

**Nouvelles technologies** :
- LangGraph (orchestration d'agents)
- Multiple agents AWS Bedrock
- Function calling
- Agent collaboration

**Ce qu'on apprend** :
- Architecture multi-agents
- Orchestration d'agents IA
- Spécialisation des agents
- Communication inter-agents
- ReAct pattern (Reasoning + Acting)

**Agents implémentés** :
```python
# 1. HR Analyst Agent
- Spécialiste des données RH
- Analyse statistiques employés
- Génération insights RH

# 2. Recruiter Agent
- Recherche de candidats
- Matching compétences/postes
- Recommandations d'embauche

# 3. Compensation Agent
- Analyse des salaires
- Benchmarking de marché
- Recommandations salariales

# 4. Coordinator Agent (Orchestrateur)
- Dispatche les questions aux bons agents
- Agrège les réponses
- Coordination workflow
```

**Architecture** :
```
User Question
     ↓
Coordinator Agent (Router)
     ↓
   /  |  \
  /   |   \
HR  Recruiter  Compensation
Agent  Agent     Agent
  \   |   /
   \  |  /
     ↓
  Aggregated Response
```

**Exemple d'utilisation** :
```python
# Question complexe nécessitant plusieurs agents
question = """
Nous voulons embaucher un développeur senior Python.
Analyser notre équipe actuelle, recommander un salaire 
compétitif, et identifier les gaps de compétences.
"""

# Le Coordinator dispatche à :
# 1. HR Analyst → analyse équipe actuelle
# 2. Recruiter → profil idéal candidat
# 3. Compensation → benchmarking salaire

# Réponse agrégée de tous les agents
```

**Nouveaux fichiers** :
```
├── agents/
│   ├── __init__.py
│   ├── base_agent.py      # Agent de base
│   ├── hr_analyst.py      # Agent RH
│   ├── recruiter.py       # Agent recrutement
│   ├── compensation.py    # Agent salaires
│   └── coordinator.py     # Orchestrateur
├── tools/
│   ├── data_tools.py      # Outils d'accès données
│   └── analysis_tools.py  # Outils d'analyse
└── langgraph_config.py    # Configuration LangGraph
```

**Temps d'apprentissage** : 2 semaines

---

### Niveau 7 : Déploiement et Production

#### Demo 12 : Docker + Docker Compose
**Repository** : `awsbedrock-demo-12-docker`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-11-docker

**Description** :
- Base de Demo 10 (Chat History)
- **AJOUT** : Containerisation Docker
- Docker Compose multi-services
- Environnements dev/prod

**Nouveaux fichiers** :
```
├── Dockerfile
├── docker-compose.yml
├── docker-compose.prod.yml
└── .dockerignore
```

**Ce qu'on apprend** :
- Containerisation
- Docker multi-stage builds
- Docker Compose
- Orchestration de services

**Temps d'apprentissage** : 3-5 jours

---

#### Demo 13 : CI/CD avec GitHub Actions
**Repository** : `awsbedrock-demo-13-cicd`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-12-cicd

**Description** :
- Base de Demo 11 (Docker)
- **AJOUT** : Pipeline CI/CD
- Tests automatiques
- Déploiement automatique

**Nouveaux fichiers** :
```
├── .github/
│   └── workflows/
│       ├── tests.yml
│       ├── build.yml
│       └── deploy.yml
├── tests/
│   ├── test_api.py
│   └── test_models.py
└── pytest.ini
```

**Ce qu'on apprend** :
- Tests automatisés
- GitHub Actions
- CI/CD pipelines
- Déploiement continu

**Temps d'apprentissage** : 1 semaine

---

#### Demo 14 : Déploiement AWS (ECS)
**Repository** : `awsbedrock-demo-14-aws-deployment`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-13-aws-deployment

**Description** :
- Base de Demo 12 (CI/CD)
- **AJOUT** : Déploiement AWS complet
- ECS + Fargate
- RDS, S3, CloudFront

**Fichiers de configuration** :
```
├── infrastructure/
│   ├── terraform/      # Infrastructure as Code
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   └── cloudformation/ # Alternative
└── deploy/
    └── ecs-task-definition.json
```

**Ce qu'on apprend** :
- Infrastructure as Code (Terraform)
- AWS ECS/Fargate
- Load balancing
- Scaling automatique

**Temps d'apprentissage** : 2 semaines

---

#### Demo 15 : Monitoring & Logging
**Repository** : `awsbedrock-demo-15-monitoring`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-14-monitoring

**Description** :
- Base de Demo 13 (AWS)
- **AJOUT** : Monitoring complet
- Logs centralisés
- Alertes et métriques

**Nouvelles technologies** :
- Prometheus + Grafana
- AWS CloudWatch
- Sentry (error tracking)
- Loguru (logging avancé)

**Nouveaux fichiers** :
```
├── monitoring/
│   ├── prometheus.yml
│   └── grafana-dashboard.json
└── logging_config.py
```

**Ce qu'on apprend** :
- Observabilité
- Métriques et KPIs
- Alerting
- Debugging en production

**Temps d'apprentissage** : 1 semaine

---

### Niveau 8 : Fonctionnalités Enterprise

#### Demo 16 : Multi-tenant
**Repository** : `awsbedrock-demo-16-multitenant`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-15-multitenant

**Description** :
- Base de Demo 14 (Monitoring)
- **AJOUT** : Support multi-tenant
- Isolation des données par entreprise
- Sous-domaines personnalisés

**Ce qu'on apprend** :
- Architecture multi-tenant
- Isolation des données
- Gestion de sous-domaines
- Facturation par tenant

**Temps d'apprentissage** : 2 semaines

---

#### Demo 17 : API Publique + Rate Limiting
**Repository** : `awsbedrock-demo-17-public-api`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-16-public-api

**Description** :
- Base de Demo 15 (Multi-tenant)
- **AJOUT** : API publique documentée
- Clés API
- Rate limiting
- Webhooks

**Nouvelles technologies** :
- slowapi (rate limiting)
- API versioning
- Webhooks

**Ce qu'on apprend** :
- API publique
- Gestion de quotas
- Versioning d'API
- Webhooks et intégrations

**Temps d'apprentissage** : 1-2 semaines

---

#### Demo 18A : Documentation Technique Automatique
**Repository** : `awsbedrock-demo-18a-documentation`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-18a-documentation

**Description** :
- Base de Demo 17 (Public API)
- **AJOUT** : Documentation technique automatique
- Docstrings améliorés
- Documentation générée
- README dynamique

**Nouvelles technologies** :
- Sphinx (documentation Python)
- MkDocs Material
- Auto-doc from docstrings
- OpenAPI/Swagger amélioré

**Ce qu'on apprend** :
- Documentation professionnelle
- Docstrings Google/NumPy style
- Génération automatique docs
- Hosting documentation

**Nouveaux fichiers** :
```
├── docs/
│   ├── index.md           # Page d'accueil
│   ├── getting-started.md
│   ├── api-reference.md   # Généré auto
│   ├── examples.md
│   └── deployment.md
├── mkdocs.yml             # Config MkDocs
└── .readthedocs.yml       # Config ReadTheDocs
```

**Documentation générée** :
- API Reference complète
- Exemples de code
- Guides d'intégration
- Architecture diagrams
- Changelog automatique

**Hosting** :
- ReadTheDocs (gratuit)
- GitHub Pages
- Netlify Docs

**Temps d'apprentissage** : 3-5 jours

---

#### Demo 18B : Application Mobile (API)
**Repository** : `awsbedrock-demo-18b-mobile-api`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-18b-mobile-api

**Description** :
- Base de Demo 18A (Documentation)
- **AJOUT** : Endpoints optimisés mobile
- Push notifications
- Offline-first support

**Ce qu'on apprend** :
- API mobile-first
- Push notifications (FCM)
- Optimisation pour mobile
- Gestion offline/online

**Temps d'apprentissage** : 1 semaine

---

### Niveau 9 : Frontend Avancé

#### Demo 19A : UI Component Library (Design System)
**Repository** : `awsbedrock-demo-19a-ui-components`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-19a-ui-components

**Description** :
- Base de Demo 18B (Mobile API)
- **AJOUT** : Bibliothèque de composants UI
- Design system complet
- Storybook pour les composants
- Tailwind avancé

**Nouvelles technologies** :
- Storybook
- Tailwind CSS avancé
- Headless UI
- Framer Motion (animations)

**Ce qu'on apprend** :
- Créer un design system
- Composants réutilisables
- Documentation composants (Storybook)
- Animations fluides
- Responsive design avancé

**Composants créés** :
```
├── components/
│   ├── Button/
│   │   ├── Button.tsx
│   │   ├── Button.stories.tsx
│   │   └── Button.test.tsx
│   ├── Card/
│   ├── Modal/
│   ├── Table/
│   ├── Form/
│   └── Charts/
```

**Design tokens** :
- Couleurs
- Typography
- Spacing
- Shadows
- Animations

**Temps d'apprentissage** : 1-2 semaines

---

#### Demo 19B : React Frontend Complete
**Repository** : `awsbedrock-demo-19b-react-app`  
**URL** : https://github.com/inskillflow/awsbedrock-demo-19b-react-app

**Description** :
- Base de Demo 19A (UI Components)
- **AJOUT** : Application React complète
- Utilise les composants du design system
- State management (Redux)
- React Query pour API

**Nouvelles technologies** :
- React + TypeScript
- Redux Toolkit
- React Query / TanStack Query
- React Router v6

**Structure** :
```
├── frontend/
│   ├── src/
│   │   ├── components/  # Du design system
│   │   ├── features/    # Features (employees, auth, etc.)
│   │   ├── pages/
│   │   ├── store/       # Redux store
│   │   ├── api/         # API client
│   │   └── hooks/       # Custom hooks
│   ├── package.json
│   └── tsconfig.json
```

**Features** :
- Authentication flows
- Employee management
- AI Chat interface
- Dashboard with charts
- Settings & Profile
- Dark mode

**Temps d'apprentissage** : 2-3 semaines

---

## Récapitulatif par Repository

| Demo | Nom Repository | Focus Principal | Temps | Difficulté |
|------|---------------|-----------------|-------|------------|
| 1 | `awsbedrock-demo-1-inmemory` | API + IA en mémoire (mode local) | 1-2 sem | Facile |
| 2 | `awsbedrock-demo-2-aws-bedrock-real` | AWS Bedrock RÉEL configuré | 2-3 j | Moyen |
| 3 | `awsbedrock-demo-3-postgresql` | PostgreSQL + Neon | 1 sem | Moyen |
| 4 | `awsbedrock-demo-4-xata` | Xata moderne | 3-5 j | Moyen |
| 5A | `awsbedrock-demo-5a-auth-clerk` | Clerk Auth (Rapide) | 1 j | Facile |
| 5B | `awsbedrock-demo-5b-auth-jwt-custom` | JWT Auth Custom (Apprentissage) | 1 sem | Avancé |
| 6 | `awsbedrock-demo-6-rbac` | Rôles & Permissions | 3-5 j | Avancé |
| 7 | `awsbedrock-demo-7-files-s3` | Upload fichiers S3 | 1 sem | Avancé |
| 8 | `awsbedrock-demo-8-notifications` | Emails + Notifications | 1 sem | Avancé |
| 9A | `awsbedrock-demo-9a-stripe` | Stripe Abonnements | 1 sem | Avancé |
| 9B | `awsbedrock-demo-9b-exports` | Exports PDF/Excel | 3-5 j | Moyen |
| 10 | `awsbedrock-demo-10-rag-pgvector` | RAG + pgvector | 1-2 sem | Expert |
| 11 | `awsbedrock-demo-11-chat-history` | Historique conversations | 3-5 j | Avancé |
| 11B | `awsbedrock-demo-11b-agentic-ai` | Agentic AI (Multi-Agent) | 2 sem | Expert |
| 12 | `awsbedrock-demo-12-docker` | Docker + Compose | 3-5 j | Avancé |
| 13 | `awsbedrock-demo-13-cicd` | CI/CD GitHub Actions | 1 sem | Avancé |
| 14 | `awsbedrock-demo-14-aws-deployment` | Déploiement AWS Final | 2 sem | Expert |
| 15 | `awsbedrock-demo-15-monitoring` | Monitoring complet | 1 sem | Avancé |
| 16 | `awsbedrock-demo-16-multitenant` | Multi-tenant | 2 sem | Expert |
| 17 | `awsbedrock-demo-17-public-api` | API publique | 1-2 sem | Avancé |
| 18A | `awsbedrock-demo-18a-documentation` | Documentation Technique | 3-5 j | Moyen |
| 18B | `awsbedrock-demo-18b-mobile-api` | API mobile | 1 sem | Avancé |
| 19A | `awsbedrock-demo-19a-ui-components` | UI Design System | 1-2 sem | Avancé |
| 19B | `awsbedrock-demo-19b-react-app` | Frontend React Complete | 2-3 sem | Expert |

**Temps total estimé** : 8-12 mois pour tout compléter (22 demos + variations)

---

## Parcours d'Apprentissage Suggérés

### Parcours 1 : Développeur Backend (3-4 mois)
1. Demo 1 - Fondations (mode local)
2. **Demo 2 - AWS Bedrock RÉEL** (Important)
3. Demo 3 - PostgreSQL
4. **Demo 5A - Clerk Auth** (rapide) OU **Demo 5B - JWT Custom** (apprentissage)
5. Demo 6 - RBAC
6. Demo 7 - Files S3
7. Demo 12 - Docker
8. Demo 13 - CI/CD

### Parcours 2 : Développeur Full Stack (5-6 mois)
1. Demo 1 - Fondations
2. **Demo 2 - AWS Bedrock RÉEL** (Important)
3. Demo 3 - PostgreSQL
4. **Demo 5A - Clerk Auth** (recommandé pour vitesse)
5. Demo 7 - Files S3
6. Demo 9 - Exports
7. Demo 12 - Docker
8. Demo 19 - React Frontend

### Parcours 3 : IA & Data Engineer (4-5 mois)
1. Demo 1 - Fondations
2. **Demo 2 - AWS Bedrock RÉEL** (Important)
3. Demo 3 - PostgreSQL
4. Demo 10 - RAG
5. Demo 11 - Chat History
6. Demo 9 - Exports & Reports
7. Demo 15 - Monitoring

### Parcours 4 : DevOps Engineer (3-4 mois)
1. Demo 1 - Fondations
2. **Demo 2 - AWS Bedrock RÉEL** (Important)
3. Demo 3 - PostgreSQL
4. Demo 12 - Docker
5. Demo 13 - CI/CD
6. Demo 14 - AWS Deployment
7. Demo 15 - Monitoring

### Parcours 5 : SaaS Entrepreneur (6-9 mois complet)
Recommandation : Utilisez **Demo 5A (Clerk)** pour aller vite en production.

Demos essentiels dans l'ordre :
1. Demo 1 - Fondations
2. **Demo 2 - AWS Bedrock RÉEL**
3. Demo 3 - PostgreSQL
4. **Demo 5A - Clerk Auth** (plus rapide)
5. Demo 6 - RBAC
6. Demo 7 - Files S3
7. Demo 8 - Notifications
8. Demo 12 - Docker
9. Demo 13 - CI/CD
10. Demo 14 - AWS Deployment
11. Demo 15 - Monitoring
12. Demo 16 - Multi-tenant
13. Demo 17 - API publique

---

## Convention de Nommage des Repositories

### Format Standard
```
awsbedrock-demo-[NUMERO]-[FEATURE-PRINCIPALE]
```

### Règles de Nommage
1. **Préfixe** : `awsbedrock-demo-`
2. **Numéro** : Ordre séquentiel (1, 2, 3...)
3. **Feature** : Nom descriptif en kebab-case
4. **Langue** : Anglais pour compatibilité internationale

### Exemples
- ✅ `awsbedrock-demo-1-inmemory`
- ✅ `awsbedrock-demo-2-postgresql`
- ✅ `awsbedrock-demo-9-rag`
- ❌ `demo-aws` (trop vague)
- ❌ `awsbedrock_demo_1` (underscores)
- ❌ `awsbedrock-demo-SQL` (pas de numéro)

---

## Structure des README pour Chaque Demo

Chaque repository doit contenir un README avec :

### 1. Badge de Version
```markdown
![Version](https://img.shields.io/badge/demo-1-blue)
![Difficulty](https://img.shields.io/badge/difficulty-easy-green)
```

### 2. Titre et Description
```markdown
# Demo 1 : Système RH avec IA (En Mémoire)

Première version du système de gestion des employés avec API REST et IA AWS Bedrock.
**Caractéristique principale** : Données en mémoire (non persistantes)
```

### 3. Nouveautés de cette Version
```markdown
## Nouveautés dans Demo 1

- ✨ API REST FastAPI complète
- ✨ Interface web moderne
- ✨ Agent IA AWS Bedrock
- ✨ Mode local fallback
```

### 4. Prérequis
```markdown
## Prérequis

- Python 3.11+
- Compte AWS (optionnel)
- Voir Demo 0 si premier projet
```

### 5. Lien vers Versions
```markdown
## Versions

- ⬅️ **Précédent** : Aucun (première version)
- ➡️ **Suivant** : [Demo 2 - PostgreSQL](../awsbedrock-demo-2-postgresql)
- 📚 **Tous les demos** : [Plan de formation](../ROADMAP.md)
```

---

## Checklist pour Créer un Nouveau Demo

Avant de publier un nouveau demo :

- [ ] Repository créé avec nom correct
- [ ] README complet avec badges
- [ ] Documentation à jour dans `/documentation`
- [ ] Fichier `.env.example` présent
- [ ] `requirements.txt` à jour
- [ ] Tests ajoutés (à partir de Demo 12)
- [ ] Dockerfile mis à jour (à partir de Demo 11)
- [ ] Lien vers demo précédent et suivant
- [ ] Changelog documenté
- [ ] Temps d'apprentissage estimé
- [ ] Niveau de difficulté indiqué

---

## Contribution et Feedback

Chaque demo est un projet d'apprentissage. N'hésitez pas à :
- Poser des questions via GitHub Issues
- Proposer des améliorations
- Partager vos réalisations
- Signaler des bugs

---

## Ressources Complémentaires

### Pour Commencer
- [Documentation Demo 1](../02-PREREQUISITES_ET_INSTALLATION.md)
- [Guide d'utilisation](../01-GUIDE_UTILISATION.md)
- [Technologies utilisées](../03-TECHNOLOGIES_ET_EVOLUTIONS.md)

### Apprentissage
- FastAPI : https://fastapi.tiangolo.com/
- SQLAlchemy : https://docs.sqlalchemy.org/
- AWS Bedrock : https://aws.amazon.com/bedrock/
- Neon : https://neon.tech/docs
- Xata : https://xata.io/docs

### Communauté
- Discord : [Lien vers Discord communauté]
- GitHub Discussions : [Lien vers Discussions]
- Stack Overflow : Tag `awsbedrock-demo`

---

**Bon apprentissage progressif ! 🚀**

Commencez par Demo 1, maîtrisez-le, puis passez au suivant à votre rythme.

