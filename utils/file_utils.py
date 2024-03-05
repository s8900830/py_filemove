import os
from .logs import log

class check:   
    # 檔案大小與檔案名稱            
    def folder_size(filepath, fileslist = {},total_size = 0):
        for root,dirs,files in os.walk(filepath) :
            for name in files:
                # size 取得的是 位元組 (byte)
                total_size+=os.path.getsize(os.path.join(root,name))
                fileslist[os.path.join(root,name)]=os.path.getsize(os.path.join(root,name))
        return total_size,fileslist
                    
    # 偵測是否有檔案存在
    def detect_files(filepath):
        list = os.walk(filepath)
        fileslist = []
        for root,dirs,files in list :
            for x in files :
                if x != '' or x is not None:
                    fileslist.append(x)
        if fileslist is None or len(fileslist) == 0:
            return False
        else :
            return True
        

    # 刪除被壓縮的檔案
    def delete_files(inputpath):
        list = os.walk(inputpath)
        for root,dirs,files in list :
            for name in files:
                try:
                    os.remove(os.path.join(root,name))
                except Exception as e:
                    log.log(e,'error')

    # 確認並建立壓縮暫存區
    def check_temp(directory= r'.\temp'):
        if not os.path.exists(directory):
            os.makedirs(directory)
            return True
        return False