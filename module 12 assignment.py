# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:26:24 2020

@author: USER
"""
nameData=[]
def acceptParameters():
        names=''
        while names !='none':
            names=input('Enter the guest name')
            if names != 'none':
                nameData.append(names)
        return(nameData)
    
def printNames(nameData):
    for name in nameData:
        print(name)
    return

def main():
    names=acceptParameters()
    printNames(names)
    return    
main()    