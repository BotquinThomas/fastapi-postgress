from configparser import ConfigParser
import datetime as dt
import logging
import os

def getCurrentDate() -> str:
	return dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d")

def getCurrentDateTime() -> str:
	return dt.datetime.strftime(dt.datetime.now(), "%Y-%m-%d %H-%M")

def createLogFile(path: str = os.getcwd(),
                  name: str = f'logfile {getCurrentDateTime()}.log',
                  level = logging.INFO, 
                  format = '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                  **kwargs):
    # Create log folder if necessary
    if not os.path.exists(path):
        os.mkdir(path)
	
    # Create logger
    logging.basicConfig(filename = os.path.join(path,name), level = level, format = format, **kwargs)

def printToLogAndConsole(message : str, level  = logging.INFO):
	if level == logging.DEBUG:
		logging.debug(message)
	elif level == logging.INFO:
		logging.info(message)
	elif level == logging.WARNING:
		logging.warning(message)
	elif level == logging.ERROR:
		logging.error(message)
	elif level == logging.CRITICAL:
		logging.critical(message)
	print(message)
 
def config(filename : str ='database.ini', section : str='postgresql') -> dict:
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    
    # get section, default to postgresql
    _dict = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            _dict[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return _dict



if __name__ == "__main__":
    pass