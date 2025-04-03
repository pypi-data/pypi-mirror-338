# -*- coding: utf-8 -*-
"""
Copyright © 2024 Santiago Guerrero-Higareda

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License
"""
import numpy as np
import scipy.integrate as sci
def ispf(data,integration=None):
    """
    Determine initial calculated *in vitro* SPF

    Parameters
    ----------
    data : list, pandas.DataFrame or numpy.array
        Each column of the array is a treatment, where rows correspond 
        to each reading measured from 290 to 400 nm (dλ=1). 
    integration : string
        Choose between "trapz" (default)
        or "simpson"
        
    Returns
    -------
    initial SPF : list containing floats
        Returns calculated *in vitro* SPF.

    """
    wavelengths=[290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,
                  321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,
                  352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,
                  383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400]
    erythema=[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.805,0.649,0.522,0.421,0.339,0.273,0.22,0.177,0.143,0.115,0.0925,0.0745,0.06,0.0483,0.0389,
              0.0313,0.0252,0.0203,0.0164,0.0132,0.0106,0.00855,0.00689,0.00555,0.00447,0.0036,0.0029,0.00233,0.00188,0.00151,0.00141,0.00136,
              0.00132,0.00127,0.00123,0.00119,0.00115,0.00111,0.00107,0.00104,0.001,0.000966,0.000933,0.000902,0.000871,0.000841,0.000813,0.000785,
              0.000759,0.000733,0.000708,0.000684,0.000661,0.000638,0.000617,0.000596,0.000575,0.000556,0.000537,0.000519,0.000501,0.000484,0.000468,
              0.000452,0.000437,0.000422,0.000407,0.000394,0.00038,0.000367,0.000355,0.000343,0.000331,0.00032,0.000309,0.000299,0.000288,0.000279,
              0.000269,0.00026,0.000251,0.000243,0.000234,0.000226,0.000219,0.000211,0.000204,0.000197,0.000191,0.000184,0.000178,0.000172,0.000166,
              0.00016,0.000155,0.00015,0.000145,0.00014,0.000135,0.00013,0.000126,0.000122]
    uv_ssr=[8.74e-06,1.45e-05,2.66e-05,4.57e-05,0.000101,0.000259,0.000704,0.00168,0.00373,0.00794,0.0148,0.0251,0.0418,0.0622,0.0869,0.122,0.162,
            0.199,0.248,0.289,0.336,0.387,0.431,0.488,0.512,0.557,0.596,0.626,0.657,0.688,0.724,0.737,0.768,0.796,0.799,0.829,0.844,0.856,0.879,
            0.895,0.901,0.916,0.943,0.944,0.943,0.957,0.966,0.977,0.977,0.997,0.994,1.01,1.01,1.01,1.02,1.03,1.03,1.03,1.04,1.03,1.05,1.04,1.04,
            1.04,1.04,1.05,1.04,1.04,1.03,1.04,1.04,1.03,1.02,1.02,0.998,0.996,0.967,0.965,0.939,0.919,0.898,0.873,0.847,0.812,0.784,0.742,0.715,
            0.669,0.628,0.586,0.534,0.493,0.448,0.393,0.343,0.299,0.257,0.215,0.18,0.149,0.119,0.094,0.0727,0.0553,0.0401,0.0289,0.0207,0.014,
            0.00951,0.00619,0.00417]
    data=np.asarray(data)
    dims=data.ndim
    if len(data.shape)==1:
        shape=data.shape[0]
        if shape==111:
            ...
        elif shape!=111:
            print("Invalid row number")
            return
    elif len(data.shape)==2:
        shape=data.shape[0]
        if shape==111:
            ...
        elif shape!=111:
            print("Invalid row number")
            return
    if integration is None:
        integration="trapz"
    if isinstance(integration, str):
        if integration=="trapz":
            spf=[]
            if dims==1:
                arrays=[erythema,uv_ssr,np.power(10,-data)]
                spf.append(np.trapz(np.multiply(erythema,uv_ssr))/np.trapz(np.prod(np.vstack(arrays),axis=0)))
            elif dims>1:
                size=data.shape
                for i in range(size[1]):
                    arrays=[erythema,uv_ssr,np.power(10,-data[:,i])]
                    spf.append(np.trapz(np.multiply(erythema,uv_ssr))/np.trapz(np.prod(np.vstack(arrays),axis=0)))
            return spf
        elif integration=="simpson":
            spf=[]
            if dims==1:
                arrays=[erythema,uv_ssr,np.power(10,-data)]
                spf.append(sci.simpson(y=np.multiply(erythema,uv_ssr),x=wavelengths)/sci.simpson(y=np.prod(np.vstack(arrays),axis=0),x=wavelengths))
            elif dims>1:
                size=data.shape
                for i in range(size[1]):
                    arrays=[erythema,uv_ssr,np.power(10,-data[:,i])]
                    spf.append(sci.simpson(y=np.multiply(erythema,uv_ssr),x=wavelengths)/sci.simpson(y=np.prod(np.vstack(arrays),axis=0),x=wavelengths))
            return spf
        else:
            print("Error: Enter a valid integration method")
    else:
        print("Error: Enter a valid integration method")
