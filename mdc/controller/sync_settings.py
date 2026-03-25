import os,sys
import json
from mdc.controller.configini_parser import configHandler

#Check input_data.json file exists
if not os.path.isfile(os.path.join(configHandler.input_json)):
    from mdc.controller.errorWindowController import eCtrl,app,engine
    eCtrl.titleText = "File Not Found Error"
    eCtrl.errorText = "The input_data.json file is missing. \nPlease ensure it is present in the Settings folder."
    engine.rootContext().setContextProperty('eCtrl', eCtrl)
    engine.load('mdc/ui/ErrorWindow.qml')
    engine.quit.connect(app.quit)
    sys.exit(app.exec())


#create empty persons.json if not exists
if not os.path.isfile(os.path.join(configHandler.persons_json)):
    with open(os.path.join(configHandler.persons_json), 'w',encoding="utf-8") as f:
        json.dump({"persons": []}, f, indent=2)

#create empty supervisors.json if not exists
if not os.path.isfile(os.path.join(configHandler.supervisors_json)):
    with open(os.path.join(configHandler.supervisors_json),'w',encoding="utf-8") as f:
        json.dump({"supervisors": []}, f, indent=2)

#create empty crs.json if not exists
if not os.path.isfile(os.path.join(configHandler.crs_json)):
    with open(os.path.join(configHandler.crs_json),'w',encoding="utf-8") as f:
        json.dump({"crs_info": []}, f, indent=2)

