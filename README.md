# Atelier-3-Challenge

Voici les étapes de l'algorithme utilisé dans la fonction de hashage créer :

1. **Inversion de la chaîne d'entrée** : 
   La chaîne d'entrée est inversée pour obtenir une version renversée, ce qui permet de commencer les transformations avec une première altération simple et uniforme.

2. **Mélange déterministe** :
   L'algorithme utilise la longueur de la chaîne inversée pour initialiser un générateur aléatoire et mélange les caractères de manière déterministe. Cela garantit que le même texte d'entrée produira toujours le même mélange.

3. **Mappage des caractères** :
   Chaque caractère du texte mélangé est ensuite transformé en un autre caractère à partir de la chaîne de mappage (`mapping_string`). Ce mappage est basé sur le code Unicode (ASCII) de chaque caractère, qui est ramené à une position valide dans `mapping_string`. Cela produit une nouvelle chaîne de caractères selon le mappage défini.

4. **Ajustement de la taille** :
   Pour garantir que la sortie a exactement la taille spécifiée (`fixed_size`), la chaîne résultante est :
   - **Tronquée** si elle est trop longue.
   - **Remplie** (avec des espaces) si elle est trop courte.

En combinant ces étapes, l’algorithme produit une chaîne de hachage de taille fixe, unique pour chaque entrée différente, tout en étant déterministe pour une même entrée.
