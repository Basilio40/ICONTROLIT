""""
    K2A:iControlIT
    GREGORIO HONROATO: GREGORIO.HONORATO@PLUS-TI.COM.BR
    WHATSAPP: (19) 99250-9913

"""

from scripts.__init__ import *


class IcontrolIt:
    def __init__(self):
        ...

    def main(self):
        self.dr = self.iniciliazar_driver()
        
    def iniciliazar_driver(self):
        dr = webdriver.Chrome(ChromeDriverManager().install())
        return dr    