import streamlit as st 
import requests 

# Ajout d'un logo
st.image('logo.png', width=200)

# Ajout d'un titre 
st.title('My Content - Recommandation d\'articles de presse')

# Ajout d'un texte de présentation 
st.markdown("Bienvenue sur My Content ! Nous sommes heureux de vous offrir une présentation personnalisée des articles les plus populaires et les plus intéressants. Pour commencer, veuillez entrer votre ID ci-dessous pour voir les articles que nous vous recommandons.")

# Récupération de l'adresse API
api_url = st.text_input('Entrez l\'adresse de l\'api (si aucune n\'est entrée, l\'adresse par défaut est https://p9.azurewebsites.net/api/) : ')
if api_url == '':
    api_url = 'https://p9.azurewebsites.net/api/'

# Récupération de l'id 
id = st.text_input('Entrez votre id : ')

if id:
    # Récupération des données de l'API
    url = '{}/{}'.format(api_url, id)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Affichage des articles recommandés
        st.balloons()
        st.success('Voici les ID des articles recommandés: ')
        for article_id in data['article_id']:
            st.write('- {}'.format(article_id))
        st.markdown("Bonne lecture !")
    else:
        st.write('Aucun article trouvé')
else:
    st.write('Veuillez entrer un ID pour afficher les articles recommandés.')
