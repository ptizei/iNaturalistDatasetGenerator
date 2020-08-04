import pandas as pd
from pathlib import Path
import requests
import re


def DownloadSoundFilesFromCsv(csvFile):
    folderToOpen = Path("./Data/")
    filePath = folderToOpen / csvFile

    folderForData = folderToOpen / filePath.stem
    folderForData.mkdir()

    df_FromCSV = pd.read_csv(filePath)

    for url in df_FromCSV.sound_url:
        if isinstance(url,str):
            urlToDownload = url.split('?')[0]
            try:
                with requests.get(urlToDownload) as r:

                    fname = ''
                    if "Content-Disposition" in r.headers.keys():
                        fname = re.findall("filename=(.+)", r.headers["Content-Disposition"])[0]
                    else:
                        fname = urlToDownload.split("/")[-1]

                    #print(fname)
            except RequestException as e:
                print(e)
            print('**** Downloading', fname)
            fname = str(folderForData.resolve()) + '\\' + fname
            open(fname, 'wb').write(r.content)
