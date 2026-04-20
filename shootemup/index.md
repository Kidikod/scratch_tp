---
language: scratch
title: "Shoot em up : Pilote ton vaisseau spatial"
description: "Créer un petit shoot em up avec Scratch"
page_js:
  - assets/js/scratchblocks.min.js
  - assets/js/translations-all.js
---

## 📋 Contexte du projet

Dans cet atelier, on va concevoir un petit shoot em up. Tu y piloteras ton vaisseau à l’aide des flèches du clavier, tout en affrontant des ennemis qui apparaissent en formation. Il faudra les éliminer en tirant dessus pour gagner des points. Mais attention : les ennemis ne se laisseront pas faire.

Au fil de ce projet, on approfondira plusieurs notions essentielles. Tu apprendras notamment à utiliser le système de clones pour générer plusieurs copies d’un même sprite, à gérer les collisions entre objets du jeu, et à manipuler des variables pour suivre le score et le nombre de vies. Enfin, tu découvriras comment utiliser des messages afin de permettre aux différents éléments du jeu de communiquer entre eux efficacement.

## 🎨 Préparation : Les sprites et le décor

### 1. Crée les 3 sprites nécessaires

Tu auras besoin de :
1. **Mon vaisseau** - le vaisseau du joueur (dessin simple : triangle pointant vers le haut) - [mon vaisseau](resources/sprites/player_ship.svg)
2. **Ennemi** - un vaisseau ennemi qui se clonera - [ennemi](resources/sprites/enemy_ship.svg)
3. **Projectile** - ton tir (petit cercle ou carré) - [projectile](resources/sprites/projectile.svg)

## 🕹️ Étape 1 : Piloter ton vaisseau

Le vaisseau du joueur doit se déplacer avec les **flèches gauche/droite** et rester en bas de l'écran.

Commence à coder le sprite "mon vaisseau", voila ce qu'il va falloir développer :
- Évalue en continu les touches pressées
- Déplace le vaisseau à gauche ou droite
- Empêche le vaisseau de sortir de l'écran

Tu vas avoir besoin de ces blocs

<pre class="blocks">
quand le drapeau vert pressé
</pre>

<pre class="blocks">
répéter indéfiniment
fin
</pre>

<pre class="blocks">
si <> alors
</pre>

<pre class="blocks">
(abscisse x)
</pre>

<pre class="blocks">
ajouter () à x
</pre>

<pre class="blocks">
mettre x à ()
</pre>

<pre class="blocks">
<touche [flèche gauche v] pressée ?>
</pre>

<pre class="blocks">
<() < ()>
</pre>

Exemple de script du joueur :

<pre class="blocks">
quand le drapeau vert pressé
  répéter indéfiniment
    si <touche [flèche gauche v] pressée ?> alors
      ajouter (-5) à x
    fin
    si <touche [flèche droite v] pressée ?> alors
      ajouter (5) à x
    fin
    si <(abscisse x) < (-240)> alors
      mettre x à (-240)
    fin
    si <(abscisse x) > (240)> alors
      mettre x à (240)
    fin
  fin
</pre>

## 🔫 Étape 2 : Ajouter le système de tir

Quand tu appuies sur **ESPACE**, un projectile est lancé. Les projectiles se clonent du sprite "Projectile".

### Code du sprite "Mon vaisseau" (ajouter à la boucle principale)

<pre class="blocks">
  si <touche [espace v] pressée ?> alors
    créer un clone de [Projectile v]
    attendre (0.2) secondes
  fin
</pre>

### Code du sprite "Projectile"

<pre class="blocks">
quand je commence comme un clone
  aller à [Mon vaisseau v]
  mettre la taille à (25) % de la taille initiale
  répéter jusqu'à ce que <(ordonnée y) > (179)>
    ajouter (8) à y
  fin
  supprimer ce clone
</pre>

**Points importants :**
- Les clones héritent de la position du vaisseau au moment du tir
- Le projectile monte à chaque étape
- Il se supprime automatiquement quand il sort de l'écran

## 👾 Étape 3 : Créer les ennemis en formation

Les ennemis vont apparaître en **formation organisée** : 3 lignes de 4 ennemis.

### Code du sprite "Ennemi" (au démarrage)

<pre class="blocks">
quand le drapeau vert pressé
  cacher
  mettre [ligne v] à (0)
  répéter (3) fois
    répéter (4) fois
      créer un clone de [moi-même v]
      attendre (0.2) secondes
    fin
    ajouter (1) à [ligne v]
  fin
</pre>

### Code du clone ennemi

<pre class="blocks">
quand je commence comme un clone
  basculer sur le costume [ennemi v]
  mettre la taille à (30) % de la taille initiale
  montrer
  aller à x: (((ligne) * (100)) + (-150)) y: ((((3) - (ligne)) * (40)) + (150))
  répéter indéfiniment
    avancer de (2) pas
    tourner droite de (2) degrés
    si <(abscisse x) > (250)> alors
      mettre x à (-250)
    fin
    ajouter (-0.5) à y
    si <(ordonnée y) < (-180)> alors
      supprimer ce clone
    fin
  fin
</pre>

## 💥 Étape 4 : Les collisions

### Variables à créer
- **score** : nombre de points
- **vies** : nombre de vies restantes

### Code du sprite "Projectile" (ajouter au clone)

<pre class="blocks">
quand je commence comme un clone
  répéter jusqu'à ce que <(ordonnée y) > (180)>
    ajouter (8) à y
    si <touche le [Ennemi v] ?> alors
      envoyer à tous [ennemi touché v]
      ajouter (10) à [score v]
      supprimer ce clone
    fin
  fin
  supprimer ce clone
</pre>

### Code du sprite "Ennemi" (gérer les collisions)

<pre class="blocks">
quand je reçois [ennemi touché v]
  si <touche le [Projectile v] ?> alors
    supprimer ce clone
  fin
  
répéter indéfiniment
  si <touche le [Mon vaisseau v] ?> alors
    envoyer à tous [collision vaisseau v]
    supprimer ce clone
  fin
fin
</pre>

### Code du sprite "Mon vaisseau" (gérer les dégâts)

<pre class="blocks">
mettre [vies v] à (3)

quand je reçois [collision vaisseau v]
  ajouter (-1) à [vies v]
  si <(vies) = (0)> alors
    dire [Fin du jeu !] pendant (2) secondes
    stop [tout v]
  fin
</pre>

## 📊 Étape 5 : Affichage du score et des vies

### Code du sprite "Arrière-plan"

<pre class="blocks">
quand le drapeau vert pressé
  mettre [score v] à (0)
  mettre [vies v] à (3)

répéter indéfiniment
  dire (regrouper [Score: ] et (regrouper (score) et (regrouper [  |  Vies: ] et (vies))))
fin
</pre>

## 🔫 Étape 6 : Ajouter les tirs ennemis

Les ennemis vont aussi tirer sur toi ! Tu dois les éviter pour ne pas perdre de vies.

### Code du sprite "Ennemi" (ajouter à la boucle du mouvement)

<pre class="blocks">
quand je commence comme un clone
  répéter indéfiniment
    si <(nombre aléatoire entre (1) et (100)) = (1)> alors
      créer un clone de [Projectile ennemi v]
    fin
    attendre (0.5) secondes
  fin
</pre>

### Code du sprite "Projectile ennemi" (nouveau sprite)

<pre class="blocks">
quand je commence comme un clone
  mettre la taille à (25) % de la taille initiale
  répéter jusqu'à ce que <(ordonnée y) < (-180)>
    ajouter (-8) à y
    si <touche le [Mon vaisseau v] ?> alors
      envoyer à tous [collision vaisseau v]
      supprimer ce clone
    fin
  fin
  supprimer ce clone
</pre>

**Points importants :**
- Les ennemis tirent **aléatoirement** (pas trop souvent)
- Les projectiles ennemis **descendent** vers le joueur
- Le joueur perd une vie au contact

## 📈 Étape 7 : Implémenter les niveaux progressifs

Le jeu devient plus difficile à chaque niveau ! Les ennemis sont plus rapides et plus nombreux.

### Variables à créer
- **niveau** : numéro du niveau actuel
- **vitesse_ennemis** : vitesse d'apparition
- **nombre_ennemis** : quantité d'ennemis par vague

### Code du sprite "Arrière-plan"

<pre class="blocks">
quand le drapeau vert pressé
  mettre [score v] à (0)
  mettre [vies v] à (3)
  mettre [niveau v] à (1)
  répéter indéfiniment
    si <(score) > ((niveau) * (50))> alors
      ajouter (1) à [niveau v]
      envoyer à tous [niveau augmenté v]
      dire (regrouper [Niveau ] et (regrouper (niveau) et [ ! ])) pendant (2) secondes
    fin
    dire (regrouper [Score: ] et (regrouper (score) et (regrouper [  |  Niveau: ] et (niveau))))
  fin
</pre>

### Code du sprite "Ennemi" (modifier la formation)

<pre class="blocks">
quand le drapeau vert pressé
  cacher
  mettre [ligne v] à (0)
  répéter ((3) + (niveau)) fois
    répéter (4) fois
      créer un clone de [moi-même v]
      attendre ((0.2) - ((niveau) * (0.01))) secondes
    fin
    ajouter (1) à [ligne v]
  fin

quand je reçois [niveau augmenté v]
  ajouter (0.5) à [vitesse_ennemis v]
</pre>

### Code du clone ennemi (modifier la vitesse)

<pre class="blocks">
quand je commence comme un clone
  basculer sur le costume [ennemi v]
  mettre la taille à (30) % de la taille initiale
  montrer
  mettre [vitesse_ennemis v] à ((2) + (niveau))
  mettre x à (((ligne) * (100)) + (-150))
  mettre y à ((((3) - (ligne)) * (40)) + (150))
  répéter indéfiniment
    avancer de (vitesse_ennemis) pas
    tourner droite de (2) degrés
    si <(abscisse x) > (250)> alors
      mettre x à (-250)
    fin
    ajouter (-0.5) à y
    si <(ordonnée y) < (-180)> alors
      supprimer ce clone
    fin
  fin
</pre>

**Difficulté progressive :**
- Niveau 1 : 3 lignes d'ennemis, vitesse 2
- Niveau 2 : 4 lignes, vitesse 2.5, tirs plus rapides
- Niveau 3+ : Plus d'ennemis, plus rapides chaque fois

## ⚡ Étape 8 : Les Power-ups

Des bonus apparaissent aléatoirement pour t'aider ! Récupère-les pour des avantages.

### Variables à créer
- **bouclier_actif** : vrai/faux si un bouclier est actif
- **cadence_rapide** : vrai/faux pour les tirs rapides

### Code du sprite "Ennemi" (générer les power-ups)

<pre class="blocks">
quand je reçois [ennemi touché v]
  si <(nombre aléatoire entre (1) et (10)) < (4)> alors
    créer un clone de [PowerUp v]
    mettre x du clone à (abscisse x)
    mettre y du clone à (ordonnée y)
  fin
  supprimer ce clone
</pre>

### Code du sprite "PowerUp" (nouveau sprite)

<pre class="blocks">
quand je commence comme un clone
  mettre la taille à (50) % de la taille initiale
  montrer
  si <(nombre aléatoire entre (1) et (2)) = (1)> alors
    basculer sur le costume [bouclier v]
    mettre [type_powerup v] à [bouclier v]
  fin
  sinon
    basculer sur le costume [rapidfire v]
    mettre [type_powerup v] à [rapidfire v]
  fin
  répéter jusqu'à ce que <(ordonnée y) < (-180)>
    ajouter (-3) à y
    si <touche le [Mon vaisseau v] ?> alors
      si <(type_powerup) = [bouclier v]> alors
        mettre [bouclier_actif v] à (vrai)
        envoyer à tous [bouclier activé v]
      sinon
        mettre [cadence_rapide v] à (vrai)
        attendre (5) secondes
        mettre [cadence_rapide v] à (faux)
      fin
      supprimer ce clone
    fin
  supprimer ce clone
</pre>

### Code du sprite "Mon vaisseau" (utiliser les bonuses)

<pre class="blocks">
quand je reçois [collision vaisseau v]
  si (bouclier_actif) alors
    mettre [bouclier_actif v] à (faux)
    envoyer à tous [bouclier désactivé v]
  sinon
    ajouter (-1) à [vies v]
  fin

répéter indéfiniment
  si <touche [espace v] pressée ?> alors
    créer un clone de [Projectile v]
    si (cadence_rapide) alors
      attendre (0.05) secondes
    sinon
      attendre (0.2) secondes
    fin
  fin
fin
</pre>

**Types de power-ups :**
- 🛡️ **Bouclier** : Protège un coup
- ⚡ **Tirs Rapides** : Double la cadence pendant 5 sec
- 🎯 Idée future : Ralentisseur d'ennemis

## 🎬 Étape 9 : Animations visuelles

Rend le jeu plus vivant avec des animations !

### Code du sprite "Arrière-plan" (Début du jeu)

<pre class="blocks">
quand le drapeau vert pressé
  dire [Prépare-toi !] pendant (1) secondes
  dire [3...] pendant (1) secondes
  dire [2...] pendant (1) secondes
  dire [1...] pendant (1) secondes
  dire [À l'attaque !] pendant (1) secondes
</pre>

### Code du sprite "Mon vaisseau" (Clignoter après collision)

<pre class="blocks">
quand je reçois [collision vaisseau v]
  répéter (4) fois
    cacher
    attendre (0.1) secondes
    montrer
    attendre (0.1) secondes
  fin
</pre>

### Code du sprite "Explosion" (nouvelle animation)

<pre class="blocks">
quand je reçois [explosion v]
  mettre x à (abscisse x du clone ennemi)
  mettre y à (ordonnée y du clone ennemi)
  montrer

  répéter (3) fois
    ajouter (5) à [taille v] %
    attendre (0.1) secondes
  fin
  
  cacher
</pre>

### Code du sprite "Ennemi" (créer l'explosion)

<pre class="blocks">
quand je reçois [ennemi touché v]
  envoyer à tous [explosion v]
  supprimer ce clone
</pre>

### Code du sprite "Mon vaisseau" (Game Over dramatique)

<pre class="blocks">
  mettre [texture v] à [GAME OVER]
  dire [GAME OVER !] pendant (3) secondes
  dire (regrouper [Score final: ] et (score)) pendant (2) secondes
  dire (regrouper [Niveau atteint: ] et (niveau)) pendant (2) secondes
  attendre (1) secondes
  dire [Appuie sur le drapeau vert pour recommencer] pendant (3) secondes
</pre>

**Animations ajoutées :**
- Compte à rebours au démarrage
- Clignotement du vaisseau après coup
- Explosion visible au centre des ennemis

## 🔊 Étape 10 : Les sons rétro 8-bit (Bonus)

Ajoute une ambiance sonore arcade !

### Code du sprite "Mon vaisseau" (Son au tir)

<pre class="blocks">
répéter indéfiniment
  si <touche [espace v] pressée ?> alors
    jouer la note [C5 v] pendant (0.05) temps
    créer un clone de [Projectile v]
    attendre (0.2) secondes
  fin
fin
</pre>

### Code du sprite "Ennemi" (Son de destruction)

<pre class="blocks">
quand je reçois [ennemi touché v]
  jouer la note [D5 v] pendant (0.1) temps
  jouer la note [B4 v] pendant (0.1) temps
  jouer la note [G4 v] pendant (0.1) temps
  supprimer ce clone
</pre>

### Code du sprite "Arrière-plan" (Musique de fond)

<pre class="blocks">
quand le drapeau vert pressé
  répéter indéfiniment
    jouer la note [C4 v] pendant (0.5) temps
    jouer la note [E4 v] pendant (0.5) temps
    jouer la note [G4 v] pendant (0.5) temps
    jouer la note [C5 v] pendant (2) temps
  fin
</pre>

### Code du sprite "Mon vaisseau" (Son de collision)

<pre class="blocks">
quand je reçois [collision vaisseau v]
  jouer la note [G3 v] pendant (0.1) temps
  jouer la note [C3 v] pendant (0.2) temps
</pre>

**Effets sonores rétro :**
- 🔊 Tir : Note aigüe courte (C5)
- 💥 Explosion : Descente de notes (D5 → B4 → G4)
- ⚠️ Collision : Deux notes basses (G3 → C3)
- 🎵 Musique : Boucle simple C-E-G-C

## 💡 Points clés à retenir

| Concept | Utilité |
|---------|---------|
| **Clones** | Créer plusieurs copies d'un sprite (ennemis, projectiles) |
| **Messages** | Faire communiquer les sprites entre eux |
| **Variables** | Suivre le score, les vies, les niveaux |
| **Touches** | Gérer les contrôles du joueur |
| **Collisions** | Détecter quand deux sprites se touchent |
| **Position** | abscisse x et ordonnée y pour placer les sprites précisément |

## 🚀 Fiche récapitulative rapide

Ordre de programmation recommandé :
1. ✅ Mouvement du vaisseau (étape 1)
2. ✅ Système de tir (étape 2)
3. ✅ Ennemis en formation (étape 3)
4. ✅ Collisions et score (étape 4)
5. ✅ Affichage score/vies (étape 5)
6. 🎁 **Tirs ennemis** (étape 6)
7. 📊 **Niveaux progressifs** (étape 7)
8. ⚡ **Power-ups** (étape 8)
9. 🎬 **Animations visuelles** (étape 9)
10. 🔊 **Sons rétro** (étape 10)

---

**Tip pour les enseignants** : Les étapes 1-5 sont essentielles. Les étapes 6-10 peuvent être faites en fonction du temps disponible. Elles offrent une bonne progressions pour les élèves avancés ! 

**Bon codage et amusement avec ton shoot em up !** 🎮

<script>
scratchblocks.renderMatching('pre.blocks', {
  style: 'scratch3',
  languages: ['fr'],
  scale: 1,
});
</script>