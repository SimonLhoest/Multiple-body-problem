# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:56:04 2020

@author: xxmoi
"""


import solveur as sl

''''Ici, notre exemple comporte 5 corps, donc on l'indique.'''
sl.setn(5)

'''
On défini les condidtions initales de nos corps :
Corps 1 : Voyager
'''
Masse = 815
Xo = 8.620811898118265*10**-1
Yo = -5.362815775434949*10**-1
VXo= 1.018617820600348*10**-2
VYo= 1.998609427696851*10**-2


'''On rentre les conditions initiales dans notre programme :'''
sl.setdata(Masse, Xo, Yo, VXo, VYo) # Voyager 2



'''On fait de même pour nos 4 corps suivants :'''

#Soleil
sl.setdata(1.989*10**30,2.246309216105666*10**-3,-4.39629484083473*10**-3,8.029313610091777*10**-6,-1.570146617228189*10**-7) 

#Terre
sl.setdata(5.972*10**24,8.615157791605411*10**-1,-5.382505307629882*10**-1,8.802784907564254*10**-3,1.455442742467161*10**-2) 

#Jupiter
sl.setdata(1.898*10**27,8.230978906159968*10**-1,5.021217065564969,-7.536246065039235*10**-3,1.568985796886243*10**-3) 

#Saturne
sl.setdata(5.683*10**26,-7.130666351091540,5.772950943135804,-3.810770594695837*10**-3,-4.350834041096856*10**-3)

'''
On demande ensuite au programme de calculer les trajectoires.
Ici on utilise la méthode numérique de Runge-Kutta d'ordre 2
On décide d'afficher une trajectoire pendant 5475 jours (15 ans), avec un pas de 1
'''
sl.Runge(5475,1)


'''
On veut ensuite afficher les trajectoires calculées précedemment.
On voudrait bien que le programme affiche les corps en mouvement, on demande donc une animation
'''
sl.animation()


'''
Pour finir, on veut afficher la norme de la vitesse d'un des corps.
Ici, on affiche la norme de la vitesse du corps 1, c'est à dire celle de la sonde Voyager 2
'''
sl.vitesse(1)

#%%
'''EXEMPLE 2 : Le système solaire''' 

import solveur as sl

sl.setn(9)

#Soleil
sl.setdata(1.989*10**30,2.246309216105666*10**-3,-4.39629484083473*10**-3,8.029313610091777*10**-6,-1.570146617228189*10**-7)

#Mercure
sl.setdata(3.3011*10**23,1.506221308589724E-01,-4.252869519307865E-01,2.090550732026586E-02,1.078455520067420E-02)

#Venus
sl.setdata(4.8685*10**24,4.240772193221299E-01,5.815916042238873E-01,-1.647150336918318E-02,1.172816490781606E-02)

#Terre
sl.setdata(5.972*10**24,8.615157791605411*10**-1,-5.382505307629882*10**-1,8.802784907564254*10**-3,1.455442742467161*10**-2)
 
#Mars
sl.setdata(6.4185*10**23,1.042659208708580E+00,1.021010099229809E+00,-9.278870690438345E-03,1.115657935656362E-02)
 
#Jupiter
sl.setdata(1.898*10**27,8.230978906159968*10**-1,5.021217065564969,-7.536246065039235*10**-3,1.568985796886243*10**-3) 

#Saturne
sl.setdata(5.683*10**26,-7.130666351091540,5.772950943135804,-3.810770594695837*10**-3,-4.350834041096856*10**-3)

#Uranus
sl.setdata(8.6810*10**25,-1.392183014347122E+01,-1.231710542296843E+01,2.576883677231733E-03,-3.129505174163754E-03)

#Neptune
sl.setdata(102.43*10**24,-7.562827304598740E+00,2.932267902840758E+01,3.019177719195125E-03,-7.667280029140879E-04)


sl.Runge(11000,1)
sl.affichage()


#%%
'''EXEMPLE 3 : 81P/WILD et Stardust'''

import solveur as sl

sl.setn(8)

#Soleil
sl.setdata(1.989*10**30,3.889510194697126E-03,2.178461543261419E-03,-2.656527492969907E-06,6.306869872086685E-06) 

#Terre
sl.setdata(5.972*10**24,-1.034327461319037E-01,9.797440029755474E-01,-1.739053516162883E-02,-1.931642290986583E-03) 

#Jupiter
sl.setdata(1.898*10**27,-4.495622658165717E+00,-3.054131950812523E+00,4.147362524399780E-03,-5.885057846238344E-03) 

#Saturne
sl.setdata(5.683*10**26,-5.430717576869026E+00,7.308623008771248E+00,-4.775951276682522E-03,-3.340056933941649E-03)

#Venus
sl.setdata(4.8685*10**24,5.315705026705553E-02,7.203424318660920E-01,-2.025048128733532E-02,1.285924465269149E-03)

#Mars
sl.setdata(6.4185*10**23,4.637530045521263E-01,1.457192268139862E+00,-1.281577951354142E-02,5.413956695314298E-03)

#Comete 81P/WILD
sl.setdata(2.3*10**13,4.609360461813961E+00,-1.848504729045900E+00,3.872473005670850E-03,4.285698208964988E-03)

#Stardust
sl.setdata(385,-4.494283489650668E-02,1.003179366078005E+00,-2.042374927665088E-02,-3.230004207387142E-03)


sl.Runge(10950,2)

sl.animation()
