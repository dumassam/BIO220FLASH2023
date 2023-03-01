from typing import Dict, List
from PIL import Image

def qa_split(s: str) -> tuple[str, str]:
    """ """
    s = s.replace('\n', '')
    i = str.find(s, '*')
    return (s[:i], s[i+1:])
    

def qa_to_dic(f) -> Dict[int, tuple[str, str]]:
    """ """
    s = f.readline()
    dic = {}
    i = 1
    while s != '':
        dic[i] = qa_split(s)
        i += 1
        s = f.readline()
    return dic

def key_to_q(i: int, dic: Dict[int, tuple[str, str]]) -> str:
    """ """
    return dic[i][0]

def key_to_a(i: int, dic: Dict[int, tuple[str, str]]) -> str:
    """ """
    return dic[i][1]

def num_list(n: int) -> List[int]:
    """ """
    i = 1
    lst = []
    while i <= n:
        lst.append(i)
        i += 1
    return lst    
    
    
  