from mdc.controller.appEngine import engine
from PySide6.QtCore import QObject, Signal, Slot, Property
from mdc.model.supervisorModel import SupervisorModel
from data_model.common import CampaignSuppliers

class SupervisorController(QObject):
    #Properties
    svCompanyChanged = Signal()
    svNameChanged = Signal()
    #signals
    load_addNew_supervisor_screen = Signal()
    pop_screen = Signal()

    def __init__(self):
        super().__init__()
        self.supervisor_model = SupervisorModel()
        if not self.supervisor_model.pool:
            self.load_addNew_supervisor_screen.emit()


    @Slot(str)
    def initialize(self, screen_name):
        match screen_name:
            case "selectSupervisor":
                self.supervisor_model.reset()
                self.update_fields()
                if len(self.supervisor_model.pool) == 1:
                    self.supervisor_model.load_supervisor()
                    self.update_fields()

            case "addNewSupervisor":
                self.supervisor_model.reset()
                self.update_fields()

    def update_fields(self):
        self.svCompanyChanged.emit()
        self.svNameChanged.emit()

    @Property(list, notify=svNameChanged)
    def lstSupervisors(self):
        if not self.supervisor_model.pool:
            return []
        return [{"name": sv.name, "company": sv.company} for sv in self.supervisor_model.pool]

    @Property(list, constant=True)
    def lstCampaignSuppliers(self):
        return [supplier.value for supplier in CampaignSuppliers]

    @Property(str, notify=svCompanyChanged)
    def sv_company(self):
        return self.supervisor_model.supervisor.company if self.supervisor_model.supervisor else None

    @sv_company.setter
    def sv_company(self, company_name):
        self.supervisor_model.supervisor.company = CampaignSuppliers(company_name)
        self.svCompanyChanged.emit()

    @Property(str, notify=svNameChanged)
    def sv_name(self):
        return self.supervisor_model.supervisor.name if self.supervisor_model.supervisor else None

    @sv_name.setter
    def sv_name(self, name):
        self.supervisor_model.supervisor.name = name
        self.svNameChanged.emit()

    @Slot()
    def select_supervisor(self):
        if self.supervisor_model.store_to.sequence():
            print(f"Supervisor '{self.sv_name}-{self.sv_company}' selected successfully.")
        else:
            print(f"Failed to load supervisor '{self.sv_name}-{self.sv_company}'. Please check the supervisor data.")

    @Slot(list)
    def load_supervisor(self, supervisor_data):
        if self.supervisor_model.load_supervisor(supervisor_data[0], CampaignSuppliers(supervisor_data[1])):
            self.update_fields()

    @Slot()
    def add_new_supervisor(self):
        if self.supervisor_model.store_to.pool():
            print(f"Supervisor '{self.supervisor_model.supervisor.name}' added to pool successfully.")
            self.pop_screen.emit()
        else:
            print(f"Failed to add supervisor '{self.supervisor_model.supervisor.name}' to pool.")

supervisor_controller = SupervisorController()
engine.rootContext().setContextProperty('svCtrl', supervisor_controller)