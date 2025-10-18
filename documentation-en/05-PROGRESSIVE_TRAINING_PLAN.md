# Progressive Training Plan - HR System with AI

This document presents a progressive learning approach to build a complete employee management system. Each step adds a new layer of complexity and corresponds to a distinct GitHub repository.

---

## Learning Philosophy

Instead of building everything at once, we proceed by **successive layers**. Each version:
- Adds ONE new major technology or feature
- Is autonomous and functional
- Can be deployed independently
- Serves as a base for the next version

**Advantage**: Progressive learning, easier debugging, deep understanding.

---

## Version Roadmap

### Level 1: Foundations

#### Demo 1: In-Memory (CURRENT)
**Repository**: `awsbedrock-demo-1-inmemory`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-1-inmemory

**Description**:
- Complete FastAPI REST API
- Modern web interface
- AWS Bedrock AI agent with local mode
- **IN-MEMORY DATA** (lost on restart)

**Technologies**:
- FastAPI + Uvicorn
- Vanilla JavaScript + Tailwind CSS
- AWS Bedrock (Claude 3 Sonnet)
- In-memory Python data

**What you learn**:
- FastAPI basics
- REST API architecture
- AWS Bedrock AI integration
- Responsive web interface

**Limitations**:
- No persistence
- No authentication
- No file management

**Learning time**: 1-2 weeks

---

### Level 2: Real AWS Configuration

#### Demo 2: Real AWS Bedrock Configured
**Repository**: `awsbedrock-demo-2-aws-bedrock-real`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-2-aws-bedrock-real

**Description**:
- Everything from Demo 1
- **ADD**: Complete AWS Bedrock configuration
- AWS account created and configured
- Functional AWS credentials
- Test with REAL Claude 3 Sonnet
- Detailed AWS setup documentation

**New technologies**:
- AWS IAM (permission management)
- AWS Bedrock activated
- AWS CLI configured
- python-dotenv (environment variables)

**What you learn**:
- Create an AWS account
- Configure IAM and permissions
- Activate AWS Bedrock
- Manage AWS credentials
- Test real AI
- Understand AWS costs

**Learning time**: 2-3 days

---

### Level 3: Data Persistence

#### Demo 3: PostgreSQL + Neon
**Repository**: `awsbedrock-demo-3-postgresql`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-3-postgresql

**Description**:
- Base from Demo 2 (real AWS)
- **ADD**: PostgreSQL database via Neon (serverless)
- Data persistence
- Schema migrations with Alembic

**New technologies**:
- SQLAlchemy (ORM)
- Alembic (migrations)
- Neon.tech (serverless PostgreSQL)

**What you learn**:
- Relational data models
- ORM (Object-Relational Mapping)
- Database migrations
- Combine AWS Bedrock + PostgreSQL

**Learning time**: 1 week

---

#### Demo 4: Xata (Modern PostgreSQL)
**Repository**: `awsbedrock-demo-4-xata`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-4-xata

**Description**:
- Alternative to Demo 3
- Base from Demo 2 (real AWS)
- **ADD**: Xata database
- Integrated full-text search
- Admin UI for database

**New technologies**:
- Xata Python SDK
- Full-text search without Elasticsearch
- File attachments (preparation)

**What you learn**:
- Modern databases
- Full-text search
- Modern API vs classic SQL
- Database branching

**Learning time**: 3-5 days

---

### Level 4: Authentication and Security

#### Demo 5A: Clerk Authentication (Quick)
**Repository**: `awsbedrock-demo-5a-auth-clerk`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-5a-auth-clerk

**Description**:
- Base from Demo 3 (PostgreSQL)
- **ADD**: Authentication with Clerk (service)
- Setup in 15 minutes
- Social OAuth included (Google, GitHub)
- Automatic 2FA

**New technologies**:
- Clerk Python SDK
- Clerk webhooks
- Automatic session management

**What you learn**:
- Third-party auth service integration
- Social OAuth
- Webhooks
- Production-ready in minutes

**Advantages**:
- Ultra fast (15 min vs 1 week)
- Elegant pre-built UI
- Security managed by experts
- Social OAuth included
- Automatic 2FA/MFA

**Learning time**: 1 day

---

#### Demo 5B: JWT Custom Authentication (Learning)
**Repository**: `awsbedrock-demo-5b-auth-jwt-custom`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-5b-auth-jwt-custom

**Description**:
- Base from Demo 3 (PostgreSQL)
- **ADD**: JWT authentication coded from scratch
- Custom registration / login
- Access and refresh tokens
- Everything coded manually

**New technologies**:
- python-jose (JWT)
- passlib (password hashing)
- OAuth2 with FastAPI

**What you learn**:
- **How authentication works** (in depth)
- JWT (JSON Web Tokens)
- Password hashing and security
- Endpoint protection
- Refresh tokens
- Session management

**Advantages**:
- Complete learning
- Total control
- Free (no service)
- 100% customizable

**Learning time**: 1 week

---

#### Demo 6: Roles & Permissions (RBAC)
**Repository**: `awsbedrock-demo-6-rbac`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-6-rbac

**Description**:
- Base from Demo 5A or 5B (Auth)
- **ADD**: Role management
- Granular permissions
- Role-Based Access Control (RBAC)

**Implemented roles**:
- **Admin**: Full access
- **HR Manager**: Complete employee management
- **Department Manager**: Own department management
- **Employee**: Read-only to own profile

**What you learn**:
- RBAC (Role-Based Access Control)
- Granular permissions
- Validation middleware
- Advanced access management

**Learning time**: 3-5 days

---

### Level 5: Advanced Features

#### Demo 7: File Upload + S3
**Repository**: `awsbedrock-demo-7-files-s3`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-7-files-s3

**Description**:
- Base from Demo 6 (RBAC)
- **ADD**: File upload
- AWS S3 storage
- Profile photos, CVs, documents

**New technologies**:
- boto3 (AWS S3)
- Pillow (image processing)
- python-multipart (upload)

**What you learn**:
- File upload with FastAPI
- Cloud storage (AWS S3)
- Image processing
- File validation

**Learning time**: 1 week

---

#### Demo 8: Notifications + Email
**Repository**: `awsbedrock-demo-8-notifications`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-8-notifications

**Description**:
- Base from Demo 7 (Files)
- **ADD**: Notification system
- Transactional emails
- Automatic HR alerts

**New technologies**:
- AWS SES (emails)
- or SendGrid (alternative)
- Celery (asynchronous tasks)
- Redis (message queue)

**What you learn**:
- Sending emails
- Asynchronous tasks
- Message queues
- Cron jobs with FastAPI

**Learning time**: 1 week

---

#### Demo 9A: Stripe Payments & Subscriptions
**Repository**: `awsbedrock-demo-9a-stripe`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-9a-stripe

**Description**:
- Base from Demo 8 (Notifications)
- **ADD**: Subscription system with Stripe
- Pricing plans (Free, Pro, Enterprise)
- Stripe webhooks
- Billing management

**New technologies**:
- Stripe Python SDK
- Stripe Webhooks
- Plan management
- Automatic billing

**What you learn**:
- Stripe integration
- SaaS subscription management
- Payment webhooks
- Recurring billing
- Free trial management
- Plan upgrade/downgrade

**Learning time**: 1 week

---

#### Demo 9B: Exports & Reports
**Repository**: `awsbedrock-demo-9b-exports`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-9b-exports

**Description**:
- Base from Demo 9A (Stripe)
- **ADD**: Data exports
- Report generation
- PDF, Excel, CSV

**New technologies**:
- reportlab (PDF)
- openpyxl (Excel)
- pandas (data manipulation)

**What you learn**:
- PDF generation
- Excel export
- Automatic reports
- Charts in PDFs

**Learning time**: 3-5 days

---

### Level 6: Advanced AI

#### Demo 10: RAG + pgvector (Semantic Search)
**Repository**: `awsbedrock-demo-10-rag-pgvector`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-10-rag-pgvector

**Description**:
- Base from Demo 9B (Exports)
- **ADD**: RAG (Retrieval Augmented Generation)
- **pgvector** for PostgreSQL
- Vector employee database
- Advanced semantic search

**New technologies**:
- LangChain
- **pgvector** (PostgreSQL extension)
- AWS Bedrock Titan embeddings
- Vector search in PostgreSQL

**What you learn**:
- Retrieval Augmented Generation (RAG)
- Vector databases with **pgvector**
- Embeddings (text → vectors conversion)
- Semantic search (cosine similarity)
- Combine classic SQL + vector search

**Advantages of pgvector**:
- Everything in PostgreSQL (no separate database)
- ACID transactions
- Vector search + classic SQL
- Excellent performance
- Free and open-source

**Learning time**: 1-2 weeks

---

#### Demo 11: Conversation History
**Repository**: `awsbedrock-demo-11-chat-history`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-11-chat-history

**Description**:
- Base from Demo 10 (RAG)
- **ADD**: Conversation history
- Multi-turn context
- Saved conversations

**What you learn**:
- Conversational history management
- Multi-turn context
- Response personalization

**Learning time**: 3-5 days

---

#### Demo 11B: Agentic AI (Multi-Agent System)
**Repository**: `awsbedrock-demo-11b-agentic-ai`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-11b-agentic-ai

**Description**:
- Base from Demo 11 (Chat History)
- **ADD**: Multi-agent AI system
- Specialized agents that collaborate
- Intelligent orchestration

**New technologies**:
- LangGraph (agent orchestration)
- Multiple AWS Bedrock agents
- Function calling
- Agent collaboration

**What you learn**:
- Multi-agent architecture
- AI agent orchestration
- Agent specialization
- Inter-agent communication
- ReAct pattern (Reasoning + Acting)

**Implemented agents**:
1. **HR Analyst Agent** - HR data specialist
2. **Recruiter Agent** - Candidate search
3. **Compensation Agent** - Salary analysis
4. **Coordinator Agent** - Orchestrator

**Learning time**: 2 weeks

---

### Level 7: Deployment and Production

#### Demo 12: Docker + Docker Compose
**Repository**: `awsbedrock-demo-12-docker`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-12-docker

**Description**:
- Base from Demo 11B (Agentic AI)
- **ADD**: Docker containerization
- Docker Compose multi-service
- Dev/prod environments

**What you learn**:
- Containerization
- Docker multi-stage builds
- Docker Compose
- Service orchestration

**Learning time**: 3-5 days

---

#### Demo 13: CI/CD with GitHub Actions
**Repository**: `awsbedrock-demo-13-cicd`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-13-cicd

**Description**:
- Base from Demo 12 (Docker)
- **ADD**: CI/CD pipeline
- Automatic tests
- Automatic deployment

**What you learn**:
- Automated tests
- GitHub Actions
- CI/CD pipelines
- Continuous deployment

**Learning time**: 1 week

---

#### Demo 14: AWS Deployment (ECS)
**Repository**: `awsbedrock-demo-14-aws-deployment`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-14-aws-deployment

**Description**:
- Base from Demo 13 (CI/CD)
- **ADD**: Complete AWS deployment
- ECS + Fargate
- RDS, S3, CloudFront

**What you learn**:
- Infrastructure as Code (Terraform)
- AWS ECS/Fargate
- Load balancing
- Auto-scaling

**Learning time**: 2 weeks

---

#### Demo 15: Monitoring & Logging
**Repository**: `awsbedrock-demo-15-monitoring`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-15-monitoring

**Description**:
- Base from Demo 14 (AWS)
- **ADD**: Complete monitoring
- Centralized logs
- Alerts and metrics

**New technologies**:
- Prometheus + Grafana
- AWS CloudWatch
- Sentry (error tracking)
- Loguru (advanced logging)

**What you learn**:
- Observability
- Metrics and KPIs
- Alerting
- Production debugging

**Learning time**: 1 week

---

### Level 8: Enterprise Features

#### Demo 16: Multi-tenant
**Repository**: `awsbedrock-demo-16-multitenant`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-16-multitenant

**Description**:
- Base from Demo 15 (Monitoring)
- **ADD**: Multi-tenant support
- Data isolation per company
- Custom subdomains

**What you learn**:
- Multi-tenant architecture
- Data isolation
- Subdomain management
- Per-tenant billing

**Learning time**: 2 weeks

---

#### Demo 17: Public API + Rate Limiting
**Repository**: `awsbedrock-demo-17-public-api`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-17-public-api

**Description**:
- Base from Demo 16 (Multi-tenant)
- **ADD**: Documented public API
- API keys
- Rate limiting
- Webhooks

**New technologies**:
- slowapi (rate limiting)
- API versioning
- Webhooks

**What you learn**:
- Public API
- Quota management
- API versioning
- Webhooks and integrations

**Learning time**: 1-2 weeks

---

#### Demo 18A: Automatic Technical Documentation
**Repository**: `awsbedrock-demo-18a-documentation`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-18a-documentation

**Description**:
- Base from Demo 17 (Public API)
- **ADD**: Automatic technical documentation
- Enhanced docstrings
- Generated documentation
- Dynamic README

**New technologies**:
- Sphinx (Python documentation)
- MkDocs Material
- Auto-doc from docstrings
- Enhanced OpenAPI/Swagger

**What you learn**:
- Professional documentation
- Google/NumPy style docstrings
- Automatic doc generation
- Documentation hosting

**Learning time**: 3-5 days

---

#### Demo 18B: Mobile Application (API)
**Repository**: `awsbedrock-demo-18b-mobile-api`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-18b-mobile-api

**Description**:
- Base from Demo 18A (Documentation)
- **ADD**: Mobile-optimized endpoints
- Push notifications
- Offline-first support

**What you learn**:
- Mobile-first API
- Push notifications (FCM)
- Mobile optimization
- Offline/online management

**Learning time**: 1 week

---

### Level 9: Advanced Frontend

#### Demo 19A: UI Component Library (Design System)
**Repository**: `awsbedrock-demo-19a-ui-components`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-19a-ui-components

**Description**:
- Base from Demo 18B (Mobile API)
- **ADD**: UI component library
- Complete design system
- Storybook for components
- Advanced Tailwind

**New technologies**:
- Storybook
- Advanced Tailwind CSS
- Headless UI
- Framer Motion (animations)

**What you learn**:
- Create a design system
- Reusable components
- Component documentation (Storybook)
- Fluid animations
- Advanced responsive design

**Learning time**: 1-2 weeks

---

#### Demo 19B: Complete React Frontend
**Repository**: `awsbedrock-demo-19b-react-app`  
**URL**: https://github.com/inskillflow/awsbedrock-demo-19b-react-app

**Description**:
- Base from Demo 19A (UI Components)
- **ADD**: Complete React application
- Uses design system components
- State management (Redux)
- React Query for API

**New technologies**:
- React + TypeScript
- Redux Toolkit
- React Query / TanStack Query
- React Router v6

**Features**:
- Authentication flows
- Employee management
- AI Chat interface
- Dashboard with charts
- Settings & Profile
- Dark mode

**Learning time**: 2-3 weeks

---

## Summary by Repository

| Demo | Repository Name | Main Focus | Time | Difficulty |
|------|----------------|------------|------|-----------|
| 1 | `awsbedrock-demo-1-inmemory` | API + In-memory AI | 1-2 wk | Easy |
| 2 | `awsbedrock-demo-2-aws-bedrock-real` | REAL AWS Bedrock | 2-3 d | Medium |
| 3 | `awsbedrock-demo-3-postgresql` | PostgreSQL + Neon | 1 wk | Medium |
| 4 | `awsbedrock-demo-4-xata` | Modern Xata | 3-5 d | Medium |
| 5A | `awsbedrock-demo-5a-auth-clerk` | Clerk Auth (Quick) | 1 d | Easy |
| 5B | `awsbedrock-demo-5b-auth-jwt-custom` | Custom JWT Auth | 1 wk | Advanced |
| 6 | `awsbedrock-demo-6-rbac` | Roles & Permissions | 3-5 d | Advanced |
| 7 | `awsbedrock-demo-7-files-s3` | S3 file upload | 1 wk | Advanced |
| 8 | `awsbedrock-demo-8-notifications` | Emails + Notifications | 1 wk | Advanced |
| 9A | `awsbedrock-demo-9a-stripe` | Stripe Subscriptions | 1 wk | Advanced |
| 9B | `awsbedrock-demo-9b-exports` | PDF/Excel exports | 3-5 d | Medium |
| 10 | `awsbedrock-demo-10-rag-pgvector` | RAG + pgvector | 1-2 wk | Expert |
| 11 | `awsbedrock-demo-11-chat-history` | Conversation history | 3-5 d | Advanced |
| 11B | `awsbedrock-demo-11b-agentic-ai` | Agentic AI (Multi-Agent) | 2 wk | Expert |
| 12 | `awsbedrock-demo-12-docker` | Docker + Compose | 3-5 d | Advanced |
| 13 | `awsbedrock-demo-13-cicd` | CI/CD GitHub Actions | 1 wk | Advanced |
| 14 | `awsbedrock-demo-14-aws-deployment` | Final AWS Deployment | 2 wk | Expert |
| 15 | `awsbedrock-demo-15-monitoring` | Complete monitoring | 1 wk | Advanced |
| 16 | `awsbedrock-demo-16-multitenant` | Multi-tenant | 2 wk | Expert |
| 17 | `awsbedrock-demo-17-public-api` | Public API | 1-2 wk | Advanced |
| 18A | `awsbedrock-demo-18a-documentation` | Technical Documentation | 3-5 d | Medium |
| 18B | `awsbedrock-demo-18b-mobile-api` | Mobile API | 1 wk | Advanced |
| 19A | `awsbedrock-demo-19a-ui-components` | UI Design System | 1-2 wk | Advanced |
| 19B | `awsbedrock-demo-19b-react-app` | Complete React Frontend | 2-3 wk | Expert |

**Total estimated time**: 8-12 months to complete everything (22 demos + variations)

---

## Suggested Learning Paths

### Path 1: Backend Developer (3-4 months)
1. Demo 1 - Foundations
2. **Demo 2 - REAL AWS Bedrock** (Important)
3. Demo 3 - PostgreSQL
4. **Demo 5A - Clerk Auth** (quick) OR **Demo 5B - Custom JWT** (learning)
5. Demo 6 - RBAC
6. Demo 7 - S3 Files
7. Demo 12 - Docker
8. Demo 13 - CI/CD

### Path 2: Full Stack Developer (5-6 months)
1. Demo 1 - Foundations
2. **Demo 2 - REAL AWS Bedrock**
3. Demo 3 - PostgreSQL
4. **Demo 5A - Clerk Auth** (recommended for speed)
5. Demo 7 - S3 Files
6. Demo 9B - Exports
7. Demo 12 - Docker
8. Demo 19B - React Frontend

### Path 3: AI & Data Engineer (4-5 months)
1. Demo 1 - Foundations
2. **Demo 2 - REAL AWS Bedrock**
3. Demo 3 - PostgreSQL
4. Demo 10 - RAG + pgvector
5. Demo 11 - Chat History
6. Demo 11B - Agentic AI
7. Demo 9B - Exports & Reports
8. Demo 15 - Monitoring

### Path 4: DevOps Engineer (3-4 months)
1. Demo 1 - Foundations
2. **Demo 2 - REAL AWS Bedrock**
3. Demo 3 - PostgreSQL
4. Demo 12 - Docker
5. Demo 13 - CI/CD
6. Demo 14 - AWS Deployment
7. Demo 15 - Monitoring

### Path 5: SaaS Entrepreneur (6-9 months complete)
Recommendation: Use **Demo 5A (Clerk)** to go fast to production.

Essential demos in order:
1. Demo 1 - Foundations
2. **Demo 2 - REAL AWS Bedrock**
3. Demo 3 - PostgreSQL
4. **Demo 5A - Clerk Auth** (faster)
5. Demo 6 - RBAC
6. **Demo 9A - Stripe** (essential SaaS)
7. Demo 7 - S3 Files
8. Demo 8 - Notifications
9. Demo 12 - Docker
10. Demo 13 - CI/CD
11. Demo 14 - AWS Deployment
12. Demo 15 - Monitoring
13. Demo 16 - Multi-tenant
14. Demo 17 - Public API

---

## Repository Naming Convention

### Standard Format
```
awsbedrock-demo-[NUMBER]-[MAIN-FEATURE]
```

### Naming Rules
1. **Prefix**: `awsbedrock-demo-`
2. **Number**: Sequential order (1, 2, 3...)
3. **Feature**: Descriptive name in kebab-case
4. **Language**: English for international compatibility

### Examples
- awsbedrock-demo-1-inmemory
- awsbedrock-demo-2-aws-bedrock-real
- awsbedrock-demo-3-postgresql
- awsbedrock-demo-10-rag-pgvector

---

## Contribution and Feedback

Each demo is a learning project. Feel free to:
- Ask questions via GitHub Issues
- Propose improvements
- Share your achievements
- Report bugs

---

## Additional Resources

### To Get Started
- [Demo 1 Documentation](../03-PREREQUISITES_INSTALLATION.md)
- [User Guide](../02-USER_GUIDE.md)
- [Technologies Used](../04-TECHNOLOGIES_EVOLUTIONS.md)

### Learning
- FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy: https://docs.sqlalchemy.org/
- AWS Bedrock: https://aws.amazon.com/bedrock/
- Neon: https://neon.tech/docs
- Xata: https://xata.io/docs

---

**Happy progressive learning!**

Start with Demo 1, master it, then move to the next at your own pace.

