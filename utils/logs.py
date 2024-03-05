import logging,datetime,os

class log:
    def log(msg,status='info'):
        dtnow=datetime.datetime.now()
        logpath=rf"{os.getcwd()}\{dtnow.strftime('%Y-%m-%d')}.log"
        logging.basicConfig(filename=logpath, encoding='utf-8', level=logging.DEBUG)
        if status == 'error':
            logging.error(f"{dtnow.strftime('%Y-%m-%d-%H:%M:%S')}---------------{msg}")
        else:    
            logging.info(f"{dtnow.strftime('%Y-%m-%d-%H:%M:%S')}---------------{msg}")