# NTLM Bruteforce

Une librairie Python pour récupérer et brute-forcer un hash NTLM à partir des fichiers SAM et SYSTEM.

## Installation

Pour installer la librairie, utilisez la commande suivante :
pip install ntml_bruteforce

## Exemple d'utilisation

```python
from ntlm_bruteforce import NTLMBruteforcer

bruteforcer = NTLMBruteforcer(
    sam_path="C:/Windows/System32/config/SAM",
    system_path="C:/Windows/System32/config/SYSTEM",
    charset="azerty123",
    min_len=1,
    max_len=5
)
bruteforcer.run()


---

### 3. Construire et publier sur PyPI (optionnel)

Si tu veux publier sur **PyPI**, tu peux utiliser ces commandes pour construire et uploader ton package.

#### Installer les outils nécessaires :
```bash
pip install setuptools wheel twine
