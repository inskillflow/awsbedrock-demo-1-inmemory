# Technologies à Apprendre - Ordre pour Débutants

Ce document liste TOUTES les technologies nécessaires dans l'ordre d'apprentissage, du plus basique au plus avancé.

---

## Phase 1 : Fondamentaux Web (2-3 semaines)

### 1. HTML5
- Balises de base (div, p, h1-h6, a, img)
- Formulaires (input, select, textarea, button)
- Structure sémantique (header, nav, main, footer, section, article)
- Attributs (id, class, data-*)

### 2. CSS3
- Sélecteurs (classe, id, élément, pseudo-classes)
- Box model (margin, padding, border)
- Display (block, inline, inline-block, none)
- Position (static, relative, absolute, fixed, sticky)
- Flexbox
- Grid
- Media queries (responsive)
- Transitions et animations

### 3. JavaScript Vanilla (Bases)
- Variables (let, const, var)
- Types de données (string, number, boolean, array, object)
- Opérateurs (+, -, *, /, %, ==, ===, !=, !==)
- Conditions (if, else, else if, switch)
- Boucles (for, while, forEach)
- Fonctions (function, arrow functions)
- DOM manipulation (querySelector, getElementById, addEventListener)
- Events (click, submit, change, input)
- Promises et async/await (bases)

---

## Phase 2 : Outils Modernes Frontend (1-2 semaines)

### 4. Tailwind CSS
- Classes utilitaires
- Responsive design (sm, md, lg, xl)
- Flexbox et Grid avec Tailwind
- Personnalisation (colors, spacing)
- Dark mode

### 5. Axios
- Requêtes HTTP (GET, POST, PUT, DELETE)
- Headers
- Gestion des erreurs (try/catch)
- Interceptors (optionnel pour débutants)

### 6. Fetch API (alternative à Axios)
- fetch() basique
- .then() et .catch()
- async/await avec fetch
- JSON.parse() et JSON.stringify()

---

## Phase 3 : Backend Python (3-4 semaines)

### 7. Python Bases
- Variables et types (str, int, float, bool, list, dict, tuple)
- Conditions (if, elif, else)
- Boucles (for, while)
- Fonctions (def, return, paramètres)
- List comprehensions
- Gestion des erreurs (try, except, finally)
- Modules et imports

### 8. Python Avancé (pour FastAPI)
- Classes et objets (class, __init__, self)
- Héritage
- Décorateurs (@)
- Type hints (str, int, List, Dict, Optional)
- Async/await en Python
- Context managers (with)

### 9. FastAPI
- Installation (pip install fastapi uvicorn)
- Routes de base (@app.get, @app.post, @app.put, @app.delete)
- Path parameters (/users/{id})
- Query parameters (?name=John&age=25)
- Request body (Pydantic models)
- Response models
- Status codes (200, 201, 404, 500)
- CORS (pour permettre frontend)
- Documentation automatique (/docs, /redoc)

### 10. Pydantic
- BaseModel
- Field validation
- Type hints
- Optional et Union
- Config

### 11. Uvicorn
- Lancer un serveur (uvicorn main:app --reload)
- Port et host
- Mode reload (développement)

---

## Phase 4 : Base de Données (2-3 semaines)

### 12. SQL Bases
- CREATE TABLE
- INSERT INTO
- SELECT (WHERE, ORDER BY, LIMIT)
- UPDATE
- DELETE
- JOIN (INNER, LEFT, RIGHT)
- Clés primaires et étrangères
- Index

### 13. PostgreSQL
- Installation
- psql (ligne de commande)
- Création de database
- Types de données PostgreSQL
- pgAdmin (optionnel)

### 14. SQLAlchemy (ORM)
- Engine et Session
- declarative_base()
- Models (Column, Integer, String, Float, DateTime)
- Relationships (ForeignKey, relationship())
- Queries (filter, filter_by, first, all)
- Create, Read, Update, Delete avec ORM

### 15. Alembic (Migrations)
- alembic init
- alembic revision --autogenerate
- alembic upgrade head
- alembic downgrade

---

## Phase 5 : Cloud et Services (2-3 semaines)

### 16. AWS Bases
- Créer un compte AWS
- Console AWS
- Régions
- IAM (Identity and Access Management)
- Utilisateurs et permissions
- Access keys et secret keys

### 17. AWS CLI
- Installation
- aws configure
- Commandes de base

### 18. Boto3 (SDK AWS Python)
- Installation (pip install boto3)
- Client vs Resource
- Configuration credentials
- Appels API AWS

### 19. AWS Bedrock
- Qu'est-ce que Bedrock
- Model access
- Modèles disponibles (Claude 3, Titan)
- invoke_model()
- Prompts et réponses
- Coûts

### 20. Neon.tech (PostgreSQL Serverless)
- Créer un compte
- Créer un projet
- Connection string
- Branching

---

## Phase 6 : Authentification et Sécurité (2-3 semaines)

### 21. JWT (JSON Web Tokens)
- Qu'est-ce qu'un JWT
- Structure (header.payload.signature)
- Création de tokens
- Vérification de tokens
- Expiration

### 22. Bcrypt / Passlib
- Hachage de mots de passe
- Vérification de mots de passe
- Salt

### 23. OAuth2
- Qu'est-ce qu'OAuth2
- Flow password
- Bearer tokens
- Refresh tokens

### 24. Clerk (Service Auth)
- Créer un compte Clerk
- Intégration frontend
- Intégration backend
- Webhooks

---

## Phase 7 : Fonctionnalités Avancées (3-4 semaines)

### 25. AWS S3
- Buckets
- Upload de fichiers
- Download de fichiers
- Permissions (ACL, Bucket Policy)
- Pre-signed URLs

### 26. AWS SES (Simple Email Service)
- Configuration
- Vérification domaine/email
- Envoi d'emails
- Templates

### 27. Stripe
- Créer un compte Stripe
- API keys (test vs production)
- Customers
- Products et Prices
- Subscriptions
- Webhooks
- Stripe CLI

### 28. Celery (Tâches Asynchrones)
- Installation
- Configuration
- Définir des tasks
- Lancer worker
- Redis comme broker

### 29. Redis
- Installation
- Commandes de base (SET, GET, DEL)
- Expiration (TTL)
- Cache

---

## Phase 8 : IA Avancée (3-4 semaines)

### 30. LangChain
- Installation
- Chains
- Prompts templates
- Memory
- Agents (optionnel)

### 31. pgvector
- Extension PostgreSQL
- Installation
- Création de colonnes vector
- Index HNSW ou IVFFlat
- Recherche de similarité

### 32. Embeddings
- Qu'est-ce qu'un embedding
- Modèles d'embeddings (Titan, OpenAI)
- Créer des embeddings
- Stocker dans pgvector

### 33. RAG (Retrieval Augmented Generation)
- Concept RAG
- Vector store
- Retriever
- Combiner retrieval + LLM

### 34. LangGraph (Optionnel Avancé)
- Multi-agent systems
- State management
- Workflows

---

## Phase 9 : Exports et Reports (1-2 semaines)

### 35. Pandas
- DataFrames
- Read CSV, Excel
- Manipulation de données
- Groupby, merge, join

### 36. ReportLab (PDF)
- Création de PDF
- Canvas
- Paragraphes et styles
- Tables
- Images dans PDF

### 37. OpenPyXL (Excel)
- Création de fichiers Excel
- Worksheets
- Styles
- Formules

---

## Phase 10 : DevOps et Déploiement (3-4 semaines)

### 38. Git
- git init, clone
- git add, commit, push, pull
- git branch, checkout, merge
- .gitignore
- Résolution de conflits

### 39. GitHub
- Créer un repository
- Push vers GitHub
- Pull requests
- Issues
- README.md

### 40. Docker
- Qu'est-ce que Docker
- Images vs Containers
- Dockerfile
- docker build
- docker run
- docker ps, logs, stop
- Volumes
- Networks

### 41. Docker Compose
- docker-compose.yml
- Services
- depends_on
- Environnement variables
- docker-compose up/down

### 42. GitHub Actions
- Workflows (.github/workflows/)
- Triggers (push, pull_request)
- Jobs et steps
- Actions marketplace
- Secrets

---

## Phase 11 : Monitoring et Logs (2-3 semaines)

### 43. Logging Python
- logging module
- Niveaux (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Handlers (FileHandler, StreamHandler)
- Formatters

### 44. Loguru (Alternative)
- Installation
- logger.info(), logger.error()
- Rotation de fichiers

### 45. AWS CloudWatch
- Logs
- Metrics
- Alarms
- Dashboards

### 46. Sentry
- Créer un compte
- Intégration Python
- Error tracking
- Performance monitoring

### 47. Prometheus
- Qu'est-ce que Prometheus
- Metrics
- Exporters
- PromQL

### 48. Grafana
- Installation
- Data sources
- Dashboards
- Panels et graphiques

---

## Phase 12 : Frontend Avancé (4-6 semaines)

### 49. Node.js et npm
- Installation
- npm init
- package.json
- npm install
- node_modules

### 50. React Bases
- create-react-app
- Components (function components)
- JSX
- Props
- State (useState)
- Events

### 51. React Hooks
- useState
- useEffect
- useContext
- useRef
- useMemo, useCallback

### 52. React Router
- BrowserRouter
- Routes et Route
- Link et NavLink
- useNavigate
- useParams

### 53. TypeScript
- Types de base (string, number, boolean)
- Interfaces
- Types
- Generics
- tsconfig.json

### 54. Redux Toolkit
- Store
- Slices
- Reducers
- Actions
- useSelector, useDispatch

### 55. React Query (TanStack Query)
- useQuery
- useMutation
- Cache
- Invalidation

### 56. Storybook
- Installation
- Stories
- Args
- Controls
- Documentation

### 57. Framer Motion
- Installation
- motion components
- Animations
- Transitions
- Variants

---

## Phase 13 : Tests (2-3 semaines - Optionnel)

### 58. Pytest
- Installation
- Tests basiques
- Fixtures
- Mocks
- Coverage

### 59. Jest (JavaScript)
- Installation
- Test suites
- Matchers
- Mocks

### 60. React Testing Library
- render
- screen
- fireEvent
- waitFor

---

## Phase 14 : Architecture Avancée (3-4 semaines - Optionnel)

### 61. REST API Design
- Ressources
- Verbes HTTP
- Status codes
- Versioning
- Pagination

### 62. Microservices
- Architecture microservices
- Service discovery
- API Gateway
- Communication inter-services

### 63. Message Queues
- RabbitMQ
- AWS SQS
- Event-driven architecture

### 64. GraphQL (Alternative REST)
- Queries
- Mutations
- Schema
- Resolvers

---

## Phase 15 : Sécurité (1-2 semaines)

### 65. HTTPS / TLS
- Certificats SSL
- Let's Encrypt
- HTTPS vs HTTP

### 66. CORS
- Qu'est-ce que CORS
- Configuration CORS
- Preflight requests

### 67. Rate Limiting
- slowapi
- Limite par IP
- Limite par utilisateur

### 68. SQL Injection Prevention
- Parameterized queries
- ORM sécurisé
- Input validation

### 69. XSS Prevention
- Escape HTML
- Content Security Policy
- Input sanitization

---

## Récapitulatif par Catégorie

### Frontend (12 technologies)
1. HTML5
2. CSS3
3. JavaScript Vanilla
4. Tailwind CSS
5. Axios / Fetch
6. React
7. React Hooks
8. React Router
9. TypeScript
10. Redux Toolkit
11. React Query
12. Storybook

### Backend (15 technologies)
13. Python Bases
14. Python Avancé
15. FastAPI
16. Pydantic
17. Uvicorn
18. SQL
19. PostgreSQL
20. SQLAlchemy
21. Alembic
22. JWT
23. Bcrypt/Passlib
24. OAuth2
25. Celery
26. Redis
27. LangChain

### Cloud AWS (7 technologies)
28. AWS Bases
29. AWS CLI
30. Boto3
31. AWS Bedrock
32. AWS S3
33. AWS SES
34. AWS CloudWatch

### Base de Données (5 technologies)
35. SQL
36. PostgreSQL
37. SQLAlchemy
38. Alembic
39. pgvector

### IA (6 technologies)
40. AWS Bedrock
41. LangChain
42. pgvector
43. Embeddings
44. RAG
45. LangGraph

### DevOps (7 technologies)
46. Git
47. GitHub
48. Docker
49. Docker Compose
50. GitHub Actions
51. AWS ECS
52. Terraform (optionnel)

### Monitoring (6 technologies)
53. Logging Python
54. Loguru
55. CloudWatch
56. Sentry
57. Prometheus
58. Grafana

### Payments & Services (5 technologies)
59. Stripe
60. Clerk
61. Neon.tech
62. SendGrid/AWS SES
63. Xata (optionnel)

---

## Ordre d'Apprentissage Recommandé pour DÉBUTANTS

### Mois 1-2 : Web Bases
1. HTML5 (1 semaine)
2. CSS3 (2 semaines)
3. JavaScript Vanilla (3 semaines)
4. Tailwind CSS (1 semaine)
5. Axios (2 jours)

### Mois 3-4 : Backend Python
6. Python Bases (2 semaines)
7. Python Avancé (2 semaines)
8. FastAPI (3 semaines)
9. Pydantic (3 jours)
10. Uvicorn (1 jour)

### Mois 5 : Base de Données
11. SQL Bases (1 semaine)
12. PostgreSQL (1 semaine)
13. SQLAlchemy (1 semaine)
14. Alembic (3 jours)

### Mois 6 : Cloud AWS
15. AWS Bases (1 semaine)
16. AWS CLI (2 jours)
17. Boto3 (1 semaine)
18. AWS Bedrock (1 semaine)

### Mois 7 : Authentification
19. JWT (1 semaine)
20. Bcrypt (2 jours)
21. OAuth2 (1 semaine)
22. Clerk (2 jours)

### Mois 8 : Features Avancées
23. AWS S3 (1 semaine)
24. AWS SES (3 jours)
25. Stripe (1 semaine)
26. Exports (PDF/Excel) (1 semaine)

### Mois 9 : IA Avancée
27. LangChain (1 semaine)
28. pgvector (1 semaine)
29. Embeddings (3 jours)
30. RAG (1 semaine)

### Mois 10 : DevOps
31. Git (1 semaine)
32. Docker (2 semaines)
33. Docker Compose (3 jours)
34. GitHub Actions (1 semaine)

### Mois 11 : Monitoring
35. Logging (3 jours)
36. CloudWatch (1 semaine)
37. Sentry (3 jours)
38. Prometheus + Grafana (1 semaine)

### Mois 12 : Frontend Avancé
39. React Bases (2 semaines)
40. React Hooks (1 semaine)
41. React Router (3 jours)
42. TypeScript (1 semaine)

---

## Temps Total Estimé

- **Minimum (MVP)** : 6 mois (technologies essentielles)
- **Complet (Full Stack)** : 12 mois (toutes technologies)
- **Expert** : 18-24 mois (avec projets réels)

---

## Ressources d'Apprentissage

### Frontend
- MDN Web Docs (HTML/CSS/JS)
- freeCodeCamp
- Tailwind CSS docs
- React docs officielle

### Backend
- Python.org tutorial
- FastAPI documentation
- Real Python (articles)

### Cloud
- AWS Free Tier
- AWS Training (gratuit)
- AWS Documentation

### Base de Données
- PostgreSQL Tutorial
- SQLAlchemy docs
- W3Schools SQL

### Général
- YouTube (Traversy Media, The Net Ninja, Corey Schafer)
- Udemy (cours payants)
- Codecademy
- Coursera
- freeCodeCamp

---

**Note** : Cette liste suit exactement l'ordre du projet awsbedrock-demo de Demo 1 à Demo 19B.

Pour chaque technologie, consacrer au minimum :
- **Débutant** : 1 semaine
- **Intermédiaire** : 3-5 jours
- **Avancé** : 2-3 jours

**Total** : 69 technologies listées

