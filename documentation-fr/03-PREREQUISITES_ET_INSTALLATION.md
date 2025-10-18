# Prérequis et Installation - Système de Gestion des Employés avec IA

Ce guide vous explique étape par étape comment installer et configurer le système.

## Prérequis Nécessaires

Avant de commencer, assurez-vous d'avoir :

### 1. Logiciels Requis

- **Python 3.9 à 3.13**
  - Vérifiez avec : `python --version`
  - Téléchargement : https://www.python.org/downloads/
  - **Recommandé :** Python 3.11 ou 3.12 (plus stable)
  - **Note :** Python 3.13 fonctionne mais peut avoir des problèmes de compilation

- **pip (gestionnaire de paquets Python)**
  - Normalement installé avec Python
  - Vérifiez avec : `pip --version`
  - **Important :** Mettez à jour pip : `python -m pip install --upgrade pip`

- **Git (optionnel mais recommandé)**
  - Pour cloner le projet
  - Téléchargement : https://git-scm.com/

### 2. Compte AWS (OPTIONNEL)

**IMPORTANT :** Le système fonctionne avec OU sans compte AWS !

- **AVEC AWS** : L'assistant IA utilisera Claude-3 via AWS Bedrock (plus intelligent)
- **SANS AWS** : L'assistant IA utilisera un mode local (fonctionnel mais plus basique)

Si vous voulez utiliser AWS Bedrock :
- Un compte AWS actif
- Accès à AWS Bedrock dans votre région
- Credentials AWS configurés (Access Key + Secret Key)

---

## Installation Étape par Étape

### ÉTAPE 1 : Télécharger le Projet

**Option A - Si vous avez Git :**
```bash
git clone <url-du-repo>
cd awsbedrock
```

**Option B - Sans Git :**
1. Téléchargez le ZIP du projet
2. Extrayez-le dans un dossier
3. Ouvrez un terminal dans ce dossier

---

### ÉTAPE 2 : Créer un Environnement Virtuel (Recommandé)

**Sur Windows :**
```bash
python -m venv venv
venv\Scripts\activate
```

**Sur Linux/Mac :**
```bash
python3 -m venv venv
source venv/bin/activate
```

Vous devriez voir `(venv)` apparaître dans votre terminal.

---

### ÉTAPE 3 : Installer les Dépendances Python

```bash
pip install -r requirements.txt
```

Cette commande installe :
- FastAPI (serveur web)
- Uvicorn (serveur ASGI)
- Boto3 (SDK AWS)
- Pydantic (validation des données)
- Et autres dépendances nécessaires

---

### ÉTAPE 4 : Configuration AWS (OPTIONNEL)

**SI VOUS NE VOULEZ PAS UTILISER AWS :**
- Passez directement à l'ÉTAPE 5
- Le système fonctionnera en mode local

**SI VOUS VOULEZ UTILISER AWS BEDROCK :**

#### 4.1 - Créer un Compte AWS

1. Allez sur https://aws.amazon.com/
2. Cliquez sur "Créer un compte AWS"
3. Suivez les instructions (carte bancaire requise)
4. Activez votre compte

#### 4.2 - Activer AWS Bedrock

1. Connectez-vous à la console AWS
2. Recherchez "Bedrock" dans la barre de recherche
3. Sélectionnez la région **us-east-1** (Virginie du Nord)
4. Allez dans "Model access" (Accès aux modèles)
5. Cliquez sur "Request model access"
6. Cochez **Anthropic Claude 3 Sonnet**
7. Cliquez sur "Request model access"
8. Attendez l'approbation (généralement instantané)

#### 4.3 - Créer des Credentials AWS

1. Dans la console AWS, allez dans **IAM** (Identity and Access Management)
2. Cliquez sur **Users** (Utilisateurs)
3. Cliquez sur **Create user** (Créer un utilisateur)
4. Nom d'utilisateur : `bedrock-app-user`
5. Cochez "Provide user access to the AWS Management Console" si nécessaire
6. Cliquez sur **Next**

#### 4.4 - Attacher les Permissions

1. Sélectionnez **Attach policies directly**
2. Recherchez et cochez : `AmazonBedrockFullAccess`
3. Cliquez sur **Next**, puis **Create user**

#### 4.5 - Créer des Access Keys

1. Cliquez sur l'utilisateur créé
2. Allez dans l'onglet **Security credentials**
3. Descendez à "Access keys"
4. Cliquez sur **Create access key**
5. Sélectionnez "Application running outside AWS"
6. Cliquez sur **Next**, puis **Create access key**
7. **IMPORTANT :** Notez votre **Access Key ID** et **Secret Access Key**
   (vous ne pourrez plus voir le secret après !)

#### 4.6 - Configurer les Credentials Localement

**Méthode 1 - Via AWS CLI (Recommandé) :**

1. Installez AWS CLI :
   - Windows : https://aws.amazon.com/cli/
   - Mac : `brew install awscli`
   - Linux : `pip install awscli`

2. Configurez :
```bash
aws configure
```

3. Entrez :
   - AWS Access Key ID : [Votre Access Key]
   - AWS Secret Access Key : [Votre Secret Key]
   - Default region name : `us-east-1`
   - Default output format : `json`

**Méthode 2 - Variables d'Environnement :**

**Sur Windows (PowerShell) :**
```powershell
$env:AWS_ACCESS_KEY_ID="votre_access_key"
$env:AWS_SECRET_ACCESS_KEY="votre_secret_key"
$env:AWS_DEFAULT_REGION="us-east-1"
```

**Sur Linux/Mac :**
```bash
export AWS_ACCESS_KEY_ID="votre_access_key"
export AWS_SECRET_ACCESS_KEY="votre_secret_key"
export AWS_DEFAULT_REGION="us-east-1"
```

**Méthode 3 - Fichier .env (Alternative) :**

Créez un fichier `.env` à la racine du projet :
```
AWS_ACCESS_KEY_ID=votre_access_key
AWS_SECRET_ACCESS_KEY=votre_secret_key
AWS_DEFAULT_REGION=us-east-1
```

---

### ÉTAPE 5 : Vérifier l'Installation

Vérifiez que tout est bien installé :

```bash
python -c "import fastapi, boto3; print('Installation OK!')"
```

Si vous voyez "Installation OK!", c'est bon !

---

### ÉTAPE 6 : Lancer le Serveur

```bash
python server.py
```

Vous devriez voir :
```
INFO:     Uvicorn running on http://0.0.0.0:8002
INFO:     Application startup complete.
```

---

### ÉTAPE 7 : Accéder à l'Application

Ouvrez votre navigateur web et allez sur :

- **Interface principale :** http://localhost:8002
- **Documentation API :** http://localhost:8002/api/docs
- **Documentation alternative :** http://localhost:8002/api/redoc

---

## Vérification du Fonctionnement

### Test 1 : Interface Web

1. Allez sur http://localhost:8002
2. Vous devriez voir la liste des employés
3. Essayez d'ajouter un employé
4. Vérifiez les onglets : Compétences, Statistiques

### Test 2 : Assistant IA

1. Cliquez sur l'onglet "Assistant IA"
2. Regardez le statut en haut à droite :
   - **"AI"** = AWS Bedrock fonctionne
   - **"OK"** = Mode local activé
   - **"ERR"** = Problème de configuration

3. Posez une question : "Combien d'employés avons-nous ?"
4. L'assistant devrait répondre

### Test 3 : API REST

Testez l'API avec curl ou directement dans la documentation :

```bash
curl http://localhost:8002/api/employees
```

Vous devriez recevoir la liste des employés en JSON.

---

## Résolution des Problèmes Courants

### Problème : "Module not found"

**Solution :**
```bash
pip install -r requirements.txt --force-reinstall
```

### Problème : "Cargo, the Rust package manager, is not installed" ou erreurs de compilation

Ce problème arrive généralement avec Python 3.13 ou des packages qui doivent être compilés.

**Solution 1 - Mettre à jour pip et réessayer (RECOMMANDÉ) :**
```bash
python -m pip install --upgrade pip
pip install --upgrade setuptools wheel
pip install -r requirements.txt
```

**Solution 2 - Installer les packages un par un :**
```bash
pip install fastapi uvicorn boto3 pydantic python-multipart
```

**Solution 3 - Utiliser des versions sans compilation :**
```bash
pip install fastapi uvicorn boto3 pydantic --only-binary :all:
pip install python-multipart
```

**Solution 4 - Downgrader Python (si vraiment rien ne fonctionne) :**
- Désinstallez Python 3.13
- Installez Python 3.11 ou 3.12
- Recréez l'environnement virtuel

### Problème : "Port 8002 already in use"

**Solution :**
- Un autre processus utilise le port 8002
- Tuez le processus ou changez le port dans `server.py` (ligne 559)

### Problème : L'assistant IA ne fonctionne pas

**Diagnostic :**
1. Allez sur http://localhost:8002/api/agent/health
2. Vérifiez le JSON retourné

**Si `bedrock_available: false` :**
- Vérifiez vos credentials AWS
- Vérifiez que Bedrock est activé dans us-east-1
- Vérifiez les permissions IAM

**Si `agent_status: "unhealthy"` :**
- Redémarrez le serveur
- Vérifiez les logs dans le terminal

### Problème : AWS Access Denied

**Solution :**
1. Vérifiez que l'utilisateur IAM a la permission `AmazonBedrockFullAccess`
2. Vérifiez que Claude 3 Sonnet est activé dans Bedrock
3. Vérifiez la région (doit être us-east-1)

### Problème : Credentials AWS non reconnus

**Solution :**
1. Vérifiez que les credentials sont bien configurés :
```bash
aws sts get-caller-identity
```

2. Si erreur, reconfigurez :
```bash
aws configure
```

---

## Structure des Fichiers Importants

```
awsbedrock/
├── server.py              # Serveur principal (à lancer)
├── employee_data.py       # Données des employés
├── ai_agent.py           # Agent IA (AWS Bedrock)
├── requirements.txt      # Dépendances Python
├── static/               # Interface web
│   ├── index.html       # Page principale
│   ├── app.js           # JavaScript frontend
│   └── guide.html       # Guide d'utilisation
└── documentation/        # Documentation
    ├── 01-GUIDE_UTILISATION.md
    └── 02-PREREQUISITES_ET_INSTALLATION.md  # Ce fichier
```

---

## Coûts AWS (IMPORTANT)

### Mode GRATUIT (Free Tier)

AWS Bedrock offre un essai gratuit limité :
- **2 premiers mois** : Inclus dans le Free Tier
- **Après** : Facturation à l'usage

### Tarification Claude 3 Sonnet

**Prix approximatifs (us-east-1) :**
- Input : ~$0.003 par 1000 tokens (~750 mots)
- Output : ~$0.015 par 1000 tokens

**Estimation pour ce projet :**
- Une question = environ 1500-2000 tokens
- Coût par question : ~$0.02-0.05
- 100 questions = ~$2-5

### Comment Contrôler les Coûts

1. **Utilisez le mode local** si vous ne voulez pas payer
2. **Surveillez AWS Cost Explorer** dans la console AWS
3. **Configurez des alertes billing** (Budget AWS)
4. **Définissez une limite de dépenses**

### Désactiver AWS Bedrock

Si vous voulez arrêter les frais :
1. Supprimez vos credentials AWS de la configuration
2. Le système passera automatiquement en mode local
3. Ou supprimez complètement l'utilisateur IAM

---

## Support et Aide

### Documentation AWS Bedrock

- Guide officiel : https://docs.aws.amazon.com/bedrock/
- Tarification : https://aws.amazon.com/bedrock/pricing/
- Console AWS : https://console.aws.amazon.com/

### Documentation du Projet

- README principal : `README.md`
- Guide d'utilisation : `documentation/01-GUIDE_UTILISATION.md`
- Documentation API : http://localhost:8002/api/docs (quand le serveur tourne)

### Commandes Utiles

```bash
# Activer l'environnement virtuel
# Windows :
venv\Scripts\activate
# Linux/Mac :
source venv/bin/activate

# Désactiver l'environnement virtuel
deactivate

# Lancer le serveur
python server.py

# Vérifier les credentials AWS
aws sts get-caller-identity

# Tester l'API
curl http://localhost:8002/api/employees

# Voir les logs en temps réel
# (Les logs s'affichent dans le terminal où vous avez lancé server.py)
```

---

## Checklist Finale

Avant de considérer l'installation terminée, vérifiez :

- [ ] Python 3.8+ installé
- [ ] Environnement virtuel créé et activé
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] AWS configuré (si désiré) ou mode local accepté
- [ ] Serveur lance sans erreur (`python server.py`)
- [ ] Interface web accessible (http://localhost:8002)
- [ ] Liste des employés visible
- [ ] Assistant IA répond aux questions
- [ ] API REST fonctionne (http://localhost:8002/api/docs)

Si tous les points sont cochés, félicitations ! Votre système est opérationnel.

---

## Prochaines Étapes

Maintenant que votre système est installé :

1. **Explorez l'interface web** - Ajoutez, modifiez, supprimez des employés
2. **Testez l'assistant IA** - Posez diverses questions sur les employés
3. **Consultez la documentation API** - Explorez les endpoints disponibles
4. **Lisez le guide d'utilisation** - `documentation/01-GUIDE_UTILISATION.md`
5. **Personnalisez le système** - Ajoutez vos propres employés et compétences

Bon développement !

