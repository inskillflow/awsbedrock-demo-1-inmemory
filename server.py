"""
Serveur FastAPI pour la gestion des employés et compétences
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional, Set
import uvicorn

from employee_data import (
    get_skills, get_employees, get_employee_by_id,
    get_employees_by_skill, get_employees_by_department,
    add_employee, update_employee, delete_employee
)
from ai_agent import ai_agent

# Modèles Pydantic pour la validation des données
class EmployeeCreate(BaseModel):
    name: str
    email: str
    department: str
    position: str
    skills: List[str]
    experience_years: int
    salary: float

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    skills: Optional[List[str]] = None
    experience_years: Optional[int] = None
    salary: Optional[float] = None

class Employee(BaseModel):
    id: int
    name: str
    email: str
    department: str
    position: str
    skills: List[str]
    experience_years: int
    salary: float

class QuestionRequest(BaseModel):
    question: str

class AIResponse(BaseModel):
    success: bool
    answer: str
    model: str
    question: str
    error: Optional[str] = None

# Création de l'application FastAPI
app = FastAPI(
    title="Employee Management & AI Assistant API",
    description="""
## Système de Gestion des Employés avec Agent IA

Cette API permet de gérer les employés d'une entreprise et d'interagir avec un agent IA intelligent pour obtenir des insights sur les données RH.

### Fonctionnalités Principales

- **Gestion CRUD des employés** : Créer, lire, modifier, supprimer
- **Suivi des compétences** : Gestion des compétences techniques
- **Statistiques avancées** : Tableaux de bord et métriques
- **Agent IA intégré** : Questions intelligentes sur les données RH
- **Filtrage avancé** : Recherche par département, compétence, etc.

### Agent IA - Exemples de Questions

- "Combien d'employés avons-nous ?"
- "Qui a la compétence Python ?"
- "Quel est le salaire moyen par département ?"
- "Quels sont les employés les plus expérimentés ?"
- "Recommandations pour la formation"

### Modèles de Données

Consultez les schémas ci-dessous pour comprendre la structure des données.

### Interface Web

Accédez à l'interface web complète sur : [http://localhost:8002](http://localhost:8002)
    """,
    version="2.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    contact={
        "name": "Support API",
        "email": "support@company.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    servers=[
        {
            "url": "http://localhost:8002",
            "description": "Serveur de développement"
        }
    ],
    tags_metadata=[
        {
            "name": "employees",
            "description": "**Gestion des employés** - Opérations CRUD complètes pour la gestion des employés",
        },
        {
            "name": "skills",
            "description": "**Compétences** - Gestion des compétences techniques disponibles",
        },
        {
            "name": "stats",
            "description": "**Statistiques** - Métriques et analyses des données RH",
        },
        {
            "name": "ai-agent",
            "description": "**Agent IA** - Intelligence artificielle pour l'analyse des données employés",
        },
        {
            "name": "system",
            "description": "**Système** - Informations système et santé de l'API",
        }
    ]
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir les fichiers statiques (frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routes API

@app.get("/", tags=["system"])
async def root():
    """**Page d'accueil** - Interface web principale
    
    Redirige vers l'interface web complète avec toutes les fonctionnalités :
    - Gestion des employés
    - Compétences
    - Statistiques 
    - Assistant IA
    """
    return FileResponse("static/index.html")

@app.get("/api/guide", tags=["system"])
async def get_usage_guide():
    """**Guide d'utilisation complet**
    
    Retourne le guide d'utilisation détaillé du système.
    Contient toutes les informations nécessaires pour utiliser l'API et l'interface web.
    
    **Contenu du guide :**
    - Instructions de démarrage
    - Guide de l'interface web
    - Documentation de l'API
    - Exemples d'utilisation
    - Résolution de problèmes
    - Bonnes pratiques
    """
    try:
        with open("GUIDE_UTILISATION.md", "r", encoding="utf-8") as f:
            guide_content = f.read()
        return {
            "title": "Guide d'Utilisation - Système de Gestion des Employés avec IA",
            "version": "2.0.0",
            "format": "markdown",
            "content": guide_content,
            "last_updated": "2024-09-24",
            "sections": [
                "Vue d'ensemble",
                "Démarrage rapide", 
                "Interface web",
                "Assistant IA",
                "API REST",
                "Modèles de données",
                "Configuration",
                "Résolution de problèmes",
                "Bonnes pratiques"
            ]
        }
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Guide d'utilisation non trouvé"
        )

@app.get("/api/skills", response_model=List[str], tags=["skills"])
async def get_all_skills():
    """**Récupère toutes les compétences disponibles**
    
    Retourne la liste complète des compétences techniques suivies dans le système.
    Utile pour :
    - Validation lors de la création/modification d'employés
    - Affichage des filtres
    - Analyse des compétences disponibles
    """
    return list(get_skills())

@app.get("/api/employees", response_model=List[Employee], tags=["employees"])
async def get_all_employees():
    """**Récupère tous les employés**
    
    Retourne la liste complète des employés avec leurs informations :
    - Données personnelles (nom, email)
    - Poste et département
    - Compétences techniques
    - Années d'expérience et salaire
    """
    return get_employees()

@app.get("/api/employees/{employee_id}", response_model=Employee, tags=["employees"])
async def get_employee(employee_id: int):
    """**Récupère un employé par son ID**
    
    Retourne les détails complets d'un employé spécifique.
    Utile pour afficher un profil détaillé ou modifier les informations.
    
    - **employee_id**: Identifiant unique de l'employé
    """
    employee = get_employee_by_id(employee_id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employé avec l'ID {employee_id} non trouvé"
        )
    return employee

@app.get("/api/employees/skill/{skill}", response_model=List[Employee], tags=["employees"])
async def get_employees_by_skill_endpoint(skill: str):
    """**Recherche d'employés par compétence**
    
    Trouve tous les employés qui possèdent une compétence technique spécifique.
    Parfait pour identifier les experts dans un domaine ou constituer des équipes.
    
    - **skill**: Nom exact de la compétence (ex: "Python", "React", "AWS")
    
    **Exemples d'utilisation :**
    - Trouver tous les développeurs Python
    - Identifier les experts AWS
    - Constituer une équipe frontend React
    """
    employees = get_employees_by_skill(skill)
    if not employees:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Aucun employé trouvé avec la compétence '{skill}'"
        )
    return employees

@app.get("/api/employees/department/{department}", response_model=List[Employee], tags=["employees"])
async def get_employees_by_department_endpoint(department: str):
    """**Recherche d'employés par département**
    
    Retourne tous les employés appartenant à un département spécifique.
    Utile pour analyser la composition d'une équipe ou gérer les ressources par département.
    
    - **department**: Nom du département (ex: "Développement", "Marketing", "RH")
    
    **Exemples d'utilisation :**
    - Lister l'équipe de développement
    - Analyser les compétences par département
    - Calculer les budgets salariaux par équipe
    """
    employees = get_employees_by_department(department)
    if not employees:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Aucun employé trouvé dans le département '{department}'"
        )
    return employees

@app.post("/api/employees", response_model=Employee, status_code=status.HTTP_201_CREATED, tags=["employees"])
async def create_employee(employee: EmployeeCreate):
    """**Crée un nouvel employé**
    
    Ajoute un nouvel employé au système avec validation automatique des compétences.
    L'ID est généré automatiquement.
    
    **Validations effectuées :**
    - Compétences doivent exister dans le système
    - Email doit être valide
    - Années d'expérience >= 0
    - Salaire >= 0
    
    **Données requises :**
    - Nom complet
    - Adresse email
    - Département
    - Poste
    - Liste des compétences
    - Années d'expérience
    - Salaire
    """
    # Validation des compétences
    available_skills = get_skills()
    invalid_skills = [skill for skill in employee.skills if skill not in available_skills]
    if invalid_skills:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Compétences invalides: {invalid_skills}. Compétences disponibles: {list(available_skills)}"
        )
    
    new_employee = add_employee(employee.dict())
    return new_employee

@app.put("/api/employees/{employee_id}", response_model=Employee, tags=["employees"])
async def update_employee_endpoint(employee_id: int, employee_update: EmployeeUpdate):
    """**Met à jour un employé existant**
    
    Modifie les informations d'un employé existant. Seuls les champs fournis sont mis à jour,
    les autres restent inchangés (mise à jour partielle).
    
    **Paramètres :**
    - **employee_id**: ID de l'employé à modifier
    
    **Champs modifiables :**
    - Nom
    - Email
    - Département
    - Poste
    - Compétences (avec validation)
    - Années d'expérience
    - Salaire
    
    **Validations :**
    - L'employé doit exister
    - Les compétences doivent être valides
    """
    # Vérifier que l'employé existe
    existing_employee = get_employee_by_id(employee_id)
    if not existing_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employé avec l'ID {employee_id} non trouvé"
        )
    
    # Validation des compétences si fournies
    if employee_update.skills:
        available_skills = get_skills()
        invalid_skills = [skill for skill in employee_update.skills if skill not in available_skills]
        if invalid_skills:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Compétences invalides: {invalid_skills}. Compétences disponibles: {list(available_skills)}"
            )
    
    # Mettre à jour seulement les champs fournis
    update_data = {k: v for k, v in employee_update.dict().items() if v is not None}
    updated_employee = update_employee(employee_id, update_data)
    return updated_employee

@app.delete("/api/employees/{employee_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["employees"])
async def delete_employee_endpoint(employee_id: int):
    """**Supprime un employé**
    
    Supprime définitivement un employé du système.
    Cette action est irréversible.
    
    **Paramètres :**
    - **employee_id**: ID de l'employé à supprimer
    
    **Réponse :**
    - Status 204 (No Content) si la suppression réussit
    - Status 404 si l'employé n'existe pas
    
    **Attention :** Cette opération est définitive !
    """
    if not get_employee_by_id(employee_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employé avec l'ID {employee_id} non trouvé"
        )
    
    success = delete_employee(employee_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la suppression de l'employé"
        )

@app.get("/api/stats", tags=["stats"])
async def get_stats():
    """**Statistiques détaillées des employés**
    
    Génère des statistiques complètes sur les employés, départements et compétences.
    Parfait pour les tableaux de bord et analyses RH.
    
    **Données retournées :**
    - Nombre total d'employés
    - Statistiques par département (effectifs, salaire moyen)
    - Répartition des compétences
    - Salaire moyen global
    - Nombre total de compétences suivies
    
    **Exemples d'utilisation :**
    - Création de tableaux de bord RH
    - Analyse des coûts par département
    - Évaluation de la répartition des compétences
    - Rapports de direction
    """
    employees = get_employees()
    departments = {}
    skills_count = {}
    total_salary = 0
    
    for emp in employees:
        # Statistiques par département
        dept = emp["department"]
        if dept not in departments:
            departments[dept] = {"count": 0, "avg_salary": 0, "total_salary": 0}
        departments[dept]["count"] += 1
        departments[dept]["total_salary"] += emp["salary"]
        
        # Comptage des compétences
        for skill in emp["skills"]:
            skills_count[skill] = skills_count.get(skill, 0) + 1
        
        total_salary += emp["salary"]
    
    # Calcul des salaires moyens par département
    for dept_data in departments.values():
        dept_data["avg_salary"] = dept_data["total_salary"] / dept_data["count"]
        del dept_data["total_salary"]
    
    return {
        "total_employees": len(employees),
        "departments": departments,
        "skills_distribution": skills_count,
        "average_salary": total_salary / len(employees) if employees else 0,
        "total_skills": len(get_skills())
    }

# Routes pour l'Agent IA

@app.post("/api/inquire", response_model=AIResponse, tags=["ai-agent"])
async def ask_agent(request: QuestionRequest):
    """**Poser une question à l'agent IA**
    
    Interagit avec l'agent IA spécialisé en gestion des employés.
    L'agent utilise AWS Bedrock (Claude-3) ou un mode local selon la disponibilité.
    
    **Exemples de questions :**
    - "Combien d'employés avons-nous ?"
    - "Qui a la compétence Python ?"
    - "Quel est le salaire moyen par département ?"
    - "Quels sont les employés les plus expérimentés ?"
    - "Recommandations pour la formation de l'équipe"
    
    **Capacités de l'agent :**
    - Analyse des données employés
    - Statistiques et comparaisons
    - Recommandations basées sur les données
    - Réponses en langage naturel
    
    **Réponse inclut :**
    - Réponse de l'IA
    - Modèle utilisé (AWS Bedrock ou local)
    - Question originale
    - Status de succès
    """
    try:
        response = await ai_agent.process_question(request.question)
        return AIResponse(**response)
    except Exception as e:
        return AIResponse(
            success=False,
            answer="Désolé, une erreur s'est produite lors du traitement de votre question.",
            model="Error Handler",
            question=request.question,
            error=str(e)
        )

@app.get("/api/agent/health", tags=["ai-agent"])
async def agent_health_check():
    """**Vérifie l'état de l'agent IA**
    
    Retourne les informations de santé et de configuration de l'agent IA.
    Utile pour le monitoring et le débogage.
    
    **Informations retournées :**
    - Statut général de l'agent
    - Disponibilité d'AWS Bedrock
    - Modèle utilisé
    - Nombre d'employés chargés
    - Compétences disponibles
    - Résultat des tests de connectivité
    """
    return ai_agent.health_check()

@app.get("/api/agent/capabilities", tags=["ai-agent"])
async def get_agent_capabilities():
    """**Capacités de l'agent IA**
    
    Décrit les fonctionnalités et capacités de l'agent IA.
    Utile pour comprendre ce que l'agent peut faire et comment l'utiliser.
    
    **Informations incluses :**
    - Description de l'agent
    - Liste des capacités
    - Exemples de questions supportées
    - Sources de données disponibles
    - Statistiques en temps réel
    """
    return {
        "name": "Employee AI Assistant",
        "description": "Assistant IA spécialisé dans la gestion des ressources humaines",
        "version": "2.0.0",
        "powered_by": "AWS Bedrock (Claude-3 Sonnet) + Mode Local",
        "capabilities": [
            "Répondre aux questions sur les employés",
            "Analyser les compétences et départements", 
            "Fournir des statistiques RH",
            "Rechercher des employés par critères",
            "Comparer les profils d'employés",
            "Recommandations basées sur les données",
            "Analyses prédictives simples",
            "Suggestions d'amélioration RH"
        ],
        "supported_queries": [
            "Combien d'employés avons-nous ?",
            "Qui a la compétence Python ?",
            "Quel est le salaire moyen par département ?",
            "Quels sont les employés les plus expérimentés ?",
            "Répartition des compétences dans l'équipe",
            "Recommandations pour la formation",
            "Analyse des écarts salariaux",
            "Identification des experts par domaine"
        ],
        "data_sources": {
            "employees": len(get_employees()),
            "skills": len(get_skills()),
            "departments": len(set(emp['department'] for emp in get_employees()))
        },
        "response_formats": [
            "Texte naturel",
            "Listes structurées",
            "Analyses comparatives",
            "Recommandations actionables"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8002,
        reload=True,
        log_level="info"
    )
