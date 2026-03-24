import json
import datetime
import copy
from typing  import Optional, List
from dataclasses import dataclass, field, asdict

from data_model.scenario import Scenario,ProcessStep,Specification

class ScenarioModel():
    pool = []
    sequence = []

    @dataclass(frozen=False)
    class Scenario():
        id: str = None
        creation_timestamp: datetime.datetime = None
        name: str
        primary_usecase: ProcessStep = None
        description: str = None
        tags: Optional[List[str]] = None
        specification: Optional[List[Specification]] = None
        facial_landmarks_mandatory: bool = False

        @property
        def as_dict(self) -> dict:
            """Get Comment as dictionary format"""

            return asdict(self)

        @property
        def as_json(self) -> json:
            """Get Comment as json format"""

            return json.dump(self.as_dict)

        def isValid(self) -> tuple[bool, Scenario | None]:
            """Validate comment"""

            try:
                return True,ScenarioModel.Scenario(**Scenario(**self.as_dict).dict())
            except Exception as e:
                print("Validation failed")
                return False,None

    def __init__(self):
        self.reset()

    def reset(self):
        self.scenario = self.Scenario()

    @property
    def store_to(self):
        class To():
            def __init__(self, model: ScenarioModel):
                self.model = model

            def __store(self, container: list, data: ScenarioModel.Scenario | dict | None):
                match data:
                    case None:
                        isValid,_ = self.model.scenario.isValid()
                        if isValid:
                            for idx,scenario in enumerate(container):
                                if scenario == self.model.scenario:
                                    container[idx] = copy.deepcopy(self.model.scenario)
                                else:
                                    container.append(copy.deepcopy(self.model.scenario))
                    case ScenarioModel.Scenario: pass
                    case dict(): pass

            def pool(self, data: ScenarioModel.Scenario | dict | None = None):
                return self.__store(self.model.pool, data)

            def sequence(self, data: ScenarioModel.Scenario | dict | None = None):
                return self.__store(self.model.sequence, data)

        return To(self)

if __name__=="__main__":
    scn = ScenarioModel()
    scn.scenario.id = "test_id"
    scn.scenario.creation_timestamp = "2023-04-18T15:01:47.000000"
    scn.scenario.name = "test_name"
    scn.scenario.primary_usecase = ProcessStep.FUNCTIONAL_TEST
    scn.scenario.description = "descr"
    scn.scenario.facial_landmarks_mandatory = True

    assert scn.scenario.isValid()[0] == True
