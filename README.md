# Serveur MCP

Ce projet contient un serveur MCP (Mission Control Platform) qui expose des outils via une API HTTP sécurisée.

## 🚀 Démarrage Rapide

### Prérequis

- Docker
- Docker Compose

### Configuration

1.  **Créer un fichier `.env`** :
    Copiez le fichier `.env.example` et renommez la copie en `.env`.

    ```bash
    cp .env.example .env
    ```

2.  **Configurer la clé API** :
    Ouvrez le fichier `.env` et remplacez `votre_cle_api` par une clé secrète de votre choix. Cette clé sera utilisée pour sécuriser l'accès au serveur.

    ```dotenv
    API_KEY=votre_cle_api_secrete
    GOOGLE_API_KEY=votre_cle_api_google
    BASE_URL=https://hypermanager-ia.endpoints.hypermanager.cloud.goog
    ```

### Lancement du serveur

Utilisez Docker Compose pour construire et lancer le serveur :

```bash
docker-compose up --build
```

Le serveur sera accessible à l'adresse `http://localhost:5000`.

## 🛠️ Utilisation de l'API

Pour exécuter un outil, envoyez une requête `POST` à l'endpoint `/tool/{tool_name}`.

- **URL** : `http://localhost:5000/tool/{nom_de_l_outil}`
- **Méthode** : `POST`
- **En-tête requis** : `X-API-KEY: votre_cle_api_secrete`
- **Corps de la requête** (JSON) : Les paramètres de l'outil.

### Exemple avec `curl`

Voici un exemple d'appel à un outil nommé `example_tool` avec des paramètres :

```bash
curl -X POST "http://localhost:5000/tool/example_tool" \
-H "Content-Type: application/json" \
-H "X-API-KEY: votre_cle_api_secrete" \
-d '{
    "param1": "valeur1",
    "param2": 123
}'
```

### Réponse

- **Succès (200 OK)** :

  ```json
  {
    "result": "Le résultat de l'outil..."
  }
  ```

- **Erreur d'authentification (403 Forbidden)** :

  ```json
  {
    "detail": "Could not validate credentials"
  }
  ```

- **Outil non trouvé (404 Not Found)** :
  ```json
  {
    "detail": "Tool 'nom_de_l_outil' not found."
  }
  ```
