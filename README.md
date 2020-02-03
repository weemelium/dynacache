#DynaCache
DynaCache permet de flouter des zones d'une image ou d'une vidéo.

##Installation
* Python 2.7 :
Les packages python nécessaires sont listés dans le fichier "envdynacache.yml".
Dans une console anaconda : conda env create -f environment.yml
Activer l'environnement : conda activate dynaboats
Lister les paquets : conda list

* FFMPEG
Pour windows :
Téléchargement https://www.ffmpeg.org/. Verifier la présence du chemin dans la variable d'environnement "path".
* FFMPEG pour Ubuntu 18.04 : 
    - $ sudo apt update
    - $ sudo apt install ffmpeg
## Usages
    $ python main.py [-h] (-f | -v) -i FILEINPUT [-o FILEOUTPUT]

###Arguments:

    -h, --help            show this help message and exit
    -f                    if image file
    -v                    if video file
    -i FILEINPUT, --fileinput FILEINPUT
                        Input video or image file
    -o FILEOUTPUT, --fileoutput FILEOUTPUT
                        Output video or image file (optionnal)
Si le fichier de sortie n'est pas spécifié alors le programme le créera automatiquement en utilisant le nom du fichier d'entré préfixé de "out_"
                        
###Exemples

    $python main.py -f -i D:\images\rgb_20191022121940256423.jpg
    $python main.py -v -i .\20200124.mp4
    
###Mode d'emploi
Au lancement du programme une image s'affiche, la première frame pour une vidéo.

Pour déssiner les polygones:

Déssiner les points du polygones en cliquant avec le bouton gauche de la souris. Cliquez avec le bouton droit pour finir le polygone.
Recommencez pour le polygone suivant et ainsi de suite.

Appuyer sur la  touche "Echap" ou "Q" ou "A" pour terminer et lancer le traitement

L'image ou la vidéo résultat s'affiche.

Vous pouver interrompre la vidéo à tout moment en appuyant que la touche "Q", la vidéo résultat sera générée jusqu'au moment de l'arrêt.
    
 