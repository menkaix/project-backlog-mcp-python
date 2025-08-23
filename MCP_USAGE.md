# Utilisation du serveur MCP avec MCP Inspector

## 🎉 Serveur MCP Fonctionnel !

Votre projet a été transformé avec succès en serveur MCP compatible avec **MCP Inspector** via le transport HTTP streamable.

## 📋 Résumé des modifications

### ✅ Ce qui a été ajouté :

- **SDK MCP Python** installé (`mcp` package)
- **Handlers MCP** dans `mcp_server/mcp_handlers.py`
- **Endpoints MCP** dans le serveur FastAPI :
  - `GET /mcp/info` - Informations sur le serveur
  - `POST /mcp/list-tools` - Liste des outils disponibles
  - `POST /mcp/call-tool` - Exécution d'outils
- **Endpoints de debug** pour tester l'authentification

### 🔧 Outils MCP disponibles :

1. **`list_projects`** - Récupère la liste des projets depuis l'API HyperManager
2. **`create_diagram`** - Crée un nouveau diagramme avec nom et définition
3. **`list_diagrams`** - Récupère la liste des diagrammes

## 🚀 Comment utiliser avec MCP Inspector

### 1. Démarrer le serveur

```bash
python -m mcp_server.main
```

Le serveur démarre sur `http://localhost:5000`

### 2. Configuration MCP Inspector

- **URL de connexion** : `http://localhost:5000`
- **Transport** : HTTP Streamable
- **Authentification** : Header `x-mcp-key`
- **Clé API** : `test_api_key_123` (API_KEY configurée dans .env)

### 3. Endpoints MCP disponibles

- **Info** : `GET /mcp/info` (pas d'auth requise)
- **Liste des outils** : `POST /mcp/list-tools`
- **Appel d'outil** : `POST /mcp/call-tool`

## 🧪 Tests effectués

### ✅ Tests réussis :

- ✅ Authentification avec `x-mcp-key`
- ✅ Listing des outils MCP
- ✅ Appel des outils (`list_projects`, `list_diagrams`)
- ✅ Format JSON-RPC 2.0 respecté
- ✅ Gestion des erreurs

### 📝 Exemple de requête MCP :

```json
POST /mcp/call-tool
Headers: x-mcp-key: test_api_key_123
Body: {
  "jsonrpc": "2.0",
  "params": {
    "name": "list_projects",
    "arguments": {}
  }
}
```

## 🔍 Debug et maintenance

### Endpoints de debug disponibles :

- `GET /debug/api-key` - Vérifier la clé API chargée
- `POST /debug/auth-test` - Tester l'authentification

### Variables d'environnement importantes :

- `API_KEY` - Clé d'authentification pour les clients MCP
- `GOOGLE_API_KEY` - Clé pour l'API Google (utilisée par les outils)
- `BASE_URL` - URL de base de l'API HyperManager

## 🎯 Prochaines étapes

Votre serveur est maintenant prêt pour MCP Inspector ! Vous pouvez :

1. **Connecter MCP Inspector** avec les paramètres ci-dessus
2. **Tester les outils** via l'interface MCP Inspector
3. **Ajouter de nouveaux outils** en modifiant `mcp_server/mcp_handlers.py`
4. **Personnaliser l'authentification** si nécessaire

## 🔧 Compatibilité

- ✅ **MCP Inspector** - Transport HTTP streamable
- ✅ **Clients MCP** - Via endpoints HTTP standard
- ✅ **API REST classique** - Les endpoints `/tool/{tool_name}` restent disponibles

Le serveur est maintenant **dual-compatible** : il fonctionne à la fois comme serveur MCP et comme API REST classique !
