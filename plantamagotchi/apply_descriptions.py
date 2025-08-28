#!/usr/bin/env python3
"""
Script pour ajouter automatiquement les descriptions d'images
à partir du fichier de descriptions
"""

import re
from image_descriptions import descriptions

def add_descriptions_to_markdown(input_file, output_file=None):
    """
    Ajoute les descriptions d'images au fichier markdown
    
    Args:
        input_file (str): Fichier markdown d'entrée
        output_file (str): Fichier de sortie (optionnel, sinon remplace l'original)
    """
    
    # Lire le fichier d'entrée
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Compteurs pour le rapport
    images_found = 0
    images_updated = 0
    images_not_found = 0
    
    # Pattern pour trouver les images sans description
    pattern = r'!\[\]\(([^)]+)\)'
    
    def replace_image(match):
        nonlocal images_found, images_updated, images_not_found
        
        images_found += 1
        image_path = match.group(1)
        image_name = image_path.split('/')[-1]
        
        if image_name in descriptions:
            description = descriptions[image_name]
            images_updated += 1
            print(f"✅ {image_name}: {description[:60]}...")
            return f'![{description}]({image_path})'
        else:
            images_not_found += 1
            print(f"❓ {image_name}: Pas de description trouvée")
            return match.group(0)  # Retourner tel quel
    
    # Appliquer les remplacements
    print("🔄 Traitement des images en cours...\n")
    new_content = re.sub(pattern, replace_image, content)
    
    # Déterminer le fichier de sortie
    if output_file is None:
        output_file = input_file
    
    # Écrire le fichier de sortie
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    # Rapport final
    print(f"\n📊 Rapport de traitement:")
    print(f"   • Images trouvées: {images_found}")
    print(f"   • Images mises à jour: {images_updated}")
    print(f"   • Images sans description: {images_not_found}")
    print(f"   • Fichier de sortie: {output_file}")
    
    if images_updated > 0:
        print(f"\n✅ {images_updated} descriptions ajoutées avec succès!")
    
    if images_not_found > 0:
        print(f"\n⚠️  {images_not_found} images n'ont pas de description dans le fichier image_descriptions.py")

def list_missing_descriptions(input_file):
    """
    Liste les images qui n'ont pas de description définie
    """
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Trouver toutes les images
    pattern = r'!\[\]\(([^)]+)\)'
    matches = re.findall(pattern, content)
    
    missing = []
    for image_path in matches:
        image_name = image_path.split('/')[-1]
        if image_name not in descriptions:
            missing.append(image_name)
    
    if missing:
        print("🔍 Images sans description:")
        for img in sorted(set(missing)):
            print(f"   • {img}")
    else:
        print("✅ Toutes les images ont une description!")
    
    return missing

if __name__ == "__main__":
    import sys
    
    # Fichier par défaut
    input_file = "index_with_images.md"
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--list-missing":
            list_missing_descriptions(input_file)
        elif sys.argv[1] == "--help":
            print("Usage:")
            print("  python apply_descriptions.py                    # Ajouter descriptions")
            print("  python apply_descriptions.py --list-missing     # Lister images sans description")
            print("  python apply_descriptions.py --help             # Afficher cette aide")
        else:
            input_file = sys.argv[1]
            add_descriptions_to_markdown(input_file)
    else:
        add_descriptions_to_markdown(input_file)
