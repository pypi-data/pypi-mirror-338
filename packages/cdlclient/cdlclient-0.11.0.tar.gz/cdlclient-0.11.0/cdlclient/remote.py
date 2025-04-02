# Copyright (c) DataLab Platform Developers, BSD 3-Clause license, see LICENSE file.

"""
DataLab remote control
----------------------

This module provides utilities to control DataLab from a Python script (e.g. with
Spyder) or from a Jupyter notebook.

The :class:`SimpleRemoteProxy` class provides the main interface
to DataLab XML-RPC server.
"""

from __future__ import annotations

import configparser as cp
import importlib
import json
import os
import os.path as osp
import sys
import time
import warnings
from io import BytesIO
from xmlrpc.client import Binary, ServerProxy

import guidata.dataset as gds
import numpy as np
from guidata.env import execenv
from guidata.io import JSONReader, JSONWriter
from guidata.userconfig import get_config_basedir

import cdlclient
from cdlclient import simplemodel
from cdlclient.baseproxy import SimpleBaseProxy
from cdlclient.simplemodel import ImageObj, SignalObj

# pylint: disable=invalid-name  # Allows short reference names like x, y, ...
# pylint: disable=duplicate-code


XMLRPCPORT_ENV = "CDL_XMLRPCPORT"


def get_xmlrpcport_from_env() -> int | None:
    """Get XML-RPC port number from environment variable."""
    try:
        return int(os.environ.get(XMLRPCPORT_ENV))
    except (TypeError, ValueError):
        return None


def array_to_rpcbinary(data: np.ndarray) -> Binary:
    """Convert NumPy array to XML-RPC Binary object, with shape and dtype.

    The array is converted to a binary string using NumPy's native binary
    format.

    Args:
        data: NumPy array to convert

    Returns:
        XML-RPC Binary object
    """
    dbytes = BytesIO()
    np.save(dbytes, data, allow_pickle=False)
    return Binary(dbytes.getvalue())


def rpcbinary_to_array(binary: Binary) -> np.ndarray:
    """Convert XML-RPC binary to NumPy array.

    Args:
        binary: XML-RPC Binary object

    Returns:
        NumPy array
    """
    dbytes = BytesIO(binary.data)
    return np.load(dbytes, allow_pickle=False)


def dataset_to_json(param: gds.DataSet) -> list[str]:
    """Convert guidata DataSet to JSON data.

    The JSON data is a list of three elements:

    - The first element is the module name of the DataSet class
    - The second element is the class name of the DataSet class
    - The third element is the JSON data of the DataSet instance

    Args:
        param: guidata DataSet to convert

    Returns:
        JSON data
    """
    writer = JSONWriter()
    param.serialize(writer)
    param_json = writer.get_json()
    klass = param.__class__
    return [klass.__module__, klass.__name__, param_json]


def json_to_dataset(param_data: list[str]) -> gds.DataSet:
    """Convert JSON data to guidata DataSet.

    Args:
        param_data: JSON data

    Returns:
        guidata DataSet
    """
    param_module, param_clsname, param_json = param_data
    # Replacing DataLab's model by DataLab Simple Client's model:
    param_module = param_module.replace("cdl.core.model.signal", simplemodel.__name__)
    param_module = param_module.replace("cdl.core.model.image", simplemodel.__name__)
    mod = importlib.__import__(param_module, fromlist=[param_clsname])
    klass = getattr(mod, param_clsname)
    param = klass()
    reader = JSONReader(param_json)
    param.deserialize(reader)
    return param


# === Python 2.7 client side:
#
# # See DataLab's doc/remotecontrol_py27.py for an almost complete Python 2.7
# # implementation of SimpleRemoteProxy class
#
# import io
# from xmlrpclib import ServerProxy, Binary
# import numpy as np
# def array_to_binary(data):
#     """Convert NumPy array to XML-RPC Binary object, with shape and dtype"""
#     dbytes = io.BytesIO()
#     np.save(dbytes, data, allow_pickle=False)
#     return Binary(dbytes.getvalue())
# s = ServerProxy("http://127.0.0.1:8000")
# data = np.array([[3, 4, 5], [7, 8, 0]], dtype=np.uint16)
# s.add_image("toto", array_to_binary(data))


def get_cdl_xmlrpc_port():
    """Return DataLab current XML-RPC port"""
    if sys.platform == "win32" and "HOME" in os.environ:
        os.environ.pop("HOME")  # Avoid getting old WinPython settings dir
    fname = osp.join(get_config_basedir(), ".DataLab", "DataLab.ini")
    ini = cp.ConfigParser()
    ini.read(fname)
    try:
        return ini.get("main", "rpc_server_port")
    except (cp.NoSectionError, cp.NoOptionError) as exc:
        raise ConnectionRefusedError("DataLab has not yet been executed") from exc


def items_to_json(items: list) -> str | None:
    """Convert plot items to JSON string.

    Args:
        items (list): list of plot items

    Returns:
        str: JSON string or None if items is empty
    """
    from plotpy.io import save_items  # pylint: disable=import-outside-toplevel

    if items:
        writer = JSONWriter(None)
        save_items(writer, items)
        return writer.get_json(indent=4)
    return None


def json_to_items(json_str: str | None) -> list:
    """Convert JSON string to plot items.

    Args:
        json_str (str): JSON string or None

    Returns:
        list: list of plot items
    """
    from plotpy.io import load_items  # pylint: disable=import-outside-toplevel

    items = []
    if json_str:
        try:
            for item in load_items(JSONReader(json_str)):
                items.append(item)
        except json.decoder.JSONDecodeError:
            pass
    return items


def is_version_at_least(version1: str, version2: str) -> bool:
    """
    Compare two version strings to check if the first version is at least
    equal to the second.

    Args:
        version1 (str): The first version string.
        version2 (str): The second version string.

    Returns:
        bool: True if version1 is greater than or equal to version2, False otherwise.

    .. note::

        Development, alpha, beta, and rc versions are considered to be equal
        to the corresponding release version.
    """
    # Split the version strings into parts
    parts1 = [part.strip() for part in version1.split(".")]
    parts2 = [part.strip() for part in version2.split(".")]

    for part1, part2 in zip(parts1, parts2):
        if part1.isdigit() and part2.isdigit():
            if int(part1) > int(part2):
                return True
            elif int(part1) < int(part2):
                return False
        elif part1 > part2:
            return True
        elif part1 < part2:
            return False

    return len(parts1) >= len(parts2)


class SimpleRemoteProxy(SimpleBaseProxy):
    """Object representing a proxy/client to DataLab XML-RPC server.
    This object is used to call DataLab functions from a Python script.

    This is a subset of DataLab's `RemoteClient` class, with only the methods
    that do not require DataLab object model to be implemented.

    Args:
        autoconnect: If True, automatically connect to DataLab XML-RPC server.
         Defaults to True.

    Raises:
        ConnectionRefusedError: DataLab is currently not running

    Examples:
        Here is a simple example of how to use SimpleRemoteProxy in a Python script
        or in a Jupyter notebook:

        >>> from cdlclient import SimpleRemoteProxy
        >>> proxy = SimpleRemoteProxy()  # autoconnect is on by default
        Connecting to DataLab XML-RPC server...OK (port: 28867)
        >>> proxy.get_version()
        '1.0.0'
        >>> proxy.add_signal("toto", np.array([1., 2., 3.]), np.array([4., 5., -1.]))
        True
        >>> proxy.get_object_titles()
        ['toto']
        >>> proxy["toto"]
        <cdlclient.model.signal.SignalObj at 0x7f7f1c0b4a90>
        >>> "toto" in proxy
        True
        >>> proxy[1]
        <cdlclient.model.signal.SignalObj at 0x7f7f1c0b4a90>
        >>> proxy[1].data
        array([1., 2., 3.])
    """

    def __init__(self, autoconnect: bool = True) -> None:
        super().__init__()
        self.port: str = None
        self._cdl: ServerProxy
        if autoconnect:
            self.connect()

    def __connect_to_server(self, port: str | None = None) -> None:
        """Connect to DataLab XML-RPC server.

        Args:
            port (str | None): XML-RPC port to connect to. If not specified,
                the port is automatically retrieved from DataLab configuration.

        Raises:
            ConnectionRefusedError: DataLab is currently not running
        """
        if port is None:
            port = get_xmlrpcport_from_env()
            if port is None:
                port = get_cdl_xmlrpc_port()
        self.port = port
        self._cdl = ServerProxy(f"http://127.0.0.1:{port}", allow_none=True)
        try:
            version = self.get_version()
        except ConnectionRefusedError as exc:
            raise ConnectionRefusedError("DataLab is currently not running") from exc
        # If DataLab version is not compatible with this client, show a warning using
        # standard `warnings` module:
        if not is_version_at_least(version, cdlclient.__required_server_version__):
            warnings.warn(
                f"DataLab version {version} is not fully compatible with "
                f"DataLab Simple Client version {cdlclient.__version__}.\n"
                f"Please upgrade DataLab to {cdlclient.__required_server_version__} "
                f"or higher."
            )

    def connect(
        self,
        port: str | None = None,
        timeout: float | None = None,
        retries: int | None = None,
    ) -> None:
        """Try to connect to DataLab XML-RPC server.

        Args:
            port (str | None): XML-RPC port to connect to. If not specified,
                the port is automatically retrieved from DataLab configuration.
            timeout (float | None): Timeout in seconds. Defaults to 5.0.
            retries (int | None): Number of retries. Defaults to 10.

        Raises:
            ConnectionRefusedError: Unable to connect to DataLab
            ValueError: Invalid timeout (must be >= 0.0)
            ValueError: Invalid number of retries (must be >= 1)
        """
        timeout = 5.0 if timeout is None else timeout
        retries = 10 if retries is None else retries
        if timeout < 0.0:
            raise ValueError("timeout must be >= 0.0")
        if retries < 1:
            raise ValueError("retries must be >= 1")
        execenv.print("Connecting to DataLab XML-RPC server...", end="")
        for _index in range(retries):
            try:
                self.__connect_to_server(port=port)
                break
            except ConnectionRefusedError:
                time.sleep(timeout / retries)
        else:
            execenv.print("KO")
            raise ConnectionRefusedError("Unable to connect to DataLab")
        execenv.print(f"OK (port: {self.port})")

    def disconnect(self) -> None:
        """Disconnect from DataLab XML-RPC server."""
        # This is not mandatory with XML-RPC, but if we change protocol in the
        # future, it may be useful to have a disconnect method.
        self._cdl = None

    def is_connected(self) -> bool:
        """Return True if connected to DataLab XML-RPC server."""
        if self._cdl is not None:
            try:
                self.get_version()
                return True
            except ConnectionRefusedError:
                self._cdl = None
        return False

    def get_method_list(self) -> list[str]:
        """Return list of available methods."""
        return self._cdl.system.listMethods()

    # === Following methods should match the register functions in XML-RPC server

    def add_signal(
        self,
        title: str,
        xdata: np.ndarray,
        ydata: np.ndarray,
        xunit: str | None = None,
        yunit: str | None = None,
        xlabel: str | None = None,
        ylabel: str | None = None,
    ) -> bool:  # pylint: disable=too-many-arguments
        """Add signal data to DataLab.

        Args:
            title (str): Signal title
            xdata (numpy.ndarray): X data
            ydata (numpy.ndarray): Y data
            xunit (str | None): X unit. Defaults to None.
            yunit (str | None): Y unit. Defaults to None.
            xlabel (str | None): X label. Defaults to None.
            ylabel (str | None): Y label. Defaults to None.

        Returns:
            bool: True if signal was added successfully, False otherwise

        Raises:
            ValueError: Invalid xdata dtype
            ValueError: Invalid ydata dtype
        """
        xbinary = array_to_rpcbinary(xdata)
        ybinary = array_to_rpcbinary(ydata)
        return self._cdl.add_signal(
            title, xbinary, ybinary, xunit, yunit, xlabel, ylabel
        )

    # pylint: disable=too-many-arguments
    def add_image(
        self,
        title: str,
        data: np.ndarray,
        xunit: str | None = None,
        yunit: str | None = None,
        zunit: str | None = None,
        xlabel: str | None = None,
        ylabel: str | None = None,
        zlabel: str | None = None,
    ) -> bool:
        """Add image data to DataLab.

        Args:
            title (str): Image title
            data (numpy.ndarray): Image data
            xunit (str | None): X unit. Defaults to None.
            yunit (str | None): Y unit. Defaults to None.
            zunit (str | None): Z unit. Defaults to None.
            xlabel (str | None): X label. Defaults to None.
            ylabel (str | None): Y label. Defaults to None.
            zlabel (str | None): Z label. Defaults to None.

        Returns:
            bool: True if image was added successfully, False otherwise

        Raises:
            ValueError: Invalid data dtype
        """
        zbinary = array_to_rpcbinary(data)
        return self._cdl.add_image(
            title, zbinary, xunit, yunit, zunit, xlabel, ylabel, zlabel
        )

    def calc(self, name: str, param: gds.DataSet | None = None) -> None:
        """Call compute function ``name`` in current panel's processor.

        Args:
            name: Compute function name
            param: Compute function parameter. Defaults to None.

        Raises:
            ValueError: unknown function
        """
        if param is None:
            return self._cdl.calc(name)
        return self._cdl.calc(name, dataset_to_json(param))

    def get_object(
        self,
        nb_id_title: int | str | None = None,
        panel: str | None = None,
    ) -> SignalObj | ImageObj:
        """Get object (signal/image) from index.

        Args:
            nb_id_title: Object number, or object id, or object title.
             Defaults to None (current object).
            panel: Panel name. Defaults to None (current panel).

        Returns:
            Object

        Raises:
            KeyError: if object not found
        """
        param_data = self._cdl.get_object(nb_id_title, panel)
        if param_data is None:
            return None
        return json_to_dataset(param_data)

    def get_object_shapes(
        self,
        nb_id_title: int | str | None = None,
        panel: str | None = None,
    ) -> list:
        """Get plot item shapes associated to object (signal/image).

        Args:
            nb_id_title: Object number, or object id, or object title.
             Defaults to None (current object).
            panel: Panel name. Defaults to None (current panel).

        Returns:
            List of plot item shapes
        """
        items_json = self._cdl.get_object_shapes(nb_id_title, panel)
        return json_to_items(items_json)

    def add_annotations_from_items(
        self, items: list, refresh_plot: bool = True, panel: str | None = None
    ) -> None:
        """Add object annotations (annotation plot items).

        .. note:: This method is only available if PlotPy is installed.

        Args:
            items (list): annotation plot items
            refresh_plot (bool | None): refresh plot. Defaults to True.
            panel (str | None): panel name (valid values: "signal", "image").
                If None, current panel is used.
        """
        try:
            items_json = items_to_json(items)
        except ImportError as exc:
            raise ImportError("PlotPy is not installed") from exc
        if items_json is not None:
            self._cdl.add_annotations_from_items(items_json, refresh_plot, panel)
