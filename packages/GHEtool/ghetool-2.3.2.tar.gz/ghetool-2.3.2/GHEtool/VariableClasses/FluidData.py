"""
This document contains the variable classes for the fluid data.
"""
from __future__ import annotations

import pygfunction as gt

from GHEtool.VariableClasses.BaseClass import BaseClass


class FluidData(BaseClass):
    """
    Contains information regarding the fluid data of the borefield.
    """

    __slots__ = 'k_f', 'rho', 'Cp', 'mu', '_mfr', '_vfr'
    __allow_none__ = ['_vfr', '_mfr']

    def __init__(self, mfr: float = None,
                 k_f: float = None,
                 rho: float = None,
                 Cp: float = None,
                 mu: float = None,
                 vfr: float = None):
        """

        Parameters
        ----------
        mfr : float
            Mass flow rate per borehole [kg/s]
        k_f : float
            Thermal Conductivity of the fluid [W/mK]
        rho : float
            Density of the fluid [kg/m3]
        Cp : float
            Thermal capacity of the fluid [J/kgK]
        mu : float
            Dynamic viscosity of the fluid [Pa/s]
        vfr : float
            Volume flow rate per borehole [l/s]
        """
        self.k_f: float | None = k_f  # Thermal conductivity W/mK
        self._mfr: float | None = mfr  # Mass flow rate per borehole kg/s
        self.rho: float | None = rho  # Density kg/m3
        self.Cp: float | None = Cp  # Thermal capacity J/kgK
        self.mu: float | None = mu  # Dynamic viscosity Pa/s
        self._vfr: float | None = vfr  # Volume flow rate l/s

        if self._mfr is not None and self._vfr is not None:
            raise ValueError('You cannot set both the mass flow rate and volume flow rate')

    @property
    def vfr(self) -> float:
        """
        This function returns the volume flow rate.

        Returns
        -------
        float
            volume flow rate [l/s]
        """
        if self._vfr is not None:
            return self._vfr
        return self.mfr / self.rho * 1000

    @vfr.setter
    def vfr(self, vfr: float) -> None:
        """
        This function sets the volume flow rate.
        The mass flow rate will be set to 0

        Parameters
        ----------
        vfr : float
            Volume flow rate [l/s]

        Returns
        -------
        None
        """
        self._vfr = vfr
        self._mfr = None

    @property
    def mfr(self) -> float:
        """
        This function returns the mass flow rate. Either based on a given mass flow rate,
        or calculated based on a volume flow rate.

        Returns
        -------
        float
            mass flow rate [kg/s]
        """
        if self._mfr is not None:
            return self._mfr
        return self.vfr / 1000 * self.rho

    @mfr.setter
    def mfr(self, mfr: float) -> None:
        """
        This function sets the mass flow rate.
        The vfr will hence be set to 0.

        Parameters
        ----------
        mfr : float
            Mass flow rate [kg/s]

        Returns
        -------
        None
        """
        self._mfr = mfr
        self._vfr = None

    def set_mass_flow_rate(self, mfr: float) -> None:
        """
        This function sets the mass flow rate per borehole.

        Parameters
        ----------
        mfr : fluid
            Mass flow rate per borehole [kg/s]

        Returns
        -------
        None
        """
        self.mfr = mfr

    def import_fluid_from_pygfunction(self, fluid_object: gt.media.Fluid) -> None:
        """
        This function loads a fluid object from pygfunction and imports it into GHEtool.
        Note that this object does not contain the mass flow rate!

        Parameters
        ----------
        fluid_object : Fluid object from pygfunction

        Returns
        -------
        None
        """
        self.k_f = fluid_object.k
        self.rho = fluid_object.rho
        self.Cp = fluid_object.cp
        self.mu = fluid_object.mu

    @property
    def Pr(self) -> float:
        """
        This function returns the Prandtl number which is defined as the ratio of momentum diffusivity
        to thermal diffusivity.

        Returns
        -------
        float
            Prandtl number
        """
        return self.Cp * self.mu / self.k_f

    def __eq__(self, other):
        if not isinstance(other, FluidData):
            return False
        for i in self.__slots__:
            if getattr(self, i) != getattr(other, i):
                return False
        return True

    def __repr__(self):
        temp = f'Fluid parameters\n\tThermal conductivity of the fluid [W/(m·K)]: {self.k_f:.3f}\n\t' \
               f'Density of the fluid [kg/m³]: {self.rho:.3f}\n\t' \
               f'Thermal capacity of the fluid [J/(kg·K)]: {self.Cp:.3f}\n\t' \
               f'Dynamic viscosity [Pa·s]: {self.mu:.3f}\n\t'
        if self._vfr is not None:
            temp += f'Volume flow rate [l/s]: {self.vfr}'
        else:
            temp += f'Mass flow rate [kg/s] : {self.mfr}'
        return temp
