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

**Author**: Haythem REHOUMA - Gneurone Inc.  
**Contact**: contact@gneuroneai.com  
**GitHub**: https://github.com/inskillflow

