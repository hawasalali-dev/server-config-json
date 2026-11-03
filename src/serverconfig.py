
import json


# Aufgabe1 JSON-Datei erstellen


server_config = {
    "Servername": "Web-Server-01",
    "Port": 8080,
    "Aktiv": True,
    "Dienste": ["HTTP", "HTTPS"]
}

with open("server_config.json", "w", encoding="utf-8") as file:
    json.dump(server_config, file, indent=4, ensure_ascii=False)

print("Konfiguration gespeichert.")



# Aufgabe2 JSON-Datei einlesen


with open("server_config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

print("\nServername:", config["Servername"])

print("Aktive Dienste:")
for dienst in config["Dienste"]:
    print("-", dienst)
    
    

# Aufgabe3 Konfiguration ändern

config["Dienste"].append("SSH")
config["Port"] = 443

with open("server_config.json", "w", encoding="utf-8") as file:
    json.dump(config, file, indent=4, ensure_ascii=False)

print("\nKonfiguration aktualisiert.")



# Aufgabe4 JSON-String verarbeiten



api_response = '''
{
    "status": "ok",
    "code": 200,
    "message": "Erfolgreich"
}
'''

response_dict = json.loads(api_response)

print("\nStatuscode:", response_dict["code"])
