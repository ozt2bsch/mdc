import os,sys
import json
import configparser

from data_model.dbgui_input import DbGuiInput,PersonListInput,SupervisorsListInput,CRSInfoListInput


class ConfigIniParser():
    def __init__(self,_file):
        self.iniFile = _file
        self.cfg = configparser.ConfigParser()
        self.cfg.read(self.iniFile)

        #sections
        section_settings_files = 'settings_files'
        section_supervisor = 'supervisor'

        #settings_files
        self.input_json = self.cfg.get(section_settings_files,'inputjson')
        self.persons_json = self.cfg.get(section_settings_files,'personsjson')
        self.supervisors_json = self.cfg.get(section_settings_files,'supervisorsjson')
        self.crs_json = self.cfg.get(section_settings_files,'crsjson')

        #supervisor
        self.is_supervisor_present = self.cfg.getboolean(section_supervisor,'is_testsupervisor_present')

configHandler = ConfigIniParser('./Settings/config.ini')
