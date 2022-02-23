""""
    K2A:iControlIT
    GREGORIO HONROATO: GREGORIO.HONORATO@PLUS-TI.COM.BR
    WHATSAPP: (19) 99250-9913

"""

from glob import glob
from time import sleep
from scripts.Log import mainlog, print

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

ARQUIVO_LOG = 'log.txt'
SRV = "http://192.168.0.150"
PST_WK = r"C:\Plusti\iControlIT"
USUARIO_ICONTROL = ""
SENHA_ICONTROL = ""