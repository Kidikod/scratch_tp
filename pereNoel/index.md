---
language: scratch
title: "Noël : La distribution des cadeaux"
description: "Créer un jeu de distribution de cadeaux de Noël avec Scratch"
page_js:
  - /assets/js/scratchblocks.min.js
  - /assets/js/translations-all.js
---

## Introduction
<img alt="image de description" src="assets/start.png"  style="display:block; margin: auto; width:50%;">
Cette année nous allons aider le Père-Noël à faire sa distribution de cadeaux. Tout en évitant les avions, le Père Noël va devoir distribuer des cadeaux aux enfants dans les maisons, mais gars au Grinch.

## Préparons la scène du jeu
Nous allons utiliser le logiciel Scratch pour faire notre jeu. Rends-toi à l'adresse https://scratch.mit.edu et clique sur le bouton _Créer_ en haut à gauche.
Le logiciel se charge. Tu peux fermer toutes les fenêtres vertes de Tutoriel. En bas à droite tu as la zone des _sprites_ (éléments de jeu). Par défaut tu as un seul sprite chat. Tu peux le supprimer car nous n'en aurons pas besoin. Pour cela, clique sur la poubelle à côté de son icône dans la zone des sprites. <br/>
Maintenant, nous allons mettre un fond à notre jeu. En bas à droite, passe ton curseur **sans cliquer** sur ce bouton:
<img alt="background" src="assets/background.png"  style="display:block; margin: auto; width:50%;">
Puis clique sur importer un arrière plan:
<img alt="import background" src="assets/importBackground.png"  style="display:block; margin: auto; width:50%;">
Choisis ensuite le fichier _fond.png_ depuis les resources du TP. Tu devrais voir s'afficher un joli paysage enneigé.

## Animons le Père-Noël 
Commençons par ajouter le sprite du Père-Noël. Assure-toi de bien être dans l'onglet _Code_ en haut à gauche puis survole ce bouton dans la zone des sprites **sans cliquer dessus**:
<img alt="addSprite" src="assets/addSprite.png"  style="display:block; margin: auto; width:50%;">
Puis clique sur le bouton _Importer un sprite_
<img alt="importSprite" src="assets/importSprite.png"  style="display:block; margin: auto; width:50%;">
Choisis ensuite le fichier _pereNoel.png_. Le Père-Noël est maintenant visible dans notre jeu mais il est un peu grand. Dans la zone des sprites, tu vois que sa taille est de 100. Change cette valeur pour mettre 30.
Maintenant nous allons faire en sorte que le Père-Noël monte et descend quand tu appuies sur les touches haut et bas de ton clavier.
Pour cela tu vas avoir besoin des blocks suivants:
<pre class="blocks">
quand le drapeau vert pressé
</pre>
<pre class="blocks">
aller à x: (-150) y:(0)
</pre>
<pre class="blocks">
répéter indéfiniment
</pre>
<pre class="blocks">
si <> alors
</pre>
<pre class="blocks">
touche [] pressée
</pre>
<pre class="blocks">
ajouter (10) à y
</pre>

Tu as trouvé ? Vérifie la correction ci-dessous:

<pre class="blocks">
quand le drapeau vert pressé
  aller à x: (-150) y:(0)
  répéter indéfiniment
      si <touche [flèche haut] pressée> alors
          ajouter (10) à y
      si <touche [flèche bas] pressée> alors
          ajouter (-10) à y
</pre>

<pre class="blocks">
quand le drapeau vert pressé
  basculer sur l'arrière-plan [écran titre v]
  aller à x: (1) y: (-123)
  basculer sur le costume [démarrage v]
  montrer
</pre>