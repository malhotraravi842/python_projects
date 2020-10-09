import os
import shutil

dict_extensions ={
    'audio_extensions' : ('.mp3','.m4a','.wav','.flac'),
    'videos_extensions' : ('.mp4','.mkv','.MKV','.flv','.mpeg'),
    'doc_extensions' : ('.doc','.docx','.html','.htm','.odt','.pdf','.txt','.csv','.xls','.xlsx','.ppt','.pptx'),
    'image_extensions' :('.png','.jpg','.jpeg','.gif','.eps','.ai','.tiff','.psd','.indd','.raw'),
    'zip_extensions' : ('.zip','.arc','.arj','.as','.b64','.btoa','.bz','.cab','.cpt','.gz','.hqx','.iso','.lha','.lzh','.mim','.mme','.pak','.pf','.rar','.rpm','.sea','.sit','.sitx','.tar','.gz','.tbz','.tbz2','.tgz','.uu','.uue','.z','.zip','.zipx','.zoo')
}

folderpath =input("Enter Folder path: ")

def file_finder(folder_path, file_extensions):
    files =[]
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files


for extension_type ,extension_tuple in dict_extensions.items():
    folder_name =extension_type.split('_')[0] +'Files'
    folder_path =os.path.join(folderpath, folder_name)
    if os.path.exists(folder_path) ==True:
        pass
    else:
        os.mkdir(folder_path)
    for item in (file_finder(folderpath, extension_tuple)):
        item_path =os.path.join(folderpath,item)
        item_new_path =os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)
