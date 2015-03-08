#! /usr/bin/env python
## file: config_app.py
import os,sys,subprocess,logging
FILE_NAME="config_app.py"
ROOT_DIR=os.getcwd()
USER_HOME= os.path.expanduser('~')
#APP_DIR=os.path.join('/home',os.getusername())
def logger_config():
    global logger
    logdir=os.path.join(sys.path[0],"Log")
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    logger = logging.getLogger('config_app.py')
    logger.setLevel(logging.DEBUG)
    
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    #filehandler
    fh = logging.FileHandler(os.path.join(ROOT_DIR,'Log','app_config.log'))
    fh.setLevel(logging.DEBUG)


    # create formatter
    formC= logging.Formatter('%(levelname)s::  %(message)s --%(asctime)s')
    formF= logging.Formatter('%(levelname)s::  %(message)s --%(asctime)s')
    # add formatter to ch
    fh.setFormatter(formF)
    ch.setFormatter(formC)
    # add ch and fh to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    # 'application' code
    #logger.debug('debug message')
    #logger.info('info message')
    #logger.warn('warn message')
    #logger.error('error message')
    #logger.critical('critical message')

def main():
    logger_config()
    logger.info("STARTING APP CONFIGURATION")
    if os.path.exists(USER_HOME):
        #logger.info("APP_DIR: %s"%APP_DIR)
        logger.info("USER_HOME: %s"%USER_HOME)
    else:
        exit(1)
    

if __name__ == "__main__":
    main()
