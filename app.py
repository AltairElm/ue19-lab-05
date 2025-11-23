import requests
import sys

# URL de l'API pour une blague simple.
API_URL = "https://v2.jokeapi.dev/joke/Any?safe-mode"

try:
    # Effectue la requête HTTP GET et lève une exception en cas d'erreur de statut (4xx/5xx).
    response = requests.get(API_URL)
    response.raise_for_status()
    
    data = response.json()
    
    # Vérifie si l'API a retourné une erreur dans le corps de la réponse.
    if data.get("error"):
        print(f"Erreur API: {data.get('message')}")
        sys.exit(1)
        
    # Affiche la blague directement.
    print(data.get("joke", "Blague non disponible."))
    
except requests.exceptions.RequestException as e:
    # Gère les erreurs de connexion (DNS, timeout, etc.).
    print(f"Erreur de connexion: {e}")
    sys.exit(1)