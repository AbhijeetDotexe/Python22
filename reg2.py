f=open("fileone.txt",'w+')
f.write('This is the first file might create another file later but i am not sure what should i write in that file .')
f.close()

f=open('filetwo.txt','w+')
f.write('This is the file i was talking about')
f.close()
import zipfile
comp_file=zipfile.ZipFile('comp_file.zip','w')
comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj=zipfile.ZipFile('comp_file.zip','r')
zip_obj.extractall('saved')

import shutil
dir_to_zip= 'C:\\Users\\ABHIJEET\\Desktop\\Py\\saved'
output_filename='example'
shutil.make_archive(output_filename,'zip',dir_to_zip)
shutil.unpack_archive('example.zip','final_unzip','zip')