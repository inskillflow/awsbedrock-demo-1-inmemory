# Prerequisites and Installation - Employee Management System with AI

This guide explains step by step how to install and configure the system.

## Required Prerequisites

Before starting, make sure you have:

### 1. Required Software

- **Python 3.9 to 3.13**
  - Check with: `python --version`
  - Download: https://www.python.org/downloads/
  - **Recommended:** Python 3.11 or 3.12 (more stable)
  - **Note:** Python 3.13 works but may have compilation issues

- **pip (Python package manager)**
  - Usually installed with Python
  - Check with: `pip --version`
  - **Important:** Update pip: `python -m pip install --upgrade pip`

- **Git (optional but recommended)**
  - To clone the project
  - Download: https://git-scm.com/

### 2. AWS Account (OPTIONAL)

**IMPORTANT:** The system works with OR without an AWS account!

- **WITH AWS**: The AI assistant will use Claude-3 via AWS Bedrock (more intelligent)
- **WITHOUT AWS**: The AI assistant will use local mode (functional but more basic)

If you want to use AWS Bedrock:
- An active AWS account
- Access to AWS Bedrock in your region
- Configured AWS credentials (Access Key + Secret Key)

---

## Step-by-Step Installation

### STEP 1: Download the Project

**Option A - If you have Git:**
```bash
git clone <repo-url>
cd awsbedrock
```

**Option B - Without Git:**
1. Download the project ZIP
2. Extract it to a folder
3. Open a terminal in that folder

---

### STEP 2: Create a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear in your terminal.

---

### STEP 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This command installs:
- FastAPI (web server)
- Uvicorn (ASGI server)
- Boto3 (AWS SDK)
- Pydantic (data validation)
- And other necessary dependencies

---

### STEP 4: AWS Configuration (OPTIONAL)

**IF YOU DON'T WANT TO USE AWS:**
- Go directly to STEP 5
- The system will work in local mode

**IF YOU WANT TO USE AWS BEDROCK:**

#### 4.1 - Create an AWS Account

1. Go to https://aws.amazon.com/
2. Click on "Create an AWS Account"
3. Follow the instructions (credit card required)
4. Activate your account

#### 4.2 - Activate AWS Bedrock

1. Log in to the AWS console
2. Search for "Bedrock" in the search bar
3. Select the **us-east-1** region (N. Virginia)
4. Go to "Model access"
5. Click on "Request model access"
6. Check **Anthropic Claude 3 Sonnet**
7. Click on "Request model access"
8. Wait for approval (usually instant)

#### 4.3 - Create AWS Credentials

1. In the AWS console, go to **IAM** (Identity and Access Management)
2. Click on **Users**
3. Click on **Create user**
4. Username: `bedrock-app-user`
5. Check "Provide user access to the AWS Management Console" if needed
6. Click on **Next**

#### 4.4 - Attach Permissions

1. Select **Attach policies directly**
2. Search for and check: `AmazonBedrockFullAccess`
3. Click on **Next**, then **Create user**

#### 4.5 - Create Access Keys

1. Click on the created user
2. Go to the **Security credentials** tab
3. Scroll down to "Access keys"
4. Click on **Create access key**
5. Select "Application running outside AWS"
6. Click on **Next**, then **Create access key**
7. **IMPORTANT:** Note your **Access Key ID** and **Secret Access Key**
   (you won't be able to see the secret again!)

#### 4.6 - Configure Credentials Locally

**Method 1 - Via AWS CLI (Recommended):**

1. Install AWS CLI:
   - Windows: https://aws.amazon.com/cli/
   - Mac: `brew install awscli`
   - Linux: `pip install awscli`

2. Configure:
```bash
aws configure
```

3. Enter:
   - AWS Access Key ID: [Your Access Key]
   - AWS Secret Access Key: [Your Secret Key]
   - Default region name: `us-east-1`
   - Default output format: `json`

**Method 2 - Environment Variables:**

**On Windows (PowerShell):**
```powershell
$env:AWS_ACCESS_KEY_ID="your_access_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret_key"
$env:AWS_DEFAULT_REGION="us-east-1"
```

**On Linux/Mac:**
```bash
export AWS_ACCESS_KEY_ID="your_access_key"
export AWS_SECRET_ACCESS_KEY="your_secret_key"
export AWS_DEFAULT_REGION="us-east-1"
```

**Method 3 - .env File (Alternative):**

Create a `.env` file at the project root:
```
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=us-east-1
```

---

### STEP 5: Verify Installation

Verify that everything is properly installed:

```bash
python -c "import fastapi, boto3; print('Installation OK!')"
```

If you see "Installation OK!", you're good!

---

### STEP 6: Start the Server

```bash
python server.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8002
INFO:     Application startup complete.
```

---

### STEP 7: Access the Application

Open your web browser and go to:

- **Main interface:** http://localhost:8002
- **API documentation:** http://localhost:8002/api/docs
- **Alternative documentation:** http://localhost:8002/api/redoc

---

## Operation Verification

### Test 1: Web Interface

1. Go to http://localhost:8002
2. You should see the list of employees
3. Try adding an employee
4. Check the tabs: Skills, Statistics

### Test 2: AI Assistant

1. Click on the "AI Assistant" tab
2. Look at the status in the top right:
   - **"AI"** = AWS Bedrock working
   - **"OK"** = Local mode active
   - **"ERR"** = Configuration problem

3. Ask a question: "How many employees do we have?"
4. The assistant should respond

### Test 3: REST API

Test the API with curl or directly in the documentation:

```bash
curl http://localhost:8002/api/employees
```

You should receive the list of employees in JSON.

---

## Common Problem Resolution

### Problem: "Module not found"

**Solution:**
```bash
pip install -r requirements.txt --force-reinstall
```

### Problem: "Cargo, the Rust package manager, is not installed" or compilation errors

This problem usually occurs with Python 3.13 or packages that need to be compiled.

**Solution 1 - Update pip and retry (RECOMMENDED):**
```bash
python -m pip install --upgrade pip
pip install --upgrade setuptools wheel
pip install -r requirements.txt
```

**Solution 2 - Install packages one by one:**
```bash
pip install fastapi uvicorn boto3 pydantic python-multipart
```

**Solution 3 - Use pre-compiled versions:**
```bash
pip install fastapi uvicorn boto3 pydantic --only-binary :all:
pip install python-multipart
```

**Solution 4 - Downgrade Python (if nothing works):**
- Uninstall Python 3.13
- Install Python 3.11 or 3.12
- Recreate the virtual environment

### Problem: "Port 8002 already in use"

**Solution:**
- Another process is using port 8002
- Kill the process or change the port in `server.py` (line 559)

### Problem: AI assistant not working

**Diagnosis:**
1. Go to http://localhost:8002/api/agent/health
2. Check the returned JSON

**If `bedrock_available: false`:**
- Check your AWS credentials
- Verify that Bedrock is activated in us-east-1
- Check IAM permissions

**If `agent_status: "unhealthy"`:**
- Restart the server
- Check logs in the terminal

### Problem: AWS Access Denied

**Solution:**
1. Verify that the IAM user has the `AmazonBedrockFullAccess` permission
2. Verify that Claude 3 Sonnet is activated in Bedrock
3. Check the region (must be us-east-1)

### Problem: AWS credentials not recognized

**Solution:**
1. Verify that credentials are properly configured:
```bash
aws sts get-caller-identity
```

2. If error, reconfigure:
```bash
aws configure
```

---

## Important File Structure

```
awsbedrock/
├── server.py              # Main server (to launch)
├── employee_data.py       # Employee data
├── ai_agent.py           # AI Agent (AWS Bedrock)
├── requirements.txt      # Python dependencies
├── static/               # Web interface
│   ├── index.html       # Main page
│   ├── app.js           # Frontend JavaScript
│   └── guide.html       # User guide
└── documentation/        # Documentation
    ├── 01-GUIDE_UTILISATION.md
    └── 02-PREREQUISITES_ET_INSTALLATION.md  # This file
```

---

## AWS Costs (IMPORTANT)

### FREE Mode (Free Tier)

AWS Bedrock offers a limited free trial:
- **First 2 months**: Included in the Free Tier
- **After**: Pay-as-you-go billing

### Claude 3 Sonnet Pricing

**Approximate prices (us-east-1):**
- Input: ~$0.003 per 1000 tokens (~750 words)
- Output: ~$0.015 per 1000 tokens

**Estimate for this project:**
- One question = approximately 1500-2000 tokens
- Cost per question: ~$0.02-0.05
- 100 questions = ~$2-5

### How to Control Costs

1. **Use local mode** if you don't want to pay
2. **Monitor AWS Cost Explorer** in the AWS console
3. **Set up billing alerts** (AWS Budget)
4. **Define a spending limit**

### Disable AWS Bedrock

If you want to stop charges:
1. Remove your AWS credentials from the configuration
2. The system will automatically switch to local mode
3. Or completely delete the IAM user

---

## Support and Help

### AWS Bedrock Documentation

- Official guide: https://docs.aws.amazon.com/bedrock/
- Pricing: https://aws.amazon.com/bedrock/pricing/
- AWS Console: https://console.aws.amazon.com/

### Project Documentation

- Main README: `README.md`
- User guide: `documentation/01-GUIDE_UTILISATION.md`
- API documentation: http://localhost:8002/api/docs (when server is running)

### Useful Commands

```bash
# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Deactivate virtual environment
deactivate

# Start server
python server.py

# Check AWS credentials
aws sts get-caller-identity

# Test API
curl http://localhost:8002/api/employees

# View logs in real-time
# (Logs are displayed in the terminal where you launched server.py)
```

---

## Final Checklist

Before considering the installation complete, verify:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] AWS configured (if desired) or local mode accepted
- [ ] Server starts without error (`python server.py`)
- [ ] Web interface accessible (http://localhost:8002)
- [ ] Employee list visible
- [ ] AI assistant responds to questions
- [ ] REST API works (http://localhost:8002/api/docs)

If all points are checked, congratulations! Your system is operational.

---

## Next Steps

Now that your system is installed:

1. **Explore the web interface** - Add, modify, delete employees
2. **Test the AI assistant** - Ask various questions about employees
3. **Consult the API documentation** - Explore available endpoints
4. **Read the user guide** - `documentation/01-GUIDE_UTILISATION.md`
5. **Customize the system** - Add your own employees and skills

Happy development!

