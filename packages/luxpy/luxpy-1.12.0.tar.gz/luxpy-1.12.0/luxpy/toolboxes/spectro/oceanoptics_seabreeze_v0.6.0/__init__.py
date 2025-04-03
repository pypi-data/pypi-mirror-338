# -*- coding: utf-8 -*-
########################################################################
# <spectropy.oceanoptics: a Python package for spectral measurement with oceanoptics spectrometers.>
# Copyright (C) <2019>  <Kevin A.G. Smet> (ksmet1977 at gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#########################################################################
"""
Module for spectral measurements using OceanOptics spectrometers 
================================================================

Installation:
-------------
    1. Download and install the seabreeze installer from sourceforge:
    https://sourceforge.net/projects/seabreeze/files/SeaBreeze/installers/
    2. Install python-seabreeze: conda install -c poehlmann python-seabreeze
    3. Windows: Force the spectrometer to use a libusb driver via Zadig 
    (http://zadig.akeo.ie/)
    4. Install pyusb ("import usb.core", "usb.core.find()" should work before proceeding)
    5. Ready to go!
    
Functions:
----------
 :initOOdev(): initialize spectrometer
 :getOOspd(): measure spectrum
 :create_dark_model(): create a model for dark counts
 :estimate_dark_from_model(): estimate dark counts for specified integration time based on model
 
Default parameters:
-------------------
 :_INT_TIME_SEC: int, default integration time
 :_CORRECT_DARK_COUNTS: bool, automatic dark count correction supported by some spectrometers
 :_CORRECT_NONLINEARITY: bool, automatic non-linearity correction
 :_TARGET_MAX_CNTS_RATIO: float, aim for e.g. 80% (0.8) of max number of counts
 :_IT_RATIO_INCREASE: float, first stage of int_time optimization: increase int_time by this fraction
 :_MAX_NUMBER_OF_RATIO_INCREASES: int, number of times to apply ration increase before estimating using lin. regr.
 :_DARK_MODEL_INT_TIMES: ndarray, e.g. np.linspace(1e-6, 7.5, 5): array with integration times for dark model
 :_SAVGOL_WINDOW: window for smoothing of dark measurements
 :_SAVGOL_ORDER: order of savgol filter
 :_VERBOSITY: (0: nothing, 1: text, 2: text + graphs)
 :_DARK_MODEL: path and file where default dark_model is stored.
    
Notes:
------
    1. Changed read_eeprom_slot() in eeprom.py in *pyseabreeze* because the 
    ubs output used ',' as decimal separator instead of '.' (probably because
    of the use of a french keyboard, despite having system set to use '.' as separator):  
    line 20 in eeprom.py: "return data.rstrip('\x00')" was changed to
    "return data.rstrip('\x00').replace(',','.')"
    
    2. More info on: https://github.com/ap--/python-seabreeze
    
    3. Cooling for supported spectrometers not yet implemented (May 2, 2019)
 
    4. Due to the way ocean optics firmware/drivers are implemented, 
    most spectrometers do not support an abort mode of the standard 'free running mode', 
    which causes spectra to be continuously stored in a FIFO array. 
    This first-in-first-out (FIFO) causes a very unpractical behavior of the spectrometers,
    such that, to ensure one gets a spectrum corresponding to the latest integration time 
    sent to the device, one is forced to call the spec.intensities() function twice! 
    This means a simple measurements now takes twice as long, resulting in a sub-optimal efficiency. 
    
    5. Hopefully, Ocean Optics will at some point implement a more simple and 
    more logical operation of their devices: one that just reads a spectrum 
    at the desired integration time the momemt the function is called and which puts the 
    spectrometer in idle mode when no spectrum is requested.
    
    
.. codeauthor:: Kevin A.G. Smet (ksmet1977 at gmail.com)
"""
from .oceanoptics import *
__all__ = oceanoptics.__all__