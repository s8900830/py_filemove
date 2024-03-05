from zipfile import ZipFile
from .size import size_change
from .logs import log
import os,shutil,datetime,config


class zip_file:
    dtnow = datetime.datetime.now()
    
    def zip_file(zipname=f"input_{dtnow.strftime('%Y-%m-%d-%H-%M-%S')}",fileslist={}):
        try:
            part_num ,zsize=1,0
            zipfiles, zipfileslist = [],[]
            zip_temp_folder=r'.\temp'

            # 壓縮檔案
            zf = ZipFile(f'{zip_temp_folder}\{zipname}_{part_num}.zip', mode="w")
            for name,fsize in fileslist.items():
                if '.zip' in name:
                    zipfiles.append(name)
                else:
                    zsize+=fsize

                # 如果超過 ZIPFILE_SINGLE_SIZE 的設定，那就會分開壓縮檔案
                if zsize > size_change.size(config.ZIPFILE_SINGLE_SIZE):
                    # 先閉環
                    zf.close()
                    log.log(f'{zip_temp_folder}\{zipname}_{part_num}.zip---成功執行檔案壓縮')  

                    # 建了一個新的壓縮檔
                    zipfileslist.append(f'{zip_temp_folder}\{zipname}_{part_num}.zip')
                    zsize=fsize
                    part_num+=1
                    zf = ZipFile(f'{zip_temp_folder}\{zipname}_{part_num}.zip', mode="w")

                    # 這段好像可以合併到上面去？
                    zf.write(name)
                else:

                    # 抓取檔案的排除有zip的檔案，避免寫入
                    if '.zip' not in name:    
                        zf.write(name)

            # 關閉所有的壓縮檔案，相當等於 Save
            zf.close()
            log.log(f'{zip_temp_folder}\{zipname}_{part_num}.zip---成功執行檔案壓縮')  

            # 返回壓縮檔表
            zipfileslist.append(f'{zip_temp_folder}\{zipname}_{part_num}.zip')
            return True,zipfileslist
        
        except Exception as e:
            log.log(str(e),'error')  

    # 解壓縮
    def unzip_file(set_internal_outputpath,temppath=r'.\temp'):
        try:
            for x in os.listdir(temppath):
                # 解壓縮到特定位置
                shutil.unpack_archive(f'{temppath}\{x}',extract_dir=set_internal_outputpath)
            return True
        
        except Exception as e:
            log.log(str(e),'error')        
