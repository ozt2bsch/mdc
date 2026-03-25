import copy
from typing import Optional
from dataclasses import dataclass,field

from data_model.common import Supervisor, CampaignSuppliers

class SupervisorModel:
    pool = []
    sequence = []

    @dataclass(frozen=False)
    class Supervisor:
        name: str = None
        company: CampaignSuppliers = None

        def check_fillout(self) -> bool:
            if self.name is None or self.company is None:
                return False
            return True

        def is_valid(self) -> bool:
            try:
                return True,SupervisorModel.Supervisor(**Supervisor(**self.__dict__).dict())
            except Exception as e:
                print(f"Error validating Supervisor: {e}")
                return False,None

    def __init__(self):
        self.reset()

    def reset(self):
        self.supervisor =self.Supervisor()

    @property
    def store_to(self):
        class To():
            def __init__(self, svModel: SupervisorModel):
                self.model = svModel

            def __store(self, container: list, data: SupervisorModel.Supervisor):
                """Handle store process"""
                isValid,_ = data.is_valid()
                if isValid:
                    if not container:
                        container.append(copy.deepcopy(data))
                        print(f"Supervisor '{data.name}' added to container")
                        return True
                    for idx,sv in enumerate(container):
                        if sv.name == data.name:
                            container[idx] = copy.deepcopy(data)
                            print(f"Supervisor '{data.name}' updated in container")
                            return True
                    container.append(copy.deepcopy(data))
                    print(f"Supervisor '{data.name}' added to container")
                    return True
                print(f"Supervisor '{data.name}' is not valid. Please check the supervisor data.")
                return False

            def __parse(self, container: list, data: SupervisorModel.Supervisor | dict | None = None):
                match data:
                    case None:
                        return self.__store(container, self.model.supervisor)
                    case SupervisorModel.Supervisor():
                        return self.__store(container, data)
                    case dict():
                        try:
                            sv = SupervisorModel.Supervisor(**data)
                            return self.__store(container, sv)
                        except Exception as e:
                            print(f"Data is not in correct format. Please check. \nError: {e}")
                            return False

            def pool(self,data: SupervisorModel.Supervisor | dict | None = None):
                """Store the current supervisor to the pool"""
                return self.__parse(self.model.pool, data)


            def sequence(self,data: SupervisorModel.Supervisor | dict | None = None):
                """Store the current supervisor to the sequence"""
                return self.__parse(self.model.sequence, data)


        return To(self)