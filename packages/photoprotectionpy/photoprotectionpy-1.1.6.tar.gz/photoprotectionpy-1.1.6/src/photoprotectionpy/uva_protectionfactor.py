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
   limitations under the License.
"""

import numpy as np
import scipy.integrate as sci
def uvapf(data,C,integration=None, batch=None):
    """
    Calculate initial UVA protection factor before 
    UV exposure (UVA-PF<sub>0<sub>) or UVA protection factor 
    after UV exposure (UVA-PF).

    Parameters
    ----------
    data : list, pandas.DataFrame or numpy.array
        Each column of the array is a treatment, where 
        rows correspond to each read measured from 290 
        to 400 nm (dλ=1). Use mean absorbance before UV 
        absorbance for UVA-PF<sub>0<sub> and mean absorbance 
        after UV exposure for UVA-PF.
    C : float
        Coefficient of adjustment "C".
    integration : string
        Choose between "trapz" (default)
        or "simpson"
     batch : boolean
         By default False. If true, will determine C or SPF of 
         all data samples against a single target SPF or an
         already calculated C value.
         
    Returns
    -------
    UVA-PF<sub>0<sub> or UVA-PF : float

    """
    wavelengths=[320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,
                  352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,
                  383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400]
    ppd=[1.0,0.975,0.95,0.925,0.9,0.875,0.85,0.825,0.8,0.775,0.75,0.725,0.7,0.675,0.65,0.625,
                  0.6,0.575,0.55,0.525,0.5,0.494,0.488,0.481,0.475,0.469,0.463,0.457,0.45,0.444,0.438,0.432,0.426,0.419,0.413,0.407,0.401,0.395,0.388,0.382,0.376,0.37,
                  0.364,0.357,0.351,0.345,0.339,0.333,0.326,0.32,0.314,0.308,0.302,0.295,0.289,0.283,0.277,0.271,0.264,0.258,0.252,0.246,0.24,0.233,0.227,0.221,0.215,
                  0.209,0.202,0.196,0.19,0.184,0.178,0.171,0.165,0.159,0.153,0.147,0.14,0.134,0.128]
    uva_source=[4.84e-06,8.47e-06,1.36e-05,2.07e-05,3.03e-05,4.29e-05,
                5.74e-05,7.6e-05,9.85e-05,0.000122,0.000151,0.000181,0.000213,0.000244,0.000283,0.000319,0.000359,0.000398,0.000439,0.000478,0.00052,
                0.000561,0.0006,0.000638,0.000674,0.000712,0.000747,0.000778,0.000818,0.000843,0.000875,0.000904,0.000929,0.000949,0.000973,0.000986,
                0.00101,0.00103,0.00105,0.00106,0.00108,0.00109,0.0011,0.0011,0.0011,0.0011,0.00109,0.00109,0.00108,0.00107,0.00105,0.00103,0.000995,
                0.00097,0.000937,0.000906,0.000876,0.000843,0.000806,0.000761,0.000711,0.000666,0.000612,0.000556,0.000499,0.000443,0.000388,0.000336,
                0.000287,0.000241,0.000201,0.000164,0.000131,0.000103,7.9e-05,5.98e-05,4.46e-05,3.26e-05,2.3e-05,1.58e-05,1.05e-05]
    data=np.asarray(data)
    dims=data.ndim
    C=np.asarray(C)
    size_C=C.size
    if len(data.shape)==1:
        shape=data.shape[0]
        if shape==111:
            data=data[30:,]
        elif shape==81:
            ...
        elif shape!=111 or shape!=81:
            print("Invalid row number")
            return
    elif len(data.shape)==2:
        shape=data.shape[0]
        if shape==111:
            data=data[30:,]
        elif shape==81:
            ...
        elif shape!=111 or shape!=81:
            print("Invalid row number")
            return
    if dims>1 and size_C>1:
        size_data=data.shape[1]
    if batch==True:
        batch_list=[]
        if len(data.shape)==1:
            print("More than one sample is needed")
            return
        size_data=data.shape[1]
        if size_C==1:
            for i in range(size_data):
                batch_list.append(C)
            C=np.asarray(batch_list)
            size_C=C.size
        else:
            print("More values that needed for batch mode")
            return
    elif batch==False:
        if size_C==1:
            print("More values are needed")
            return
        else:
            ...
    elif batch==None:
        ...
    elif batch!=False or batch!=True:
        print("Enter a True or False")
        return
    else:
        print("Enter a True or False")
    if integration is None:
        integration="trapz"
    if isinstance(integration, str):
        if integration=="trapz":
            C_array=np.asarray(C)
            uvapf=[]
            if dims==1:
                arrays=[ppd,uva_source,np.power(10,-data*C_array)]
                uvapf.append(np.trapz(np.multiply(ppd,uva_source))/np.trapz(np.prod(np.vstack(arrays),axis=0)))
            elif dims>1:
                if size_C==size_data:
                    for i in range(size_data):
                        arrays=[ppd,uva_source,np.power(10,-data[:,i]*C_array[i])]
                        uvapf.append(np.trapz(np.multiply(ppd,uva_source))/np.trapz(np.prod(np.vstack(arrays),axis=0)))
                else:
                    print("Dimensions of data and value arrays do not match")
            else:
                print("Dimensions of data and value arrays do not match")
            return uvapf
        elif integration=="simpson":
            C_array=np.asarray(C)
            uvapf=[]
            if dims==1:
                arrays=[ppd,uva_source,np.power(10,-data*C_array)]
                uvapf.append(sci.simpson(np.multiply(ppd,uva_source),x=wavelengths)/sci.simpson(np.prod(np.vstack(arrays),axis=0),x=wavelengths))
            elif dims>1:
                if size_C==size_data:
                    for i in range(size_data):
                        arrays=[ppd,uva_source,np.power(10,-data[:,i]*C_array[i])]
                        uvapf.append(sci.simpson(np.multiply(ppd,uva_source),x=wavelengths)/sci.simpson(np.prod(np.vstack(arrays),axis=0),x=wavelengths))
                else:
                    print("Dimensions of data and value arrays do not match")
            else:
                print("Dimensions of data and value arrays do not match")
            return uvapf
        else:
            print("Enter a valid integration method")
    else:
        print("Enter a valid integration method")
