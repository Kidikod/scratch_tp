# Conversion PDF vers Markdown - Plantagotchi

Ce dossier contient les fichiers pour la conversion du PDF Plantagotchi en Markdown avec descriptions d'images.

## Fichiers principaux

- `index.md` - Fichier Markdown final avec toutes les images et descriptions
- `Plantamagotchi.pdf` - Fichier PDF source
- `assets/` - Dossier contenant les 70 images extraites du PDF

## Scripts de conversion

### `image_descriptions.py`
Fichier contenant toutes les descriptions d'images organisées par nom de fichier.

### `apply_descriptions.py`
Script pour appliquer automatiquement les descriptions aux images dans un fichier Markdown.

**Usage :**
```bash
# Appliquer les descriptions au fichier par défaut
python apply_descriptions.py

# Appliquer à un fichier spécifique
python apply_descriptions.py mon_fichier.md

# Lister les images sans description
python apply_descriptions.py --list-missing

# Afficher l'aide
python apply_descriptions.py --help
```

## Processus de conversion utilisé

1. **Conversion PDF → Markdown** avec `pymupdf4llm` :
   ```python
   md_text = pymupdf4llm.to_markdown('Plantamagotchi.pdf', write_images=True, image_path='assets')
   ```

2. **Ajout des descriptions** avec le script personnalisé :
   - Analyse de toutes les images `![](...)` dans le Markdown
   - Remplacement par `![description](...)` basé sur le fichier de descriptions
   - Rapport détaillé des modifications

## Résultats

- ✅ **70 images** extraites automatiquement
- ✅ **70 descriptions** ajoutées manuellement
- ✅ **799 lignes** de contenu Markdown structuré
- ✅ **100% des images** ont une description contextuelle

## Avantages de cette approche

1. **Séparation des préoccupations** : descriptions dans un fichier dédié
2. **Réutilisabilité** : scripts applicables à d'autres PDFs
3. **Maintenance facile** : modifications des descriptions sans toucher au Markdown
4. **Qualité** : descriptions manuelles précises et contextuelles
5. **Traçabilité** : rapport détaillé des modifications

## Fichiers de sauvegarde

- `index_old.md` - Version originale avant modifications
- `index_old_backup.md` - Sauvegarde avant remplacement final
