import os,sys
import json
from PySide6.QtCore import QSettings

_settings = QSettings('./Settings/config.ini', QSettings.IniFormat)

input_json = _settings.value('settings_files/inputjson')
persons_json = _settings.value('settings_files/personsjson')
supervisors_json = _settings.value('settings_files/supervisorsjson')
crs_json = _settings.value('settings_files/crsjson')
is_supervisor_present = _settings.value('supervisor/is_testsupervisor_present', type=bool)
