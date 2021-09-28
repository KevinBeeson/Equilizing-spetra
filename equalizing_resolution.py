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
def equalizing_resolution(synthetic_spectra,reduced_observed_spectra):
    
    #Changes the data part of the temp_reduced_observed_spectra to the synthetic spectra and saves it as a random file.
    random_number='171027003801055'+str(np.random.randint(100000000))
    synthetic_temp=copy.copy(reduced_observed_spectra)

    synthetic_temp[1].data=synthetic_spectra
    if os.path.exists(random_number+'_synthetic.fits'):
        os.remove(random_number+'_synthetic.fits')
    reduced_observed_spectra.writeto(random_number+'_synthetic.fits')    
    synthetic_temp.close()     	
    
    #Uses gtools to read the spectra and then equalizes the resolution and returns the equilized resolution
    syn=gtools.read(random_number+'_synthetic')
    syn.equalize_resolution()
    os.remove(random_number+'_synthetic.fits')
    
    return syn.f
