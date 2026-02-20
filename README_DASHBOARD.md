# 🤾 BHB Handball Analytics Dashboard

Dashboard interactif Streamlit pour l'analyse des performances handball de BHB.

## 🎯 Fonctionnalités

### 📊 Visualisations Incluses

1. **Rapport de Force Temporel**
   - Évolution du rapport de force (DMA BHB - DMA ADV) au fil du match
   - Comparaison multi-matchs sur le même graphique
   - Ligne de référence à l'équilibre (0)

2. **Évolution des Scores**
   - Courbes de score BHB vs Adversaire minute par minute
   - Vue séparée par match
   - Heatmap de l'écart de score

3. **Statistiques INF/SUP**
   - Efficacité en situation normale, infériorité et supériorité numérique
   - Comparaison BHB vs Adversaires
   - Pourcentages de réussite

4. **Distribution des Tireurs**
   - Nombre de tirs par joueur BHB
   - Taux de réussite avec code couleur
   - Vue détaillée (buts/tirs)

5. **Analyse Avancée**
   - Radar chart multi-critères
   - Tableau de données interactif
   - Export CSV des données filtrées

### 🔍 Filtres Disponibles

- **Par Matchs** : Sélection multiple de matchs spécifiques
- **Par Lieu** : Domicile, Extérieur, ou les deux
- **Par Équipe** : BHB, Adversaires, ou toutes
- **Par Période** : Filtrage par minutes (ex: 1ère mi-temps, dernières 10 min)

### 📈 Indicateurs Clés (KPIs)

- Efficacité BHB (% de réussite)
- Rapport de Force Moyen
- % de temps en Infériorité Numérique
- % de temps en Supériorité Numérique

## 🚀 Installation et Lancement

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de packages Python)

### Installation

1. **Cloner ou télécharger le projet**
```bash
cd handball-analytics
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Placer votre fichier de données**
   - Placer `Base_Donnees_Handball.xlsx` dans le même dossier que `dashboard_handball.py`
   - OU utiliser l'upload de fichier dans l'interface

### Lancement Local

```bash
streamlit run dashboard_handball.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse `http://localhost:8501`

## 🌐 Déploiement sur Streamlit Cloud (Gratuit)

### Étape 1 : Préparer votre repository GitHub

1. Créer un repository GitHub (public ou privé)
2. Y placer les fichiers suivants :
   ```
   handball-analytics/
   ├── dashboard_handball.py
   ├── requirements.txt
   ├── Base_Donnees_Handball.xlsx
   ├── .streamlit/
   │   └── config.toml
   └── README.md
   ```

### Étape 2 : Déployer sur Streamlit Cloud

1. Aller sur [share.streamlit.io](https://share.streamlit.io)
2. Se connecter avec GitHub
3. Cliquer "New app"
4. Sélectionner :
   - Repository: votre-repo/handball-analytics
   - Branch: main
   - Main file path: dashboard_handball.py
5. Cliquer "Deploy"

**Votre app sera disponible à :** `https://votre-app.streamlit.app`

### Étape 3 : Partager avec les Entraîneurs

Envoyez simplement l'URL aux entraîneurs. Aucune installation requise de leur côté !

## 📱 Utilisation

### Démarrage Rapide

1. **Charger les données**
   - Si `Base_Donnees_Handball.xlsx` est dans le dossier → chargement automatique
   - Sinon, utiliser l'upload dans la sidebar

2. **Sélectionner les filtres**
   - Sidebar gauche : Choisir matchs, lieu, équipe, période

3. **Explorer les onglets**
   - **Rapport de Force** : Voir l'évolution tactique
   - **Scores** : Analyser la dynamique du match
   - **INF/SUP** : Évaluer l'efficacité en situations spéciales
   - **Tireurs** : Identifier les meilleurs buteurs
   - **Analyse Avancée** : Comparaison multi-matchs et export données

4. **Exporter**
   - Graphiques : Clic droit → "Save as PNG"
   - Données : Bouton "Télécharger CSV" dans l'onglet Analyse Avancée

### Exemples de Cas d'Usage

#### Analyse d'un Match Spécifique
```
Filtres:
- Matchs: J13 (BHB-CRE)
- Lieu: Tous
- Équipe: Toutes

Vue: Rapport de Force → Voir les phases clés du match
```

#### Comparaison Domicile vs Extérieur
```
Filtres:
- Matchs: Tous
- Lieu: Domicile (puis refaire avec Extérieur)
- Équipe: BHB

Comparer: Efficacité BHB, Rapport de Force moyen
```

#### Analyse de Fin de Match
```
Filtres:
- Matchs: Tous
- Période: 50-60 minutes
- Équipe: BHB

Vue: Efficacité, distribution tireurs
Question: Qui marque en fin de match ?
```

## 🎨 Personnalisation

### Modifier les Couleurs

Éditer `.streamlit/config.toml` :
```toml
[theme]
primaryColor = "#votre-couleur"  # Couleur principale
backgroundColor = "#FFFFFF"       # Fond de page
secondaryBackgroundColor = "#f0f2f6"  # Fond des widgets
```

### Ajouter des Graphiques

Dans `dashboard_handball.py`, créer une nouvelle fonction :
```python
def create_votre_graphique(df):
    fig = go.Figure()
    # Votre code de visualisation
    return fig
```

Puis l'ajouter dans un onglet :
```python
with tab_votre_onglet:
    st.plotly_chart(create_votre_graphique(filtered_df))
```

## 🔄 Mise à Jour des Données

### Méthode 1 : Upload Manuel
1. Ouvrir l'app
2. Sidebar → "Charger un fichier de données"
3. Sélectionner le nouveau fichier Excel

### Méthode 2 : Remplacement du Fichier
1. Remplacer `Base_Donnees_Handball.xlsx` dans le dossier
2. Rafraîchir la page (F5)

### Méthode 3 : Automatisation (Avancé)
Créer un script qui :
1. Exécute `consolidation_handball.py` pour mettre à jour les données
2. Push sur GitHub → Streamlit Cloud se met à jour automatiquement

## 📊 Structure des Données Attendues

Le fichier Excel doit contenir les colonnes suivantes :

```
Journée, Match, Date Match, Lieu, PossessionID, Minute, Equipe, Issue,
Tireur, Score BHB, Score ADV, Ecart, MA BHB, MA ADV, DMA BHB, DMA ADV,
TM, Rapport de force, INF, SUP
```

Généré automatiquement par le script `consolidation_handball.py`

## 🐛 Dépannage

### "Aucune donnée disponible"
- Vérifier que `Base_Donnees_Handball.xlsx` est dans le bon dossier
- OU utiliser l'upload de fichier dans la sidebar

### "Module not found"
```bash
pip install -r requirements.txt
```

### L'app ne démarre pas
```bash
# Vérifier la version de Python
python --version  # Doit être >= 3.8

# Réinstaller Streamlit
pip install --upgrade streamlit
```

### Graphiques ne s'affichent pas
- Vérifier que les données filtrées ne sont pas vides
- Essayer de réinitialiser les filtres (bouton dans sidebar)

## 📈 Fonctionnalités Futures

- [ ] Export PDF de rapports complets
- [ ] Annotations sur les graphiques (événements clés)
- [ ] Comparaison avec moyennes de championnat
- [ ] Prédictions de fin de match (ML)
- [ ] Analyse vidéo synchronisée
- [ ] Mode sombre

## 🤝 Contribution

Pour suggérer des améliorations :
1. Utiliser le feedback de Streamlit (icône en haut à droite)
2. Contacter l'équipe technique

## 📄 Licence

Usage interne BHB. Ne pas distribuer publiquement.

## 👥 Contact

Pour toute question :
- Email: votre-email@bhb.com
- Slack: #handball-analytics

---

**Version** : 1.0  
**Dernière mise à jour** : Février 2026  
**Développé avec** : Streamlit 1.31 + Plotly 5.18
