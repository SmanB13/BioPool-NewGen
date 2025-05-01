#!/bin/bash

# Nom du dépôt GitHub local
REPO_NAME="BioPool-NewGen"
ZIP_NAME="BioPool-NewGen-HACS-v0.3.0-alpha3-FINAL.zip"
TAG="v0.3.0-alpha3"
COMMIT_MSG="🚀 Version ${TAG} avec 100% tests, AutoTests, Lovelace intégrée"

# Vérifie que le dépôt existe
if [ ! -d "$REPO_NAME/.git" ]; then
    echo "❌ Le dossier $REPO_NAME n'est pas un dépôt Git valide."
    exit 1
fi

cd "$REPO_NAME" || exit 1

# Vérifie si le ZIP est présent
if [ ! -f "../$ZIP_NAME" ]; then
    echo "❌ Archive $ZIP_NAME non trouvée dans le dossier parent."
    exit 1
fi

# Demande confirmation avant d'écraser les fichiers
read -p "⚠️ Ce script va remplacer les fichiers de votre dépôt local avec ceux du ZIP. Continuer ? (o/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Oo]$ ]]; then
    echo "⏹ Annulé."
    exit 1
fi

# Extraction avec écrasement
unzip -o "../$ZIP_NAME" -d .

# Git commit + tag
git add .
git commit -m "$COMMIT_MSG"
git tag "$TAG"
git push origin main --tags

echo "✅ Déploiement terminé. Release prête sur GitHub avec le tag $TAG."
