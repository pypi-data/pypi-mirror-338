"""
module for handling a `nxsample <https://manual.nexusformat.org/classes/base_classes/NXsample.html>`_
"""

from __future__ import annotations

import logging
from functools import partial
from operator import is_not
from typing import Iterable

import numpy
from silx.utils.proxy import docstring
from nxtomo.paths.nxtomo import get_paths as get_nexus_paths
from pyunitsystem.metricsystem import MetricSystem

from nxtomo.nxobject.nxobject import ElementWithUnit, NXobject
from nxtomo.nxobject.nxtransformations import NXtransformations
from nxtomo.utils import cast_and_check_array_1D, get_data, get_data_and_unit

_logger = logging.getLogger(__name__)

__all__ = [
    "NXsample",
]


class NXsample(NXobject):
    def __init__(self, node_name="sample", parent: NXobject | None = None) -> None:
        """
        representation of `nexus NXsample <https://manual.nexusformat.org/classes/base_classes/NXsample.html>`_.
        A monitor of incident beam data.

        :param node_name: name of the detector in the hierarchy
        :param parent: parent in the nexus hierarchy
        """
        super().__init__(node_name=node_name, parent=parent)
        self._set_freeze(False)
        self._name = None
        self._rotation_angle = None
        self.rocking = None
        self.n_steps_rocking = None
        self.n_steps_rotation = None
        self._x_translation = ElementWithUnit(default_unit=MetricSystem.METER)
        self._y_translation = ElementWithUnit(default_unit=MetricSystem.METER)
        self._z_translation = ElementWithUnit(default_unit=MetricSystem.METER)
        self._transformations = tuple()
        self._set_freeze(True)

    @property
    def name(self) -> str | None:
        """sample name"""
        return self._name

    @name.setter
    def name(self, name: str | None) -> None:
        if not isinstance(name, (type(None), str)):
            raise TypeError(f"name is expected to be None or str not {type(name)}")
        self._name = name

    @property
    def rotation_angle(self) -> numpy.ndarray | None:
        """sample rotation angle. One per frame"""
        return self._rotation_angle

    @rotation_angle.setter
    def rotation_angle(self, rotation_angle: Iterable | None):
        self._rotation_angle = cast_and_check_array_1D(rotation_angle, "rotation_angle")

    @property
    def x_translation(self) -> numpy.ndarray | None:
        """sample translation along x. See `modelling at esrf <https://tomo.gitlab-pages.esrf.fr/ebs-tomo/master/modelization.html>`_ for more information"""
        return self._x_translation

    @x_translation.setter
    def x_translation(self, x_translation: Iterable | None):
        self._x_translation.value = cast_and_check_array_1D(
            x_translation, "x_translation"
        )

    @property
    def y_translation(self) -> numpy.ndarray | None:
        """sample translation along y. See `modelling at esrf <https://tomo.gitlab-pages.esrf.fr/ebs-tomo/master/modelization.html>`_ for more information"""
        return self._y_translation

    @y_translation.setter
    def y_translation(self, y_translation: Iterable | None):
        self._y_translation.value = cast_and_check_array_1D(
            y_translation, "y_translation"
        )

    @property
    def z_translation(self) -> numpy.ndarray | None:
        """sample translation along z. See `modelling at esrf <https://tomo.gitlab-pages.esrf.fr/ebs-tomo/master/modelization.html>`_ for more information"""
        return self._z_translation

    @z_translation.setter
    def z_translation(self, z_translation: Iterable | None):
        self._z_translation.value = cast_and_check_array_1D(
            z_translation, "z_translation"
        )

    @property
    def transformations(self) -> tuple[NXtransformations]:
        """detector transformations as `NXtransformations <https://manual.nexusformat.org/classes/base_classes/NXtransformations.html>`_"""
        return self._transformations

    @transformations.setter
    def transformations(self, transformations: tuple[NXtransformations]):
        if not isinstance(transformations, tuple):
            raise TypeError
        for transformation in transformations:
            if not isinstance(transformation, NXtransformations):
                raise TypeError

    @docstring(NXobject)
    def to_nx_dict(
        self,
        nexus_path_version: float | None = None,
        data_path: str | None = None,
    ) -> dict:
        nexus_paths = get_nexus_paths(nexus_path_version)
        nexus_sample_paths = nexus_paths.nx_sample_paths

        nx_dict = {}

        if self.name is not None:
            path_name = f"{self.path}/{nexus_sample_paths.NAME}"
            nx_dict[path_name] = self.name
        if self.rotation_angle is not None:
            path_rotation_angle = f"{self.path}/{nexus_sample_paths.ROTATION_ANGLE}"
            nx_dict[path_rotation_angle] = self.rotation_angle
            nx_dict["@".join([path_rotation_angle, "units"])] = "degree"
        if self.rocking is not None:
            path_rocking = f"{self.path}/{nexus_sample_paths.ROCKING}"
            nx_dict[path_rocking] = self.rocking
        if self.n_steps_rocking is not None:
            path_n_steps_rocking = f"{self.path}/{nexus_sample_paths.N_STEPS_ROCKING}"
            nx_dict[path_n_steps_rocking] = self.n_steps_rocking
        if self.n_steps_rotation is not None:
            path_n_steps_rotation = f"{self.path}/{nexus_sample_paths.N_STEPS_ROTATION}"
            nx_dict[path_n_steps_rotation] = self.n_steps_rotation
        if self.x_translation.value is not None:
            path_x_translation = f"{self.path}/{nexus_sample_paths.X_TRANSLATION}"
            nx_dict[path_x_translation] = self.x_translation.value
            nx_dict["@".join([path_x_translation, "units"])] = str(
                self.x_translation.unit
            )
        if self.y_translation.value is not None:
            path_y_translation = f"{self.path}/{nexus_sample_paths.Y_TRANSLATION}"
            nx_dict[path_y_translation] = self.y_translation.value
            nx_dict["@".join([path_y_translation, "units"])] = str(
                self.y_translation.unit
            )
        if self.z_translation.value is not None:
            path_z_translation = f"{self.path}/{nexus_sample_paths.Z_TRANSLATION}"
            nx_dict[path_z_translation] = self.z_translation.value
            nx_dict["@".join([path_z_translation, "units"])] = str(
                self.z_translation.unit
            )

        if nx_dict != {}:
            nx_dict[f"{self.path}@NX_class"] = "NXsample"
        return nx_dict

    def _load(self, file_path: str, data_path: str, nexus_version: float) -> NXobject:
        """
        Create and load an NXsample from data on disk
        """
        nexus_paths = get_nexus_paths(nexus_version)
        nexus_sample_paths = nexus_paths.nx_sample_paths

        self.name = get_data(
            file_path=file_path,
            data_path="/".join([data_path, nexus_sample_paths.NAME]),
        )
        self.rotation_angle, angle_unit = get_data_and_unit(
            file_path=file_path,
            data_path="/".join([data_path, nexus_sample_paths.ROTATION_ANGLE]),
            default_unit="degree",
        )
        if angle_unit == "degree":
            pass
        elif isinstance(angle_unit, str) and angle_unit.lower() in ("rad", "radian"):
            self.rotation_angle = numpy.rad2deg(self.rotation_angle)
        elif angle_unit is not None:
            raise ValueError(f"rotation angle unit not recognized: {angle_unit}")

        self.x_translation, self.x_translation.unit = get_data_and_unit(
            file_path=file_path,
            data_path="/".join([data_path, nexus_sample_paths.X_TRANSLATION]),
            default_unit=MetricSystem.METER,
        )
        self.y_translation, self.y_translation.unit = get_data_and_unit(
            file_path=file_path,
            data_path="/".join([data_path, nexus_sample_paths.Y_TRANSLATION]),
            default_unit=MetricSystem.METER,
        )
        self.z_translation, self.z_translation.unit = get_data_and_unit(
            file_path=file_path,
            data_path="/".join([data_path, nexus_sample_paths.Z_TRANSLATION]),
            default_unit=MetricSystem.METER,
        )

    @staticmethod
    @docstring(NXobject)
    def concatenate(nx_objects: tuple, node_name="sample"):
        nx_objects = tuple(filter(partial(is_not, None), nx_objects))
        # filter None obj
        if len(nx_objects) == 0:
            return None
        # warning: later we make the assumption that nx_objects contains at least one element
        for nx_obj in nx_objects:
            if not isinstance(nx_obj, NXsample):
                raise TypeError("Cannot concatenate non NXsample object")

        nx_sample = NXsample(node_name)
        _logger.info(f"sample name {nx_objects[0].name} will be picked")
        nx_sample.name = nx_objects[0].name

        rotation_angles = [
            nx_obj.rotation_angle
            for nx_obj in nx_objects
            if nx_obj.rotation_angle is not None
        ]
        if len(rotation_angles) > 0:
            nx_sample.rotation_angle = numpy.concatenate(rotation_angles)

        x_translations = [
            nx_obj.x_translation.value * nx_obj.x_translation.unit.value
            for nx_obj in nx_objects
            if (
                nx_obj.x_translation is not None
                and nx_obj.x_translation.value is not None
            )
        ]
        if len(x_translations) > 0:
            nx_sample.x_translation = numpy.concatenate(x_translations)

        y_translations = [
            nx_obj.y_translation.value * nx_obj.y_translation.unit.value
            for nx_obj in nx_objects
            if (
                nx_obj.y_translation is not None
                and nx_obj.y_translation.value is not None
            )
        ]
        if len(y_translations) > 0:
            nx_sample.y_translation = numpy.concatenate(y_translations)

        z_translations = [
            nx_obj.z_translation.value * nx_obj.z_translation.unit.value
            for nx_obj in nx_objects
            if (
                nx_obj.z_translation is not None
                and nx_obj.z_translation.value is not None
            )
        ]
        if len(z_translations) > 0:
            nx_sample.z_translation = numpy.concatenate(z_translations)

        rocking_list = list(
            filter(
                partial(is_not, None),
                [nx_obj.rocking for nx_obj in nx_objects],
            )
        )
        if len(rocking_list) > 0:
            nx_sample.rocking = numpy.concatenate(rocking_list)

        return nx_sample
