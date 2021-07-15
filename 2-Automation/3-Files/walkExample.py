import os
import shutil

for folderName, subFolders, fileNames, in os.walk('test/'):
    print("The folder is: " + folderName)
    print("The subfolders in " + folderName + " are: " + str(subFolders))
    print("The filenames in " + folderName + " are: " + str(fileNames))
    
    for subFolder in subFolders:
        if 'fish' in subFolder:
            os.rmdir(subFolder)

    for file in fileNames:
        if file.endswith('.py'):
            shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))
