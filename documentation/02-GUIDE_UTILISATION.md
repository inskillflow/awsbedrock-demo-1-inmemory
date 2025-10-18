# Guide Complet d'Utilisation - Système de Gestion des Employés avec IA

## Vue d'Ensemble

Ce système offre une solution complète de gestion des employés avec un agent IA intelligent intégré. Il combine une API REST FastAPI robuste, une interface web moderne et un assistant IA alimenté par AWS Bedrock.

## Démarrage Rapide

### 1. Installation

```bash
# Cloner ou naviguer vers le projet
cd C:\03-projetsGA\awsbedrock

# Installer les dépendances
pip install -r requirements.txt

# Démarrer le serveur
python server.py
```

### 2. Accès aux Interfaces

- **Interface Web** : http://localhost:8002
- **Documentation API (Swagger)** : http://localhost:8002/api/docs
- **Documentation Alternative (ReDoc)** : http://localhost:8002/api/redoc

## Interface Web - Guide Utilisateur

### Page d'Accueil
L'interface web propose 4 sections principales accessibles via les onglets :

#### **Onglet Employés**
- **Vue d'ensemble** : Liste de tous les employés avec leurs informations clés
- **Filtres avancés** :
  - **Recherche textuelle** : Par nom, email ou poste
  - **Filtre département** : Sélection par département
  - **Filtre compétence** : Recherche par compétence technique
- **Actions disponibles** :
  - **Ajouter** : Bouton "Ajouter Employé" en haut à droite
  - **Modifier** : Icône crayon sur chaque carte employé
  - **Supprimer** : Icône corbeille sur chaque carte employé

#### **Onglet Compétences**
- **Catalogue complet** : Toutes les compétences techniques disponibles
- **Statistiques** : Nombre d'employés par compétence
- **Visualisation** : Cartes colorées avec compteurs

#### **Onglet Statistiques**
- **Métriques globales** :
  - Total employés
  - Salaire moyen
  - Nombre de compétences
  - Nombre de départements
- **Analyses détaillées** :
  - Répartition par département (effectifs + salaire moyen)
  - Compétences les plus demandées (graphiques)

#### **Onglet Assistant IA**
- **Interface de chat** : Conversation en temps réel avec l'agent IA
- **Questions rapides** : Boutons pour questions fréquentes
- **Indicateurs de statut** : AWS Bedrock ou mode local
- **Historique** : Conservation des conversations

## Assistant IA - Guide d'Utilisation

### Capacités de l'Agent

L'assistant IA peut répondre à diverses questions sur vos données RH :

#### **Questions Statistiques**
```
"Combien d'employés avons-nous ?"
"Quel est le salaire moyen ?"
"Quelle est la répartition par département ?"
```

#### **Recherches Spécifiques**
```
"Qui a la compétence Python ?"
"Quels sont les développeurs frontend ?"
"Montrez-moi l'équipe DevOps"
```

#### **Analyses Avancées**
```
"Quels sont les employés les plus expérimentés ?"
"Quel département a le salaire moyen le plus élevé ?"
"Quelles compétences sont les plus populaires ?"
```

#### **Recommandations**
```
"Recommandations pour la formation de l'équipe"
"Quelles compétences manquent dans notre équipe ?"
"Suggestions pour améliorer la diversité des compétences"
```

### Modes de Fonctionnement

- **Mode AWS Bedrock** : Utilise Claude-3 Sonnet pour des réponses avancées
- **Mode Local** : Traitement intelligent local si AWS n'est pas configuré
- **Basculement automatique** : L'agent s'adapte selon la disponibilité

## API REST - Guide Développeur

### Base URL
```
http://localhost:8002/api
```

### Authentification
Aucune authentification requise pour le développement.

### Endpoints Principaux

#### **Gestion des Employés**

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/employees` | Liste tous les employés |
| `GET` | `/employees/{id}` | Détails d'un employé |
| `POST` | `/employees` | Créer un employé |
| `PUT` | `/employees/{id}` | Modifier un employé |
| `DELETE` | `/employees/{id}` | Supprimer un employé |

#### **Recherches Avancées**

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/employees/skill/{skill}` | Employés par compétence |
| `GET` | `/employees/department/{dept}` | Employés par département |

#### **Compétences**

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/skills` | Liste des compétences |

#### **Statistiques**

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/stats` | Statistiques complètes |

#### **Agent IA**

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| `POST` | `/inquire` | Poser une question à l'IA |
| `GET` | `/agent/health` | État de l'agent |
| `GET` | `/agent/capabilities` | Capacités de l'agent |

### Exemples d'Utilisation

#### Créer un Employé
```bash
curl -X POST "http://localhost:8002/api/employees" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Marie Dubois",
       "email": "marie.dubois@company.com",
       "department": "Data Science",
       "position": "Data Scientist Senior",
       "skills": ["Python", "Machine Learning", "SQL"],
       "experience_years": 4,
       "salary": 62000
     }'
```

#### Rechercher par Compétence
```bash
curl "http://localhost:8002/api/employees/skill/Python"
```

#### Poser une Question à l'IA
```bash
curl -X POST "http://localhost:8002/api/inquire" \
     -H "Content-Type: application/json" \
     -d '{"question": "Combien d'\''employés ont plus de 5 ans d'\''expérience ?"}'
```

#### Obtenir les Statistiques
```bash
curl "http://localhost:8002/api/stats"
```

## Modèles de Données

### **Employé (Employee)**
```json
{
  "id": 1,
  "name": "Alice Dupont",
  "email": "alice.dupont@company.com",
  "department": "Développement",
  "position": "Senior Developer",
  "skills": ["Python", "FastAPI", "AWS"],
  "experience_years": 5,
  "salary": 65000
}
```

### **Création d'Employé (EmployeeCreate)**
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

### **Mise à Jour d'Employé (EmployeeUpdate)**
```json
{
  "name": "string (optionnel)",
  "email": "string (optionnel)",
  "department": "string (optionnel)",
  "position": "string (optionnel)",
  "skills": ["string"] (optionnel),
  "experience_years": 0 (optionnel),
  "salary": 0 (optionnel)
}
```

### **Question IA (QuestionRequest)**
```json
{
  "question": "Combien d'employés avons-nous ?"
}
```

### **Réponse IA (AIResponse)**
```json
{
  "success": true,
  "answer": "Vous avez actuellement 5 employés...",
  "model": "Claude-3 Sonnet via AWS Bedrock",
  "question": "Combien d'employés avons-nous ?",
  "error": null
}
```

## Configuration Avancée

### Configuration AWS Bedrock (Optionnel)

Pour utiliser l'agent IA avec AWS Bedrock :

1. **Configurer les credentials AWS** :
```bash
aws configure
```

2. **Variables d'environnement** :
```bash
export AWS_REGION=us-east-1
export AWS_ACCESS_KEY_ID=your_key
export AWS_SECRET_ACCESS_KEY=your_secret
```

3. **Permissions IAM requises** :
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

### Personnalisation du Serveur

Modifiez `server.py` pour changer :
- **Port** : Ligne `port=8002`
- **Host** : Ligne `host="0.0.0.0"`
- **Mode debug** : Ligne `reload=True`

## Résolution de Problèmes

### Problèmes Courants

#### **"ModuleNotFoundError: No module named 'boto3'"**
```bash
pip install boto3 botocore
```

#### **L'agent IA ne répond pas**
- Vérifiez le statut avec : `GET /api/agent/health`
- L'agent fonctionne en mode local même sans AWS

#### **Erreur de compétences invalides**
- Consultez la liste des compétences : `GET /api/skills`
- Utilisez exactement les noms de compétences listés

#### **Interface web ne se charge pas**
- Vérifiez que le serveur fonctionne sur http://localhost:8002
- Contrôlez les logs du serveur pour les erreurs

### Logs et Debugging

Les logs du serveur affichent :
- Démarrage de l'agent IA
- Requêtes API
- Erreurs éventuelles
- Rechargements automatiques

## Bonnes Pratiques

### Utilisation de l'API
1. **Validation** : Toujours valider les données avant envoi
2. **Gestion d'erreurs** : Gérer les codes de statut HTTP
3. **Performance** : Utiliser les filtres pour réduire les données

### Utilisation de l'Assistant IA
1. **Questions précises** : Plus la question est claire, meilleure est la réponse
2. **Contexte** : Donnez du contexte pour des analyses complexes
3. **Itération** : Posez des questions de suivi pour approfondir

### Sécurité
1. **Données sensibles** : Ne jamais exposer en production sans authentification
2. **CORS** : Configurer correctement en production
3. **Rate limiting** : Implémenter des limites de requêtes si nécessaire

## Support et Communauté

### Ressources Utiles
- **Documentation Swagger** : http://localhost:8002/api/docs
- **Documentation ReDoc** : http://localhost:8002/api/redoc
- **Code source** : Fichiers du projet dans `C:\03-projetsGA\awsbedrock`

### Contact
- **Email** : support@company.com
- **Documentation API** : Consultez Swagger pour les détails techniques

---

**Vous êtes maintenant prêt à utiliser pleinement le système de gestion des employés avec IA !**
