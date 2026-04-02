# PreSkool - Système de Gestion Scolaire (Projet PFM Django)

Bienvenue sur le dépôt du projet **PreSkool**, une application web complète de gestion scolaire développée avec le framework **Django (Python)**. Ce projet met en place une architecture robuste suivant le motif MVT (Modèle-Vue-Template) pour simplifier l'administration complète d'un établissement de la maternelle au lycée.

## 🌟 Introduction

Le secteur éducatif moderne a besoin de solutions intégrées pour le suivi des élèves et l'encadrement des enseignants. PreSkool répond à cette problématique avec un tableau de bord intuitif permettant aux administrateurs, aux professeurs et aux étudiants d'avoir une vue claire et simplifiée sur leurs responsabilités respectives (notes, absences, emplois du temps, vacances).

---

## 📸 Aperçu du Système (Captures d'écran)

Voici un aperçu visuel des différentes interfaces du système, réparties selon les profils d'utilisateurs.

### 🛡️ Espace Administrateur (Admin Dashboard)

L'espace Administrateur est conçu pour donner une vue d'ensemble sur l'établissement. L'administrateur peut gérer les utilisateurs, les filières, les emplois du temps et les résultats globaux.

<p align="center">
  <img src="admin/admin_1.jpg?raw=true" width="48%" alt="Admin View 1">
  <img src="admin/admin_2.jpg?raw=true" width="48%" alt="Admin View 2">
</p>
<p align="center">
  <img src="admin/admin_3.jpg?raw=true" width="48%" alt="Admin View 3">
  <img src="admin/admin_4.jpg?raw=true" width="48%" alt="Admin View 4">
</p>
<p align="center">
  <img src="admin/admin_5.jpg?raw=true" width="48%" alt="Admin View 5">
  <img src="admin/admin_6.jpg?raw=true" width="48%" alt="Admin View 6">
</p>
<p align="center">
  <img src="admin/admin_7.jpg?raw=true" width="48%" alt="Admin View 7">
  <img src="admin/admin_8.jpg?raw=true" width="48%" alt="Admin View 8">
</p>
<p align="center">
  <img src="admin/admin_9.jpg?raw=true" width="48%" alt="Admin View 9">
  <img src="admin/admin_10.jpg?raw=true" width="48%" alt="Admin View 10">
</p>
<p align="center">
  <img src="admin/admin_11.jpg?raw=true" width="48%" alt="Admin View 11">
  <img src="admin/admin_12.jpg?raw=true" width="48%" alt="Admin View 12">
</p>
<p align="center">
  <img src="admin/admin_13.jpg?raw=true" width="90%" alt="Admin View 13">
</p>

### 🧑‍🎓 Espace Étudiant (Student Dashboard)

L'espace Étudiant permet à l'élève d'accéder à ses résultats, ses matières, son planning, ainsi qu'à la liste des jours fériés.

<p align="center">
  <img src="student/student_1.jpg?raw=true" width="48%" alt="Student View 1">
  <img src="student/student_2.jpg?raw=true" width="48%" alt="Student View 2">
</p>
<p align="center">
  <img src="student/student_3.jpg?raw=true" width="48%" alt="Student View 3">
  <img src="student/student_4.jpg?raw=true" width="48%" alt="Student View 4">
</p>
<p align="center">
  <img src="student/student_5.jpg?raw=true" width="90%" alt="Student View 5">
</p>

---

## 🚀 Fonctionnalités Détaillées

Le système est structuré autour de plusieurs modules clés avec un contrôle d'accès strict (Role-Based Access Control) pour trois types d'utilisateurs métiers : **Administrateur**, **Professeur (Teacher)** et **Étudiant (Student)**.

- 🧑‍🎓 **Gestion des Étudiants et Professeurs** : Opérations CRUD complètes pour gérer les dossiers scolaires, les informations personnelles et le suivi des enseignants.
- 🏢 **Départements & Matières** : Administration des départements académiques (ex: Sciences, Informatique) et de la grille des matières enseignées de manière relationnelle.
- 📅 **Emplois du Temps (Time Tables)** : Création et consultation des plannings de cours, gestion de l'affectation des professeurs et des salles.
- 📝 **Examens & Résultats** : Planification des sessions d'examens et diffusion sécurisée des notes. L'étudiant ne voit que ses propres résultats.
- 🏖️ **Congés et Jours Fériés (Holidays)** : Calendrier scolaire informatif sur l'année académique partagé avec professeurs et étudiants.
- 🔒 ** Sécurité & Authentification** : Espaces et tableaux de bord personnalisés sécurisés par des Mixins Django avec restriction d'accès aux vues dédiées selon le rôle.

---

## 🛠️ Technologies & Stack Technique

Notre architecture technique repose sur des outils reconnus, fiables et robustes :

- **Back-end** : Python 3.x, Django 4.x/5.x
- **Base de données** : SQLite3 (par défaut, idéale pour le développement et la démonstration) / PostgreSQL/MySQL supporté
- **Front-end** : HTML5 sémantique, CSS3, JavaScript, framework Bootstrap (pour garantir une responsivité parfaite sur ordinateur et mobile).
- **Architecture Logique** : Modèle-Vue-Template (MVT) optimisée par la généricité de Django (Class-based Views).

---

## ⚙️ Installation et Déploiement Local

Pour tester ou héberger ce projet sur votre machine locale, veuillez suivre de manière rigoureuse ces étapes :

### 1. Cloner le dépôt
```bash
git clone https://github.com/Python-grp/PFM.git
cd PFM
```

### 2. Créer et activer un environnement virtuel
Pour isoler les dépendances et éviter les conflits avec le système global.
```bash
python -m venv venv

# Sous Windows :
venv\Scripts\activate

# Sous macOS/Linux :
source venv/bin/activate
```

### 3. Installer les dépendances (Requirements)
```bash
pip install -r requirements.txt
```

### 4. Base de données : Migrations et Préparation
Avant de lancer le projet, initialisez la base de données.
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Créer un accès de Super-Utilisateur (Admin Local)
Ce compte aura un accès total sans restrictions pour gérer la plateforme.
```bash
python manage.py createsuperuser
```
(entrez vos identifiants, courriel et mot de passe lorsqu'invité).

### 6. Démarrage du Serveur Django
```bash
python manage.py runserver
```

L'application fonctionnera alors en local et sera accessible mondialement à l'adresse locale suivante :
🔗 **`http://127.0.0.1:8000/`**

---

## 👥 À propos de l'Équipe

*Ce projet a été réalisé avec rigueur dans le cadre d'un module académique intensif (PFM - Projet de Fin de Module).*
Merci à toute l'équipe pour ses efforts de programmation et ses précieuses contributions !