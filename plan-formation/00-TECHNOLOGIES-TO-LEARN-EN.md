# Technologies to Learn - Order for Beginners

This document lists ALL necessary technologies in learning order, from most basic to most advanced.

---

## Phase 1: Web Fundamentals (2-3 weeks)

### 1. HTML5
- Basic tags (div, p, h1-h6, a, img)
- Forms (input, select, textarea, button)
- Semantic structure (header, nav, main, footer, section, article)
- Attributes (id, class, data-*)

### 2. CSS3
- Selectors (class, id, element, pseudo-classes)
- Box model (margin, padding, border)
- Display (block, inline, inline-block, none)
- Position (static, relative, absolute, fixed, sticky)
- Flexbox
- Grid
- Media queries (responsive)
- Transitions and animations

### 3. Vanilla JavaScript (Basics)
- Variables (let, const, var)
- Data types (string, number, boolean, array, object)
- Operators (+, -, *, /, %, ==, ===, !=, !==)
- Conditions (if, else, else if, switch)
- Loops (for, while, forEach)
- Functions (function, arrow functions)
- DOM manipulation (querySelector, getElementById, addEventListener)
- Events (click, submit, change, input)
- Promises and async/await (basics)

---

## Phase 2: Modern Frontend Tools (1-2 weeks)

### 4. Tailwind CSS
- Utility classes
- Responsive design (sm, md, lg, xl)
- Flexbox and Grid with Tailwind
- Customization (colors, spacing)
- Dark mode

### 5. Axios
- HTTP requests (GET, POST, PUT, DELETE)
- Headers
- Error handling (try/catch)
- Interceptors (optional for beginners)

### 6. Fetch API (alternative to Axios)
- Basic fetch()
- .then() and .catch()
- async/await with fetch
- JSON.parse() and JSON.stringify()

---

## Phase 3: Python Backend (3-4 weeks)

### 7. Python Basics
- Variables and types (str, int, float, bool, list, dict, tuple)
- Conditions (if, elif, else)
- Loops (for, while)
- Functions (def, return, parameters)
- List comprehensions
- Error handling (try, except, finally)
- Modules and imports

### 8. Advanced Python (for FastAPI)
- Classes and objects (class, __init__, self)
- Inheritance
- Decorators (@)
- Type hints (str, int, List, Dict, Optional)
- Async/await in Python
- Context managers (with)

### 9. FastAPI
- Installation (pip install fastapi uvicorn)
- Basic routes (@app.get, @app.post, @app.put, @app.delete)
- Path parameters (/users/{id})
- Query parameters (?name=John&age=25)
- Request body (Pydantic models)
- Response models
- Status codes (200, 201, 404, 500)
- CORS (to allow frontend)
- Automatic documentation (/docs, /redoc)

### 10. Pydantic
- BaseModel
- Field validation
- Type hints
- Optional and Union
- Config

### 11. Uvicorn
- Start server (uvicorn main:app --reload)
- Port and host
- Reload mode (development)

---

## Phase 4: Database (2-3 weeks)

### 12. SQL Basics
- CREATE TABLE
- INSERT INTO
- SELECT (WHERE, ORDER BY, LIMIT)
- UPDATE
- DELETE
- JOIN (INNER, LEFT, RIGHT)
- Primary and foreign keys
- Indexes

### 13. PostgreSQL
- Installation
- psql (command line)
- Database creation
- PostgreSQL data types
- pgAdmin (optional)

### 14. SQLAlchemy (ORM)
- Engine and Session
- declarative_base()
- Models (Column, Integer, String, Float, DateTime)
- Relationships (ForeignKey, relationship())
- Queries (filter, filter_by, first, all)
- Create, Read, Update, Delete with ORM

### 15. Alembic (Migrations)
- alembic init
- alembic revision --autogenerate
- alembic upgrade head
- alembic downgrade

---

## Phase 5: Cloud and Services (2-3 weeks)

### 16. AWS Basics
- Create AWS account
- AWS Console
- Regions
- IAM (Identity and Access Management)
- Users and permissions
- Access keys and secret keys

### 17. AWS CLI
- Installation
- aws configure
- Basic commands

### 18. Boto3 (AWS Python SDK)
- Installation (pip install boto3)
- Client vs Resource
- Credential configuration
- AWS API calls

### 19. AWS Bedrock
- What is Bedrock
- Model access
- Available models (Claude 3, Titan)
- invoke_model()
- Prompts and responses
- Costs

### 20. Neon.tech (Serverless PostgreSQL)
- Create account
- Create project
- Connection string
- Branching

---

## Phase 6: Authentication and Security (2-3 weeks)

### 21. JWT (JSON Web Tokens)
- What is a JWT
- Structure (header.payload.signature)
- Token creation
- Token verification
- Expiration

### 22. Bcrypt / Passlib
- Password hashing
- Password verification
- Salt

### 23. OAuth2
- What is OAuth2
- Password flow
- Bearer tokens
- Refresh tokens

### 24. Clerk (Auth Service)
- Create Clerk account
- Frontend integration
- Backend integration
- Webhooks

---

## Phase 7: Advanced Features (3-4 weeks)

### 25. AWS S3
- Buckets
- File upload
- File download
- Permissions (ACL, Bucket Policy)
- Pre-signed URLs

### 26. AWS SES (Simple Email Service)
- Configuration
- Domain/email verification
- Sending emails
- Templates

### 27. Stripe
- Create Stripe account
- API keys (test vs production)
- Customers
- Products and Prices
- Subscriptions
- Webhooks
- Stripe CLI

### 28. Celery (Asynchronous Tasks)
- Installation
- Configuration
- Define tasks
- Start worker
- Redis as broker

### 29. Redis
- Installation
- Basic commands (SET, GET, DEL)
- Expiration (TTL)
- Cache

---

## Phase 8: Advanced AI (3-4 weeks)

### 30. LangChain
- Installation
- Chains
- Prompt templates
- Memory
- Agents (optional)

### 31. pgvector
- PostgreSQL extension
- Installation
- Create vector columns
- HNSW or IVFFlat index
- Similarity search

### 32. Embeddings
- What is an embedding
- Embedding models (Titan, OpenAI)
- Create embeddings
- Store in pgvector

### 33. RAG (Retrieval Augmented Generation)
- RAG concept
- Vector store
- Retriever
- Combine retrieval + LLM

### 34. LangGraph (Optional Advanced)
- Multi-agent systems
- State management
- Workflows

---

## Phase 9: Exports and Reports (1-2 weeks)

### 35. Pandas
- DataFrames
- Read CSV, Excel
- Data manipulation
- Groupby, merge, join

### 36. ReportLab (PDF)
- PDF creation
- Canvas
- Paragraphs and styles
- Tables
- Images in PDF

### 37. OpenPyXL (Excel)
- Create Excel files
- Worksheets
- Styles
- Formulas

---

## Phase 10: DevOps and Deployment (3-4 weeks)

### 38. Git
- git init, clone
- git add, commit, push, pull
- git branch, checkout, merge
- .gitignore
- Conflict resolution

### 39. GitHub
- Create repository
- Push to GitHub
- Pull requests
- Issues
- README.md

### 40. Docker
- What is Docker
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
- Environment variables
- docker-compose up/down

### 42. GitHub Actions
- Workflows (.github/workflows/)
- Triggers (push, pull_request)
- Jobs and steps
- Actions marketplace
- Secrets

---

## Phase 11: Monitoring and Logs (2-3 weeks)

### 43. Python Logging
- logging module
- Levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Handlers (FileHandler, StreamHandler)
- Formatters

### 44. Loguru (Alternative)
- Installation
- logger.info(), logger.error()
- File rotation

### 45. AWS CloudWatch
- Logs
- Metrics
- Alarms
- Dashboards

### 46. Sentry
- Create account
- Python integration
- Error tracking
- Performance monitoring

### 47. Prometheus
- What is Prometheus
- Metrics
- Exporters
- PromQL

### 48. Grafana
- Installation
- Data sources
- Dashboards
- Panels and charts

---

## Phase 12: Advanced Frontend (4-6 weeks)

### 49. Node.js and npm
- Installation
- npm init
- package.json
- npm install
- node_modules

### 50. React Basics
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
- Routes and Route
- Link and NavLink
- useNavigate
- useParams

### 53. TypeScript
- Basic types (string, number, boolean)
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

## Phase 13: Testing (2-3 weeks - Optional)

### 58. Pytest
- Installation
- Basic tests
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

## Phase 14: Advanced Architecture (3-4 weeks - Optional)

### 61. REST API Design
- Resources
- HTTP verbs
- Status codes
- Versioning
- Pagination

### 62. Microservices
- Microservices architecture
- Service discovery
- API Gateway
- Inter-service communication

### 63. Message Queues
- RabbitMQ
- AWS SQS
- Event-driven architecture

### 64. GraphQL (REST Alternative)
- Queries
- Mutations
- Schema
- Resolvers

---

## Phase 15: Security (1-2 weeks)

### 65. HTTPS / TLS
- SSL Certificates
- Let's Encrypt
- HTTPS vs HTTP

### 66. CORS
- What is CORS
- CORS configuration
- Preflight requests

### 67. Rate Limiting
- slowapi
- Rate limit by IP
- Rate limit by user

### 68. SQL Injection Prevention
- Parameterized queries
- Secure ORM
- Input validation

### 69. XSS Prevention
- HTML escape
- Content Security Policy
- Input sanitization

---

## Summary by Category

### Frontend (12 technologies)
1. HTML5
2. CSS3
3. Vanilla JavaScript
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
13. Python Basics
14. Advanced Python
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

### AWS Cloud (7 technologies)
28. AWS Basics
29. AWS CLI
30. Boto3
31. AWS Bedrock
32. AWS S3
33. AWS SES
34. AWS CloudWatch

### Database (5 technologies)
35. SQL
36. PostgreSQL
37. SQLAlchemy
38. Alembic
39. pgvector

### AI (6 technologies)
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
52. Terraform (optional)

### Monitoring (6 technologies)
53. Python Logging
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
63. Xata (optional)

---

## Recommended Learning Order for BEGINNERS

### Months 1-2: Web Basics
1. HTML5 (1 week)
2. CSS3 (2 weeks)
3. Vanilla JavaScript (3 weeks)
4. Tailwind CSS (1 week)
5. Axios (2 days)

### Months 3-4: Python Backend
6. Python Basics (2 weeks)
7. Advanced Python (2 weeks)
8. FastAPI (3 weeks)
9. Pydantic (3 days)
10. Uvicorn (1 day)

### Month 5: Database
11. SQL Basics (1 week)
12. PostgreSQL (1 week)
13. SQLAlchemy (1 week)
14. Alembic (3 days)

### Month 6: AWS Cloud
15. AWS Basics (1 week)
16. AWS CLI (2 days)
17. Boto3 (1 week)
18. AWS Bedrock (1 week)

### Month 7: Authentication
19. JWT (1 week)
20. Bcrypt (2 days)
21. OAuth2 (1 week)
22. Clerk (2 days)

### Month 8: Advanced Features
23. AWS S3 (1 week)
24. AWS SES (3 days)
25. Stripe (1 week)
26. Exports (PDF/Excel) (1 week)

### Month 9: Advanced AI
27. LangChain (1 week)
28. pgvector (1 week)
29. Embeddings (3 days)
30. RAG (1 week)

### Month 10: DevOps
31. Git (1 week)
32. Docker (2 weeks)
33. Docker Compose (3 days)
34. GitHub Actions (1 week)

### Month 11: Monitoring
35. Logging (3 days)
36. CloudWatch (1 week)
37. Sentry (3 days)
38. Prometheus + Grafana (1 week)

### Month 12: Advanced Frontend
39. React Basics (2 weeks)
40. React Hooks (1 week)
41. React Router (3 days)
42. TypeScript (1 week)

---

## Total Estimated Time

- **Minimum (MVP)**: 6 months (essential technologies)
- **Complete (Full Stack)**: 12 months (all technologies)
- **Expert**: 18-24 months (with real projects)

---

## Learning Resources

### Frontend
- MDN Web Docs (HTML/CSS/JS)
- freeCodeCamp
- Tailwind CSS docs
- Official React docs

### Backend
- Python.org tutorial
- FastAPI documentation
- Real Python (articles)

### Cloud
- AWS Free Tier
- AWS Training (free)
- AWS Documentation

### Database
- PostgreSQL Tutorial
- SQLAlchemy docs
- W3Schools SQL

### General
- YouTube (Traversy Media, The Net Ninja, Corey Schafer)
- Udemy (paid courses)
- Codecademy
- Coursera
- freeCodeCamp

---

**Note**: This list follows exactly the order of the awsbedrock-demo project from Demo 1 to Demo 19B.

For each technology, spend at minimum:
- **Beginner**: 1 week
- **Intermediate**: 3-5 days
- **Advanced**: 2-3 days

**Total**: 69 technologies listed

