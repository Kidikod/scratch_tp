# 🎨 Guide de Style Rétro 16-bit pour le Shoot em Up

## Palette de couleurs officielle du projet

### Couleurs principales
```
🟦 Joueur        : #00FF00  (Vert éclatant)
🟥 Ennemis       : #FF3333  (Rouge agressif)
🟦 Projectile    : #00FFFF  (Cyan/Bleu)
⚪ Accent jaune  : #FFFF00  (Jaune vif)
🟨 Feu/Énergie   : #FF6600  (Orange)
🟩 Power-up      : #00AA00  (Vert sec)
```

### Couleurs secondaires
```
Gris métallique  : #333333  (Détails)
Noir             : #000000  (Contours)
Blanc            : #FFFFFF  (Flash/Lumière)
Magenta          : #FF00FF  (Spécial)
```

## Principes de design rétro 16-bit

### 1️⃣ Grille de pixels
- Travaille sur une **grille de 8x8, 16x16 ou 32x32 pixels**
- Aligne tous tes éléments sur la grille
- Pas de courbes complexes (sauf les diagonales 45°)

### 2️⃣ Limitation de couleurs
- Maximum 4-6 couleurs par sprite
- Utilise des contours (`stroke`) pour délimiter les formes
- Privilégie les blocs rectangulaires

### 3️⃣ Dimension des sprites
```
Petit (projectile)     : 16x16 px
Moyen (power-up)       : 24x24 px
Grand (vaisseau)       : 32x32 px
Très grand (boss)      : 48x48 px
```

### 4️⃣ Éléments graphiques
| Élément | Couleur | Exemple |
|---------|---------|---------|
| Corps du sprite | Primaire | #00FF00 (vert) |
| Contour | Sombre | -30% de luminosité |
| Accent/Cockpit | Accent | #FFFF00 (jaune) |
| Détails | Gris | #333333 |

## 📋 Checklist de création pour nouveaux sprites

- [ ] Dimensions respectées (16x16, 24x24 ou 32x32)
- [ ] Grille de pixels alignée
- [ ] Palette limitée à 4-6 couleurs max
- [ ] Tous les éléments ont un contour
- [ ] Symétrie respectée (si applicable)
- [ ] Contraste suffisant (couleurs lisibles)
- [ ] Testé en petit et grand size

## 🎮 Conseils pour garder l'ambiance rétro

### ✅ À FAIRE
- Des formes géométriques simples
- Des contours nets et visibles
- Des couleurs vives et contrastées
- Une cohérence sur tous les sprites
- Des animations en 2-3 frames

### ❌ À ÉVITER
- Les dégradés
- Les ombres réalistes
- Les textures complexes
- Les courbes lissées
- Les trop nombreuses couleurs

## 🛠️ Outils recommandés pour créer tes propres sprites

### Gratuit
1. **Aseprite** (alternative gratuite) - Specialized pixel art
2. **Piskel** (piskelapp.com) - En ligne, simple
3. **Krita** - Gratuit et puissant
4. **Inkscape** - Vecteur (comme nos SVG)

### Payant mais pas cher
1. **Aseprite** ($20) - THE gold standard
2. **PyxelEdit** ($10) - Simple et efficace

## 📐 Exemple de création d'un vaisseau ennemi lourd

```
Étapes :
1. Crée un carré 32x32 comme base
2. Ajoute un corps principal 8x12 px de couleur ennemis (#FF3333)
3. Ajoute deux ailes 6x8 px de chaque côté
4. Ajoute un cockpit 4x4 px en haut (#FF0000)
5. Ajoute des détails (moteurs, canons) en gris (#333333)
6. Ajoute des contours sombres autour de chaque élément
7. Ajoute un accent jaune (#FFFF00) pour la "technologie"
```

## 🎬 Animation pixel art (Optionnel pour Scratch)

Pour des sprites animés, crée plusieurs costumes :
1. Crée `enemy_ship_frame1.svg`, `enemy_ship_frame2.svg`, etc.
2. Change légèrement entre les frames (ex: ailes qui bougent)
3. Dans Scratch : crée plusieurs costumes du même sprite
4. Ajoute un bloc `costume suivant` dans une boucle

**Exemple blink** (2 frames > effet vivant) :
- Frame 1 : cockpit normal (#FF0000)
- Frame 2 : cockpit éteint (#AA0000)

## 💡 Idées de nouveaux sprites

- **Hidden Enemy** : Un ennemi petit et rapide
- **Tank Enemy** : Grand, lent, blindé
- **Missile** : Projectile ennemi plus gros
- **Asteroid** : Obstacle à éviter
- **Star** : Décor d'arrière-plan
- **Health Pickup** : Restaure des vies
- **Level Badge** : Affiche le niveau actuel

---

**Astuce ultime** : Garde un fichier de référence avec tous tes sprites côte à côte pour assurer la cohérence visuelle ! 🚀✨
