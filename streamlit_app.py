import streamlit as st
import wandb

# Connexion W&B
wandb.login(key="af2eeae6b46bcf5c0a0f64d2abf38a4ebe1d57f2")

st.set_page_config(page_title="NetSecurePro - W&B Logs", layout="centered")
st.title("Visualisation IA - NetSecurePro")
st.markdown("Connecté à **Weights & Biases** via l'organisation `gfbleu-netsecurepro-`")

st.markdown("---")
st.markdown("### Derniers Logs :")

# Récupération des runs W&B (derniers 5 runs)
api = wandb.Api()
runs = api.runs("gfbleu-netsecurepro-/NetSecurePro")

for run in runs[:5]:
    st.subheader(run.name)
    st.write(f"Créé le : {run.created_at}")
    st.write(f"Résumé : {run.summary}")
    st.markdown("---")

st.markdown("Accès complet : [Tableau de bord W&B](https://wandb.ai/gfbleu-netsecurepro-/NetSecurePro)")