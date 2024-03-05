from zipfile import ZipFile
from .file_utils import check
from .size import size_change
from .logs import log
import config,datetime


class zip_file:
    dtnow = datetime.datetime.now()
    
    def zip_file(zipname=f"input_{dtnow.strftime('%Y-%m-%d-%H-%M-%S')}",fileslist={}):
        try:
            part_num ,zsize=1,0
            zipfiles = []
            zip_temp_folder=r'.\temp'

            # 確認並建立壓縮暫存區
            check.check_temp()

            # 壓縮檔案
            zip_filename= f'{zip_temp_folder}\{zipname}_{part_num}.zip'

            zf = ZipFile(f'{zip_temp_folder}\{zipname}_{part_num}.zip', mode="w")
            for name,fsize in fileslist.items():
                if '.zip' in name:
                    zipfiles.append(name)
                else:
                    zsize+=fsize

                # 如果超過 ZIPFILE_SINGLE_SIZE 的設定，那就會分開壓縮檔案
                if zsize > size_change.size(config.ZIPFILE_SINGLE_SIZE):
                    zf.close()
                    log.log(f'{zip_temp_folder}\{zipname}_{part_num}.zip---成功執行檔案壓縮')  
                    zsize=fsize
                    part_num+=1
                    zf = ZipFile(f'{zip_temp_folder}\{zipname}_{part_num}.zip', mode="w")
                    zf.write(name)
                else:    
                    zf.write(name)
            zf.close()
            log.log(f'{zip_temp_folder}\{zipname}_{part_num}.zip---成功執行檔案壓縮')  
        except Exception as e:
            log.log(f'{e}','error')  
            
        return zipfiles
