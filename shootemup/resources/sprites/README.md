# Sprites Rétro 16-bit pour Shoot em Up

Ce dossier contient tous les sprites du jeu shoot em up au style pixel art rétro 16-bit.

## 📁 Fichiers des sprites

### `player_ship.svg` - Vaisseau du joueur
- **Couleur** : Vert éclatant (#00FF00)
- **Style** : Vaisseau futuriste symétrique avec cockpit jaune
- **Utilisation** : Sprite "Mon vaisseau" du jeu

### `enemy_ship.svg` - Vaisseau ennemi
- **Couleur** : Rouge agressif (#FF3333)
- **Style** : Vaisseau enemi avec des canons et détails technologiques
- **Utilisation** : Sprite "Ennemi" - se clonnera pour les formations

### `projectile.svg` - Projectile
- **Couleur** : Cyan/bleu (#00FFFF) avec pointe jaune
- **Style** : Petit bolt d'énergie pointu
- **Utilisation** : Sprite "Projectile" - tirs du joueur

## 🎮 Comment importer dans Scratch

### Méthode 1 : Via l'interface web (Recommandée)
1. Ouvre [scratch.mit.edu](https://scratch.mit.edu)
2. Crée un nouveau projet
3. Pour chaque sprite :
   - Clique sur le bouton **Ajouter un sprite**
   - Sélectionne **Importer un sprite**
   - Télécharge le fichier `.svg` correspondant
   - Renomme le sprite (ex: "Mon vaisseau", "Ennemi", "Projectile")

### Méthode 2 : Convertir en PNG (pour plus de compatibilité)
1. Exporte les SVG en PNG (32x32 pixels pour les vaisseaux, 16x16 pour le projectile)
2. Importe les PNG comme décrit ci-dessus

## 🎨 Personnalisations possibles

### Modifier les couleurs
Ouvre un fichier `.svg` avec un éditeur de texte et change les valeurs `fill` et `stroke` :
- Les codes couleurs sont en format hexadécimal (#RRGGBB)
- Par exemple : `#00FF00` = vert, `#FF0000` = rouge

### Ajouter des animations
Tu peux créer plusieurs costumes (variantes) :
1. Duplication des fichiers SVG
2. Modifications légères (ex: `enemy_ship_alt.svg`)
3. Importer chaque variante comme costume différent dans Scratch

## 🖌️ Styles de jeu recommandés

Pour garder l'ambiance rétro 16-bit :
- Garde les formes **géométriques simples**
- Utilise des **couleurs vives et contrastées**
- Évite les courbes complexes
- Blocs de **8x8 ou 16x16 pixels** pour l'effet pixelisé

## 📐 Tailles recommandées dans Scratch

- **Vaisseau du joueur** : 70-100% de la taille
- **Ennemis** : 60-80% (plus petit que le joueur)
- **Projectiles** : 20-30% (très petit)

## 💡 Idées d'améliorations

1. **Explosions** : Créer `explosion.svg` pour l'effet collision
2. **PowerUps** : Dessiner `shield.svg`, `rapid_fire.svg`
3. **Variantes ennemis** : `heavy_enemy.svg`, `fast_enemy.svg`
4. **Fond étoilé** : `starfield.svg` pour la scène
5. **UI Elements** : `health_bar.svg`, `score_indicator.svg`

## 🎵 Combinaison avec le son (Optionnel)

Pour une expérience complète rétro :
- Son de tir : "pew pew" aigu
- Son de collision : "boom" bas
- Son de boost moteur : "whoosh"
- Musique de fond : 8-bit chiptune

---

**Astuce** : Ces sprites sont parfaitement alignés avec le tutoriel du projet pour un jeu shoot em up en Scratch ! 🚀
