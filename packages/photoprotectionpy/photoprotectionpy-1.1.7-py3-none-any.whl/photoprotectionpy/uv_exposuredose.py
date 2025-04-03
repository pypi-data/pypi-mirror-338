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
def uvdose(UVAPF0):
    """
    Determine UV exposure dose.

    Parameters
    ----------
    UVA-PF<sub>0<sub> : float
        Initial UVA protection factor 
        before UV exposure.

    Returns
    -------
    D : float
        UV dose in J/cm^2

    """
    D=np.array(UVAPF0)*1.2
    return D
