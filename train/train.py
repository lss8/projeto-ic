import os
import requests

BASE_DATA_SOURCES_PATH = os.environ["BASE_DATA_SOURCES_PATH"]
DATA_SOURCE_EXTENSION = os.environ["DATA_SOURCE_EXTENSION"]
MACHINE_LEARNING_FOR_KIDS_API_TRAIN_URL = os.environ["MACHINE_LEARNING_FOR_KIDS_API_TRAIN_URL"]

def storeTraining(text, label):
    response = requests.post(MACHINE_LEARNING_FOR_KIDS_API_TRAIN_URL, json = { "data" : text, "label" : label })
    if response.ok == False:
        print(response.json())

def getLabelNameFromFileName(fileName):
    fileExtensionSize = len(DATA_SOURCE_EXTENSION)
    return fileName[:-fileExtensionSize]

trainingFiles = os.listdir('train/data_sources')

print("Starting training")
for trainingFileName in trainingFiles:
        labelName = getLabelNameFromFileName(trainingFileName)
        print("Training for", labelName)
        trainFile = open(BASE_DATA_SOURCES_PATH + trainingFileName, "r")
        for line in trainFile:
                storeTraining(line, labelName)
        trainFile.close()
print("Training completed")
