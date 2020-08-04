from DownloadSoundFiles import DownloadSoundFiles
from pathlib import Path


pathToDataFolder = Path('./Data/')
for item in pathToDataFolder.iterdir():
    if item.suffix:
        pathToTest = pathToDataFolder / item.stem
        if pathToTest.exists():
            print('Data for ',str(item),'already downloaded, so it will be skipped')
        else:
            DownloadSoundFiles.DownloadSoundFilesFromCsv(str(item.name))
