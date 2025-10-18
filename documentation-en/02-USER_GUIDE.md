# Complete User Guide - Employee Management System with AI

## Overview

This system offers a complete employee management solution with an integrated intelligent AI agent. It combines a robust FastAPI REST API, a modern web interface, and an AI assistant powered by AWS Bedrock.

## Quick Start

### 1. Installation

```bash
# Clone or navigate to the project
cd C:\03-projetsGA\awsbedrock

# Install dependencies
pip install -r requirements.txt

# Start the server
python server.py
```

### 2. Access Interfaces

- **Web Interface**: http://localhost:8002
- **API Documentation (Swagger)**: http://localhost:8002/api/docs
- **Alternative Documentation (ReDoc)**: http://localhost:8002/api/redoc

## Web Interface - User Guide

### Home Page
The web interface offers 4 main sections accessible via tabs:

#### **Employees Tab**
- **Overview**: List of all employees with their key information
- **Advanced filters**:
  - **Text search**: By name, email, or position
  - **Department filter**: Selection by department
  - **Skill filter**: Search by technical skill
- **Available actions**:
  - **Add**: "Add Employee" button in the top right
  - **Edit**: Pencil icon on each employee card
  - **Delete**: Trash icon on each employee card

#### **Skills Tab**
- **Complete catalog**: All available technical skills
- **Statistics**: Number of employees per skill
- **Visualization**: Colored cards with counters

#### **Statistics Tab**
- **Global metrics**:
  - Total employees
  - Average salary
  - Number of skills
  - Number of departments
- **Detailed analyses**:
  - Distribution by department (headcount + average salary)
  - Most requested skills (charts)

#### **AI Assistant Tab**
- **Chat interface**: Real-time conversation with the AI agent
- **Quick questions**: Buttons for frequently asked questions
- **Status indicators**: AWS Bedrock or local mode
- **History**: Conversation preservation

## AI Assistant - Usage Guide

### Agent Capabilities

The AI assistant can answer various questions about your HR data:

#### **Statistical Questions**
```
"How many employees do we have?"
"What is the average salary?"
"What is the distribution by department?"
```

#### **Specific Searches**
```
"Who has Python skills?"
"Who are the frontend developers?"
"Show me the DevOps team"
```

#### **Advanced Analyses**
```
"Who are the most experienced employees?"
"Which department has the highest average salary?"
"What are the most popular skills?"
```

#### **Recommendations**
```
"Recommendations for team training"
"What skills are missing in our team?"
"Suggestions to improve skill diversity"
```

### Operating Modes

- **AWS Bedrock Mode**: Uses Claude-3 Sonnet for advanced responses
- **Local Mode**: Intelligent local processing if AWS is not configured
- **Automatic failover**: The agent adapts according to availability

## REST API - Developer Guide

### Base URL
```
http://localhost:8002/api
```

### Authentication
No authentication required for development.

### Main Endpoints

#### **Employee Management**

| Method | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/employees` | List all employees |
| `GET` | `/employees/{id}` | Employee details |
| `POST` | `/employees` | Create an employee |
| `PUT` | `/employees/{id}` | Update an employee |
| `DELETE` | `/employees/{id}` | Delete an employee |

#### **Advanced Searches**

| Method | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/employees/skill/{skill}` | Employees by skill |
| `GET` | `/employees/department/{dept}` | Employees by department |

#### **Skills**

| Method | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/skills` | List of skills |

#### **Statistics**

| Method | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/stats` | Complete statistics |

#### **AI Agent**

| Method | Endpoint | Description |
|---------|----------|-------------|
| `POST` | `/inquire` | Ask the AI a question |
| `GET` | `/agent/health` | Agent status |
| `GET` | `/agent/capabilities` | Agent capabilities |

### Usage Examples

#### Create an Employee
```bash
curl -X POST "http://localhost:8002/api/employees" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Marie Dubois",
       "email": "marie.dubois@company.com",
       "department": "Data Science",
       "position": "Senior Data Scientist",
       "skills": ["Python", "Machine Learning", "SQL"],
       "experience_years": 4,
       "salary": 62000
     }'
```

#### Search by Skill
```bash
curl "http://localhost:8002/api/employees/skill/Python"
```

#### Ask the AI a Question
```bash
curl -X POST "http://localhost:8002/api/inquire" \
     -H "Content-Type: application/json" \
     -d '{"question": "How many employees have more than 5 years of experience?"}'
```

#### Get Statistics
```bash
curl "http://localhost:8002/api/stats"
```

## Data Models

### **Employee**
```json
{
  "id": 1,
  "name": "Alice Dupont",
  "email": "alice.dupont@company.com",
  "department": "Development",
  "position": "Senior Developer",
  "skills": ["Python", "FastAPI", "AWS"],
  "experience_years": 5,
  "salary": 65000
}
```

### **Employee Creation (EmployeeCreate)**
```json
{
  "name": "string",
  "email": "string",
  "department": "string",
  "position": "string",
  "skills": ["string"],
  "experience_years": 0,
  "salary": 0
}
```

### **Employee Update (EmployeeUpdate)**
```json
{
  "name": "string (optional)",
  "email": "string (optional)",
  "department": "string (optional)",
  "position": "string (optional)",
  "skills": ["string"] (optional),
  "experience_years": 0 (optional),
  "salary": 0 (optional)
}
```

### **AI Question (QuestionRequest)**
```json
{
  "question": "How many employees do we have?"
}
```

### **AI Response (AIResponse)**
```json
{
  "success": true,
  "answer": "You currently have 5 employees...",
  "model": "Claude-3 Sonnet via AWS Bedrock",
  "question": "How many employees do we have?",
  "error": null
}
```

## Advanced Configuration

### AWS Bedrock Configuration (Optional)

To use the AI agent with AWS Bedrock:

1. **Configure AWS credentials**:
```bash
aws configure
```

2. **Environment variables**:
```bash
export AWS_REGION=us-east-1
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
```

3. **Required IAM permissions**:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel"
            ],
            "Resource": "arn:aws:bedrock:*:*:model/anthropic.claude-3-sonnet-20240229-v1:0"
        }
    ]
}
```

### Server Customization

Modify `server.py` to change:
- **Port**: Line `port=8002`
- **Host**: Line `host="0.0.0.0"`
- **Debug mode**: Line `reload=True`

## Troubleshooting

### Common Problems

#### **"ModuleNotFoundError: No module named 'boto3'"**
```bash
pip install boto3 botocore
```

#### **AI agent not responding**
- Check status with: `GET /api/agent/health`
- The agent works in local mode even without AWS

#### **Invalid skills error**
- Check the skills list: `GET /api/skills`
- Use exactly the listed skill names

#### **Web interface not loading**
- Verify the server is running on http://localhost:8002
- Check server logs for errors

### Logs and Debugging

Server logs display:
- AI agent startup
- API requests
- Any errors
- Automatic reloads

## Best Practices

### API Usage
1. **Validation**: Always validate data before sending
2. **Error handling**: Handle HTTP status codes
3. **Performance**: Use filters to reduce data

### Using the AI Assistant
1. **Precise questions**: The clearer the question, the better the response
2. **Context**: Provide context for complex analyses
3. **Iteration**: Ask follow-up questions to delve deeper

### Security
1. **Sensitive data**: Never expose in production without authentication
2. **CORS**: Configure correctly in production
3. **Rate limiting**: Implement request limits if necessary

## Support and Community

### Useful Resources
- **Swagger Documentation**: http://localhost:8002/api/docs
- **ReDoc Documentation**: http://localhost:8002/api/redoc
- **Source code**: Project files in `C:\03-projetsGA\awsbedrock`

### Contact
- **Email**: support@company.com
- **API Documentation**: Check Swagger for technical details

---

**You are now ready to fully use the employee management system with AI!**

