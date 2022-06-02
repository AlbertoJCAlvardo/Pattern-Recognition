# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:30:41 2022

@author: argen
"""
import numpy as np


class RandomColor:
    def genHexCode():
    
        r = hex(np.random.randint(0,255))
        g = hex(np.random.randint(0,255))
        b = hex(np.random.randint(0,255))
            
        
        sr=""
        sg=""
        sb=""
        
        for i in range(2,len(r)):
            if(len(r)<4):
                sr += "0"
            sr += str(r[i])
        for i in range(2,len(g)):
            if(len(g)<4):
                sg += "0"
            sg += str(g[i])
        for i in range(2,len(b)):
            if(len(b)<4):
                sb += "0"
            sb += str(b[i])
            
        
        
        
        f = "#"+sr+sg+sb
        
        return f
