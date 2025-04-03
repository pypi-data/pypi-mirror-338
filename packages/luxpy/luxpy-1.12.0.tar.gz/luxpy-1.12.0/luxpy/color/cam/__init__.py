# -*- coding: utf-8 -*-
########################################################################
# <LUXPY: a Python package for lighting and color science.>
# Copyright (C) <2017>  <Kevin A.G. Smet> (ksmet1977 at gmail.com)
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
cam: sub-package with color appearance models
=============================================

 :_UNIQUE_HUE_DATA: | database of unique hues with corresponding 
                    | Hue quadratures and eccentricity factors 
                    | for ciecam02, ciecam16, ciecam97s, cam15u, cam18sl)

 :_SURROUND_PARAMETERS: | database of surround param. c, Nc, F and FLL 
                        | for ciecam02, ciecam16, ciecam97s and cam15u.

 :_NAKA_RUSHTON_PARAMETERS: | database with parameters (n, sig, scaling and noise) 
                            | for the Naka-Rushton function: 
                            | NK(x) = sign(x) * scaling * ((abs(x)**n) / ((abs(x)**n) + (sig**n))) + noise

 :_CAM_UCS_PARAMETERS: | database with parameters specifying the conversion 
                       |  from ciecamX to:
                       |    camXucs (uniform color space), 
                       |    camXlcd (large color diff.), 
                       |    camXscd (small color diff).

 :_CAM15U_PARAMETERS: database with CAM15u model parameters.

 :_CAM_SWW16_PARAMETERS: cam_sww16 model parameters.

 :_CAM18SL_PARAMETERS: database with CAM18sl model parameters

 :_CAM_DEFAULT_WHITE_POINT: Default internal reference white point (xyz)

 :_CAM_DEFAULT_CONDITIONS: Default CAM model parameters for model.

 :_CAM_AXES: dict with list[str,str,str] containing axis labels of defined cspaces.

 :deltaH(): Compute a hue difference, dH = 2*C1*C2*sin(dh/2).

 :naka_rushton(): applies a Naka-Rushton function to the input

 :hue_angle(): calculates a positive hue angle

 :hue_quadrature(): calculates the Hue quadrature from the hue.


 :ciecam02(): | calculates ciecam02 output 
              | `N. Moroney, M. D. Fairchild, R. W. G. Hunt, C. Li, M. R. Luo, and T. Newman, 
                “The CIECAM02 color appearance model,” 
                IS&T/SID Tenth Color Imaging Conference. p. 23, 2002. <http://rit-mcsl.org/fairchild/PDFs/PRO19.pdf>`_

 :cam16(): | calculates cam16 output 
           | `C. Li, Z. Li, Z. Wang, Y. Xu, M. R. Luo, G. Cui, M. Melgosa, M. H. Brill, and M. Pointer, 
             “Comprehensive color solutions: CAM16, CAT16, and CAM16-UCS,” 
             Color Res. Appl., p. n/a–n/a. <http://onlinelibrary.wiley.com/doi/10.1002/col.22131/abstract>`_

 :cam02ucs(): | calculates ucs (or lcd, scd) output based on ciecam02 
              | (forward + inverse available)
              | `M. R. Luo, G. Cui, and C. Li, 
                “Uniform colour spaces based on CIECAM02 colour appearance model,” 
                Color Res. Appl., vol. 31, no. 4, pp. 320–330, 2006.
                <http://onlinelibrary.wiley.com/doi/10.1002/col.20227/abstract>`_

 :cam16ucs(): | calculates ucs (or lcd, scd) output based on cam16 
              |  (forward + inverse available)
              | `C. Li, Z. Li, Z. Wang, Y. Xu, M. R. Luo, G. Cui, M. Melgosa, M. H. Brill, and M. Pointer, 
                “Comprehensive color solutions: CAM16, CAT16, and CAM16-UCS,” 
                Color Res. Appl. <http://onlinelibrary.wiley.com/doi/10.1002/col.22131/abstract>`_

 :cam15u(): | calculates the output for the CAM15u model for self-luminous unrelated stimuli. 
            | `M. Withouck, K. A. G. Smet, W. R. Ryckaert, and P. Hanselaer, 
              “Experimental driven modelling of the color appearance of 
              unrelated self-luminous stimuli: CAM15u,” 
              Opt. Express, vol. 23, no. 9, pp. 12045–12064, 2015.
              <https://www.osapublishing.org/oe/abstract.cfm?uri=oe-23-9-12045&origin=search>`_
            | `M. Withouck, K. A. G. Smet, and P. Hanselaer, (2015), 
              “Brightness prediction of different sized unrelated self-luminous stimuli,” 
              Opt. Express, vol. 23, no. 10, pp. 13455–13466. 
              <https://www.osapublishing.org/oe/abstract.cfm?uri=oe-23-10-13455&origin=search>`_

 :cam_sww16(): | A simple principled color appearance model based on a mapping of the Munsell color system.
               | `Smet, K. A. G., Webster, M. A., & Whitehead, L. A. (2016). 
                 “A simple principled approach for modeling and understanding uniform color metrics.” 
                 Journal of the Optical Society of America A, 33(3), A319–A331. 
                 <https://doi.org/10.1364/JOSAA.33.00A319>`_

 :cam18sl(): | calculates the output for the CAM18sl model for self-luminous related stimuli. 
             | `Hermans, S., Smet, K. A. G., & Hanselaer, P. (2018). 
               “Color appearance model for self-luminous stimuli.“
               Journal of the Optical Society of America A, 35(12), 2000–2009. 
               <https://doi.org/10.1364/JOSAA.35.002000>`_           

 :camXucs(): Wraps ciecam02(), ciecam16(), cam02ucs(), cam16ucs().

 :specific wrappers in the 'xyz_to_cspace()' and 'cpsace_to_xyz()' format:
      | 'xyz_to_jabM_ciecam02', 'jabM_ciecam02_to_xyz',
      | 'xyz_to_jabC_ciecam02', 'jabC_ciecam02_to_xyz',
      | 'xyz_to_jabM_ciecam16', 'jabM_ciecam16_to_xyz',
      | 'xyz_to_jabC_ciecam16', 'jabC_ciecam16_to_xyz',
      | 'xyz_to_jabz',          'jabz_to_xyz',
      | 'xyz_to_jabM_camjabz', 'jabM_camjabz_to_xyz',
      | 'xyz_to_jabC_camjabz', 'jabC_camjabz_to_xyz',
      | 'xyz_to_jab_cam02ucs', 'jab_cam02ucs_to_xyz', 
      | 'xyz_to_jab_cam02lcd', 'jab_cam02lcd_to_xyz',
      | 'xyz_to_jab_cam02scd', 'jab_cam02scd_to_xyz', 
      | 'xyz_to_jab_cam16ucs', 'jab_cam16ucs_to_xyz',
      | 'xyz_to_jab_cam16lcd', 'jab_cam16lcd_to_xyz',
      | 'xyz_to_jab_cam16scd', 'jab_cam16scd_to_xyz',
      | 'xyz_to_qabW_cam15u',  'qabW_cam15u_to_xyz',
      | 'xyz_to_lab_cam_sww16','lab_cam_sww16_to_xyz',
      | 'xyz_to_qabM_cam18sl', 'qabM_cam18sl_to_xyz',
      | 'xyz_to_qabS_cam18sl', 'qabS_cam18sl_to_xyz',
      

 :_update_parameter_dict(): Get parameter dict and update with values in args dict

 :_setup_default_adaptation_field(): Setup a default illuminant adaptation field with Lw = 100 cd/m² for selected CIE observer.

 :_massage_input_and_init_output(): Redimension input data to ensure most they have the appropriate sizes for easy and efficient looping.

 :_massage_output_data_to_original_shape(): Massage output data to restore original shape of original CAM input.

 :_get_absolute_xyz_xyzw(): Calculate absolute xyz tristimulus values of stimulus and white point from spectral input or convert relative xyz values to absolute ones.

 :_simple_cam(): An example CAM illustration the usage of the functions in luxpy.cam.helpers 


Module for CAM "front-end" cmf adaptation
=========================================

 :translate_cmfI_to_cmfS(): | Using smooth RGB primaries, translate input data (spectral or tristimlus)
                            | for an indivual observer to the expected tristimulus values for a standard observer. 

 :get_conversion_matrix():  | Using smooth RGB primaries, get the 'translator' matrix to convert 
                            | tristimulus values calculated using an individual observer's 
                            | color matching functions (cmfs) to those calculated using the cmfs of 
                            | a standard observer.
                            
 :get_rgb_smooth_prims(): Get smooth R, G, B primaries with specified wavelength range
 
 :_R,_G,_B: precalculated smooth primaries with [360,830,1] wavelength range.
 


.. codeauthor:: Kevin A.G. Smet (ksmet1977 at gmail.com)
"""
from . import cmf_translator_sww2021 as cmftranslator
__all__ = ['cmftranslator']

from .colorappearancemodels import *
__all__ += colorappearancemodels.__all__


