---
language: scratch
title: "Shoot em up : Pilote ton vaisseau spatial"
description: "Créer un petit shoot em up avec Scratch"
page_js:
  - assets/js/scratchblocks.min.js
  - assets/js/translations-all.js
---

# 🚀 Shoot em up : Pilote ton vaisseau spatial

## 📋 Contexte du projet

Dans cet atelier, tu vas créer un **petit jeu de tir spatial** où :
- Tu pilotes ton vaisseau avec les flèches du clavier
- Tu tires sur des ennemis qui apparaissent en formation
- Chaque ennemi détruit te rapporte des points
- Tu perds une vie si un ennemi te touche

Les notions clés que tu vas approfondir :
- ⭐ Le système de **clones** (créer plusieurs copies d'un sprite)
- 🎮 La gestion des collisions
- 📊 Les variables pour score et vies
- ⏰ L'utilisation de messages pour la communication entre sprites

---

## 🎨 Préparation : Les sprites et le décor

### 1. Crée les 3 sprites nécessaires

Tu auras besoin de :
1. **Mon vaisseau** - le vaisseau du joueur (dessin simple : triangle pointant vers le haut)
2. **Ennemi** - un vaisseau ennemi qui se clonera
3. **Projectile** - ton tir (petit cercle ou carré)

> **Conseil** : Dessine des formes simples ou utilise la galerie de Scratch. Les sprites peuvent même être des emojis ou des formes géométriques.

### 2. Configure la scène

Définis une taille de scène adaptée, par exemple **480 × 360** pixels (par défaut dans Scratch).

---

## 🕹️ Étape 1 : Piloter ton vaisseau

Le vaisseau du joueur doit se déplacer avec les **flèches gauche/droite** et rester en bas de l'écran.

```scratch
quand le drapeau vert est cliqué

répète indéfiniment
  si <touche [flèche gauche v] appuyée ?> alors
    ajoute (-5) à x
  fin
  si <touche [flèche droite v] appuyée ?> alors
    ajoute (5) à x
  fin
  
  :: comment Garder le vaisseau dans les limites
  si <(position x) < (-240)> alors
    mets x à (-240)
  fin
  si <(position x) > (240)> alors
    mets x à (240)
  fin
fin
```

**Ce que fait ce code :**
- Évalue en continu les touches pressées
- Déplace le vaisseau à gauche ou droite
- Empêche le vaisseau de sortir de l'écran

---

## 🔫 Étape 2 : Ajouter le système de tir

Quand tu appuies sur **ESPACE**, un projectile est lancé. Les projectiles se clonent du sprite "Projectile".

### Code du sprite "Mon vaisseau" (ajouter à la boucle principale)

```scratch
répète indéfiniment
  si <touche [espace v] appuyée ?> alors
    crée un clone de [Projectile v]
    attends (0.2) secondes
  fin
fin
```

### Code du sprite "Projectile"

```scratch
quand je commence en tant que clone
  
  mets x à (position x de [Mon vaisseau v])
  mets y à (position y de [Mon vaisseau v])
  mets la taille à (25) %
  
  répète jusqu'à <(position y) > (180)>
    ajoute (8) à y
  fin
  
  supprime ce clone
```

**Points importants :**
- Les clones héritent de la position du vaisseau au moment du tir
- Le projectile monte à chaque étape
- Il se supprime automatiquement quand il sort de l'écran

---

## 👾 Étape 3 : Créer les ennemis en formation

Les ennemis vont apparaître en **formation organisée** : 3 lignes de 4 ennemis.

### Code du sprite "Ennemi" (au démarrage)

```scratch
quand le drapeau vert est cliqué
  cache-toi
  mets [ligne v] à (0)
  
  répète (3)
    répète (4)
      crée un clone de moi-même
      attends (0.2) secondes
    fin
    ajoute (1) à [ligne v]
  fin
```

### Code du clone ennemi

```scratch
quand je commence en tant que clone
  mets le costume à [ennemi v]
  mets la taille à (30) %
  montre-toi
  
  :: comment Positionner en formation
  mets x à (((ligne) * (100)) + (-150))
  mets y à ((((3) - (ligne)) * (40)) + (150))
  
  :: comment Mouvement sinusoïdal
  répète indéfiniment
    avance de (2)
    tourne de (2) degrés vers la droite
    
    si <(position x) > (250)> alors
      mets x à (-250)
    fin
    
    :: comment Descendre lentement
    ajoute (-0.5) à y
    
    :: comment Disparaître si trop bas
    si <(position y) < (-180)> alors
      supprime ce clone
    fin
  fin
```

---

## 💥 Étape 4 : Les collisions

### Variables à créer
- **score** : nombre de points
- **vies** : nombre de vies restantes

### Code du sprite "Projectile" (ajouter au clone)

```scratch
quand je commence en tant que clone
  répète jusqu'à <(position y) > (180)>
    ajoute (8) à y
    
    :: comment Vérifier les collisions avec les ennemis
    si <touchant [Ennemi v] ?> alors
      diffuse [ennemi touché v]
      ajoute (10) à [score v]
      supprime ce clone
    fin
  fin
```

### Code du sprite "Ennemi" (gérer les collisions)

```scratch
quand je reçois [ennemi touché v]
  supprime ce clone
fin

:: comment Collision avec le vaisseau du joueur
répète indéfiniment
  si <touchant [Mon vaisseau v] ?> alors
    diffuse [collision vaisseau v]
    supprime ce clone
  fin
fin
```

### Code du sprite "Mon vaisseau" (gérer les dégâts)

```scratch
mets [vies v] à (3)

quand je reçois [collision vaisseau v]
  ajoute (-1) à [vies v]
  
  si <(vies) = (0)> alors
    dis [Fin du jeu !] pendant (2) secondes
    diffuse [fin du jeu v]
    arrête [tout v]
  fin
fin
```

---

## 📊 Étape 5 : Affichage du score et des vies

### Code du sprite "Arrière-plan"

```scratch
quand le drapeau vert est cliqué
  mets [score v] à (0)
  mets [vies v] à (3)

répète indéfiniment
  dis (assemblage [Score: ] (assemblage (score) (assemblage [  |  Vies: ] (vies))))
fin
```

---

## 🔫 Étape 6 : Ajouter les tirs ennemis

Les ennemis vont aussi tirer sur toi ! Tu dois les éviter pour ne pas perdre de vies.

### Code du sprite "Ennemi" (ajouter à la boucle du mouvement)

```scratch
quand je commence en tant que clone
  :: comment Toute la logique de mouvement existante...
  
  :: comment Ajouter le tir ennemi
  répète indéfiniment
    si <nombre aléatoire entre (1) et (100) = (1)> alors
      crée un clone de [Projectile ennemi v]
    fin
    attends (0.5) secondes
  fin
fin
```

### Code du sprite "Projectile ennemi" (nouveau sprite)

```scratch
quand je commence en tant que clone
  mets x à (position x du clone ennemi)
  mets y à (position y du clone ennemi)
  mets la taille à (25) %
  
  :: comment Descendre vers le joueur
  répète jusqu'à <(position y) < (-180)>
    ajoute (-8) à y
    
    :: comment Vérifie la collision avec le joueur
    si <touchant [Mon vaisseau v] ?> alors
      diffuse [collision vaisseau v]
      supprime ce clone
    fin
  fin
  
  supprime ce clone
```

**Points importants :**
- Les ennemis tirent **aléatoirement** (pas trop souvent)
- Les projectiles ennemis **descendent** vers le joueur
- Le joueur perd une vie au contact

---

## 📈 Étape 7 : Implémenter les niveaux progressifs

Le jeu devient plus difficile à chaque niveau ! Les ennemis sont plus rapides et plus nombreux.

### Variables à créer
- **niveau** : numéro du niveau actuel
- **vitesse_ennemis** : vitesse d'apparition
- **nombre_ennemis** : quantité d'ennemis par vague

### Code du sprite "Arrière-plan"

```scratch
quand le drapeau vert est cliqué
  mets [score v] à (0)
  mets [vies v] à (3)
  mets [niveau v] à (1)
  
  répète indéfiniment
    :: comment Le score augmente = levels up
    si <(score) > ((niveau) * (50))> alors
      ajoute (1) à [niveau v]
      diffuse [niveau augmenté v]
      dis (assemblage [Niveau ] (assemblage (niveau) [ ! ])) pendant (2) secondes
    fin
    
    dis (assemblage [Score: ] (assemblage (score) (assemblage [  |  Niveau: ] (niveau))))
  fin
end
```

### Code du sprite "Ennemi" (modifier la formation)

```scratch
quand le drapeau vert est cliqué
  cache-toi
  mets [ligne v] à (0)
  
  :: comment Nombre d'ennemis augmente avec le niveau
  répète ((3) + (niveau))
    répète (4)
      crée un clone de moi-même
      attends ((0.2) - ((niveau) * (0.01))) secondes
    fin
    ajoute (1) à [ligne v]
  fin
end

quand je reçois [niveau augmenté v]
  :: comment Augmente la vitesse des ennemis
  ajoute (0.5) à [vitesse_ennemis v]
end
```

### Code du clone ennemi (modifier la vitesse)

```scratch
quand je commence en tant que clone
  mets le costume à [ennemi v]
  mets la taille à (30) %
  montre-toi
  
  :: comment Vitesse dépend du niveau
  mets [vitesse_ennemis v] à ((2) + (niveau))
  
  mets x à (((ligne) * (100)) + (-150))
  mets y à ((((3) - (ligne)) * (40)) + (150))
  
  répète indéfiniment
    avance de (vitesse_ennemis)
    tourne de (2) degrés vers la droite
    
    si <(position x) > (250)> alors
      mets x à (-250)
    fin
    
    ajoute (-0.5) à y
    
    si <(position y) < (-180)> alors
      supprime ce clone
    fin
  fin
```

**Difficulté progressive :**
- Niveau 1 : 3 lignes d'ennemis, vitesse 2
- Niveau 2 : 4 lignes, vitesse 2.5, tirs plus rapides
- Niveau 3+ : Plus d'ennemis, plus rapides chaque fois

---

## ⚡ Étape 8 : Les Power-ups

Des bonus apparaissent aléatoirement pour t'aider ! Récupère-les pour des avantages.

### Variables à créer
- **bouclier_actif** : vrai/faux si un bouclier est actif
- **cadence_rapide** : vrai/faux pour les tirs rapides

### Code du sprite "Ennemi" (générer les power-ups)

```scratch
quand je reçois [ennemi touché v]
  :: comment 30% de chance de droper un power-up
  si <(nombre aléatoire entre (1) et (10)) < (4)> alors
    crée un clone de [PowerUp v]
    mets x du clone à (position x)
    mets y du clone à (position y)
  fin
  supprime ce clone
end
```

### Code du sprite "PowerUp" (nouveau sprite)

```scratch
quand je commence en tant que clone
  mets la taille à (50) %
  montre-toi
  
  :: comment Choisir un type aléatoire
  si <(nombre aléatoire entre (1) et (2)) = (1)> alors
    mets le costume à [bouclier v]
    mets [type_powerup v] à [bouclier]
  sinon
    mets le costume à [rapidfire v]
    mets [type_powerup v] à [rapidfire]
  fin
  
  :: comment Descendre
  répète jusqu'à <(position y) < (-180)>
    ajoute (-3) à y
    
    :: comment Collision avec le joueur
    si <touchant [Mon vaisseau v] ?> alors
      si <(type_powerup) = [bouclier]> alors
        mets [bouclier_actif v] à (vrai)
        diffuse [bouclier activé v]
      sinon
        mets [cadence_rapide v] à (vrai)
        attends (5) secondes
        mets [cadence_rapide v] à (faux)
      fin
      supprime ce clone
    fin
  fin
  
  supprime ce clone
end
```

### Code du sprite "Mon vaisseau" (utiliser les bonuses)

```scratch
:: comment Bouclier : absorbe un coup
quand je reçois [collision vaisseau v]
  si <(bouclier_actif)> alors
    mets [bouclier_actif v] à (faux)
    diffuse [bouclier désactivé v]
  sinon
    ajoute (-1) à [vies v]
  fin
end

:: comment Tirs rapides : diminue le délai
répète indéfiniment
  si <touche [espace v] appuyée ?> alors
    crée un clone de [Projectile v]
    
    :: comment Délai variable selon power-up
    si <(cadence_rapide)> alors
      attends (0.05) secondes
    sinon
      attends (0.2) secondes
    fin
  fin
fin
```

**Types de power-ups :**
- 🛡️ **Bouclier** : Protège un coup
- ⚡ **Tirs Rapides** : Double la cadence pendant 5 sec
- 🎯 Idée future : Ralentisseur d'ennemis

---

## 🎬 Étape 9 : Animations visuelles

Rend le jeu plus vivant avec des animations !

### Code du sprite "Arrière-plan" (Début du jeu)

```scratch
quand le drapeau vert est cliqué
  dis [Prépare-toi !] pendant (1) secondes
  dis [3...] pendant (1) secondes
  dis [2...] pendant (1) secondes
  dis [1...] pendant (1) secondes
  dis [À l'attaque !] pendant (1) secondes
end
```

### Code du sprite "Mon vaisseau" (Clignoter après collision)

```scratch
quand je reçois [collision vaisseau v]
  :: comment Effet de clignotement
  répète (4)
    cache-toi
    attends (0.1) secondes
    montre-toi
    attends (0.1) secondes
  fin
end
```

### Code du sprite "Explosion" (nouvelle animation)

```scratch
quand je reçois [explosion v]
  mets x à (position x du clone ennemi)
  mets y à (position y du clone ennemi)
  montre-toi
  
  :: comment Animation d'explosion
  répète (3)
    ajoute (5) à [taille v] %
    attends (0.1) secondes
  fin
  
  cache-toi
end
```

### Code du sprite "Ennemi" (créer l'explosion)

```scratch
quand je reçois [ennemi touché v]
  :: comment L'explosion apparaît à ma position
  diffuse [explosion v]
  supprime ce clone
end
```

### Code du sprite "Mon vaisseau" (Game Over dramatique)

```scratch
quand je reçois [fin du jeu v]
  mets [texture v] à [GAME OVER]
  dis [GAME OVER !] pendant (3) secondes
  
  dis (assemblage [Score final: ] (score)) pendant (2) secondes
  dis (assemblage [Niveau atteint: ] (niveau)) pendant (2) secondes
  
  attends (1) secondes
  dis [Appuie sur le drapeau vert pour recommencer] pendant (3) secondes
end
```

**Animations ajoutées :**
- Compte à rebours au démarrage
- Clignotement du vaisseau après coup
- Explosion visible au centre des ennemis
- Écran de fin dramatique

---

## 🔊 Étape 10 : Les sons rétro 8-bit (Bonus)

Ajoute une ambiance sonore arcade !

### Code du sprite "Mon vaisseau" (Son au tir)

```scratch
répète indéfiniment
  si <touche [espace v] appuyée ?> alors
    joue la note [C5 v] pendant (0.05) beats
    crée un clone de [Projectile v]
    attends (0.2) secondes
  fin
fin
```

### Code du sprite "Ennemi" (Son de destruction)

```scratch
quand je reçois [ennemi touché v]
  :: comment Joue une note descendante pour l'explosion
  joue la note [D5 v] pendant (0.1) beats
  joue la note [B4 v] pendant (0.1) beats
  joue la note [G4 v] pendant (0.1) beats
  supprime ce clone
end
```

### Code du sprite "Arrière-plan" (Musique de fond)

```scratch
quand le drapeau vert est cliqué
  :: comment Boucle musicale simple (peux la modifier)
  répète indéfiniment
    joue la note [C4 v] pendant (0.5) beats
    joue la note [E4 v] pendant (0.5) beats
    joue la note [G4 v] pendant (0.5) beats
    joue la note [C5 v] pendant (2) beats
  fin
end
```

### Code du sprite "Mon vaisseau" (Son de collision)

```scratch
quand je reçois [collision vaisseau v]
  joue la note [G3 v] pendant (0.1) beats
  joue la note [C3 v] pendant (0.2) beats
end
```

**Effets sonores rétro :**
- 🔊 Tir : Note aigüe courte (C5)
- 💥 Explosion : Descente de notes (D5 → B4 → G4)
- ⚠️ Collision : Deux notes basses (G3 → C3)
- 🎵 Musique : Boucle simple C-E-G-C

---

---

## 💡 Points clés à retenir

| Concept | Utilité |
|---------|---------|
| **Clones** | Créer plusieurs copies d'un sprite (ennemis, projectiles) |
| **Messages** | Faire communiquer les sprites entre eux |
| **Variables** | Suivre le score, les vies, les niveaux |
| **Touches** | Gérer les contrôles du joueur |
| **Collisions** | Détecter quand deux sprites se touchent |
| **Position** | x et y pour placer les sprites précisément |

---

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