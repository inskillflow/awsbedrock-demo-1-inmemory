# System Architecture - Progressive Evolution

This document presents the system architecture and its evolution through different demos.

## Table of Contents

- [Current Architecture (Demo 1)](#current-architecture-demo-1)
- [Evolution Level 2: AWS Bedrock](#evolution-level-2-aws-bedrock)
- [Evolution Level 3: Persistence](#evolution-level-3-persistence)
- [Evolution Level 4: Authentication](#evolution-level-4-authentication)
- [Evolution Level 5: Advanced Features](#evolution-level-5-advanced-features)
- [Evolution Level 6: Advanced AI](#evolution-level-6-advanced-ai)
- [Evolution Level 7: Production](#evolution-level-7-production)
- [Final Architecture (Demo 19B)](#final-architecture-demo-19b)

---

## Current Architecture (Demo 1)

**Repository**: [awsbedrock-demo-1-inmemory](https://github.com/inskillflow/awsbedrock-demo-1-inmemory)

### Description

Simple system with REST API, web interface, and local AI mode. All data is in-memory.

### Architecture Diagram - Simplified View

```mermaid
flowchart LR
    User[User]
    Frontend[Frontend<br/>HTML + JS]
    Backend[Backend<br/>FastAPI]
    Data[Data<br/>In-Memory]
    AI[AI<br/>Local Mode]
    
    User --> Frontend
    Frontend -->|HTTP/REST| Backend
    Backend --> Data
    Backend --> AI
    AI --> Data
    
    style User fill:#61DAFB,stroke:#333,stroke-width:3px,color:#000,font-size:16px
    style Frontend fill:#E34F26,stroke:#333,stroke-width:3px,color:#fff,font-size:16px
    style Backend fill:#009688,stroke:#333,stroke-width:3px,color:#fff,font-size:16px
    style Data fill:#FF6B6B,stroke:#333,stroke-width:3px,color:#fff,font-size:16px
    style AI fill:#FFA500,stroke:#333,stroke-width:3px,color:#000,font-size:16px
```

### Detailed Architecture

```mermaid
graph TB
    Browser[Web Browser]
    HTML[index.html]
    JS[app.js]
    
    API[server.py<br/>FastAPI]
    Data[employee_data.py<br/>Python List]
    AI[ai_agent.py<br/>if/else Rules]
    
    Browser --> HTML
    HTML --> JS
    JS -->|HTTP Requests| API
    
    API --> Data
    API --> AI
    AI -->|Reads Data| Data
    
    style Browser fill:#61DAFB,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style HTML fill:#E34F26,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style JS fill:#F7DF1E,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style API fill:#009688,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Data fill:#FF6B6B,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style AI fill:#FFA500,stroke:#333,stroke-width:4px,color:#000,font-size:18px
```

### Components

| Component | Technology | Status | Notes |
|-----------|------------|--------|-------|
| Frontend | HTML5 + JavaScript | ✅ Current | Responsive web interface |
| REST API | FastAPI | ✅ Current | Complete CRUD endpoints |
| Data | Python Lists | ⚠️ Temporary | In-memory, non-persistent |
| AI | Local Mode | ⚠️ Basic | Simple rules, not real AI |

### Limitations

- ❌ No persistence (data lost on restart)
- ❌ Basic AI (local mode with rules)
- ❌ No authentication
- ❌ No file management

---

## Evolution Level 2: AWS Bedrock

**Repository**: [awsbedrock-demo-2-aws-bedrock-real](https://github.com/inskillflow/awsbedrock-demo-2-aws-bedrock-real)

### Additions

- Complete AWS configuration
- Real AI with Claude 3 Sonnet
- Secured AWS credentials

### Architecture Diagram - Simplified View

```mermaid
flowchart LR
    User[User]
    Frontend[Frontend<br/>HTML + JS]
    Backend[Backend<br/>FastAPI]
    Data[Data<br/>In-Memory]
    AWS[AWS Bedrock<br/>Claude 3]
    
    User --> Frontend
    Frontend -->|HTTP/REST| Backend
    Backend --> Data
    Backend -->|AI Call| AWS
    AWS -->|Response| Backend
    
    style User fill:#61DAFB,stroke:#333,stroke-width:3px,color:#000,font-size:16px
    style Frontend fill:#E34F26,stroke:#333,stroke-width:3px,color:#fff,font-size:16px
    style Backend fill:#009688,stroke:#333,stroke-width:3px,color:#fff,font-size:16px
    style Data fill:#FF6B6B,stroke:#333,stroke-width:3px,color:#fff,font-size:16px
    style AWS fill:#FF6600,stroke:#333,stroke-width:4px,color:#fff,font-size:16px
```

### Detailed Architecture

```mermaid
graph TB
    Browser[Browser]
    JS[app.js]
    
    API[server.py<br/>FastAPI]
    Data[Data<br/>In-Memory]
    AI[ai_agent.py]
    
    Bedrock[AWS Bedrock<br/>Claude 3]
    IAM[AWS IAM]
    
    Browser --> JS
    JS -->|HTTP| API
    
    API --> Data
    API --> AI
    AI -->|boto3| Bedrock
    AI --> IAM
    
    style Browser fill:#61DAFB,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style JS fill:#F7DF1E,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style API fill:#009688,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Data fill:#FF6B6B,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style AI fill:#FFA500,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style Bedrock fill:#FF6600,stroke:#333,stroke-width:5px,color:#fff,font-size:18px
    style IAM fill:#DD4814,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
```

### New Components

| Component | Technology | Addition | Notes |
|-----------|------------|----------|-------|
| AWS Bedrock | Claude 3 Sonnet | ✅ Demo 2 | Real and powerful AI |
| AWS IAM | Credentials | ✅ Demo 2 | Security and permissions |
| Boto3 | Python SDK | ✅ Demo 2 | AWS Client |

---

## Evolution Level 3: Persistence

**Repositories**: 
- [awsbedrock-demo-3-postgresql](https://github.com/inskillflow/awsbedrock-demo-3-postgresql)
- [awsbedrock-demo-4-xata](https://github.com/inskillflow/awsbedrock-demo-4-xata)

### Additions

- PostgreSQL database (Neon)
- SQLAlchemy ORM
- Alembic migrations
- Alternative: Xata

### Architecture Diagram - Simplified View

```mermaid
flowchart LR
    User[User]
    Frontend[Frontend]
    Backend[Backend]
    DB[PostgreSQL<br/>Neon]
    AWS[AWS Bedrock]
    
    User --> Frontend
    Frontend -->|HTTP/REST| Backend
    Backend --> DB
    Backend --> AWS
    
    style User fill:#61DAFB,stroke:#333,stroke-width:3px,color:#000,font-size:16px
    style Frontend fill:#E34F26,stroke:#333,stroke-width:3px,color:#fff,font-size:16px
    style Backend fill:#009688,stroke:#333,stroke-width:3px,color:#fff,font-size:16px
    style DB fill:#1E40AF,stroke:#333,stroke-width:4px,color:#fff,font-size:16px
    style AWS fill:#FF6600,stroke:#333,stroke-width:4px,color:#fff,font-size:16px
```

### Detailed Architecture

```mermaid
graph TB
    Browser[Browser]
    JS[app.js]
    
    API[server.py]
    ORM[SQLAlchemy]
    AI[ai_agent.py]
    
    DB[(PostgreSQL<br/>Neon)]
    
    Bedrock[AWS Bedrock<br/>Claude 3]
    
    Browser --> JS
    JS -->|HTTP| API
    API --> ORM
    ORM --> DB
    API --> AI
    AI --> Bedrock
    AI --> ORM
    
    style Browser fill:#61DAFB,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style JS fill:#F7DF1E,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style API fill:#009688,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style ORM fill:#336791,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style AI fill:#FFA500,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style DB fill:#1E40AF,stroke:#333,stroke-width:5px,color:#fff,font-size:18px
    style Bedrock fill:#FF6600,stroke:#333,stroke-width:5px,color:#fff,font-size:18px
```

### New Components

| Component | Technology | Addition | Notes |
|-----------|------------|----------|-------|
| PostgreSQL | Neon Serverless | ✅ Demo 3 | Persistent database |
| ORM | SQLAlchemy | ✅ Demo 3 | Object-relational mapping |
| Migrations | Alembic | ✅ Demo 3 | Schema management |
| Alternative DB | Xata | ✅ Demo 4 | Modern database with search |

---

## Evolution Level 4: Authentication

**Repositories**:
- [awsbedrock-demo-5a-auth-clerk](https://github.com/inskillflow/awsbedrock-demo-5a-auth-clerk)
- [awsbedrock-demo-5b-auth-jwt-custom](https://github.com/inskillflow/awsbedrock-demo-5b-auth-jwt-custom)
- [awsbedrock-demo-6-rbac](https://github.com/inskillflow/awsbedrock-demo-6-rbac)

### Additions

- Authentication (Clerk or JWT)
- Session management
- Roles and permissions (RBAC)
- Endpoint protection

### Architecture Diagram - Simplified View

```mermaid
flowchart LR
    User[User]
    Login[Login]
    Auth[Auth<br/>Clerk/JWT]
    Backend[Backend<br/>+ RBAC]
    DB[PostgreSQL<br/>+ Users]
    
    User --> Login
    Login --> Auth
    Auth -->|Token| Backend
    Backend --> DB
    
    style User fill:#61DAFB,stroke:#333,stroke-width:3px,color:#000,font-size:16px
    style Login fill:#059669,stroke:#333,stroke-width:3px,color:#fff,font-size:16px
    style Auth fill:#6C5CE7,stroke:#333,stroke-width:4px,color:#fff,font-size:16px
    style Backend fill:#009688,stroke:#333,stroke-width:3px,color:#fff,font-size:16px
    style DB fill:#1E40AF,stroke:#333,stroke-width:4px,color:#fff,font-size:16px
```

### Detailed Architecture

```mermaid
graph TB
    Browser[Browser]
    Login[Login Interface]
    
    Clerk[Clerk Service]
    Auth[Middleware Auth]
    
    API[FastAPI]
    RBAC[RBAC Engine]
    
    DB[(PostgreSQL)]
    Users[Users Table]
    Roles[Roles Table]
    
    Browser --> Login
    Login --> Clerk
    Login -->|JWT Token| Auth
    Auth --> API
    API --> RBAC
    RBAC -->|Checks| Roles
    
    API --> DB
    DB --> Users
    DB --> Roles
    
    style Browser fill:#61DAFB,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style Login fill:#059669,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Clerk fill:#6C5CE7,stroke:#333,stroke-width:5px,color:#fff,font-size:18px
    style Auth fill:#7C3AED,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style API fill:#009688,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style RBAC fill:#DC2626,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style DB fill:#1E40AF,stroke:#333,stroke-width:5px,color:#fff,font-size:18px
    style Users fill:#0EA5E9,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Roles fill:#0284C7,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
```

### New Components

| Component | Technology | Addition | Notes |
|-----------|------------|----------|-------|
| Auth Service | Clerk | ✅ Demo 5A | Quick auth (15 min) |
| Custom JWT | python-jose | ✅ Demo 5B | JWT from scratch |
| RBAC | Custom | ✅ Demo 6 | Role management |
| Middleware | FastAPI | ✅ Demo 5 | Endpoint protection |

---

## Evolution Level 5: Advanced Features

**Repositories**:
- [awsbedrock-demo-7-files-s3](https://github.com/inskillflow/awsbedrock-demo-7-files-s3)
- [awsbedrock-demo-8-notifications](https://github.com/inskillflow/awsbedrock-demo-8-notifications)
- [awsbedrock-demo-9a-stripe](https://github.com/inskillflow/awsbedrock-demo-9a-stripe)
- [awsbedrock-demo-9b-exports](https://github.com/inskillflow/awsbedrock-demo-9b-exports)

### Additions

- File upload to S3
- Notifications and emails
- Stripe subscriptions
- PDF/Excel exports

### Architecture Diagram

```mermaid
graph TB
    subgraph "Frontend"
        Browser[Web Browser]
        Upload[File Upload UI]
        Payment[Payment UI]
    end
    
    subgraph "Backend - FastAPI"
        API[server.py]
        Auth[Auth Middleware]
        Files[File Handler]
        Email[Email Service]
        Stripe[Stripe Handler]
        Export[Export Service]
    end
    
    subgraph "AWS Services"
        S3[S3 Bucket<br/>File Storage]
        SES[SES<br/>Email Service]
        Bedrock[Bedrock<br/>Claude 3]
    end
    
    subgraph "External Services"
        StripeAPI[Stripe API<br/>Payments]
        Webhooks[Webhooks<br/>Events]
    end
    
    subgraph "Database"
        DB[(PostgreSQL)]
        Subscriptions[Subscriptions]
        FilesMeta[Files Metadata]
    end
    
    Browser --> Upload
    Upload --> Files
    Files --> S3
    Files --> FilesMeta
    
    Browser --> Payment
    Payment --> Stripe
    Stripe --> StripeAPI
    StripeAPI --> Webhooks
    Webhooks --> Subscriptions
    
    API --> Email
    Email --> SES
    
    API --> Export
    Export --> DB
    
    API --> Auth
    API --> Bedrock
    
    style Browser fill:#61DAFB,stroke:#333,stroke-width:2px,color:#000
    style Upload fill:#059669,stroke:#333,stroke-width:2px,color:#fff
    style Payment fill:#047857,stroke:#333,stroke-width:2px,color:#fff
    style API fill:#009688,stroke:#333,stroke-width:2px,color:#fff
    style Auth fill:#7C3AED,stroke:#333,stroke-width:2px,color:#fff
    style Files fill:#0891B2,stroke:#333,stroke-width:2px,color:#fff
    style Email fill:#DC2626,stroke:#333,stroke-width:2px,color:#fff
    style Stripe fill:#635BFF,stroke:#333,stroke-width:2px,color:#fff
    style Export fill:#059669,stroke:#333,stroke-width:2px,color:#fff
    style S3 fill:#FF9900,stroke:#333,stroke-width:3px,color:#000
    style SES fill:#DD4814,stroke:#333,stroke-width:3px,color:#fff
    style Bedrock fill:#FF6600,stroke:#333,stroke-width:3px,color:#fff
    style StripeAPI fill:#635BFF,stroke:#333,stroke-width:3px,color:#fff
    style Webhooks fill:#5B21B6,stroke:#333,stroke-width:2px,color:#fff
    style RDS fill:#1E40AF,stroke:#333,stroke-width:3px,color:#fff
    style Subscriptions fill:#0EA5E9,stroke:#333,stroke-width:2px,color:#fff
    style FilesMeta fill:#0284C7,stroke:#333,stroke-width:2px,color:#fff
```

### New Components

| Component | Technology | Addition | Notes |
|-----------|------------|----------|-------|
| S3 Storage | AWS S3 | ✅ Demo 7 | File storage |
| Email | AWS SES | ✅ Demo 8 | Email notifications |
| Payments | Stripe | ✅ Demo 9A | SaaS subscriptions |
| Exports | reportlab/openpyxl | ✅ Demo 9B | PDF, Excel, CSV |

---

## Evolution Level 6: Advanced AI

**Repositories**:
- [awsbedrock-demo-10-rag-pgvector](https://github.com/inskillflow/awsbedrock-demo-10-rag-pgvector)
- [awsbedrock-demo-11-chat-history](https://github.com/inskillflow/awsbedrock-demo-11-chat-history)
- [awsbedrock-demo-11b-agentic-ai](https://github.com/inskillflow/awsbedrock-demo-11b-agentic-ai)

### Additions

- RAG with pgvector
- Vector embeddings
- Conversation history
- Multi-agent system

### Architecture Diagram

```mermaid
graph TB
    subgraph "Frontend"
        Browser[Web Browser]
        Chat[Chat Interface]
    end
    
    subgraph "AI Layer"
        Coordinator[Coordinator Agent]
        HRAgent[HR Analyst Agent]
        RecruiterAgent[Recruiter Agent]
        CompAgent[Compensation Agent]
        RAG[RAG Engine]
    end
    
    subgraph "Backend - FastAPI"
        API[server.py]
        Embeddings[Embeddings Service]
        Search[Semantic Search]
    end
    
    subgraph "Database"
        DB[(PostgreSQL + pgvector)]
        Vectors[Vector Embeddings]
        Conversations[Conversations]
        Messages[Messages]
    end
    
    subgraph "AWS Services"
        Bedrock[Bedrock Claude 3]
        BedrockEmbed[Bedrock Titan<br/>Embeddings]
    end
    
    Browser --> Chat
    Chat --> API
    
    API --> Coordinator
    Coordinator --> HRAgent
    Coordinator --> RecruiterAgent
    Coordinator --> CompAgent
    
    HRAgent --> RAG
    RecruiterAgent --> RAG
    CompAgent --> RAG
    
    RAG --> Search
    Search --> Vectors
    
    API --> Embeddings
    Embeddings --> BedrockEmbed
    Embeddings --> Vectors
    
    HRAgent --> Bedrock
    RecruiterAgent --> Bedrock
    CompAgent --> Bedrock
    
    API --> Conversations
    Conversations --> Messages
    
    style Browser fill:#61DAFB,stroke:#333,stroke-width:2px,color:#000
    style Chat fill:#059669,stroke:#333,stroke-width:2px,color:#fff
    style API fill:#009688,stroke:#333,stroke-width:2px,color:#fff
    style Coordinator fill:#0891B2,stroke:#333,stroke-width:3px,color:#fff
    style HRAgent fill:#0E7490,stroke:#333,stroke-width:2px,color:#fff
    style RecruiterAgent fill:#0C4A6E,stroke:#333,stroke-width:2px,color:#fff
    style CompAgent fill:#075985,stroke:#333,stroke-width:2px,color:#fff
    style RAG fill:#DC2626,stroke:#333,stroke-width:3px,color:#fff
    style Embeddings fill:#B91C1C,stroke:#333,stroke-width:2px,color:#fff
    style Search fill:#991B1B,stroke:#333,stroke-width:2px,color:#fff
    style DB fill:#1E40AF,stroke:#333,stroke-width:3px,color:#fff
    style Vectors fill:#7C3AED,stroke:#333,stroke-width:2px,color:#fff
    style Conversations fill:#0EA5E9,stroke:#333,stroke-width:2px,color:#fff
    style Messages fill:#0284C7,stroke:#333,stroke-width:2px,color:#fff
    style Bedrock fill:#FF6600,stroke:#333,stroke-width:3px,color:#fff
    style BedrockEmbed fill:#FF9900,stroke:#333,stroke-width:2px,color:#000
```

### New Components

| Component | Technology | Addition | Notes |
|-----------|------------|----------|-------|
| pgvector | PostgreSQL Extension | ✅ Demo 10 | Vector database |
| RAG | LangChain | ✅ Demo 10 | Semantic search |
| Embeddings | AWS Bedrock Titan | ✅ Demo 10 | Text vectorization |
| Chat History | SQLAlchemy | ✅ Demo 11 | Conversations |
| Multi-Agents | LangGraph | ✅ Demo 11B | Agent orchestration |

---

## Evolution Level 7: Production

**Repositories**:
- [awsbedrock-demo-12-docker](https://github.com/inskillflow/awsbedrock-demo-12-docker)
- [awsbedrock-demo-13-cicd](https://github.com/inskillflow/awsbedrock-demo-13-cicd)
- [awsbedrock-demo-14-aws-deployment](https://github.com/inskillflow/awsbedrock-demo-14-aws-deployment)
- [awsbedrock-demo-15-monitoring](https://github.com/inskillflow/awsbedrock-demo-15-monitoring)

### Additions

- Docker containerization
- CI/CD Pipeline
- AWS ECS deployment
- Monitoring and logs

### Architecture Diagram

```mermaid
graph TB
    subgraph "Development"
        Dev[Developer]
        Git[GitHub Repo]
    end
    
    subgraph "CI/CD Pipeline"
        Actions[GitHub Actions]
        Build[Docker Build]
        Tests[Automated Tests]
        Deploy[Deploy Script]
    end
    
    subgraph "AWS Production"
        subgraph "Compute"
            ALB[Application Load Balancer]
            ECS[ECS Cluster]
            Fargate1[Fargate Task 1]
            Fargate2[Fargate Task 2]
        end
        
        subgraph "Storage"
            RDS[(RDS PostgreSQL)]
            S3[S3 Buckets]
        end
        
        subgraph "Monitoring"
            CloudWatch[CloudWatch Logs]
            Metrics[CloudWatch Metrics]
            Alarms[CloudWatch Alarms]
        end
        
        subgraph "Security"
            VPC[VPC]
            SecGroups[Security Groups]
            IAM[IAM Roles]
        end
        
        subgraph "AI Services"
            Bedrock[Bedrock Claude 3]
        end
    end
    
    subgraph "External Monitoring"
        Grafana[Grafana Dashboard]
        Prometheus[Prometheus]
        Sentry[Sentry<br/>Error Tracking]
    end
    
    Dev --> Git
    Git --> Actions
    Actions --> Build
    Build --> Tests
    Tests --> Deploy
    Deploy --> ECS
    
    ECS --> Fargate1
    ECS --> Fargate2
    
    ALB --> Fargate1
    ALB --> Fargate2
    
    Fargate1 --> RDS
    Fargate2 --> RDS
    Fargate1 --> S3
    Fargate2 --> S3
    Fargate1 --> Bedrock
    Fargate2 --> Bedrock
    
    Fargate1 --> CloudWatch
    Fargate2 --> CloudWatch
    CloudWatch --> Metrics
    Metrics --> Alarms
    
    CloudWatch --> Prometheus
    Prometheus --> Grafana
    
    Fargate1 --> Sentry
    Fargate2 --> Sentry
    
    VPC --> ECS
    SecGroups --> Fargate1
    SecGroups --> Fargate2
    IAM --> Fargate1
    IAM --> Fargate2
    
    style Dev fill:#2C3E50,stroke:#333,stroke-width:2px,color:#fff
    style Git fill:#24292E,stroke:#333,stroke-width:2px,color:#fff
    style Actions fill:#2088FF,stroke:#333,stroke-width:3px,color:#fff
    style Build fill:#2496ED,stroke:#333,stroke-width:2px,color:#fff
    style Tests fill:#059669,stroke:#333,stroke-width:2px,color:#fff
    style Deploy fill:#047857,stroke:#333,stroke-width:2px,color:#fff
    style ECS fill:#FF9900,stroke:#333,stroke-width:3px,color:#000
    style Fargate1 fill:#FF6600,stroke:#333,stroke-width:2px,color:#fff
    style Fargate2 fill:#FF6600,stroke:#333,stroke-width:2px,color:#fff
    style ALB fill:#DD4814,stroke:#333,stroke-width:3px,color:#fff
    style RDS fill:#1E40AF,stroke:#333,stroke-width:3px,color:#fff
    style S3 fill:#FF9900,stroke:#333,stroke-width:2px,color:#000
    style CloudWatch fill:#DD4814,stroke:#333,stroke-width:2px,color:#fff
    style Metrics fill:#E97435,stroke:#333,stroke-width:2px,color:#fff
    style Alarms fill:#DC2626,stroke:#333,stroke-width:2px,color:#fff
    style VPC fill:#5B21B6,stroke:#333,stroke-width:2px,color:#fff
    style SecGroups fill:#7C3AED,stroke:#333,stroke-width:2px,color:#fff
    style IAM fill:#DD4814,stroke:#333,stroke-width:2px,color:#fff
    style Bedrock fill:#FF6600,stroke:#333,stroke-width:3px,color:#fff
    style Grafana fill:#F46800,stroke:#333,stroke-width:2px,color:#fff
    style Prometheus fill:#E6522C,stroke:#333,stroke-width:2px,color:#fff
    style Sentry fill:#362D59,stroke:#333,stroke-width:2px,color:#fff
```

### New Components

| Component | Technology | Addition | Notes |
|-----------|------------|----------|-------|
| Docker | Containerization | ✅ Demo 12 | Docker images |
| CI/CD | GitHub Actions | ✅ Demo 13 | Automated pipeline |
| ECS | AWS Fargate | ✅ Demo 14 | Container orchestration |
| Load Balancer | AWS ALB | ✅ Demo 14 | Load distribution |
| Monitoring | CloudWatch + Grafana | ✅ Demo 15 | Observability |
| Error Tracking | Sentry | ✅ Demo 15 | Error tracking |

---

## Final Architecture (Demo 19B)

**Repository**: [awsbedrock-demo-19b-react-app](https://github.com/inskillflow/awsbedrock-demo-19b-react-app)

### Ultra-Simplified Overview

```mermaid
flowchart TD
    Users[Users<br/>Web + Mobile]
    CDN[CloudFront CDN]
    LB[Load Balancer]
    App[Backend API<br/>FastAPI]
    Agents[Multi-Agent AI]
    DB[PostgreSQL<br/>+ pgvector]
    AWS[AWS Services<br/>Bedrock + S3 + SES]
    External[External Services<br/>Stripe + Clerk]
    
    Users --> CDN
    CDN --> LB
    LB --> App
    App --> Agents
    App --> DB
    App --> AWS
    App --> External
    Agents --> AWS
    Agents --> DB
    
    style Users fill:#61DAFB,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style CDN fill:#FF9900,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style LB fill:#FF6600,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style App fill:#009688,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Agents fill:#0891B2,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style DB fill:#1E40AF,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style AWS fill:#DD4814,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style External fill:#635BFF,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
```

### Diagram 1: Frontend → Backend Flow

```mermaid
flowchart LR
    React[React App]
    CDN[CloudFront]
    LB[Load Balancer]
    Auth[Auth]
    API[FastAPI]
    
    React --> CDN
    CDN --> LB
    LB --> Auth
    Auth --> API
    
    style React fill:#61DAFB,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style CDN fill:#FF9900,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style LB fill:#FF6600,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Auth fill:#6C5CE7,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style API fill:#009688,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
```

### Diagram 2: Backend → Database

```mermaid
flowchart TD
    API[FastAPI API]
    ORM[SQLAlchemy]
    DB[(PostgreSQL<br/>+ pgvector)]
    Replicas[(Replicas)]
    Cache[(Redis Cache)]
    
    API --> ORM
    API --> Cache
    ORM --> DB
    DB --> Replicas
    
    style API fill:#009688,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style ORM fill:#336791,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style DB fill:#1E40AF,stroke:#333,stroke-width:5px,color:#fff,font-size:18px
    style Replicas fill:#3B82F6,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Cache fill:#DC382D,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
```

### Diagram 3: Multi-Agent AI System

```mermaid
flowchart TD
    Question[User Question]
    Coord[Coordinator]
    HR[HR Agent]
    Recruiter[Recruiter]
    Comp[Compensation]
    RAG[RAG Engine]
    Bedrock[AWS Bedrock]
    DB[(PostgreSQL)]
    
    Question --> Coord
    Coord --> HR
    Coord --> Recruiter
    Coord --> Comp
    
    HR --> RAG
    Recruiter --> RAG
    Comp --> RAG
    
    HR --> Bedrock
    Recruiter --> Bedrock
    Comp --> Bedrock
    
    RAG --> DB
    
    style Question fill:#61DAFB,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style Coord fill:#0891B2,stroke:#333,stroke-width:5px,color:#fff,font-size:18px
    style HR fill:#0E7490,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Recruiter fill:#155E75,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Comp fill:#0C4A6E,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style RAG fill:#DC2626,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Bedrock fill:#FF6600,stroke:#333,stroke-width:5px,color:#fff,font-size:18px
    style DB fill:#1E40AF,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
```

### Diagram 4: External Services

```mermaid
flowchart LR
    API[Backend API]
    S3[AWS S3]
    Email[SES Email]
    Stripe[Stripe]
    Clerk[Clerk Auth]
    
    API --> S3
    API --> Email
    API --> Stripe
    API --> Clerk
    
    style API fill:#009688,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style S3 fill:#FF9900,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style Email fill:#DD4814,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Stripe fill:#635BFF,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Clerk fill:#6C5CE7,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
```

### Diagram 5: CI/CD Deployment

```mermaid
flowchart LR
    Dev[Developer]
    GitHub[GitHub]
    Actions[GitHub Actions]
    Docker[Docker Build]
    ECS[AWS ECS]
    
    Dev --> GitHub
    GitHub --> Actions
    Actions --> Docker
    Docker --> ECS
    
    style Dev fill:#2C3E50,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style GitHub fill:#24292E,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Actions fill:#2088FF,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Docker fill:#2496ED,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style ECS fill:#FF9900,stroke:#333,stroke-width:4px,color:#000,font-size:18px
```

### Diagram 6: Monitoring

```mermaid
flowchart TD
    App[Application]
    CloudWatch[CloudWatch]
    Prometheus[Prometheus]
    Grafana[Grafana]
    Sentry[Sentry]
    
    App --> CloudWatch
    App --> Sentry
    CloudWatch --> Prometheus
    Prometheus --> Grafana
    
    style App fill:#009688,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style CloudWatch fill:#DD4814,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Prometheus fill:#E6522C,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Grafana fill:#F46800,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Sentry fill:#362D59,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
```

### Enterprise Architecture - Simplified Diagrams

#### Diagram 7A: Multi-Tenant (Data Isolation)

```mermaid
flowchart TD
    Gateway[API Gateway]
    Router[Tenant Router]
    
    TenantA[Tenant A<br/>Company A]
    TenantB[Tenant B<br/>Company B]
    
    DBA[(DB Schema A)]
    DBB[(DB Schema B)]
    
    Gateway --> Router
    Router -->|tenant=A| TenantA
    Router -->|tenant=B| TenantB
    
    TenantA --> DBA
    TenantB --> DBB
    
    style Gateway fill:#047857,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Router fill:#059669,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style TenantA fill:#EF4444,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style TenantB fill:#3B82F6,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style DBA fill:#DC2626,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style DBB fill:#1D4ED8,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
```

#### Diagram 7B: Microservices

```mermaid
flowchart TD
    Gateway[API Gateway]
    
    Emp[Employee Service]
    AI[AI Service]
    Pay[Payment Service]
    Notif[Notification Service]
    File[File Service]
    
    Gateway --> Emp
    Gateway --> AI
    Gateway --> Pay
    Gateway --> Notif
    Gateway --> File
    
    style Gateway fill:#047857,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Emp fill:#0891B2,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style AI fill:#0E7490,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Pay fill:#155E75,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Notif fill:#0C4A6E,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style File fill:#075985,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
```

#### Diagram 7C: Message Queue (Asynchronous Tasks)

```mermaid
flowchart LR
    Services[Services]
    Queue[Message Queue<br/>SQS/RabbitMQ]
    EventBus[Event Bus]
    Workers[Background Workers]
    
    Services --> Queue
    Queue --> EventBus
    EventBus --> Workers
    
    style Services fill:#009688,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Queue fill:#F59E0B,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style EventBus fill:#D97706,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Workers fill:#B45309,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
```

#### Diagram 7D: Security

```mermaid
flowchart TD
    Internet[Internet]
    WAF[WAF<br/>Firewall]
    Shield[AWS Shield<br/>DDoS]
    App[Application]
    Secrets[Secrets Manager]
    KMS[KMS Encryption]
    
    Internet --> WAF
    WAF --> Shield
    Shield --> App
    App --> Secrets
    App --> KMS
    
    style Internet fill:#61DAFB,stroke:#333,stroke-width:4px,color:#000,font-size:18px
    style WAF fill:#DC2626,stroke:#333,stroke-width:5px,color:#fff,font-size:18px
    style Shield fill:#991B1B,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style App fill:#009688,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style Secrets fill:#7C3AED,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
    style KMS fill:#5B21B6,stroke:#333,stroke-width:4px,color:#fff,font-size:18px
```

### Complete Technology Stack

| Layer | Technologies | Demos |
|-------|--------------|-------|
| **Frontend** | React, TypeScript, Redux, TailwindCSS, Storybook | 19A, 19B |
| **Backend** | FastAPI, Python, Pydantic | 1-19 |
| **Auth** | Clerk, JWT, OAuth2 | 5A, 5B, 6 |
| **Database** | PostgreSQL, pgvector, Neon/Xata | 3, 4, 10 |
| **Caching** | Redis, ElastiCache | 12, 14 |
| **AI** | AWS Bedrock (Claude 3, Titan), LangChain, LangGraph | 2, 10, 11B |
| **Storage** | AWS S3 | 7 |
| **Payments** | Stripe | 9A |
| **Email** | AWS SES, SendGrid | 8 |
| **Notifications** | AWS SNS, Push | 8, 18B |
| **Exports** | reportlab, openpyxl, pandas | 9B |
| **Container** | Docker, Docker Compose | 12 |
| **Orchestration** | AWS ECS, Fargate | 14 |
| **CI/CD** | GitHub Actions, Terraform | 13, 14 |
| **Monitoring** | CloudWatch, Grafana, Prometheus, Sentry | 15 |
| **Load Balancer** | AWS ALB, CloudFront | 14 |
| **Security** | WAF, Shield, KMS, Secrets Manager | 14, 16 |
| **API** | REST, OpenAPI, Rate Limiting | 17 |
| **Documentation** | MkDocs, Sphinx, Storybook | 18A, 19A |

---

## Data Evolution

### Demo 1: In-Memory

```python
# employee_data.py
EMPLOYEES = [
    {"id": 1, "name": "Alice", ...}
]
```

### Demo 3: PostgreSQL

```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    ...
);
```

### Demo 10: + pgvector

```sql
CREATE EXTENSION vector;

ALTER TABLE employees 
ADD COLUMN embedding vector(1536);

CREATE INDEX ON employees 
USING ivfflat (embedding vector_cosine_ops);
```

### Demo 16: Multi-tenant

```sql
CREATE SCHEMA tenant_a;
CREATE SCHEMA tenant_b;

CREATE TABLE tenant_a.employees (...);
CREATE TABLE tenant_b.employees (...);
```

---

## Data Flows

### Simple Flow (Demo 1-3)

```
User → Frontend → API → Data → Database
```

### Flow with AI (Demo 10)

```
User → Frontend → API → AI Agent → RAG Engine → pgvector → Database
                                  → AWS Bedrock → Response
```

### Multi-Agent Flow (Demo 11B)

```
User Question
    ↓
Coordinator Agent
    ↓
├─→ HR Analyst Agent ─→ RAG ─→ Bedrock ─→ Response 1
├─→ Recruiter Agent ─→ RAG ─→ Bedrock ─→ Response 2
└─→ Compensation Agent ─→ RAG ─→ Bedrock ─→ Response 3
    ↓
Aggregated Response
    ↓
User
```

### Complete Flow with Webhooks (Demo 9A)

```
User → Payment UI → Stripe API
                      ↓
                   Webhook
                      ↓
                   Backend API
                      ↓
                 Update Subscription
                      ↓
                   Send Email (SES)
                      ↓
                   Update UI
```

---

## Scalability

### Horizontal Scaling

```mermaid
graph LR
    subgraph "Load Balancer"
        ALB[ALB]
    end
    
    subgraph "Auto Scaling Group"
        App1[App Instance 1]
        App2[App Instance 2]
        App3[App Instance 3]
        AppN[App Instance N]
    end
    
    subgraph "Database"
        Primary[(Primary DB)]
        Replica1[(Replica 1)]
        Replica2[(Replica 2)]
    end
    
    subgraph "Cache"
        Redis[(Redis Cluster)]
    end
    
    ALB --> App1
    ALB --> App2
    ALB --> App3
    ALB --> AppN
    
    App1 --> Redis
    App2 --> Redis
    App3 --> Redis
    AppN --> Redis
    
    App1 --> Primary
    App2 --> Primary
    App3 --> Primary
    AppN --> Primary
    
    Primary --> Replica1
    Primary --> Replica2
    
    App1 -.read.-> Replica1
    App2 -.read.-> Replica1
    App3 -.read.-> Replica2
    AppN -.read.-> Replica2
```

---

## Security by Layer

| Layer | Security Mechanisms | Demos |
|-------|---------------------|-------|
| **Frontend** | HTTPS, CORS, CSP, XSS Protection | 1-19 |
| **API** | JWT, OAuth2, Rate Limiting | 5A, 5B, 17 |
| **Application** | RBAC, Input Validation, SQL Injection Protection | 6 |
| **Network** | VPC, Security Groups, Private Subnets | 14 |
| **Data** | Encryption at Rest (KMS), Encryption in Transit (TLS) | 14, 16 |
| **Secrets** | AWS Secrets Manager, Environment Variables | 14 |
| **DDoS** | AWS Shield, WAF, CloudFront | 14 |
| **Monitoring** | CloudWatch Alarms, Sentry Alerts | 15 |

---

## Estimated Costs by Architecture

| Architecture | Monthly Cost | Users | Notes |
|--------------|--------------|-------|-------|
| Demo 1 (Local) | $0 | Development | Free |
| Demo 2 (+ AWS Bedrock) | $30-50 | Testing | Real AI |
| Demo 3 (+ Neon) | $30-50 | < 100 | Neon free tier |
| Demo 14 (Production) | $200-500 | 1000 | ECS + RDS + Bedrock |
| Demo 16 (Multi-tenant) | $500-2000 | 10,000 | Scale |
| Demo 19 (Enterprise) | $2000-5000 | 100,000 | Full scale |

---

## Performance Metrics

### Targets by Level

| Metric | Demo 1-3 | Demo 14 | Demo 19 |
|--------|----------|---------|---------|
| Response Time | < 1s | < 500ms | < 200ms |
| Availability | 95% | 99.5% | 99.9% |
| Concurrent Users | 10 | 1,000 | 100,000 |
| Requests/sec | 10 | 1,000 | 10,000 |
| Database Size | 1 MB | 10 GB | 1 TB |

---

## Evolution Summary

```mermaid
timeline
    title Architecture Evolution
    section Foundations
        Demo 1 : REST API + Local AI + Memory
    section Cloud
        Demo 2 : Real AWS Bedrock
    section Persistence
        Demo 3-4 : PostgreSQL / Xata
    section Security
        Demo 5-6 : Auth + RBAC
    section Features
        Demo 7-9 : S3 + Emails + Stripe + Exports
    section Advanced AI
        Demo 10-11 : RAG + pgvector + Multi-Agents
    section Production
        Demo 12-15 : Docker + CI/CD + AWS + Monitoring
    section Enterprise
        Demo 16-19 : Multi-tenant + Public API + React
```

---

**Author**: Haythem REHOUMA - Gneurone Inc.  
**Contact**: contact@gneuroneai.com  
**GitHub**: https://github.com/inskillflow
