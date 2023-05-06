import os, shutil, time, zipfile, sys, datetime, pathlib
from pathlib import Path

def backupToZip(args):
    if (len(args) > 1):
        folder = args[1]
        folder = os.path.abspath(folder) # make sure folder is absolute
    else:
        raise Exception("Required parameter")

    timestamp = str(datetime.datetime.now()).split(' ')
    timestampStr = timestamp[0]+'_'+timestamp[1].split('.')[0]
    # zipFilename = str(Path(folder).parent) + "\\" + timestampStr + '-' + Path(folder).stem + ".zip"
    zipFilename = timestampStr + '-' + Path(folder).stem + ".zip"

    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files from %s...' % (foldername))
        backupZip.write(foldername)

        for filename in filenames:
            if filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')
    return zipFilename

def moveFolderToBackup(zipPath):
    backupFolder = ""
    if "BACKUPS_DIR" in os.environ:
        backupFolder = os.environ["BACKUPS_DIR"]
    else:
        backupFolder = os.path.join(os.path.expanduser('~'), '.backups')
    if not os.path.exists(backupFolder):
        os.makedirs(backupFolder)
    shutil.move(zipPath, backupFolder)
    print('Done.')

    
if __name__ == '__main__':
        moveFolderToBackup(backupToZip(sys.argv))