"""
Agent IA utilisant AWS Bedrock pour répondre aux questions sur les employés
"""

import boto3
import json
from typing import Dict, List, Any, Optional
from botocore.exceptions import ClientError
import logging
from employee_data import get_employees, get_skills, get_employees_by_skill, get_employees_by_department

# Configuration des logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EmployeeAIAgent:
    def __init__(self):
        """Initialise l'agent IA avec AWS Bedrock"""
        try:
            # Initialiser le client Bedrock
            self.bedrock_client = boto3.client(
                'bedrock-runtime',
                region_name='us-east-1'  # Région par défaut
            )
            self.model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
            logger.info("Agent IA initialisé avec succès")
        except Exception as e:
            logger.warning(f"Impossible d'initialiser AWS Bedrock: {e}")
            self.bedrock_client = None
    
    def get_employee_context(self) -> str:
        """Récupère le contexte des employés pour l'IA"""
        employees = get_employees()
        skills = get_skills()
        
        context = f"""
CONTEXTE DES EMPLOYÉS:

Nombre total d'employés: {len(employees)}
Compétences disponibles: {', '.join(sorted(skills))}

LISTE DES EMPLOYÉS:
"""
        
        for emp in employees:
            context += f"""
- {emp['name']} ({emp['id']})
  * Poste: {emp['position']}
  * Département: {emp['department']}
  * Email: {emp['email']}
  * Expérience: {emp['experience_years']} ans
  * Salaire: {emp['salary']}€
  * Compétences: {', '.join(emp['skills'])}
"""
        
        # Ajouter des statistiques
        departments = {}
        skill_counts = {}
        
        for emp in employees:
            dept = emp['department']
            departments[dept] = departments.get(dept, 0) + 1
            
            for skill in emp['skills']:
                skill_counts[skill] = skill_counts.get(skill, 0) + 1
        
        context += f"""
RÉPARTITION PAR DÉPARTEMENT:
{chr(10).join([f"- {dept}: {count} employé(s)" for dept, count in departments.items()])}

COMPÉTENCES LES PLUS POPULAIRES:
{chr(10).join([f"- {skill}: {count} employé(s)" for skill, count in sorted(skill_counts.items(), key=lambda x: x[1], reverse=True)[:10]])}
"""
        
        return context

    async def process_question(self, question: str) -> Dict[str, Any]:
        """Traite une question et génère une réponse"""
        try:
            # Si Bedrock n'est pas disponible, utiliser une réponse locale
            if not self.bedrock_client:
                return await self._process_question_locally(question)
            
            # Préparer le contexte
            context = self.get_employee_context()
            
            # Construire le prompt
            prompt = f"""Tu es un assistant IA spécialisé dans la gestion des ressources humaines. Tu as accès aux informations sur les employés d'une entreprise.

{context}

INSTRUCTIONS:
- Réponds uniquement aux questions concernant les employés, leurs compétences, départements, salaires, etc.
- Utilise les données fournies ci-dessus
- Sois précis et factuel
- Si on te demande des informations non disponibles, indique-le clairement
- Formate tes réponses de manière claire et structurée
- Tu peux faire des analyses, comparaisons et recommandations basées sur les données

QUESTION: {question}

RÉPONSE:"""

            # Appeler Claude via Bedrock
            body = {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 1000,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.3,
                "top_p": 0.9
            }

            response = self.bedrock_client.invoke_model(
                modelId=self.model_id,
                body=json.dumps(body)
            )

            response_body = json.loads(response['body'].read())
            answer = response_body['content'][0]['text']

            return {
                "success": True,
                "answer": answer,
                "model": "Claude-3 Sonnet via AWS Bedrock",
                "question": question
            }

        except ClientError as e:
            logger.error(f"Erreur AWS Bedrock: {e}")
            return await self._process_question_locally(question)
        except Exception as e:
            logger.error(f"Erreur lors du traitement: {e}")
            return {
                "success": False,
                "error": str(e),
                "answer": "Désolé, je n'ai pas pu traiter votre question.",
                "question": question
            }

    async def _process_question_locally(self, question: str) -> Dict[str, Any]:
        """Traite une question localement sans AWS Bedrock"""
        logger.info("Traitement local de la question (AWS Bedrock indisponible)")
        
        question_lower = question.lower()
        employees = get_employees()
        
        # Analyse simple des mots-clés pour générer une réponse basique
        if any(word in question_lower for word in ['combien', 'nombre', 'total']):
            if 'employé' in question_lower:
                return {
                    "success": True,
                    "answer": f"Nous avons actuellement {len(employees)} employés dans l'entreprise.",
                    "model": "Traitement local",
                    "question": question
                }
            elif any(word in question_lower for word in ['compétence', 'skill']):
                return {
                    "success": True,
                    "answer": f"Nous suivons {len(get_skills())} compétences différentes dans notre système.",
                    "model": "Traitement local",
                    "question": question
                }
        
        elif any(word in question_lower for word in ['département', 'dept']):
            departments = {}
            for emp in employees:
                dept = emp['department']
                departments[dept] = departments.get(dept, 0) + 1
            
            dept_list = [f"- {dept}: {count} employé(s)" for dept, count in departments.items()]
            return {
                "success": True,
                "answer": f"Voici la répartition par département:\n{chr(10).join(dept_list)}",
                "model": "Traitement local",
                "question": question
            }
        
        elif any(word in question_lower for word in ['salaire', 'salary']):
            salaries = [emp['salary'] for emp in employees]
            avg_salary = sum(salaries) / len(salaries)
            return {
                "success": True,
                "answer": f"Le salaire moyen est de {avg_salary:,.0f}€. Le salaire minimum est {min(salaries):,}€ et le maximum {max(salaries):,}€.",
                "model": "Traitement local",
                "question": question
            }
        
        elif any(word in question_lower for word in ['compétence', 'skill']) and any(word in question_lower for word in ['qui', 'quels', 'employé']):
            # Recherche de compétences spécifiques
            skills = get_skills()
            found_skills = [skill for skill in skills if skill.lower() in question_lower]
            
            if found_skills:
                skill = found_skills[0]
                employees_with_skill = get_employees_by_skill(skill)
                names = [emp['name'] for emp in employees_with_skill]
                return {
                    "success": True,
                    "answer": f"Les employés avec la compétence '{skill}' sont: {', '.join(names)}",
                    "model": "Traitement local",
                    "question": question
                }
        
        # Réponse par défaut
        return {
            "success": True,
            "answer": f"""Je suis un assistant IA pour la gestion des employés. Je peux vous aider avec:

• Informations sur les {len(employees)} employés
• Répartition par départements
• Compétences et expertise
• Statistiques salariales
• Recherche d'employés par critères

Exemples de questions:
- "Combien d'employés avons-nous ?"
- "Qui a la compétence Python ?"
- "Quel est le salaire moyen ?"
- "Répartition par département ?"

Posez-moi une question spécifique !""",
            "model": "Traitement local",
            "question": question
        }

    def health_check(self) -> Dict[str, Any]:
        """Vérifie l'état de l'agent IA"""
        status = {
            "agent_status": "healthy",
            "bedrock_available": self.bedrock_client is not None,
            "model_id": self.model_id if self.bedrock_client else "local_processing",
            "employees_loaded": len(get_employees()),
            "skills_available": len(get_skills())
        }
        
        if self.bedrock_client:
            try:
                # Test simple pour vérifier la connectivité
                test_body = {
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 10,
                    "messages": [{"role": "user", "content": "Test"}],
                    "temperature": 0.1
                }
                
                self.bedrock_client.invoke_model(
                    modelId=self.model_id,
                    body=json.dumps(test_body)
                )
                status["bedrock_test"] = "success"
            except Exception as e:
                status["bedrock_test"] = f"failed: {str(e)}"
                status["bedrock_available"] = False
        
        return status

# Instance globale de l'agent
ai_agent = EmployeeAIAgent()
