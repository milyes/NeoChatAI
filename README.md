# NeoChat AI

NeoChat AI est une application de messagerie en temps réel basée sur **FastAPI** et **Vue.js**, avec support WebSocket et architecture prête pour l'intégration IA.

## Fonctionnalités
- Messagerie en temps réel via WebSocket
- Frontend moderne avec Vue 3 + TailwindCSS
- Architecture prête pour :
  - Authentification utilisateur
  - Multi-salons
  - Base de données (SQLite, PostgreSQL)
  - Intégration GPT / IA de réponse automatique

## Démarrage rapide

### Backend (FastAPI)

```bash
cd backend
pip install fastapi uvicorn
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend (Vue 3)

```bash
cd frontend
npm install
npm run dev
```

L’application est ensuite accessible sur :
- Frontend : `http://localhost:5173`
- Backend : `http://localhost:8000`
- WebSocket : `ws://localhost:8000/ws/chat`

## Auteur
Mohammed Ilyes — Projet NeoChatAI sous licence MIT.
