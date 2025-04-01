from mvola_api import MVolaClient
import time

# Initialiser le client
client = MVolaClient(
    consumer_key="gwazRgSr3HIIgfzUchatsMbqwzUa",
    consumer_secret="Ix1FR6_EHu1KN18G487VNcEWEgYa",
    partner_name="CNTEMAD",
    partner_msisdn="0343500004",  # Numéro marchand
    sandbox=True  # Utiliser l'environnement sandbox
)

# Générer un token
token_data = client.generate_token()
print(f"Token généré: {token_data['access_token'][:10]}...")

# Initier un paiement 
# IMPORTANT: Selon l'exemple qui fonctionne, on inverse les numéros de débit et de crédit
# Dans l'exemple fonctionnel, le 0343500004 est le débiteur et 0343500003 est le créditeur
result = client.initiate_payment(
    amount=1000,
    debit_msisdn="0343500004",  # Le débiteur est le marchand dans l'exemple qui fonctionne
    credit_msisdn="0343500003",  # Le créditeur est le client dans l'exemple qui fonctionne
    description="Test Transaction",
    callback_url="https://example.com/callback"
)

# Suivre l'ID de corrélation du serveur pour les vérifications de statut
server_correlation_id = result['response']['serverCorrelationId']
print(f"Transaction initiée avec l'ID de corrélation: {server_correlation_id}")

# Test 1: Vérifier le statut initial de la transaction
print("\n=== Test de get_transaction_status (statut initial) ===")
status_result = client.get_transaction_status(server_correlation_id)
print(f"Statut HTTP: {status_result['status_code']}")
print(f"Statut initial de la transaction: {status_result['response']['status']}")
print(f"Détails complets: {status_result['response']}")

# Boucle de vérification du statut
print("\n=== Boucle de vérification du statut ===")
max_attempts = 70  # Nombre maximum de tentatives
waiting_time = 1    # Temps d'attente entre chaque vérification (en secondes)
current_attempt = 1
transaction_status = status_result['response']['status']

while transaction_status == "pending" and current_attempt <= max_attempts:
    print(f"Tentative {current_attempt}/{max_attempts} - Statut actuel: {transaction_status}")
    print(f"Attente de {waiting_time} secondes avant nouvelle vérification...")
    time.sleep(waiting_time)
    
    # Revérifier le statut
    status_result = client.get_transaction_status(server_correlation_id)
    transaction_status = status_result['response']['status']
    current_attempt += 1

print(f"\nStatut final après {current_attempt-1} vérifications: {transaction_status}")

# Afficher un message spécifique selon le statut de la transaction
if transaction_status == "pending":
    print("En attente d'approbation")
    print("La transaction est toujours en attente après toutes les tentatives de vérification.")
    print("Vous devrez peut-être l'approuver manuellement dans le portail développeur MVola.")
elif transaction_status == "completed":
    print("La transaction est Réussie")
    print("Le paiement a été approuvé et traité avec succès.")
elif transaction_status == "failed":
    print("Échec de transaction")
    print("Le paiement a été rejeté ou a échoué pendant le traitement.")
else:
    print(f"Statut final: {transaction_status}")
    print("Statut non reconnu ou en cours de traitement.")

# Test 3: Obtenir les détails de la transaction
print("\n=== Test de get_transaction_details ===")

# Vérifier si un objectReference est disponible (ID de transaction)
transaction_id = status_result['response'].get('objectReference')

if transaction_id and transaction_id.strip():
    print(f"ID de transaction obtenu: {transaction_id}")
    
    try:
        # Récupérer les détails avec l'ID de transaction
        details_result = client.get_transaction_details(transaction_id)
        print(f"Statut HTTP: {details_result['status_code']}")
        print(f"Détails de la transaction: {details_result['response']}")
    except Exception as e:
        print(f"Erreur lors de la récupération des détails: {str(e)}")
else:
    print("L'objectReference est vide ou non disponible")
    
    # Message spécifique selon le statut
    if transaction_status == "pending":
        print("La transaction est encore en attente d'approbation")
        print("\nNote: Dans l'environnement sandbox, les transactions restent souvent en état 'pending'")
        print("Pour les tests, vous devriez approuver manuellement la transaction dans le portail développeur MVola")
    elif transaction_status == "completed":
        print("La transaction est complétée mais l'ID de référence n'est pas disponible")
        print("C'est inhabituel - vérifiez dans le portail développeur MVola")
    elif transaction_status == "failed":
        print("La transaction a échoué. Aucun ID de référence n'est généré pour les transactions échouées")
        print("Vérifiez les détails de l'échec dans le portail développeur MVola")
    else:
        print(f"La transaction a un statut inhabituel: {transaction_status}")
        print("Vérifiez le portail développeur MVola pour plus de détails") 