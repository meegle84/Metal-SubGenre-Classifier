#!/usr/bin/env python
# encoding: utf-8

# import libraries
import os
import argparse
import shutil
from .metallum import band_search

# class MSC:
#	def __init__(self, inputFolder, outputFolder):
#		self.inputFolder = inputFolder
#		self.outputFolder = outputFolder

def parseArguments():
    parser = argparse.ArgumentParser(
        description='Simple script to classify a mp3 metal folders by gerne based on info from Metallum')
    parser.add_argument('-i', '--input', help='Input folder wanted to classify', required=True)
    parser.add_argument('-o', '--output', help='Output folder where want to reside ordered', required=True)
    args = vars(parser.parse_args())
    global inputFolder
    inputFolder = args['input']
    global outputFolder
    outputFolder = args['output']


def listFolders(inputFolder):
    list = os.listdir(inputFolder)
    return list


def queryBand(bandName):
    bands = band_search(bandName)
    return bands


def getGenre(bandQuery):
    if len(bandQuery) == 0:
        print("not found!")
    elif len(bandQuery) == 1:
        bandInfo = bandQuery[0].get()
        genres = bandInfo.genres
        if len(genres) > 1:
            genre = '-'.join(genres)
        else:
            genre = genres[0]
        return genre.replace(" ", "_").replace("/", "-")
    else:
        print("too many bands with the same name ")
        for band in bandQuery:
            print(band)

def createDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        print("creating: "+dir)

def moveFolder(inFolder, outFolder):
    shutil.move(inFolder, outFolder)
    print("moving: "+inFolder)
    print("to: "+outFolder)

parseArguments()
listBands = listFolders(inputFolder)
for band in listBands:
    print("searching: "+band)
    bandName = band[0:band.find("[") - 1]
    bandQuery = queryBand(bandName)
    genre = getGenre(bandQuery)
    if not genre is None:
        createDir(outputFolder+"/"+genre)
        moveFolder(inputFolder+"/"+band, outputFolder+"/"+genre)
