"""
dialog_state.py

Global constants, strings and dictionaries used to
maintain the state of the various threaded dialogs.

Created on 16 Aug 2023

:author: semuadmin
:copyright: 2020 SEMU Consulting
:license: BSD 3-Clause
"""

from pygpsclient.about_dialog import AboutDialog
from pygpsclient.globals import CFG, CLASS, THD
from pygpsclient.gpx_dialog import GPXViewerDialog
from pygpsclient.importmap_dialog import ImportMapDialog
from pygpsclient.nmea_config_dialog import NMEAConfigDialog
from pygpsclient.ntrip_client_dialog import NTRIPConfigDialog
from pygpsclient.spartn_dialog import SPARTNConfigDialog
from pygpsclient.strings import (
    DLG,
    DLGTABOUT,
    DLGTGPX,
    DLGTIMPORTMAP,
    DLGTNMEA,
    DLGTNTRIP,
    DLGTSPARTN,
    DLGTUBX,
)
from pygpsclient.ubx_config_dialog import UBXConfigDialog

dialog_state = {
    DLGTABOUT: {CLASS: AboutDialog, THD: None, DLG: None, CFG: False},
    DLGTUBX: {CLASS: UBXConfigDialog, THD: None, DLG: None, CFG: True},
    DLGTNMEA: {CLASS: NMEAConfigDialog, THD: None, DLG: None, CFG: True},
    DLGTNTRIP: {CLASS: NTRIPConfigDialog, THD: None, DLG: None, CFG: True},
    DLGTSPARTN: {CLASS: SPARTNConfigDialog, THD: None, DLG: None, CFG: True},
    DLGTGPX: {CLASS: GPXViewerDialog, THD: None, DLG: None, CFG: True},
    DLGTIMPORTMAP: {CLASS: ImportMapDialog, THD: None, DLG: None, CFG: True},
    # add any new dialogs here
}
