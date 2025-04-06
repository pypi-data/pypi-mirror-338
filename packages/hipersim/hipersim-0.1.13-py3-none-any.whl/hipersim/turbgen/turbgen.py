# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 18:01:13 2021

@author: Nikolay Dimitrov, DTU Wind Energy

contributors: Mads Mølgaard Pedersen, DTU Wind Energy
              Asta Hannesdottir, DTU Wind Energy
"""

import xarray as xr
import numpy as np
import os


class turb_field:
    def __init__(self, **kwargs):
        ''' Parse inputs
        '''
        if 'params' in kwargs:
            self.params = kwargs['params']
        else:
            self.params = {'BaseName': 'turb_py',
                           'alphaepsilon': 1.0,
                           'L': 29.4,
                           'Gamma': 3.9,
                           'SeedNo': 1,
                           'Nx': 8192,
                           'Ny': 32,
                           'Nz': 32,
                           'dx': 1,
                           'dy': 1,
                           'dz': 1,
                           'HighFreqComp': 0,
                           'SaveToFile': 0
                           }

        # Parameters directly included as inputs will override the "params" dictionary
        if 'Nx' in kwargs:
            self.params['Nx'] = kwargs['Nx']
        if 'Ny' in kwargs:
            self.params['Ny'] = kwargs['Ny']
        if 'Nz' in kwargs:
            self.params['Nz'] = kwargs['Nz']
        if 'dx' in kwargs:
            self.params['dx'] = kwargs['dx']
        if 'dy' in kwargs:
            self.params['dy'] = kwargs['dy']
        if 'dz' in kwargs:
            self.params['dz'] = kwargs['dz']
        if 'L' in kwargs:
            self.params['L'] = kwargs['L']
        if 'Gamma' in kwargs:
            self.params['Gamma'] = kwargs['Gamma']
        if 'alphaepsilon' in kwargs:
            self.params['alphaepsilon'] = kwargs['alphaepsilon']
        if 'SeedNo' in kwargs:
            self.params['SeedNo'] = kwargs['SeedNo']
        if 'SaveToFile' in kwargs:
            self.params['SaveToFile'] = kwargs['SaveToFile']
        if 'HighFreqComp' in kwargs:
            self.params['HighFreqComp'] = kwargs['HighFreqComp']
        if 'BaseName' in kwargs:
            self.params['BaseName'] = kwargs['BaseName']
        if 'TurbOptions' in kwargs:
            self.TurbOptions = kwargs['TurbOptions']
        else:
            self.TurbOptions = {'FileFormat': 0}

    def generate(self):

        from hipersim.turbgen.generate_field import generate_field

        u, v, w = generate_field(
            BaseName=self.params['BaseName'],
            alphaepsilon=self.params['alphaepsilon'],
            L=self.params['L'],
            Gamma=self.params['Gamma'],
            SeedNo=self.params['SeedNo'],
            Nx=self.params['Nx'],
            Ny=self.params['Ny'],
            Nz=self.params['Nz'],
            dx=self.params['dx'],
            dy=self.params['dy'],
            dz=self.params['dz'],
            HighFreqComp=self.params['HighFreqComp'],
            SaveToFile=self.params['SaveToFile'],
            TurbOptions=self.TurbOptions
        )
        self.u = u
        self.v = v
        self.w = w

        return u, v, w

    def output(self):
        from hipersim.turbgen.turb_utils import output_field
        u, v, w = output_field(self.u, self.v, self.w, self.params, self.TurbOptions)
        return u, v, w

    def to_xarray(self):
        """Return xarray dataarray with u,v,w along x,y,z,uvw axes with all input parameters as attributes:
        - x: In direction of U, i.e. first yz-plane hits wind turbine last
        - y: to the left, when looking in the direction of the wind
        - z: up
        """
        ae, L, G, seed, Nx, Ny, Nz, dx, dy, dz, hfc = [self.params[k]
                                                       for k in ['alphaepsilon', 'L', 'Gamma', 'SeedNo',
                                                                 'Nx', 'Ny', 'Nz', 'dx', 'dy', 'dz', 'HighFreqComp']]
        from hipersim import MannTurbulenceField
        return MannTurbulenceField(uvw=np.array([self.u, self.v, self.w]),
                                   alphaepsilon=ae, L=L, Gamma=G, Nxyz=(Nx, Ny, Nz), dxyz=(dx, dy, dz),
                                   seed=seed, HighFreqComp=hfc,
                                   double_xyz=(self.TurbOptions.get('double_x', False),
                                   self.TurbOptions.get('double_y', True),
                                   self.TurbOptions.get('double_z', True)),
                                   generator='hipersim',
                                   ).to_xarray()

    def to_netcdf(self, folder='', filename=None):
        da = self.to_xarray()
        filename = os.path.join(folder, filename or (da.attrs['name'] + ".nc"))
        da.to_netcdf(filename)

    def constrain(self, Constraints=None, Component=None, TurbOptions=None):
        if Constraints is None:
            Constraints = self.Constraints
        else:
            self.Constraints = Constraints
        if TurbOptions is None:
            TurbOptions = {
                'HighFreqComp': self.params['HighFreqComp'],
                'SeedNo': self.params['SeedNo'],
                'FileFormat': self.TurbOptions['FileFormat']}

        if Component is None:
            from hipersim.turbgen.constrain_field import constrain_field

            if not (hasattr(self, 'u') and hasattr(self, 'v') and hasattr(self, 'w')):
                # at least one of u,v,w is missing
                self.generate()
            u, v, w = constrain_field(Constraints,
                                      self.u,
                                      self.v,
                                      self.w,
                                      BaseName=self.params['BaseName'],
                                      alphaepsilon=self.params['alphaepsilon'],
                                      L=self.params['L'],
                                      Gamma=self.params['Gamma'],
                                      Nx=self.params['Nx'],
                                      Ny=self.params['Ny'],
                                      Nz=self.params['Nz'],
                                      dx=self.params['dx'],
                                      dy=self.params['dy'],
                                      dz=self.params['dz'],
                                      SaveToFile=self.params['SaveToFile'],
                                      UseNormalization=0,
                                      TurbOptions=TurbOptions)
            self.u = u
            self.v = v
            self.w = w

            return u, v, w
        else:
            from hipersim.turbgen.constrain_field_1d import constrain_field_1d

            if (((Component == 'u') and not hasattr(self, 'u')) or
                ((Component == 'v') and not hasattr(self, 'v')) or
                    ((Component == 'w') and not hasattr(self, 'w'))):
                self.generate()
            if Component == 'u':
                c_0 = self.u
            if Component == 'v':
                c_0 = self.v
            if Component == 'w':
                c_0 = self.w
            c = constrain_field_1d(
                Constraints,
                Component,
                c=c_0,
                BaseName=self.params['BaseName'],
                alphaepsilon=self.params['alphaepsilon'],
                L=self.params['L'],
                Gamma=self.params['Gamma'],
                Nx=self.params['Nx'],
                Ny=self.params['Ny'],
                Nz=self.params['Nz'],
                dx=self.params['dx'],
                dy=self.params['dy'],
                dz=self.params['dz'],
                SaveToFile=self.params['SaveToFile'],
                UseNormalization=0,
                TurbOptions=TurbOptions)

            if Component == 'u':
                self.u = c
            if Component == 'v':
                self.v = c
            if Component == 'w':
                self.w = c

            return c
