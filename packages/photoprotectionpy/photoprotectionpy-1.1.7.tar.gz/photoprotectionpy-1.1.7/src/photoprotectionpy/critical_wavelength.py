# -*- coding: utf-8 -*-
"""
Copyright 2024 Santiago Guerrero-Higareda

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
wavelengths=[290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,
              321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,
              352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,
              383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400]
def criticalwave(data,integration=None):
    """
    Calculate the Critical Wavelength (CW)

    Parameters
    ----------
    data : list, pandas.DataFrame or numpy.array
        Absorbance values of treatment(s)
    integration : string
        Choose between "trapz" (default)
        or "simpson"

    Returns
    -------
    CW: int
        Returns CW.

    """
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
    if dims>1:
        size=data.shape[1]
    if integration is None:
        integration="trapz"
    if isinstance(integration, str):
        if integration=="trapz":
            cw_arrays=[]
            if dims==1:
                cw=400
                auc_10=np.trapz(data)/10
                for i in range(111):
                    auc=np.trapz(data[list.index(wavelengths,cw):])
                    cw=cw-1
                    if auc>=auc_10:
                        cw_arrays.append(cw)
                        return cw
                        break
            elif dims>1:
                for i in range(size):
                    cw=400
                    auc_10=np.trapz(data[:,i])/10
                    plates=data[:,i]
                    for j in range(111):
                        auc=np.trapz(plates[list.index(wavelengths,cw):])
                        cw=cw-1
                        if auc>=auc_10:
                            cw_arrays.append(cw)
                            break
            return cw_arrays
        elif integration=="simpson":
            cw_arrays=[]
            if dims==1:
                cw=400
                auc_10=sci.simpson(y=data,x=wavelengths)/10
                for i in range(111):
                    auc=sci.simpson(y=data[list.index(wavelengths,cw):],
                                    x=wavelengths[list.index(wavelengths,cw):])
                    cw=cw-1
                    if auc>=auc_10:
                        cw_arrays.append(cw)
                        return cw_arrays
                        break
            elif dims>1:
                for i in range(size):
                    cw=400
                    auc_10=sci.simpson(y=data[:,i],x=wavelengths)/10
                    plates=data[:,i]
                    for j in range(111):
                        auc=sci.simpson(y=plates[list.index(wavelengths,cw):],
                                        x=wavelengths[list.index(wavelengths,cw):])
                        cw=cw-1
                        if auc>=auc_10:
                            cw_arrays.append(cw)
                            break
            return cw_arrays    
        else:
            print("Error: Enter a valid integration method")
    else:
        print("Error: Enter a valid integration method")
