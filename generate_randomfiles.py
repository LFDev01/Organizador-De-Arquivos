import os

def createFiles(extension):
    for i in range(10):
        file = open(f'file_n{i}-type{extension.upper()}.{extension}', 'a')
        file.close()


os.mkdir('Test')
os.chdir('Test')

createFiles('pdf')
createFiles('txt')
createFiles('png')
createFiles('docx')
createFiles('exe')
createFiles('mp4')
createFiles('mp3')
createFiles('rar')
createFiles('zip')
