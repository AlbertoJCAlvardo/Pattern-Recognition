# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:35:00 2022

@author: argen
"""

class ConfussionMatrix:
    
    def putBlock(self,s,length):
        a = ""
        sep = length-len(a)
        
        for i in range(0,length):
            if(sep%2 == 0):
                if(i<sep/2):
                    a+=" "
                if(i == sep/2):
                    a+=s
                    i+=len(s)
                if(i>sep/2+len(s)):
                    a+=" "
            else:
                if(i<sep//2):
                    a+=" "
                if(i == sep//2):
                    a+=s
                    i+=len(s)
                if(i>sep//2+len(s)):
                    a+=" "
                
        
        return a
    
    def printConfussion(self,cm,members,ar):
            s = self.putBlock(" ",len(str(members))+1)+"  "
            full = ""
            sigma=0
            k = len(cm[0])
            ef =[]
            
            
               
            if ar == 2 :
                b = members
                for i in range(len(cm)-1):
                    ind = cm[i].index(max(cm[i]))
                    cm[i][ind] -= 1
                    cm[i][i]+=1
                
            sigma = 0
            
            for i in range(len(cm)):
                s+=self.putBlock(" C"+str(i+1)+"",len(str(members))+1)+" "
            s+=self.putBlock("",len(str(members))+1)+"Rendimiento\n"
            for i in range(k):
                
                s+=self.putBlock("C"+str(i+1),len(str(members))+1)+" " 
                for j in range(k):
                    s+=self.putBlock(str(cm[i][j])+" ",len(str(members))+1)+" " 
                s+=self.putBlock(str(round(cm[i][i]/members*100,3))+"%",len("Rendimiento"))+"\n"
                sigma+=cm[i][i]/members*100
                ef.append(sigma)
            print(s)
            c = []
            
            for i in range(len(cm[0])):
                c.append(i+2)
                    
            
            print("\nRendimiento total:  "+str(sigma/len(cm)))
    
    
    def getPerformance(self,cm,members,scale):
        performance = [[],[]]
        sigma = 0
        for i in range(len(cm)):
        
            sigma = cm[i][i]/members*100 + scale*0.5
            performance[0].append((i+1)*10)
            performance[1].append(sigma)
        
       
        return performance