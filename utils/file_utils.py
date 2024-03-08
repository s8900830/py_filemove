import os,stat,shutil
from .logs import log


class utils:
    # 重新命名 IDOLContent IDX檔案
    def rename(filepath):
        try:
            for root, dirs, files in os.walk(filepath):
                for name in files:
                    if 'IDOLContent' in name:
                        os.rename(f'{root}\{name}',f'{root}\{name.replace("Clean_",""''"")}')
            return True

        except Exception as e:
            log.log(str(e), 'error')
    # 檔案大小與檔案名稱
    def folder_size(filepath, fileslist={}, total_size=0):
        try:
            for root, dirs, files in os.walk(filepath):
                for name in files:
                    # size 取得的是 位元組 (byte)
                    total_size += os.path.getsize(os.path.join(root, name))
                    fileslist[os.path.join(root, name)] = os.path.getsize(
                        os.path.join(root, name))
            return total_size, fileslist

        except Exception as e:
            log.log(str(e), 'error')

    # 偵測是否有檔案存在
    def detect_files(filepath):
        try:
            list = os.walk(filepath)
            fileslist = []
            for root, dirs, files in list:
                for x in files:
                    if x != '' or x is not None:
                        fileslist.append(x)
            if fileslist is None or len(fileslist) == 0:
                return False
            else:
                return True

        except Exception as e:
            log.log(str(e), 'error')

    # 從 pre_input 移動 zip 檔案到 input 或是 移動 temp 內的壓縮檔案到 input
    def move_files(fileslist, despath):
        try:
            for files in fileslist:
                if '.zip' in files:
                    shutil.move(files, despath)
            return True

        except Exception as e:
            log.log(str(e)+'---move', 'error')

    # 給與使用者有檔案存取權限
    def chmod(despath):
        try:
            os.chmod(despath,stat.S_IRWXO)
            return True
        
        except Exception as e:
            log.log(str(e)+'---move', 'error')

    # 刪除被壓縮的檔案
    def delete_files(inputpath):
        try:
            list = os.walk(inputpath)
            for root, dirs, files in list:
                for name in files:
                    os.remove(os.path.join(root, name))

        except Exception as e:
            log.log(str(e)+'---delete', 'error')

    # 確認並建立資料夾
    def check_temp(directory=r'.\temp'):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
                return True
            return False

        except Exception as e:
            log.log(str(e), 'error')

    # 過濾器
    def internal_filter(fileslist):
        # 建立篩選容器
        newsfileslist, ofileslist = [], []
        try:
            for files in fileslist:
                # 建立篩選方式，以檔名分
                if 'Clean_NewsFiles' in files:
                    newsfileslist.append(files)
                elif 'Clean_input' in files:
                    ofileslist.append(files)
            return newsfileslist, ofileslist

        except Exception as e:
            log.log(str(e), 'error')
