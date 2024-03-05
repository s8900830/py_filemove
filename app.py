from utils import file_utils,zip_file,logs
import sys,datetime,config

class external:
    def move_file():

        # 設定
        file_utils_ = file_utils.utils
        zip_file_ = zip_file.zip_file
        log_=logs.log
        get_external_inputpath=config.GET_EXTERNAL_INPUT_PATH
        set_external_outputpath=config.SET_EXTERNAL_OUTPUT_PATH

        # 先確認有沒有檔案
        if file_utils_.detect_files(filepath=get_external_inputpath) :
            total_size , fileslist = file_utils_.folder_size(filepath=get_external_inputpath)


            zf,zipfileslist = zip_file_.zip_file(fileslist=fileslist)
            if zf is None :
                log_.log('錯誤，檔案壓縮失敗','error')
                return False
            
            # 移動兩個資料夾內的檔案到 input 位置
            file_utils_.move_files(fileslist,despath=set_external_outputpath)
            file_utils_.move_files(zipfileslist,despath=set_external_outputpath)

            # 刪除 pre_input 資料夾內的檔案及 temp 的內容
            file_utils_.delete_files(config.GET_EXTERNAL_INPUT_PATH)
            file_utils_.delete_files(r'.\temp')

            return fileslist,zf
        else:
            log_.log('沒有檔案可以壓縮')
            return 
            

class internal:
    def move_file():
        
        # 設定
        file_utils_ = file_utils.utils
        zip_file_ = zip_file.zip_file
        log_=logs.log
        get_internal_inputpath=config.GET_INTERNAL_INPUT_PATH
        set_internal_outputpath=config.SET_INTERNAL_OUTPUT_PATH
        
        # 先確認有沒有檔案
        if file_utils_.detect_files(filepath=get_internal_inputpath) :
            
            # 取得檔案表
            total_size , fileslist = file_utils_.folder_size(filepath=get_internal_inputpath)
            
            # 篩選檔案
            newsfileslist,ofileslist=file_utils_.internal_filter(fileslist=fileslist)

            # 移動檔案到特定位置
            file_utils_.move_files(newsfileslist,set_internal_outputpath)
            file_utils_.move_files(ofileslist,r'.\temp')
            
            # 解壓縮檔案
            zip_file_.unzip_file(set_internal_outputpath=set_internal_outputpath)

            # 檔案回到上一層
            file_utils_.internal_move(set_internal_outputpath=set_internal_outputpath)
            
            # 刪除 temp 內的東西
            file_utils_.delete_files(r'.\temp')

            return fileslist
        else:
            log_.log('沒有檔案可以壓縮')
        return 

external_ = external 
internal_ = internal

def check():

    file_utils_ = file_utils.utils
    
    # 確認並建立logs
    file_utils_.check_temp(directory=r'.\logs')

    # 確認並建立壓縮暫存區
    file_utils_.check_temp()

if __name__=='__main__':
    args = sys.argv[1]
    
    # 初始化必要項
    check()

    if args == 'external':
        print(external_.move_file())
    elif args == 'internal':
        print(internal_.move_file())
    
