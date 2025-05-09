# 🧪 App de démonstration CI/CD + Streamlit

Ce projet est un exemple simple de pipeline de CI/CD avec GitHub Actions et déploiement automatique d’une application **Streamlit** sur **Streamlit Cloud**.

---

## 🚀 Aperçu de l'application

Additionneur simple :  
Entrez deux nombres et obtenez leur somme en un clic.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://<TON-USER>.streamlit.app)

---

## 📁 Structure du projet

├── src/
│ └── app.py # App principale Streamlit
├── tests/
│ └── test_app.py # Tests unitaires
├── streamlit_app.py # Point d'entrée pour Streamlit Cloud
├── requirements.txt # Dépendances Python
├── .github/workflows/ci.yml# Pipeline CI avec pytest
├── README.md



---

## ⚙️ Installation locale

```bash
git clone https://github.com/<TON-USER>/<TON-REPO>.git
cd <TON-REPO>
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate sous Windows
pip install -r requirements.txt
streamlit run streamlit_app.py

✅ Tests unitaires
pytest -v

🤖 CI avec GitHub Actions

À chaque push, les tests sont exécutés automatiquement via le fichier :

.github/workflows/ci.yml


☁️ Déploiement avec Streamlit Cloud

L’app est déployée automatiquement à partir du fichier streamlit_app.py.
