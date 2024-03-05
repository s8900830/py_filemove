from utils import file_check,zip_file
import datetime
import config

class external:
        def move_file():
            dtnow = datetime.datetime.now()
            file_check_ = file_check.check
            zip_file_ = zip_file.zip_file
            get_external_inputpath=config.GET_EXTERNAL_INPUT_PATH

            # 先確認有沒有檔案
            if file_check_.detect_files(filepath=get_external_inputpath) :
                total_size , fileslist = file_check_.folder_size(filepath=get_external_inputpath)

                zf = zip_file_.zip_file(fileslist=fileslist)


            return fileslist,zf





external_ = external 
if __name__=='__main__':
        print(external_.move_file())
