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

            def __store(self, container: list, sv = None):
                """Handle store process"""
                isValid, sv = self.model.supervisor.is_valid()
                if isValid:
                    pass

            def pool(self):
                """Store the current supervisor to the pool"""
                self.__store(self.model.pool, sv = None)


            def sequence(self):
                """Store the current supervisor to the sequence"""
                self.__store(self.model.sequence, sv = None)


        return To(self)