import os,sys
import json
from mdc.controller.configini_parser import configHandler
from mdc.model.scenarioModel import ScenarioModel
from data_model.dbgui_input import DbGuiInput,PersonListInput,SupervisorsListInput,CRSInfoListInput
from mdc.model.supervisorModel import SupervisorModel

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

#parse input_data.json
with open(configHandler.input_json,'r',encoding="utf-8") as f:
    oDBGuiInput = DbGuiInput(**json.load(f))

#fetch and store scenarios
print("parsing scenarios...")
print(" ",len(oDBGuiInput.scenarios) if oDBGuiInput.scenarios else 0, "Scenario(s) found in input_data.json")
if oDBGuiInput.scenarios:
    for scn in oDBGuiInput.scenarios:
        ScenarioModel().store_to.pool(ScenarioModel.Scenario(**scn.dict()))

#fetch and store supervisors
print("parsing supervisors...")
print(" ",len(oDBGuiInput.supervisors) if oDBGuiInput.supervisors else 0, "Supervisor(s) found in input_data.json")
if oDBGuiInput.supervisors:
    for sv in oDBGuiInput.supervisors:
        SupervisorModel().store_to.pool(SupervisorModel.Supervisor(**sv.dict()))

pass