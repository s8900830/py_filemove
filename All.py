import os,shutil,datetime,zipfile
from utils.logs import log
from utils.file_utils import check
import config

# 外網
class input:
    
    def move_file():
        msg = ''
        
        # 輸入檔案的路徑
        # input file path
        inputpath=config.GET_EXTERNAL_INPUT_PATH

        # 要壓縮到哪裡去
        archive_path=r'E:\Input'
        dtnow = datetime.datetime.now()
        try:
            if inputpath is not None and inputpath != '':
                
                # 少判斷有沒有檔案要不要執行，其實也可以不用理反正一定會有一種，例如：ArcGIS的氣象圖片資料
                # 但我還是寫了
                if check.detect_files(inputpath) is True:
                    
                # 壓縮檔案
                    total_size_bytes,fileslist = input.folder_size(inputpath)
                    zipname = f"input_{dtnow.strftime('%Y-%m-%d-%H-%M-%S')}"

                    part_num = 1
                    zsize=0
                    zipfiles = []
                    zf = zipfile.ZipFile(f"{zipname}_{part_num}.zip", mode="w")
                    for name,fsize in fileslist.items():
                        if '.zip' in name:
                            zipfiles.append(name)
                        else:
                            zsize+=fsize
                            
                        # 如果超過1.5GB，那就要分開壓縮檔案
                        if zsize/1024/1024/1024 > 1.5:
                            zf.close()
                            log.log(f'{zipname}_{part_num}.zip---成功執行檔案壓縮')  
                            zsize=fsize
                            part_num+=1
                            zf = zipfile.ZipFile(f"{zipname}_{part_num}.zip", mode="w")
                            zf.write(name)
                        else:    
                            zf.write(name)
                    zf.close()
                    log.log(f'{zipname}_{part_num}.zip---成功執行檔案壓縮')  
                    for x in zipfiles:
                        shutil.move(x,archive_path) 

                    # 搬移壓縮檔到輸出目錄               
                    for x in os.listdir(os.getcwd()):
                        if '.zip' in x:
                            shutil.move(os.getcwd()+f'\{x}',archive_path)
                            msg='Success'

                    # 刪除原本要壓縮的檔案，不然檔案會累積
                    if check.detect_files(inputpath) is True:
                        check.delete_files(inputpath)
                else:
                    msg='Success'
                    log.log('沒有檔案可以壓縮')
        except Exception as e:
            log.log(e,'error')
        return msg
    
# 內網
class output:
    # 重新命名 ArcGIS 圖檔名稱
    def ArcGIS_Weather_Pic():
        msg=''
        # ArcGIS 氣象圖檔放置位置
        ArcGISImagePath=r'C:\Users\Administrator\Desktop\QRCode2.1N\Receive\weather'
        try:
            list = os.walk(ArcGISImagePath)
            for root,dirs,files in list :
                for name in files:
                    os.rename(os.path.join(root,name),os.path.join(root,name.replace('Clean_','')))
            log.log(f'---重新命名成功')
        except Exception as e:
            log.log(e,'error')
        return msg

    def move_file():

        #紀錄訊息
        msg=''

        # 輸出檔案的路徑
        # output file path
        outputpath=r'D:\Output'

        # 要解壓縮到哪邊去
        unarchive_path=r'C:\Users\Administrator\Desktop\QRCode2.1N\Receive'
        try:
            if outputpath is not None and outputpath != '':
                # 尋找能解壓縮的檔案
                for x in os.listdir(outputpath):

                    # 搬移公情圖片、影片壓縮檔
                    if 'Clean_NewsFiles' in x: 
                        shutil.move(f'{outputpath}\{x}',f'{unarchive_path}\IDOLData\{x}') 

                    # 如果是其他檔案 做解壓縮到 unarchive_path 下的 Send 資料夾
                    elif '.zip' in x and 'Clean_input' in x :
                        shutil.unpack_archive(f'{outputpath}\{x}',extract_dir=unarchive_path)
                        msg='Success'
                        log.log(f'{x}---成功執行檔案解壓縮')

                # 刪除 Output 內的壓縮檔
                for x in os.listdir(outputpath):
                    os.remove(f'{outputpath}\{x}') 
                    log.log(f'{x}---成功刪除解壓縮檔')

                # 移動檔案從 \Send 到原本資料夾
                list = os.walk(f'{unarchive_path}\Send')
                for root,dirs,files in list :
                    for name in files:
                        shutil.move(os.path.join(root,name),os.path.join(root.replace('\Send',''),name)) 

                # 重新命名ArcGIS氣象圖圖檔
                output.ArcGIS_Weather_Pic()

                # 迴圈完沒有檔案的話會記錄這個資料
                if os.listdir(outputpath) is None or len(os.listdir(outputpath))==0:
                    log.log('沒有檔案可以解壓縮')

        except Exception as e:
            log.log(e,'error')

        return msg

input_ = input 
output_ = output
if __name__=='__main__':
        print(input_.move_file())
        #print(input_.move_file())
        #print(output_.move_file())