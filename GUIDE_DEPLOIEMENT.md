# 🚀 Guide de Déploiement - Dashboard Handball BHB

## Table des Matières
1. [Test en Local](#test-en-local)
2. [Déploiement sur Streamlit Cloud](#déploiement-streamlit-cloud)
3. [Configuration GitHub](#configuration-github)
4. [Partage avec les Entraîneurs](#partage)
5. [Maintenance et Mises à Jour](#maintenance)

---

## 📍 ÉTAPE 1 : Test en Local

### 1.1 Installation de Python

**Windows :**
1. Télécharger Python 3.11 depuis [python.org](https://www.python.org/downloads/)
2. ⚠️ **IMPORTANT** : Cocher "Add Python to PATH" lors de l'installation
3. Vérifier : Ouvrir CMD et taper `python --version`

**Mac :**
```bash
# Installer Homebrew si pas déjà fait
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Installer Python
brew install python@3.11
```

**Linux (Ubuntu/Debian) :**
```bash
sudo apt update
sudo apt install python3.11 python3-pip
```

### 1.2 Préparation des Fichiers

1. **Créer un dossier pour le projet**
```bash
mkdir handball-analytics
cd handball-analytics
```

2. **Copier les fichiers suivants dans ce dossier :**
   - `dashboard_handball.py` (le code de l'application)
   - `requirements.txt` (liste des dépendances)
   - `Base_Donnees_Handball.xlsx` (vos données)
   - Dossier `.streamlit/` avec `config.toml` (configuration)

**Structure attendue :**
```
handball-analytics/
├── dashboard_handball.py
├── requirements.txt
├── Base_Donnees_Handball.xlsx
├── .streamlit/
│   └── config.toml
└── README_DASHBOARD.md
```

### 1.3 Installation des Dépendances

**Ouvrir un terminal/CMD dans le dossier handball-analytics**

```bash
# Créer un environnement virtuel (recommandé)
python -m venv venv

# Activer l'environnement
# Windows :
venv\Scripts\activate
# Mac/Linux :
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### 1.4 Lancement de l'Application

```bash
streamlit run dashboard_handball.py
```

**Résultat attendu :**
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

**➡️ Le navigateur s'ouvre automatiquement sur http://localhost:8501**

### 1.5 Test de l'Application

✅ **Checklist de vérification :**
- [ ] Le dashboard s'affiche correctement
- [ ] Les données sont chargées (indicateurs visibles)
- [ ] Les filtres fonctionnent (sidebar)
- [ ] Les graphiques s'affichent dans chaque onglet
- [ ] L'export CSV fonctionne (onglet Analyse Avancée)

**🎉 Si tout fonctionne → Passer à l'étape 2**

---

## 📍 ÉTAPE 2 : Configuration GitHub

### 2.1 Créer un Compte GitHub (si pas déjà fait)

1. Aller sur [github.com](https://github.com)
2. Cliquer "Sign up"
3. Créer un compte gratuit

### 2.2 Installer Git

**Windows :**
- Télécharger depuis [git-scm.com](https://git-scm.com/download/win)
- Installer avec les options par défaut

**Mac :**
```bash
brew install git
```

**Linux :**
```bash
sudo apt install git
```

### 2.3 Créer un Repository GitHub

**Via l'interface web :**

1. Se connecter à GitHub
2. Cliquer sur le "+" en haut à droite → "New repository"
3. Remplir :
   - **Repository name** : `handball-analytics-bhb`
   - **Description** : "Dashboard d'analyse handball pour BHB"
   - **Public** ou **Private** (Private recommandé si données sensibles)
   - ⚠️ **NE PAS** cocher "Initialize with README"
4. Cliquer "Create repository"

### 2.4 Pousser le Code sur GitHub

**Dans votre terminal, dans le dossier handball-analytics :**

```bash
# Initialiser le repository Git
git init

# Configurer votre identité (première fois seulement)
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"

# Créer un fichier .gitignore
echo "venv/" > .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore

# Ajouter tous les fichiers
git add .

# Faire le premier commit
git commit -m "Initial commit - Dashboard Handball BHB"

# Lier au repository GitHub (remplacer VOTRE-USERNAME)
git remote add origin https://github.com/VOTRE-USERNAME/handball-analytics-bhb.git

# Pousser le code
git push -u origin main
```

**Si erreur "main" n'existe pas :**
```bash
git branch -M main
git push -u origin main
```

**✅ Vérifier sur GitHub que tous les fichiers sont bien présents**

---

## 📍 ÉTAPE 3 : Déploiement sur Streamlit Cloud

### 3.1 Accéder à Streamlit Cloud

1. Aller sur [share.streamlit.io](https://share.streamlit.io)
2. Cliquer "Sign up" ou "Sign in"
3. **Se connecter avec GitHub** (c'est important !)
4. Autoriser Streamlit à accéder à votre compte GitHub

### 3.2 Déployer l'Application

1. **Cliquer sur "New app"**

2. **Remplir le formulaire :**

   **Repository :**
   - Sélectionner `VOTRE-USERNAME/handball-analytics-bhb`

   **Branch :**
   - `main` (par défaut)

   **Main file path :**
   - `dashboard_handball.py`

   **App URL (optionnel) :**
   - Choisir un nom personnalisé : `bhb-handball` 
   - Votre URL sera : `https://bhb-handball.streamlit.app`
   - Ou laisser auto-généré

3. **Cliquer "Deploy!"**

### 3.3 Attendre le Déploiement

**Processus (2-5 minutes) :**
```
[1/4] Cloning repository...
[2/4] Installing dependencies...
[3/4] Building app...
[4/4] Launching app...
```

**✅ Quand c'est prêt, vous verrez :** `Your app is live! 🎉`

### 3.4 Tester l'Application en Ligne

1. Cliquer sur l'URL de votre app
2. Vérifier que tout fonctionne comme en local
3. Tester sur mobile/tablette

**🎉 Votre dashboard est maintenant en ligne !**

---

## 📍 ÉTAPE 4 : Partage avec les Entraîneurs

### 4.1 Obtenir l'URL

**L'URL de votre app :**
```
https://bhb-handball.streamlit.app
```
(ou le nom que vous avez choisi)

### 4.2 Créer un Guide Utilisateur Simple

**Email type à envoyer :**

```
Objet : 🤾 Nouveau Dashboard d'Analyse Handball BHB

Bonjour,

Je suis heureux de vous présenter notre nouveau dashboard d'analyse des matchs de handball.

🔗 Lien d'accès : https://bhb-handball.streamlit.app

📱 Utilisation :
1. Cliquer sur le lien (fonctionne sur PC, tablette, mobile)
2. Dans la barre latérale gauche, sélectionner :
   - Les matchs à analyser
   - Domicile/Extérieur
   - La période de jeu
3. Explorer les différents onglets pour voir les graphiques

💡 Fonctionnalités clés :
- Évolution du Rapport de Force
- Analyse des scores
- Efficacité en INF/SUP
- Statistiques des tireurs

📥 Export : Possibilité de télécharger les graphiques (clic droit → "Save as PNG")

Pour toute question : [votre email]

Sportivement,
[Votre nom]
```

### 4.3 Formation (Optionnel)

**Session de 15 minutes avec les entraîneurs :**
1. Ouvrir l'app ensemble
2. Montrer comment utiliser les filtres
3. Expliquer chaque onglet
4. Répondre aux questions

**Créer une vidéo de démo (2 minutes) :**
- Utiliser OBS Studio (gratuit) ou Loom
- Montrer l'utilisation basique
- Partager le lien vidéo avec l'URL de l'app

---

## 📍 ÉTAPE 5 : Maintenance et Mises à Jour

### 5.1 Mettre à Jour les Données

**Méthode 1 : Via GitHub (Recommandé)**

```bash
# 1. Générer les nouvelles données
python consolidation_handball.py

# 2. Remplacer le fichier Excel
# (copier Base_Donnees_Handball.xlsx dans le dossier)

# 3. Pousser sur GitHub
git add Base_Donnees_Handball.xlsx
git commit -m "Mise à jour des données - [Date]"
git push

# L'app Streamlit se met à jour automatiquement en ~30 secondes
```

**Méthode 2 : Upload Manuel dans l'App**
- Les utilisateurs peuvent uploader un nouveau fichier via la sidebar
- ⚠️ Les données uploadées ne sont pas sauvegardées entre les sessions

### 5.2 Modifier le Code du Dashboard

```bash
# 1. Modifier dashboard_handball.py localement
# 2. Tester en local :
streamlit run dashboard_handball.py

# 3. Si OK, pousser sur GitHub :
git add dashboard_handball.py
git commit -m "Description des modifications"
git push

# Streamlit Cloud redéploie automatiquement
```

### 5.3 Gérer les Versions

**Bonnes pratiques :**

```bash
# Créer une branche pour les tests
git checkout -b dev
# Modifier et tester...
git commit -m "Nouveau graphique XYZ"

# Une fois validé, merger dans main
git checkout main
git merge dev
git push
```

### 5.4 Monitorer l'Application

**Streamlit Cloud Dashboard :**
1. Aller sur [share.streamlit.io](https://share.streamlit.io)
2. Voir vos apps déployées
3. Accéder aux logs en temps réel
4. Voir les statistiques d'utilisation

**Logs :**
- Cliquer sur votre app → "Manage app" → "Logs"
- Voir les erreurs éventuelles
- Debugger les problèmes

---

## 🔒 Sécurité et Confidentialité

### Données Sensibles

**Si vos données sont confidentielles :**

1. **Repository GitHub privé**
   - Gratuit sur GitHub
   - Settings → Visibility → Private

2. **Mot de passe sur l'app (optionnel)**
   
   Ajouter au début de `dashboard_handball.py` :
   ```python
   import streamlit as st
   
   def check_password():
       def password_entered():
           if st.session_state["password"] == "VotreMotDePasse":
               st.session_state["password_correct"] = True
           else:
               st.session_state["password_correct"] = False
       
       if "password_correct" not in st.session_state:
           st.text_input("Mot de passe", type="password", 
                        on_change=password_entered, key="password")
           return False
       elif not st.session_state["password_correct"]:
           st.text_input("Mot de passe", type="password",
                        on_change=password_entered, key="password")
           st.error("😕 Mot de passe incorrect")
           return False
       else:
           return True
   
   if check_password():
       # Le code normal du dashboard
       main()
   ```

3. **Authentification Streamlit Cloud (Pro)**
   - 20$/mois pour des fonctionnalités avancées
   - Gestion des utilisateurs
   - SSO

---

## 📞 Support et Dépannage

### Problèmes Fréquents

**1. "Module not found" lors du déploiement**
- Vérifier que `requirements.txt` est bien dans le repository
- Vérifier les versions des packages

**2. L'app ne démarre pas**
- Regarder les logs sur Streamlit Cloud
- Vérifier que `Base_Donnees_Handball.xlsx` est bien présent

**3. Données ne s'affichent pas**
- Vérifier le format du fichier Excel
- Vérifier les noms des colonnes

**4. App très lente**
- Les apps gratuites "hibernent" après inactivité
- Premier chargement peut prendre 30s
- Solutions : upgrade Streamlit Cloud ($20/mois) ou attendre

### Obtenir de l'Aide

**Documentation officielle :**
- [Streamlit Docs](https://docs.streamlit.io)
- [Streamlit Forum](https://discuss.streamlit.io)

**Communauté :**
- Stack Overflow (tag `streamlit`)
- Discord Streamlit officiel

---

## 🎯 Checklist Finale

Avant de partager avec les entraîneurs :

- [ ] ✅ App testée en local
- [ ] ✅ Code pushé sur GitHub
- [ ] ✅ App déployée sur Streamlit Cloud
- [ ] ✅ URL de l'app notée
- [ ] ✅ App testée en ligne (PC + mobile)
- [ ] ✅ Email de présentation rédigé
- [ ] ✅ Guide utilisateur prêt
- [ ] ✅ Personne de contact désignée pour le support

---

## 🚀 Prochaines Étapes Avancées

Une fois le dashboard en production :

1. **Collecter les retours utilisateurs**
   - Quels graphiques sont les plus utilisés ?
   - Quelles fonctionnalités manquent ?

2. **Itérer et améliorer**
   - Ajouter de nouveaux graphiques
   - Optimiser les filtres
   - Améliorer le design

3. **Former les utilisateurs avancés**
   - Sessions de formation spécifiques
   - Documentation détaillée
   - Cas d'usage concrets

4. **Étendre les fonctionnalités**
   - Export PDF de rapports
   - Comparaison avec d'autres équipes
   - Analyse prédictive

---

**🎉 Félicitations ! Vous avez déployé votre dashboard handball !**

Pour toute question : [Insérer vos coordonnées]

---

**Version** : 1.0  
**Dernière mise à jour** : Février 2026
