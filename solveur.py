# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:19:25 2020

@author: lhoes
"""

import matplotlib.pyplot as plt
import numpy as np

def setn(N):
    '''
    Fixe le nombre de corps, réinitialise les valeurs déjà rentré si il y en a.
    Créer l'array Data, permettant l'utilisation de setdata().

    Paramètre
    ----------
    N : int
        Nombre de corps
    ----------
    
    Returns None
    '''
    global No,d
    No=N
    global Data
    Data=np.zeros(No*5)
    Data.shape=(No,5)
    d=0
        
    
d=0
def setdata(m,x,y,vx,vy):
    '''
    Défini les caractéristiques de l'objet.
    Passe à l'objet suivant à chaque ittération.
    Le nombre de corps doit être défini auparavent (setn(N)).

    Paramètres
    ----------
    m : float
        Masse de l'objet.
    x : float
        Position initale en x.
    y : float
        Position initale en y.
    vx : float
        Vitesse initale en x.
    vy : float
        Vitesse initiale en y.
    ----------
    
    Returns None
    '''
    global d
     
    try :
        if d==No:
            return print('setdata() Erreur : Nombre de corps maximal atteint ({})'.format(No))
    except NameError:
        return print('setdata() Erreur : N non défini')
    Data[d,0]=m
    Data[d,1]=x
    Data[d,2]=y
    Data[d,3]=vx
    Data[d,4]=vy
    d += 1
    
    
    
  
def F(Y):
    '''
    Fonction permettant de calculer l'accélération des corps.
    
    Paramètre
    ----------
    Y : array
        Array contenant les valeurs initiales des corps.
    ----------
    
    Returns l'accélération des corps et leurs positions.
    '''   
    G = 1.4872 * 10**-34 #constante gravitationelle
    var = np.zeros(No*4)
    for i in range(No):
        Ax = 0
        Ay = 0
        for j in (range(No)):
            if i != j:
                Ax = Ax + ((-G*Data[j,0]*(Y[i*4]-Y[j*4]) / (((Y[i*4]-Y[j*4])**2 + (Y[(1 + 4*i)]-Y[1 +j*4])**2)**(3/2) )))
                Ay = Ay + ((-G*Data[j,0]*(Y[i*4 + 1]-Y[j*4 + 1]) / (((Y[i*4]-Y[j*4])**2 + (Y[(1 + 4*i)]-Y[1 +j*4])**2)**(3/2) )))
        var[i*4   ]= Y[i*4 + 2]
        var[i*4 +1]= Y[i*4 + 3]
        var[i*4 +2]= Ax
        var[i*4 +3]= Ay
    return var
    

def Euler(tmp,h):
    '''
    Méthode numérique d'Euler explicite permettant de calculer la valeur suivante d'une suite.

    Paramètres
    ----------
    tmp : int
        Temps total de la simulation, en jour.
    h : float
        Pas.
    ----------
    
    Returns None
    '''
    global Y
    global t
    t = np.arange(0,tmp,h)
    try :
        Y=np.zeros((No*4,len(t)))
    except NameError:
        return(print('Euler() Erreur : Nombre de corps non défini (N).'))
    for i in range (0,No*4,4):
        for j in range (4):
            Y[i+j,0]=Data[i//4,j+1]
    for i in range(1, len(t)):
        Y[:,i]= Y[:,i-1] + h * F(Y[:,i-1])
    
    
def Runge(tmp,h):
    '''
    Méthode numérique de Runge-Kutta d'ordre permettant de calculer la valeur suivante d'une suite.

    Paramètres
    ----------
    tmp : int
        Temps total de la simulation, en jour.
    h : float
        Pas.
    ----------
    
    Returns None
    '''
    global Y
    global t
    t = np.arange(0,tmp,h)
    try :
        Y=np.zeros((No*4,len(t)))
    except NameError:
        return(print('Runge() Erreur : Nombre de corps non défini (N).'))
    for i in range (0,No*4,4):
        for j in range (4):
            Y[i+j,0]=Data[i//4,j+1]
    for i in range (1, len(t)):
        Y[:,i]= Y[:,i-1] + (h/2)*(  F(Y[:,i-1]) + F(Y[:,i-1] + h*F(Y[:,i-1])))
        
        
def affichage():#Affichage des trajéctoires
    '''
    Affiche les trajéctoires calculées par Euler() ou Runge().
    
    Returns None
    '''
    plt.figure("Trajectoire(s)")
    plt.title("Trajectoire(s)")
    plt.grid(which='major')
    plt.xlabel('x')
    plt.ylabel('y')
    try :        
        for i in range (No):
            phrase='Corps n°{}'.format(i+1)
            plt.plot(Y[i*4],Y[i*4+1])
            plt.text(Y[i*4,-1],Y[i*4+1,-1],phrase)
    except NameError : 
        return(print('affichage() Erreur : Nombre de corps non défini (N).'))
        
        
def animation(): #Affichage avec animations
    '''
    Affiche les trajéctoires calculées par Euler() ou Runge() avec animations.
    
    Returns None
    '''
    affichage()
    line=[0 for i in range(No)]
    for i in range (No):
        line[i],=(plt.plot(Y[i*4,0],Y[i*4+1,0],'ko'))
        
    for j in range(1,len(t),12):
        plt.pause(0.1)
        for k in range(No):
            line[k].set_data(Y[k*4,j],Y[k*4+1,j])
    

def vitesse(n):
    '''
    Affiche la norme de la vitesse d'un corps choisi en fonction du temps.
    Runge() ou Euler() doit être éffectué avant.
    
    Paramètre 
    ----------
    n : int
        Numéro du corps dont l'on veut afficher la vitesse.
    ----------
    
    Reurns None
    '''
    V = []
    if n>No :
        return(print('vitesse() Erreur : Numéro de corps trop grand : {}. Le nombre de corps actuel est de {}.'.format(n,No)))
    try :
        for i in range (len(t)):
            V.append(((Y[n*4-2,i])**2+(Y[n*4-1,i])**2)**(1/2))
    except NameError: 
        return(print('vitesse() Erreur : Le temps n\'a pas été défini. Utilisez la fonction Runge() ou Euleur().'))
    titre = "Norme de la vitesse du corps {}".format(n)
    
    plt.figure(titre)
    plt.title(titre)
    plt.grid(which="major")
    plt.xlabel('temps,')
    plt.ylabel('Norme de la vitesse')
    plt.plot(t,V)
    
    