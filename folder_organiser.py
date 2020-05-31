import os,sys



def organise(folder):
    for file in os.listdir(folder):
        
        src=folder+'/'+file
        if(os.path.isfile(src)):
            dest=folder_maker(file,folder)+'/'+file
            os.rename(src,dest)

def folder_maker(filename,folder):
    
    ext=os.path.splitext(filename)[1]
    Extenstions={
        '.pdf':"PDF",
        '.txt':"TEXT",
        '.jpg':"IMAGES",
        'jpeg':"IMAGES",
        '.pptx':"PPT",
        '.ppt':"PPT",
        '.doc':"TEXT",
        '.docx':"TEXT", 
        '.xlsx':"EXCEL",
        '.zip':"ZIP",      
    }
    if(ext in Extenstions.keys()):
        destination=folder+"/"+Extenstions[ext]
    else:
        destination=folder+"/OTHERS"
    folder_exists(destination)
    return destination

def folder_exists(path):
    exists=os.path.isdir(path)
    if(not exists):
        os.mkdir(path)
        
        
if __name__ == "__main__":
    folder=sys.argv[1:]
    path=''
    for word in folder:
        path+=word+' '
    path=path.replace("\\","/")
    path=path[0:len(path)-1]
    organise(path)
    
    
    

