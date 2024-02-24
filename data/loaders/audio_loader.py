"""Module qui charge les audios"""
from os import listdir
import pygame as pg

pg.mixer.init()

SFX = {}
SFX_PATH = "data/sfx/"
EFFECTS_PATHS = SFX_PATH + "effects/"


def load_sound(filepath):
    """charge un son"""
    sound = pg.mixer.Sound(filepath)
    return sound


def load_dir(dirpath):
    """charge des sons dans un dossier"""
    sounds = {}
    for file in listdir(dirpath):
        filename = file[0:-4]
        filepath = dirpath + file
        sounds[filename] = load_sound(filepath)
    return sounds


def load_sfx(folders):
    """Charge tout les sons des dossiers"""
    for folder in folders:
        SFX[folder] = load_dir(SFX_PATH + folder + "/")


SFX["effects"] = load_dir(SFX_PATH + "effects" + "/")
SFX["music"] = load_dir(SFX_PATH + "music" + "/")
