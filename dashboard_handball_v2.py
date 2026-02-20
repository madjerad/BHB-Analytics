#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BHB Handball Analytics Dashboard - Version Professionnelle
Dashboard moderne et épuré pour l'analyse des performances handball

Auteur: Claude (Anthropic)
Date: Février 2026
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="BHB Analytics Pro",
   -- page_icon="🤾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS moderne et professionnel
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem 3rem;
    }
    
    /* Header */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    }
    
    .main-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-align: center;
        letter-spacing: -0.5px;
    }
    
    .main-subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 1.1rem;
        font-weight: 400;
        text-align: center;
        margin-top: 0.5rem;
    }
    
    /* Cards */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid rgba(0,0,0,0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    }
    
    .metric-label {
        color: #64748b;
        font-size: 0.875rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        color: #1e293b;
        font-size: 2rem;
        font-weight: 700;
        line-height: 1;
    }
    
    .metric-delta {
        color: #10b981;
        font-size: 0.875rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: white;
    }
    
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        border-right: 1px solid #e2e8f0;
    }
    
    section[data-testid="stSidebar"] .stMarkdown {
        padding: 0 1rem;
    }
    
    /* Filter Section */
    .filter-section {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .filter-title {
        color: #1e293b;
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #667eea;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: white;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0 2rem;
        background: transparent;
        border-radius: 8px;
        color: #64748b;
        font-weight: 500;
        border: none;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Charts Container */
    .chart-container {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 2rem;
    }
    
    .chart-title {
        color: #1e293b;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid #e2e8f0;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Dataframe */
    .dataframe {
        border: none !important;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    }
    
    /* Remove Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f5f9;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# FONCTIONS DE CHARGEMENT
# ============================================================================

@st.cache_data
def load_data(filepath):
    """Charge les données depuis le fichier Excel consolidé"""
    try:
        df = pd.read_excel(filepath)
        df['Date Match'] = pd.to_datetime(df['Date Match'], format='%d/%m/%Y', errors='coerce')
        return df
    except Exception as e:
        st.error(f"❌ Erreur de chargement : {str(e)}")
        return None

# ============================================================================
# FONCTIONS D'ANALYSE
# ============================================================================

def calculate_stats_by_match(df, selected_matches):
    """Calcule les statistiques par match ou moyennes multi-matchs"""
    
    stats_list = []
    
    for match in selected_matches:
        match_data = df[df['Match'] == match].copy()
        
        if len(match_data) == 0:
            continue
        
        # Informations de base
        journee = match_data['Journée'].iloc[0]
        date = match_data['Date Match'].iloc[0]
        lieu = match_data['Lieu'].iloc[0]
        
        # Séparer par mi-temps
        mt1 = match_data[match_data['Minute'] <= 30]
        mt2 = match_data[match_data['Minute'] > 30]
        
        stats = {
            'Match': match,
            'Journée': journee,
            'Date': date.strftime('%d/%m/%Y') if pd.notna(date) else '',
            'Lieu': lieu,
        }
        
        # Calculer stats pour chaque mi-temps
        for period_data, suffix in [(mt1, '1'), (mt2, '2'), (match_data, 'Total')]:
            if len(period_data) == 0:
                continue
                
            bhb_data = period_data[period_data['Equipe'] == 'BHB']
            adv_data = period_data[period_data['Equipe'] == 'ADV']
            
            # Buts
            stats[f'Buts BHB {suffix}'] = bhb_data['Issue'].sum()
            stats[f'Buts ADV {suffix}'] = adv_data['Issue'].sum()
            
            # Possessions
            stats[f'Poss BHB {suffix}'] = len(bhb_data)
            stats[f'Poss ADV {suffix}'] = len(adv_data)
            stats[f'Poss Total {suffix}'] = len(period_data)
            
            # Efficacité
            if len(bhb_data) > 0:
                stats[f'Eff BHB {suffix}'] = (bhb_data['Issue'].sum() / len(bhb_data) * 100)
            else:
                stats[f'Eff BHB {suffix}'] = 0
                
            if len(adv_data) > 0:
                stats[f'Eff ADV {suffix}'] = (adv_data['Issue'].sum() / len(adv_data) * 100)
            else:
                stats[f'Eff ADV {suffix}'] = 0
            
            # DMA
            if len(bhb_data) > 0:
                dma_bhb = bhb_data['DMA BHB'].dropna()
                if len(dma_bhb) > 0:
                    stats[f'DMA BHB Moy {suffix}'] = dma_bhb.mean()
                    stats[f'DMA BHB Std {suffix}'] = dma_bhb.std()
                else:
                    stats[f'DMA BHB Moy {suffix}'] = 0
                    stats[f'DMA BHB Std {suffix}'] = 0
            else:
                stats[f'DMA BHB Moy {suffix}'] = 0
                stats[f'DMA BHB Std {suffix}'] = 0
                
            if len(adv_data) > 0:
                dma_adv = adv_data['DMA ADV'].dropna()
                if len(dma_adv) > 0:
                    stats[f'DMA ADV Moy {suffix}'] = dma_adv.mean()
                    stats[f'DMA ADV Std {suffix}'] = dma_adv.std()
                else:
                    stats[f'DMA ADV Moy {suffix}'] = 0
                    stats[f'DMA ADV Std {suffix}'] = 0
            else:
                stats[f'DMA ADV Moy {suffix}'] = 0
                stats[f'DMA ADV Std {suffix}'] = 0
            
            # Déchet technique (Tireur vide ou 0 pour BHB)
            dechet = bhb_data[bhb_data['Tireur'].isna() | (bhb_data['Tireur'] == 0)]
            stats[f'Déchet Tech {suffix}'] = len(dechet)
            
            # INF/SUP
            inf_count = period_data['INF'].notna().sum()
            sup_count = period_data['SUP'].notna().sum()
            stats[f'Nb INF {suffix}'] = inf_count
            stats[f'Nb SUP {suffix}'] = sup_count
        
        stats_list.append(stats)
    
    return stats_list

def aggregate_stats(stats_list):
    """Agrège les statistiques de plusieurs matchs"""
    if len(stats_list) == 0:
        return None
    
    if len(stats_list) == 1:
        return stats_list[0]
    
    # Moyenne des stats numériques
    agg_stats = {
        'Match': f"{len(stats_list)} matchs sélectionnés",
        'Journée': 'Multiple',
        'Date': 'Multiple',
        'Lieu': 'Multiple'
    }
    
    numeric_fields = [col for col in stats_list[0].keys() 
                     if col not in ['Match', 'Journée', 'Date', 'Lieu']]
    
    for field in numeric_fields:
        values = [s[field] for s in stats_list if field in s and s[field] is not None]
        if values:
            agg_stats[field] = np.mean(values)
        else:
            agg_stats[field] = 0
    
    return agg_stats

# ============================================================================
# FONCTIONS DE VISUALISATION
# ============================================================================

def create_rapport_force_chart(df, selected_matches):
    """
    Graphique du rapport de force minute par minute
    - 1 match : courbe unique
    - Plusieurs matchs : courbe moyenne
    """
    
    fig = go.Figure()
    
    if len(selected_matches) == 1:
        # Un seul match - courbe simple
        match = selected_matches[0]
        match_data = df[df['Match'] == match].sort_values('Minute')
        
        fig.add_trace(go.Scatter(
            x=match_data['Minute'],
            y=match_data['Rapport de force'],
            mode='lines',
            name=match,
            line=dict(color='#667eea', width=3),
            fill='tozeroy',
            fillcolor='rgba(102, 126, 234, 0.1)',
            hovertemplate='<b>Minute %{x}</b><br>Rapport de Force: %{y:.3f}<extra></extra>'
        ))
        
        title_text = f"Rapport de Force - {match}"
        
    else:
        # Plusieurs matchs - moyenne
        all_minutes = []
        all_rf = []
        
        for match in selected_matches:
            match_data = df[df['Match'] == match]
            all_minutes.extend(match_data['Minute'].tolist())
            all_rf.extend(match_data['Rapport de force'].tolist())
        
        # Créer DataFrame pour agréger
        combined = pd.DataFrame({
            'Minute': all_minutes,
            'RF': all_rf
        })
        
        # Moyenne par minute
        avg_by_minute = combined.groupby('Minute')['RF'].agg(['mean', 'std']).reset_index()
        
        # Courbe moyenne
        fig.add_trace(go.Scatter(
            x=avg_by_minute['Minute'],
            y=avg_by_minute['mean'],
            mode='lines',
            name='Moyenne',
            line=dict(color='#667eea', width=4),
            fill='tozeroy',
            fillcolor='rgba(102, 126, 234, 0.1)',
            hovertemplate='<b>Minute %{x}</b><br>RF Moyen: %{y:.3f}<extra></extra>'
        ))
        
        # Bandes d'écart-type
        fig.add_trace(go.Scatter(
            x=avg_by_minute['Minute'],
            y=avg_by_minute['mean'] + avg_by_minute['std'],
            mode='lines',
            line=dict(width=0),
            showlegend=False,
            hoverinfo='skip'
        ))
        
        fig.add_trace(go.Scatter(
            x=avg_by_minute['Minute'],
            y=avg_by_minute['mean'] - avg_by_minute['std'],
            mode='lines',
            line=dict(width=0),
            fillcolor='rgba(102, 126, 234, 0.2)',
            fill='tonexty',
            name='Écart-type',
            hoverinfo='skip'
        ))
        
        title_text = f"Rapport de Force Moyen - {len(selected_matches)} matchs"
    
    # Ligne de référence à 0
    fig.add_hline(
        y=0, 
        line_dash="dash", 
        line_color="rgba(0,0,0,0.3)",
        annotation_text="Équilibre",
        annotation_position="right",
        annotation_font_size=10,
        annotation_font_color="rgba(0,0,0,0.5)"
    )
    
    fig.update_layout(
        title=dict(
            text=title_text,
            font=dict(size=20, color='#1e293b'),
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(
            title="Minute de jeu",
            gridcolor='rgba(0,0,0,0.05)',
            showgrid=True,
            zeroline=False
        ),
        yaxis=dict(
            title="Rapport de Force (DMA BHB - DMA ADV)",
            gridcolor='rgba(0,0,0,0.05)',
            showgrid=True,
            zeroline=True,
            zerolinecolor='rgba(0,0,0,0.2)'
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        hovermode='x unified',
        height=500,
        margin=dict(l=60, r=40, t=80, b=60),
        font=dict(family='Inter, sans-serif')
    )
    
    return fig

def create_dma_chart(df, selected_matches):
    """
    Graphique DMA BHB et ADV minute par minute
    - 1 match : 2 courbes
    - Plusieurs matchs : 2 courbes moyennes
    """
    
    fig = go.Figure()
    
    if len(selected_matches) == 1:
        # Un seul match
        match = selected_matches[0]
        match_data = df[df['Match'] == match].sort_values('Minute')
        
        # DMA BHB
        bhb_data = match_data[match_data['Equipe'] == 'BHB']
        fig.add_trace(go.Scatter(
            x=bhb_data['Minute'],
            y=bhb_data['DMA BHB'],
            mode='lines',
            name='DMA BHB',
            line=dict(color='#10b981', width=3),
            hovertemplate='<b>Minute %{x}</b><br>DMA BHB: %{y:.3f}<extra></extra>'
        ))
        
        # DMA ADV
        adv_data = match_data[match_data['Equipe'] == 'ADV']
        fig.add_trace(go.Scatter(
            x=adv_data['Minute'],
            y=adv_data['DMA ADV'],
            mode='lines',
            name='DMA ADV',
            line=dict(color='#ef4444', width=3),
            hovertemplate='<b>Minute %{x}</b><br>DMA ADV: %{y:.3f}<extra></extra>'
        ))
        
        title_text = f"DMA BHB vs ADV - {match}"
        
    else:
        # Plusieurs matchs - moyennes
        bhb_minutes = []
        bhb_dma = []
        adv_minutes = []
        adv_dma = []
        
        for match in selected_matches:
            match_data = df[df['Match'] == match]
            
            bhb_data = match_data[match_data['Equipe'] == 'BHB']
            bhb_minutes.extend(bhb_data['Minute'].tolist())
            bhb_dma.extend(bhb_data['DMA BHB'].tolist())
            
            adv_data = match_data[match_data['Equipe'] == 'ADV']
            adv_minutes.extend(adv_data['Minute'].tolist())
            adv_dma.extend(adv_data['DMA ADV'].tolist())
        
        # DMA BHB moyenne
        bhb_df = pd.DataFrame({'Minute': bhb_minutes, 'DMA': bhb_dma})
        bhb_avg = bhb_df.groupby('Minute')['DMA'].mean().reset_index()
        
        fig.add_trace(go.Scatter(
            x=bhb_avg['Minute'],
            y=bhb_avg['DMA'],
            mode='lines',
            name='DMA BHB (Moy)',
            line=dict(color='#10b981', width=4),
            hovertemplate='<b>Minute %{x}</b><br>DMA BHB: %{y:.3f}<extra></extra>'
        ))
        
        # DMA ADV moyenne
        adv_df = pd.DataFrame({'Minute': adv_minutes, 'DMA': adv_dma})
        adv_avg = adv_df.groupby('Minute')['DMA'].mean().reset_index()
        
        fig.add_trace(go.Scatter(
            x=adv_avg['Minute'],
            y=adv_avg['DMA'],
            mode='lines',
            name='DMA ADV (Moy)',
            line=dict(color='#ef4444', width=4),
            hovertemplate='<b>Minute %{x}</b><br>DMA ADV: %{y:.3f}<extra></extra>'
        ))
        
        title_text = f"DMA BHB vs ADV Moyen - {len(selected_matches)} matchs"
    
    fig.update_layout(
        title=dict(
            text=title_text,
            font=dict(size=20, color='#1e293b'),
            x=0.5,
            xanchor='center'
        ),
        xaxis=dict(
            title="Minute de jeu",
            gridcolor='rgba(0,0,0,0.05)',
            showgrid=True
        ),
        yaxis=dict(
            title="DMA (Différence de Moyenne Mobile)",
            gridcolor='rgba(0,0,0,0.05)',
            showgrid=True
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        hovermode='x unified',
        height=500,
        margin=dict(l=60, r=40, t=80, b=60),
        font=dict(family='Inter, sans-serif'),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    
    return fig

def create_stats_table(stats):
    """Créer un tableau de statistiques formaté"""
    
    if stats is None:
        return None
    
    # Créer le DataFrame
    rows = []
    
    # Section: Informations générales
    rows.append({'Catégorie': 'INFO', 'Métrique': 'Match', '1ère MT': '-', '2ème MT': '-', 'Total': stats['Match']})
    rows.append({'Catégorie': 'INFO', 'Métrique': 'Journée', '1ère MT': '-', '2ème MT': '-', 'Total': stats['Journée']})
    rows.append({'Catégorie': 'INFO', 'Métrique': 'Lieu', '1ère MT': '-', '2ème MT': '-', 'Total': stats['Lieu']})
    
    # Section: Buts
    rows.append({'Catégorie': 'BUTS', 'Métrique': 'BHB', 
                 '1ère MT': f"{stats.get('Buts BHB 1', 0):.0f}",
                 '2ème MT': f"{stats.get('Buts BHB 2', 0):.0f}",
                 'Total': f"{stats.get('Buts BHB Total', 0):.0f}"})
    rows.append({'Catégorie': 'BUTS', 'Métrique': 'ADV',
                 '1ère MT': f"{stats.get('Buts ADV 1', 0):.0f}",
                 '2ème MT': f"{stats.get('Buts ADV 2', 0):.0f}",
                 'Total': f"{stats.get('Buts ADV Total', 0):.0f}"})
    rows.append({'Catégorie': 'BUTS', 'Métrique': 'Écart',
                 '1ère MT': f"{stats.get('Buts BHB 1', 0) - stats.get('Buts ADV 1', 0):.0f}",
                 '2ème MT': f"{stats.get('Buts BHB 2', 0) - stats.get('Buts ADV 2', 0):.0f}",
                 'Total': f"{stats.get('Buts BHB Total', 0) - stats.get('Buts ADV Total', 0):.0f}"})
    
    # Section: Possessions
    rows.append({'Catégorie': 'POSS', 'Métrique': 'BHB',
                 '1ère MT': f"{stats.get('Poss BHB 1', 0):.0f}",
                 '2ème MT': f"{stats.get('Poss BHB 2', 0):.0f}",
                 'Total': f"{stats.get('Poss BHB Total', 0):.0f}"})
    rows.append({'Catégorie': 'POSS', 'Métrique': 'ADV',
                 '1ère MT': f"{stats.get('Poss ADV 1', 0):.0f}",
                 '2ème MT': f"{stats.get('Poss ADV 2', 0):.0f}",
                 'Total': f"{stats.get('Poss ADV Total', 0):.0f}"})
    rows.append({'Catégorie': 'POSS', 'Métrique': 'Total',
                 '1ère MT': f"{stats.get('Poss Total 1', 0):.0f}",
                 '2ème MT': f"{stats.get('Poss Total 2', 0):.0f}",
                 'Total': f"{stats.get('Poss Total Total', 0):.0f}"})
    
    # Section: Efficacité
    rows.append({'Catégorie': 'EFF', 'Métrique': 'BHB',
                 '1ère MT': f"{stats.get('Eff BHB 1', 0):.1f}%",
                 '2ème MT': f"{stats.get('Eff BHB 2', 0):.1f}%",
                 'Total': f"{stats.get('Eff BHB Total', 0):.1f}%"})
    rows.append({'Catégorie': 'EFF', 'Métrique': 'ADV',
                 '1ère MT': f"{stats.get('Eff ADV 1', 0):.1f}%",
                 '2ème MT': f"{stats.get('Eff ADV 2', 0):.1f}%",
                 'Total': f"{stats.get('Eff ADV Total', 0):.1f}%"})
    
    # Section: DMA
    rows.append({'Catégorie': 'DMA', 'Métrique': 'BHB Moy',
                 '1ère MT': f"{stats.get('DMA BHB Moy 1', 0):.3f}",
                 '2ème MT': f"{stats.get('DMA BHB Moy 2', 0):.3f}",
                 'Total': f"{stats.get('DMA BHB Moy Total', 0):.3f}"})
    rows.append({'Catégorie': 'DMA', 'Métrique': 'BHB Std',
                 '1ère MT': f"{stats.get('DMA BHB Std 1', 0):.3f}",
                 '2ème MT': f"{stats.get('DMA BHB Std 2', 0):.3f}",
                 'Total': f"{stats.get('DMA BHB Std Total', 0):.3f}"})
    rows.append({'Catégorie': 'DMA', 'Métrique': 'ADV Moy',
                 '1ère MT': f"{stats.get('DMA ADV Moy 1', 0):.3f}",
                 '2ème MT': f"{stats.get('DMA ADV Moy 2', 0):.3f}",
                 'Total': f"{stats.get('DMA ADV Moy Total', 0):.3f}"})
    rows.append({'Catégorie': 'DMA', 'Métrique': 'ADV Std',
                 '1ère MT': f"{stats.get('DMA ADV Std 1', 0):.3f}",
                 '2ème MT': f"{stats.get('DMA ADV Std 2', 0):.3f}",
                 'Total': f"{stats.get('DMA ADV Std Total', 0):.3f}"})
    
    # Section: Autres
    rows.append({'Catégorie': 'AUTRE', 'Métrique': 'Déchet Tech',
                 '1ère MT': f"{stats.get('Déchet Tech 1', 0):.0f}",
                 '2ème MT': f"{stats.get('Déchet Tech 2', 0):.0f}",
                 'Total': f"{stats.get('Déchet Tech Total', 0):.0f}"})
    rows.append({'Catégorie': 'AUTRE', 'Métrique': 'Nb INF',
                 '1ère MT': f"{stats.get('Nb INF 1', 0):.0f}",
                 '2ème MT': f"{stats.get('Nb INF 2', 0):.0f}",
                 'Total': f"{stats.get('Nb INF Total', 0):.0f}"})
    rows.append({'Catégorie': 'AUTRE', 'Métrique': 'Nb SUP',
                 '1ère MT': f"{stats.get('Nb SUP 1', 0):.0f}",
                 '2ème MT': f"{stats.get('Nb SUP 2', 0):.0f}",
                 'Total': f"{stats.get('Nb SUP Total', 0):.0f}"})
    
    df_stats = pd.DataFrame(rows)
    
    return df_stats

# ============================================================================
# APPLICATION PRINCIPALE
# ============================================================================

def main():
    
    # En-tête moderne
    st.markdown("""
        <div class="main-header">
            <h1 class="main-title">🤾 BHB ANALYTICS PRO</h1>
            <p class="main-subtitle">Plateforme d'Analyse Avancée des Performances Handball</p>
        </div>
    """, unsafe_allow_html=True)
    
    # ========================================================================
    # SIDEBAR - CHARGEMENT ET FILTRES
    # ========================================================================
    
    with st.sidebar:
        st.markdown("### 📁 Données")
        
        uploaded_file = st.file_uploader(
            "Charger fichier Excel",
            type=['xlsx', 'xls'],
            help="Fichier Base_Donnees_Handball.xlsx"
        )
        
        if uploaded_file is not None:
            df = load_data(uploaded_file)
        else:
            try:
                df = load_data('Base_Donnees_Handball.xlsx')
            except:
                st.warning("⚠️ Veuillez charger un fichier de données")
                st.stop()
        
        if df is None:
            st.stop()
        
        st.markdown("---")
        
        # Filtres
        st.markdown("### 🎯 Filtres de Sélection")
        
        # Options de sélection rapide
        selection_mode = st.radio(
            "Mode de sélection",
            ["🎯 Sélection Personnalisée", "🏠 Tous Domicile", "✈️ Tous Extérieur", "📊 Tous les Matchs"],
            label_visibility="collapsed"
        )
        
        all_matches = sorted(df['Match'].unique().tolist())
        
        if selection_mode == "🏠 Tous Domicile":
            selected_matches = df[df['Lieu'] == 'Domicile']['Match'].unique().tolist()
        elif selection_mode == "✈️ Tous Extérieur":
            selected_matches = df[df['Lieu'] == 'Extérieur']['Match'].unique().tolist()
        elif selection_mode == "📊 Tous les Matchs":
            selected_matches = all_matches
        else:
            selected_matches = st.multiselect(
                "Sélectionner les matchs",
                options=all_matches,
                default=[all_matches[0]] if all_matches else []
            )
        
        if not selected_matches:
            st.warning("⚠️ Sélectionnez au moins un match")
            st.stop()
        
        # Affichage du nombre de matchs sélectionnés
        st.markdown("---")
        st.markdown(f"**📌 {len(selected_matches)} match(s) sélectionné(s)**")
        
        if len(selected_matches) == 1:
            match_info = df[df['Match'] == selected_matches[0]].iloc[0]
            st.info(f"🏆 {match_info['Journée']}\n\n📍 {match_info['Lieu']}")
        
    # ========================================================================
    # CONTENU PRINCIPAL
    # ========================================================================
    
    # Onglets
    tab1, tab2, tab3 = st.tabs(["📈 Rapport de Force", "📊 DMA BHB vs ADV", "📋 Statistiques"])
    
    # TAB 1: Rapport de Force
    with tab1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig_rf = create_rapport_force_chart(df, selected_matches)
        st.plotly_chart(fig_rf, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Info contextuelle
        with st.expander("ℹ️ Interprétation du Rapport de Force"):
            st.markdown("""
            **Le Rapport de Force** représente la différence entre DMA BHB et DMA ADV :
            
            - **Valeurs positives** 🟢 : BHB domine (avantage tactique)
            - **Valeurs négatives** 🔴 : Adversaire domine
            - **Autour de 0** ⚪ : Équilibre du jeu
            
            *Plus la courbe est haute, meilleure est la situation pour BHB.*
            """)
    
    # TAB 2: DMA
    with tab2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        fig_dma = create_dma_chart(df, selected_matches)
        st.plotly_chart(fig_dma, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Info contextuelle
        with st.expander("ℹ️ À propos de la DMA"):
            st.markdown("""
            **DMA (Différence de Moyenne Mobile)** mesure la dynamique offensive :
            
            - **Courbe montante** 📈 : Amélioration de l'efficacité
            - **Courbe descendante** 📉 : Baisse de performance
            - **Écart entre courbes** : Avantage de l'équipe avec la DMA supérieure
            
            *Une DMA élevée indique une meilleure efficacité récente dans les possessions.*
            """)
    
    # TAB 3: Statistiques
    with tab3:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        
        # Calculer les stats
        stats_list = calculate_stats_by_match(df, selected_matches)
        aggregated_stats = aggregate_stats(stats_list)
        
        if aggregated_stats:
            # Titre
            if len(selected_matches) == 1:
                st.markdown(f"### 📊 Statistiques - {selected_matches[0]}")
            else:
                st.markdown(f"### 📊 Statistiques Moyennes - {len(selected_matches)} matchs")
            
            # Créer et afficher le tableau
            stats_df = create_stats_table(aggregated_stats)
            
            if stats_df is not None:
                # Appliquer un style au DataFrame
                st.dataframe(
                    stats_df,
                    use_container_width=True,
                    height=600,
                    hide_index=True
                )
                
                # Bouton d'export
                st.markdown("---")
                csv = stats_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Télécharger les statistiques (CSV)",
                    data=csv,
                    file_name=f"stats_handball_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime='text/csv',
                )
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: #64748b; font-size: 0.875rem;'>
            <p>BHB Analytics Pro v2.0 | Dashboard Professionnel</p>
            <p style='font-size: 0.75rem; margin-top: 0.5rem;'>Développé avec Streamlit & Plotly | © 2026 BHB Handball</p>
        </div>
    """, unsafe_allow_html=True)

# ============================================================================
# POINT D'ENTRÉE
# ============================================================================

if __name__ == "__main__":
    main()

