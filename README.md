# Projet de sécurité des systèmes cyber-physiques

<!-- SOMMAIRE -->
<details>
  <summary><strong style="color:red">Sommaire</strong></summary>
  <ol>
    <li>
      <a href="#présentation-du-projet">Présentation du projet</a>
      <ul>
        <li><a href="#membres-du-groupe">Membres du groupe</a></li>
        <li><a href="#matériel-fourni">Matériel fourni</a></li>
        <li><a href="#objectif">Objectif</a></li>
        <li><a href="#contenu-du-github">Contenu du github</a></li>
      </ul>
    </li>
    <li>
      <a href="#description-de-lattaque-réalisée">Description de l'attaque réalisée</a>
      <ul>
        <li><a href="#phase-1--initialisation-serverpy">phase 1 : Initialisation (server.py)</a></li>
        <li><a href="#phase-2--attaque-via-bash-bunny-clientpy-payloadtxt">phase 2 : Attaque via Bash Bunny (client.py, payload.txt)</a></li>
        <li><a href="#phase-3--pilotage-et-visualisation-de-lattaque-avec-lesp32-mainpy">phase 3 : Pilotage et visualisation de l'attaque avec l'ESP32 (main.py)</a></li>
      </ul>
    </li>
  </ol>
</details>

## **Présentation du projet**

### **Membres du groupe**
- JOUFFRAULT Guillaume
- LAFLEUR Hugo
- MAGNIEZ Clément

### **Matériel fourni**
- ATOM Matrix (de M5Stack et basé sur un ESP32-Pico)
- Bash Bunny (Hak5)

### **Objectif**
L'objectif de ce projet est de réaliser une attaque en utilisant à la fois la Bash Bunny et l'ESP32.
<br />
- La Bash Bunny permet de s'introduire sur le pc de la victime et d'effectuer une attaque (en écrivant des commandes et en lançant des scripts).
- L'ESP32 permet de piloter physiquement l'attaque (à l'aide du bouton) et de visualiser l'attaque (à l'aide des leds).

### **Contenu du github**
Ce github se décompose en 3 parties :
- <text style="color:red;">**README.md**</text> contient le rapport du projet.
- <text style="color:green;">**demo.mp4**</text>
est une démonstration vidéo (2min20s) de l'attaque réalisée sur un pc windows.
- <text style="color:blue;">**files/**</text>
est un dossier contenant tous les fichiers permettant de réaliser l'attaque (sur windows ou sur linux).

## **Description de l'attaque réalisée**

L'attaque se déroule en 3 phases. Les languages de programmation utilisés sont Python et Bunny Script (pour la Bash Bunny).

### **phase 1 : Initialisation (server.py)**
Durant cette phase l'attaquant réalise 2 actions :
- Se placer à proximité du pc de la victime et activer la source wifi (ici on utilise un partage de connexion depuis le pc de l'attaquant).
- Lancer le script server.py sur le pc de l'attaquant.
Ce script permet au pc de l'attaquant de jouer le rôle du serveur dans l'interface client/serveur mis en place dans l'attaque.
L'attaquant (serveur) recevra les données envoyées par la victime (client). Cela nécessite que l'attaquant et la victime soient sur le même réseau wifi.

### **phase 2 : Attaque via Bash Bunny (client.py, payload.txt)**
Durante cette phase l'attaquant doit accéder physiquement au pc de la victime et brancher la Bash Bunny en usb.

Nous avons développé 2 payloads selon que le pc soit sous windows ou sous linux. L'attaque se réalise de façon similaire sous windows et sous linux :
- le pc de la victime se connecte au wifi de l'attaquant.
Sous linux c'est une simple commande nmcli tandis que sous windows il faut créer un profil wifi (car la victime ne s'est jamais connecté à ce wifi), on réalise cela avec un script powershell 'connect_to_wifi.ps1'.
- lancement du script client.py (qui est situé dans la Bash Bunny). L'interface client/serveur est maintenant en place.

Une fois ces 2 actions réalisées par la Bash Bunny (cela dure 15 secondes environ), il n'y a plus de trace visuelle sur le pc de la victime (l'exécution du fichier client.py en fond n'est pas directement visible).

### **phase 3 : Pilotage et visualisation de l'attaque avec l'ESP32 (main.py)**
L'attaquant observe sur son pc que la victime s'est connectée.
<br/>
L'attaquant connecte l'ESP32 à son pc et lance le script main.py. Ce script permet de réaliser 3 attaques :
- visualiser sur les leds de l'ESP32 ce qu'écrit la victime sur son pc (client.py contient un keylogger et main.py transforme les touches activées en signal led)
- appuyer sur le bouton de l'ESP32 prend un screenshot en temps réel du pc de la victime (le screenshot est enregistré sur le pc de l'attaquant).
- appuyer 2 fois sur le bouton de l'ESP32 prend une photo avec la caméra du pc de la victime (la photo est enregistrée sur le pc de l'attaquant).

