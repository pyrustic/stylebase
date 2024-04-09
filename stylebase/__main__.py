from collections import namedtuple
from enum import Enum

UrlConfig = namedtuple("UrlConfig", ["project_url", "src_url_template",
                                      "docs_url_template"])

UrlConfig.__doc__ = "Namedtuple"
UrlConfig.project_url.__doc__ = "Custom doc"

class Meo(Enum):
    AAA = 1
    BBB = 2


FIELD_1 = "hello"
FIELD_2 = 42
FIELD_3 = ("hello", 42)
MY_CONSTANT = 1

def main():
    """
    main function
    """
    print("https://github.com/pyrustic/stylebase")

def func1(a, b="hi", c=42):
    """
    This is a short descriptiondfd fad dfj sllze djdf zadfda
    
    This is the longer description
    dfdf dfdf dfdfdf dfdf ddfdfd
    
    [params]
    - a: ddff
    - b: dffdf
    - c: dfdfdf
    
    [return]
    Tdff dfhjks dfsjksdf sdfjsk 
    """
    pass
    
def func2():
    pass
    
def func3():
    """"""
    pass


class MerryDoc:
    """Class doc here"""
    CONST_1 = 42
    """hola"""
    CONST_2 = "hello"
    ZETA_2 = "hello"
    def __init__(self, a, b="hi", c=42):
        """Short doc"""
        pass
      
    @property
    def prop(self):
        pass
        
    @prop.setter
    def prop(self, v):
        pass
      
    def _hella(self):
        "doccccc !"
        pass
          
    def hello(self):
        pass
  
    
class Lac:
    """Class doc here"""
    CONST_1 = 42
    """hola"""
    CONST_2 = "hello"
    ZETA_2 = "hello"
    def __init__(self, a, b="hi", c=42):
        """Short doc"""
        pass
      
    @property
    def prop(self):
        pass
        
    @prop.setter
    def prop(self, v):
        pass
      
    def _hella(self):
        "doccccc !"
        pass
          
    def hello(self):
        pass
        

if __name__ == "__main__":
    main()
