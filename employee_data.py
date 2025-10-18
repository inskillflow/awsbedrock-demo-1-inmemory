"""
Module contenant les données et fonctions pour la gestion des employés
"""

from typing import List, Dict, Set

# Données des compétences disponibles
SKILLS = {
    "Python", "JavaScript", "React", "FastAPI", "AWS", "Docker", 
    "Machine Learning", "Data Analysis", "SQL", "NoSQL", "Git",
    "CI/CD", "Kubernetes", "Terraform", "MongoDB", "PostgreSQL",
    "Node.js", "Vue.js", "Angular", "TypeScript", "GraphQL"
}

# Données des employés
EMPLOYEES = [
    {
        "id": 1,
        "name": "Alice Dupont",
        "email": "alice.dupont@company.com",
        "department": "Développement",
        "position": "Senior Developer",
        "skills": ["Python", "FastAPI", "AWS", "Machine Learning", "SQL"],
        "experience_years": 5,
        "salary": 65000
    },
    {
        "id": 2,
        "name": "Bob Martin",
        "email": "bob.martin@company.com", 
        "department": "Frontend",
        "position": "Frontend Developer",
        "skills": ["JavaScript", "React", "Vue.js", "TypeScript", "CSS"],
        "experience_years": 3,
        "salary": 45000
    },
    {
        "id": 3,
        "name": "Claire Rousseau",
        "email": "claire.rousseau@company.com",
        "department": "DevOps",
        "position": "DevOps Engineer", 
        "skills": ["Docker", "Kubernetes", "AWS", "Terraform", "CI/CD"],
        "experience_years": 4,
        "salary": 58000
    },
    {
        "id": 4,
        "name": "David Chen",
        "email": "david.chen@company.com",
        "department": "Data",
        "position": "Data Scientist",
        "skills": ["Python", "Machine Learning", "Data Analysis", "SQL", "MongoDB"],
        "experience_years": 6,
        "salary": 70000
    },
    {
        "id": 5,
        "name": "Emma Wilson",
        "email": "emma.wilson@company.com",
        "department": "Backend",
        "position": "Backend Developer",
        "skills": ["Node.js", "PostgreSQL", "GraphQL", "Docker", "Git"],
        "experience_years": 2,
        "salary": 42000
    }
]

def get_skills() -> Set[str]:
    """Retourne toutes les compétences disponibles"""
    return SKILLS

def get_employees() -> List[Dict]:
    """Retourne tous les employés"""
    return EMPLOYEES

def get_employee_by_id(employee_id: int) -> Dict:
    """Retourne un employé par son ID"""
    for employee in EMPLOYEES:
        if employee["id"] == employee_id:
            return employee
    return None

def get_employees_by_skill(skill: str) -> List[Dict]:
    """Retourne tous les employés ayant une compétence spécifique"""
    return [emp for emp in EMPLOYEES if skill in emp["skills"]]

def get_employees_by_department(department: str) -> List[Dict]:
    """Retourne tous les employés d'un département"""
    return [emp for emp in EMPLOYEES if emp["department"].lower() == department.lower()]

def add_employee(employee_data: Dict) -> Dict:
    """Ajoute un nouvel employé"""
    new_id = max([emp["id"] for emp in EMPLOYEES]) + 1
    employee_data["id"] = new_id
    EMPLOYEES.append(employee_data)
    return employee_data

def update_employee(employee_id: int, updated_data: Dict) -> Dict:
    """Met à jour un employé existant"""
    for i, emp in enumerate(EMPLOYEES):
        if emp["id"] == employee_id:
            EMPLOYEES[i].update(updated_data)
            return EMPLOYEES[i]
    return None

def delete_employee(employee_id: int) -> bool:
    """Supprime un employé"""
    global EMPLOYEES
    initial_count = len(EMPLOYEES)
    EMPLOYEES = [emp for emp in EMPLOYEES if emp["id"] != employee_id]
    return len(EMPLOYEES) < initial_count
