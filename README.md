# Wallpaper Updater

A basic daily wallpaper updater for MacOS.

## Overview

Utilizes [Unsplash's API](https://source.unsplash.com/) to curate a random relection of wallpaper 
images that would be replaced everyday at 2 AM.

## Running

Main is the executable. To run, ```cd``` into the this reposity after downloading it (specifically 
```wallpaper.py``` and ```main.py```). Then run the command ```nohup python wallpaper.py &```. This will run 
this command forever, at least until your computer is shut off. If it is, you will need to 
restart the program.

## Personalization

If you would like to personalize the wallpapers, you can change the global variables that are on 
lines 8-10 inside ```main.py```. 

  * ```directory```: should be a directory that you will place the downloaded wallpaper in to update everday.
  * ```collections_url```: the link to the desired collection on [Unsplash's website](https://unsplash.com/).
  * ```keywords```: keywords that you would want to be used during the psuedo-randomized wallpaper selection.
