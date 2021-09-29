#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 17:11:58 2021

@author: kevin
"""


import os.path
import numpy as np
#I think I only changed the print functions from the python2 galah tools
import Galah_tool_py3 as gtools
import os
import copy




#The_reduced_observed spectra needs to have the same syntax as the latest galah data release
def equalizing_resolution(synthetic_spectra,synthetic_frequency,reduced_observed_spectra):
    #Creates a copy of the observe spectra so it doesn't change it
    synthetic_temp=copy.deepcopy(reduced_observed_spectra)

    #Changes the resolution of the temporary spectra to match the resolution of the synthetic spectra.
    fstart= float(synthetic_temp[1].header.get('CRVAL1'))
    length=np.array([fstart+y*synthetic_temp[1].header.get('CDELT1') for y in range(0,len(synthetic_temp[1].data))])
    synthetic_temp[2].data=np.interp(synthetic_frequency,length,synthetic_temp[2].data)
    synthetic_temp[7].data=np.interp(synthetic_frequency,length,synthetic_temp[7].data)
    synthetic_temp[1].header['CDELT1']=synthetic_frequency[1]-synthetic_frequency[0]
    
    
    #Changes the data part of the temp_reduced_observed_spectra to the synthetic spectra and saves it as a random file.
    random_number='171027003801055'+str(np.random.randint(100000000))

    synthetic_temp[1].data=synthetic_spectra
    if os.path.exists(random_number+'_synthetic.fits'):
        os.remove(random_number+'_synthetic.fits')
    synthetic_temp.writeto(random_number+'_synthetic.fits')    
    synthetic_temp.close()     	
    
    #Uses gtools to read the spectra and then equalizes the resolution and returns the equilized resolution
    syn=gtools.read(random_number+'_synthetic')
    syn.equalize_resolution(synthetic=True)
    os.remove(random_number+'_synthetic.fits')
    
    return syn.f
