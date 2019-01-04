
import zipfile as zf

SOURCE = r'<path_to_zip'
DESTINATION = r'<path_to_dest>'

with zf.ZipFile(SOURCE, 'r') as zf:
    zf.extractall(DESTINATION)
    zf.close() #cleanup
