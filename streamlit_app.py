import streamlit as st
import wandb

# Connexion sécurisée à W&B
wandb.login()  # Laisse WandB chercher le token dans l’environnement

st.set_page_config(page_title="NetSecurePro - W&B Logs", layout="centered")
st.title("Visualisation IA - NetSecurePro")
st.markdown("Connecté à **Weights & Biases** via l'organisation `gfbleu-netsecurepro`")

st.markdown("---")
st.markdown("### Derniers Logs :")

try:
    # Correction du nom du projet
    api = wandb.Api()
    runs = api.runs("gfbleu-netsecurepro/NetSecurePro")

    if not runs:
        st.warning("Aucun run trouvé pour ce projet.")
    else:
        for run in runs[:5]:
            st.subheader(run.name)
            st.write(f"Créé le : {run.created_at}")
            st.write(f"Résumé : {run.summary}")
            st.markdown("---")
except Exception as e:
    st.error(f"Erreur lors de la récupération des données : {e}")

st.markdown("Accès complet : [Tableau de bord W&B](https://wandb.ai/gfbleu-netsecurepro/NetSecurePro)")
