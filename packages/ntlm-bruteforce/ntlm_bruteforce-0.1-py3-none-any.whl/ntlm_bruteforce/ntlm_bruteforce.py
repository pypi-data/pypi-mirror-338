import argparse
import random
import string
from ntlm_bruteforce import NTLMBruteforcer

# Liste des utilisateurs pour l'exemple (remplace avec ta vraie logique)
users = ["user1", "user2", "user3"]  # Exemple de liste d'utilisateurs

def list_users():
    """Lister les utilisateurs disponibles."""
    for idx, user in enumerate(users):
        print(f"{idx}: {user}")

def show_hash(user_index):
    """Afficher le hash de l'utilisateur sélectionné."""
    user = users[user_index]
    # Logique pour obtenir le hash de l'utilisateur (remplace par la logique réelle)
    print(f"Hash pour {user}: (exemple de hash)")

def generate_wordlist(min_len, max_len):
    """Générer une wordlist avec des mots aléatoires de longueur entre min_len et max_len."""
    wordlist = []
    for length in range(min_len, max_len + 1):
        word = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        wordlist.append(word)
    print(f"Wordlist générée avec des mots de longueur {min_len} à {max_len}:")
    for word in wordlist:
        print(word)
    return wordlist

def test_create_and_delete(user_index, wordlist):
    """Tester la création de mots de passe, les tester, puis les supprimer jusqu'à ce que le bon mot de passe soit trouvé."""
    user = users[user_index]
    for word in wordlist:
        print(f"Tentative de création du mot de passe: {word}")
        # Logique pour tester le mot de passe (remplace par ta logique de test réel)
        print(f"Tester le mot de passe pour {user}: {word}")
        # Si le mot de passe est correct, tu peux ajouter la logique pour arrêter
        if word == "correct_password":  # Remplace par ta condition pour trouver le bon mot de passe
            print(f"Mot de passe trouvé pour {user}: {word}")
            break
        else:
            print(f"Mot de passe incorrect pour {user}: {word}")
            # Logique pour supprimer le mot de passe si nécessaire
            print(f"Suppression du mot de passe: {word}")
            # Puis recréer le mot de passe pour tester le suivant

def run_bruteforce(user_index, wordlist_path):
    """Lancer le bruteforce avec un utilisateur sélectionné et une wordlist."""
    user = users[user_index]
    bruteforcer = NTLMBruteforcer(
        sam_path="C:/Windows/System32/config/SAM",  # Remplace avec ton chemin
        system_path="C:/Windows/System32/config/SYSTEM",  # Remplace avec ton chemin
        charset="azerty123",  # Par défaut, tu peux ajuster selon ta logique
        min_len=1,
        max_len=5
    )
    print(f"Bruteforce pour {user} avec la wordlist {wordlist_path}")
    bruteforcer.run()  # Lance le bruteforce

def main():
    parser = argparse.ArgumentParser(description="Outil de bruteforce NTLM")
    
    # Argument pour lister les utilisateurs
    parser.add_argument('-list', action='store_true', help="Lister les utilisateurs")
    
    # Argument pour sélectionner un utilisateur
    parser.add_argument('-s', type=int, help="Sélectionner un utilisateur par index")
    
    # Argument pour afficher le hash d'un utilisateur
    parser.add_argument('-h', type=int, help="Afficher le hash de l'utilisateur sélectionné")
    
    # Argument pour la wordlist
    parser.add_argument('-w', type=str, help="Spécifier le fichier de la wordlist")
    
    # Argument pour générer une wordlist avec une plage de longueur spécifiée
    parser.add_argument('-wm', type=str, help="Générer une wordlist avec une plage de longueur (par exemple, 8;16)")
    
    # Argument pour tester la création et suppression des mots de passe
    parser.add_argument('-test', action='store_true', help="Tester la création et suppression de mots de passe")

    args = parser.parse_args()
    
    if args.list:
        list_users()
    elif args.s is not None:
        if args.h is not None:
            show_hash(args.s)
        elif args.w:
            run_bruteforce(args.s, args.w)
        elif args.wm:
            # Gérer la génération de la wordlist avec la plage dynamique
            try:
                min_len, max_len = map(int, args.wm.split(';'))
                wordlist = generate_wordlist(min_len, max_len)
                if args.test:
                    test_create_and_delete(args.s, wordlist)
                else:
                    run_bruteforce(args.s, wordlist)
            except ValueError:
                print("Erreur : La syntaxe de l'argument -wm doit être sous la forme 'min_len;max_len' (ex: 8;16).")
        else:
            print("Erreur : Si un utilisateur est sélectionné, tu dois spécifier une wordlist avec -w ou -wm.")
    else:
        print("Erreur : Tu dois spécifier une option valide.")

if __name__ == "__main__":
    main()
