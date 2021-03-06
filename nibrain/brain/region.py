#!/usr/bin/env python

# region class

from geometry import Points
from scalar import Scalar


class Region(object):
    """ Region class represents data related to anatomical and functional regions of the brain.

    Attributes 
    ----------

    ga: Points object, geometry attributs of the region
    sa: Scalar object, scalar attributes of the region.
    """

    def __init__(self, ga=None, sa=None):
        """ init the region with image, geometry, scalar attributes
        
        Parameters 
        ----------
        ga: Points object, geometry attributs of the region
        sa: Scalar object, scalar attributes of the region.
        """
        self.ga = ga
        self.sa = sa

    @property
    def ga(self):
        return self._ga

    @ga.setter
    def ga(self, ga):
        assert isinstance(ga, Points), "ga should be a Points obejct."
        self._ga = ga

    @property
    def sa(self):
        return self._sa

    @sa.setter
    def sa(self, sa):
        assert isinstance(sa, Scalar), "sa should be a Scalar object"
        self._sa = sa

    def merge(self, other, axis=0):
        """ Merge other region into the region.

        Parameters
        ----------
        other: a Region object, another region
        axis: integer, 0 or 1

        Return
        ----------
        self: merged region
        """
        assert isinstance(other, Region), "other should be a Region obejct."
        if axis == 0: # merge both ga and sa in rows
            if hasattr(self, 'ga'):
                self.ga = self.ga.merge(other.ga)
            if hasattr(self, 'sa'):
                self.sa = self.sa.append(other.sa)
        else: # only merge sa in column
            if hasattr(self, 'sa'):
                self.sa = self.sa.join(other.sa)

        return  self

    def intersect(self, other):
        """ Intersect with other region

        Parameters
        ----------
        other: a Region object, another region

        Return
        ----------
        self: the intersected region
        """

        assert isinstance(other, Region), "other is not a Region obejct."
        if hasattr(self, 'ga'):
            self.ga, idx = self.ga.intersect(other.ga)
            if hasattr(self, 'sa'):
                self.sa = self.sa.remove(idx)

        return self

    def exclude(self, other):
        """ Exclude other region from the region.

        Parameters
        ----------
        other: a Region object, another region

        Return
        ----------
        self: the left region
        """

        assert isinstance(other, Region), "other is not a Region obejct."
        if hasattr(self, 'ga'):
            self.ga, idx = self.ga.exclude(other)
            if hasattr(self, 'sa'):
                self.sa = self.sa.remove(idx)

        return  self

    def centralize(self):
        if hasattr(self, 'ga'):
            self.ga = self.ga.get_center()
        if hasattr(self,'sa'):
            self.sa = self.sa.mean()

        return self

    def create_from_scratch(self, gs=None, ss=None, roi=None):
        """ Create region object from raw data which contain the image, geometry and scalar information of the region

        Parameters
        ----------
        gs:  a Image or Surface object, or a pathstr to a surface or image file
            The source for ga
        ss:  a Image or Surface object, or a pathstr to a surface or image file
            The source for sa
        roi:  a Image or Surface object, or a pathstr to a surface or image file
            The mask image, representing spatial location of the region

        Returns
        -------
        self: created region object
        """
        pass
    
    def load(self, filename):
        """ Load region object from serializing persistence file(Jason or pickle file)

        Parameters
        ----------
        filename: str
            File pathstr to a region serializing persistence file
        Returns
        -------
        self: Tract object

        """
        pass

    def save(self, filename):
        """ save region object to a serializing persistence file(Jason or pickle file)

        Parameters
        ----------
        filename: str
            File pathstr to a region serializing persistence file

        Returns
        -------
        bool: sucessful or not
        """
