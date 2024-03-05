import logging,datetime,os

class log:
    # 建立 log
    def log(msg,status='info'):
        # 時間函數
        dtnow=datetime.datetime.now()

        # 設定路徑位置與檔名
        logpath=rf"{os.getcwd()}\logs\{dtnow.strftime('%Y-%m-%d')}.log"

        # 設定基本log參數
        logging.basicConfig(filename=logpath, encoding='utf-8', level=logging.DEBUG)

        # 判斷狀態
        if status == 'error':
            logging.error(f"{dtnow.strftime('%Y-%m-%d-%H:%M:%S')}---------------{msg}")
        else:    
            logging.info(f"{dtnow.strftime('%Y-%m-%d-%H:%M:%S')}---------------{msg}")