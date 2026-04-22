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
1. **joueur** - le vaisseau du joueur (dessin simple : triangle pointant vers le haut) - [joueur](resources/sprites/player_ship.svg)
2. **ennemi** - un vaisseau ennemi qui se clonera - [ennemi](resources/sprites/enemy_ship.svg)
3. **projectile** - ton tir (petit cercle ou carré) - [projectile](resources/sprites/projectile.svg)

## 🕹️ Étape 1 : Piloter ton vaisseau

Le vaisseau du joueur doit se déplacer avec les **flèches gauche/droite** et rester en bas de l'écran.

Commence à coder le sprite "joueur", voila ce qu'il va falloir développer :
- Évalue en continu les touches pressées
- Déplace le vaisseau à gauche ou droite
- Empêche le vaisseau de sortir de l'écran

Tu vas avoir besoin de ces blocs :

<pre class="blocks">
quand le drapeau vert pressé

répéter indéfiniment
fin

si <> alors

(abscisse x)

ajouter () à x

mettre x à ()

mettre y à ()

<touche [ v] pressée ?>

<() < ()>
</pre>

<details>
  <summary>Exemple de script du "joueur"</summary>

  <pre class="blocks">
  quand le drapeau vert pressé
    mettre y à (-140)
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
</details>

## 🔫 Étape 2 : Ajouter le système de tir

Quand tu appuies sur **ESPACE**, un projectile est lancé. Les projectiles sont des clones du sprite "projectile".

Voila ce qu'il va falloir développer :
- Les clones héritent de la position du vaisseau au moment du tir
- Le projectile monte à chaque étape
- Il se supprime automatiquement quand il sort de l'écran

Tu vas avoir besoin de ces blocs :
<pre class="blocks">
quand le drapeau vert pressé

créer un clone de [ v]

quand je commence comme un clone

supprimer ce clone

si <> alors
fin

répéter jusqu'à ce que <>
fin

(ordonnée y)

ajouter () à y

aller à x: () y: ()

aller à [ v]

<() > ()>

(() + ())

(() modulo ())

réinitialiser le chronomètre

(chronomètre)

mettre [ v] à ()

cacher

montrer
</pre>

<details>
  <summary>Code du sprite "joueur" (ajouter à la boucle principale)</summary>

  <pre class="blocks">
    réinitialiser le chronomètre
    mettre [décompte tir v] à (chronomètre)

    si <<touche [espace v] pressée ?> et <(chronomètre) > (décompte tir)>> alors
      créer un clone de [projectile v]
      mettre [décompte tir v] à ((chronomètre) + (0.5))
    fin
  </pre>
</details>

<details>
  <summary>Code du sprite "projectile"</summary>

  <pre class="blocks">
  quand le drapeau vert pressé
    aller à x: (-240) y: (-180)
    cacher

  quand je commence comme un clone
    aller à [joueur v]
    montrer
    répéter jusqu'à ce que <(ordonnée y) > (179)>
      ajouter (8) à y
    fin
    supprimer ce clone
  </pre>
</details>

## 👾 Étape 3 : Créer les ennemis en formation

Les ennemis vont apparaître en **formation organisée** : 5 lignes de 4 ennemis.

Voila ce qu'il va falloir développer :
- Les clones apparaisse en dehors de l'écran
- Les clones se déplace pour arriver à leur emplacement de formation

Tu vas avoir besoin d'une variable "ligne" et "chrono ennemi"

Tu vas avoir besoin de ces blocs :
<pre class="blocks">
quand le drapeau vert pressé

créer un clone de [ v]

quand je commence comme un clone

supprimer ce clone

attendre () secondes

cacher

montrer

basculer sur le costume [ v]

si <> alors
fin

répéter () fois
fin

répéter indéfiniment
fin

avancer de () pas

(abscisse x)

mettre x à ()

(ordonnée y)

aller à x: () y: ()

s'orienter à ()

tourner droite de () degrés

<() < ()>

<() > ()>

(() + ())

(() - ())

(() * ())

([sin v] de ())

(chronomètre)

mettre [ v] à ()

ajouter () à [ v]
</pre>

<details>
  <summary>Code du sprite "ennemi" (au démarrage)</summary>

  <pre class="blocks">
  quand le drapeau vert pressé
    cacher
    mettre [ligne v] à (0)
    répéter (5) fois
      répéter (4) fois
        aller à x: (((ligne) * (100)) + (-150)) y: (179)
        s'orienter à ((180) + ((ligne) * (30)))
        créer un clone de [moi-même v]
        attendre (0.5) secondes 
      fin
      ajouter (1) à [ligne v]
    fin
  </pre>
</details>

<details>
  <summary>Code du clone "ennemi"</summary>

  <pre class="blocks">
  quand je commence comme un clone
    mettre [chrono ennemi v] à (chronomètre)
    basculer sur le costume [ennemi v]
    montrer
    répéter indéfiniment
      tourner droite de (([sin v] de (((chronomètre) - (chrono ennemi)) * (100))) * (-2)) degrés
      avancer de (2) pas
      si <(abscisse x) > (239)> alors
        mettre x à (-239)
      sinon
        si <(-239) > (abscisse x)> alors
          mettre x à (239)
        fin
      fin
      si <(ordonnée y) < (-179)> alors
        supprimer ce clone
      fin
    fin
  </pre>
</details>

## 💥 Étape 4 : Les collisions

On va mettre en place le système de collision.

Ces collisions servent à plusieurs choses :
- La partie commence avec 3 vies et un score de 0
- Lorsqu'un projectile touche un vaisseau ennemi, le projectile et le vaisseau doivent disparaitre et on gagne 100 points
- Lorsqu'un vaisseau ennemi touche le vaisseau du joueur, le vaisseau ennemi dois disparaitres et l'on perd une vie

Tu vas avoir besoin d'une variable "score" et "vies". Ces variables sont globales

Tu vas avoir besoin de ces blocs :
<pre class="blocks">
si <> alors
fin
  
supprimer ce clone

stop [ v]

quand je reçois [ v]

envoyer à tous [ v] et attendre

<touche le [ v] ?>

mettre [ v] à ()

ajouter () à [ v]

dire [] pendant () secondes

<() = ()>
</pre>

<details>
  <summary>Code du sprite "projectile" (lors de la création du clone pendant qu'il avance)</summary>

  <pre class="blocks">
  si <touche le [ennemi v] ?> alors
    envoyer à tous [ennemi touché v] et attendre
    supprimer ce clone
  fin
  </pre>
</details>

<details>
  <summary>Code du sprite "ennemi" (gérer la collisions avec le projectile)</summary>

  <pre class="blocks">
  quand je reçois [ennemi touché v]
    si <touche le [projectile v] ?> alors
      supprimer ce clone
    fin
  </pre>
</details>
  
<details>
  <summary>Code du sprite "ennemi" (lors de la création du clone pendant qu'il avance)</summary>

  <pre class="blocks">
  si <touche le [joueur v] ?> alors
    envoyer à tous [joueur touché v] et attendre
    supprimer ce clone
  fin
  </pre>
</details>

<details>
  <summary>Code du sprite "joueur" (au démarrage)</summary>

  <pre class="blocks">
  mettre [vies v] à (3)
  mettre [score v] à (0)
  </pre>
</details>

<details>
  <summary>Code du sprite "joueur" (gérer la collisions avec l'ennemi)</summary>

  <pre class="blocks">
  quand je reçois [joueur touché v]
  ajouter (-1) à [vies v]
  si <(vies) = (0)> alors
    cacher
    attendre (2) secondes
    stop [tout v]
  fin
  </pre>
</details>

<details>
  <summary>Code du sprite "joueur" (gérer la collisions du projectile avec l'ennemi)</summary>

  <pre class="blocks">
  quand je reçois [ennemi touché v]
  ajouter (10) à [score v]
  </pre>
</details>

## 🔫 Étape 5 : Ajouter les tirs ennemis

Les ennemis vont aussi tirer sur toi ! Tu dois les éviter pour ne pas perdre de vies.

Voila comment ils vont s'y prendre :
- Les ennemis tirent **aléatoirement** (pas trop souvent)
- Les projectiles ennemis **descendent** vers le joueur
- Le joueur perd une vie au contact avec le projectile

Tu vas avoir besoin de deux variables liste "file x tir ennemi" et "file y tir ennemi". Ces listes vont te servir à passer les coordonnée des vaisseaux ennemi vers les projectiles à créer durant leur déplacement.

Tu vas avoir besoin de ces blocs :
<pre class="blocks">
quand le drapeau vert pressé

créer un clone de [ v]

quand je commence comme un clone

supprimer ce clone

répéter indéfiniment
fin

répéter jusqu'à ce que <>
fin

si <> alors
fin

attendre () secondes

ajouter [] à [ v]

supprimer tous les éléments de la liste [ v]

supprimer l'élément () de [ v]

envoyer à tous [ v]

envoyer à tous [ v] et attendre

s'orienter à ()

(abscisse x)

(ordonnée y)

ajouter () à y

aller à x:() y:()

cacher

montrer

<touche le [ v] ?>
</pre>

<details>
  <summary>Code du sprite "ennemi"</summary>

<pre class="blocks">
quand je commence comme un clone
  répéter indéfiniment
    si <(nombre aléatoire entre (1) et (100)) < (3)> alors
      ajouter [(abscisse x)] à [file x tir ennemi v]
      ajouter [(ordonnée y)] à [file y tir ennemi v]
      créer un clone de [projectile ennemi v]
    fin
    attendre (0.1) secondes
  fin
</pre>
</details>

<details>
  <summary>Code du sprite "projectile ennemi" (initialisation)</summary>

<pre class="blocks">
quand le drapeau vert pressé
  supprimer tous les éléments de la liste [file x tir ennemi v]
  supprimer tous les éléments de la liste [file y tir ennemi v]
  s'orienter à (180)
  cacher
</pre>
</details>

<details>
  <summary>Code du sprite "projectile ennemi" (création du clone)</summary>

<pre class="blocks">
quand je commence comme un clone
  aller à x:(élément (1) de [file x tir ennemi v]) y:(élément (1) de [file y tir ennemi v])
  supprimer l'élément (1) de [file x tir ennemi v]
  supprimer l'élément (1) de [file y tir ennemi v]
  répéter jusqu'à ce que <(ordonnée y) < (-179)>
    ajouter (-8) à y
    si <touche le [joueur v] ?> alors
      envoyer à tous [joueur touché v] et attendre
      supprimer ce clone
    fin
  fin
  supprimer ce clone
</pre>
</details>

## ⚡ Étape 6 : Les Power-ups

Des bonus apparaissent aléatoirement pour t'aider ! Récupère-les pour des avantages.

On va commencer par en faire 2 :
- 🛡️ **Bouclier** : Protège un coup
- ⚡ **Tirs Rapides** : Double la cadence pendant 5 sec

Tu vas avoir besoin de deux nouvelles variable "bouclier" et "cadence rapide". 
Il faudra aussi deux variables liste "file x powerup" et "file y powerup". Ces listes vont te servir à passer les coordonnée des vaisseaux ennemi vers les powerups à créer durant leur déplacement.

<details>
  <summary>Code du sprite "ennemi" (à ajouter lorsque le vaisseau ennemi est touché)</summary>

<pre class="blocks">
  si <(nombre aléatoire entre (1) et (100)) < (40)> alors
    ajouter [(abscisse x)] à [file x powerup v]
    ajouter [(ordonnée y)] à [file y powerup v]
    créer un clone de [powerup v]
  fin
</pre>
</details>

<details>
  <summary>Code du sprite "powerup" (initialisation)</summary>

<pre class="blocks">
quand le drapeau vert pressé
  supprimer tous les éléments de la liste [file x powerup v]
  supprimer tous les éléments de la liste [file y powerup v]
  cacher
</pre>
</details>


<details>
  <summary>Code du sprite "PowerUp" (nouveau sprite)</summary>
<pre class="blocks">
quand je commence comme un clone
  aller à x:(élément (1) de [file x powerup v]) y:(élément (1) de [file y powerup v])
  supprimer l'élément (1) de [file x powerup v]
  supprimer l'élément (1) de [file y powerup v]
  répéter jusqu'à ce que <(ordonnée y) < (-179)>
    ajouter (-4) à y
    si <touche le [joueur v] ?> alors
      si <([numéro] du costume) = (1)>
        envoyer à tous [bouclier actif v]
      sinon
        envoyer à tous [rapidefire actif v]
      fin
      supprimer ce clone
    fin
  fin
  supprimer ce clone
</pre>
</details>

<details>
  <summary>Code du sprite "joueur" (à ajouter à l'initialisation)</summary>
<pre class="block">
quand le drapeau vert pressé
  mettre [bouclier actif v] à (0)
  mettre [rapidefire actif v] à (0)
  basculer sur le costume [vaisseau joueur v]
</pre>

<details>
  <summary>Code du sprite "joueur" (nouveau blocs à créer pour gérer les powerups)</summary>
<pre class="block">
quand je reçois [bouclier actif v]
  mettre [bouclier actif v] à (1)
  basculer sur le costume [vaisseau joueur bouclier v]

quand je reçois [rapidefire actif v]
  mettre [rapidefire actif v] à (1)
  attendre (5) seconds
  mettre [rapidefire actif v] à (0)
</pre>
</details>

<details>
  <summary>Code du sprite "joueur" (à ajouter lorsqu'on se fait toucher)</summary>
<pre class="blocks">
  si <(bouclier actif) > (0)> alors
    mettre [bouclier actif v] à (0)
    basculer sur le costume [vaisseau joueur v]
  sinon
    ajouter (-1) à [vies v]
  fin
</pre>
</details>

<details>
  <summary>Code du sprite "joueur" (modifier la gestion du tir)</summary>
<pre class="blocks">
  mettre [décompte tir v] à ((chronomètre) + ((0.5) - ((rapidefire actif) * (0.4))))
</pre>
</details>

## 🎬 Étape 7 : Animations visuelles

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

### Code du sprite "joueur" (Clignoter après collision)

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

### Code du sprite "ennemi" (créer l'explosion)

<pre class="blocks">
quand je reçois [ennemi touché v]
  envoyer à tous [explosion v]
  supprimer ce clone
</pre>

### Code du sprite "joueur" (Game Over dramatique)

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

## 🔊 Étape 8 : Les sons rétro 8-bit (Bonus)

Ajoute une ambiance sonore arcade !

### Code du sprite "joueur" (Son au tir)

<pre class="blocks">
répéter indéfiniment
  si <touche [espace v] pressée ?> alors
    jouer la note [C5 v] pendant (0.05) temps
    créer un clone de [projectile v]
    attendre (0.2) secondes
  fin
fin
</pre>

### Code du sprite "ennemi" (Son de destruction)

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

### Code du sprite "joueur" (Son de collision)

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