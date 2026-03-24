import json
import copy
import datetime
from dataclasses import dataclass, field, asdict
from typing import Optional, List

from data_model.scenario import Scenario,ProcessStep,Specification

class ScenarioModel():
    pool = []
    sequence = []

    @dataclass(frozen=False)
    class Scenario():
        id: str = None
        creation_timestamp: datetime.datetime = None
        name: str = None
        primary_usecase: ProcessStep = None
        description: str = None
        tags: Optional[List[str]] = None
        specification: Optional[List[Specification]] = None
        facial_landmarks_mandatory: bool = False

        @property
        def check_fillout(self) -> bool:
            """Check if all mandatory fields are filled out"""
            _id: bool = True if self.id not in [None, ""] else False
            _timestamp: bool = True if self.creation_timestamp not in [None, ""] else False
            _name: bool = True if self.name not in [None, ""] else False
            _primary_usecase: bool = True if self.primary_usecase in list(ProcessStep) else False
            _description: bool = True if self.description not in [None, ""] else False
            _facial_landmark: bool = True if self.facial_landmarks_mandatory in [True, False] else False

            match _id:
                case False:
                    print("id is not filled out")
            match _timestamp:
                case False:
                    print("creation_timestamp is not filled out")
            match _name:
                case False:
                    print("name is not filled out")
            match _primary_usecase:
                case False:
                    print("primary_usecase is not filled out")
            match _description:
                case False:
                    print("description is not filled out")
            match _facial_landmark:
                case False:
                    print("facial_landmarks_mandatory is not filled out")

            return all([_id, _timestamp, _name, _primary_usecase, _description, _facial_landmark])

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

            def __something(self, container: list, data: ScenarioModel.Scenario | dict | None) -> bool:
                isValid,_ = data.isValid()
                if isValid:
                    if not container:
                        container.append(copy.deepcopy(data))
                        return True
                    for idx,scn in enumerate(container):
                        if scn.id == data.id:
                            container[idx] = copy.deepcopy(data)
                            return True
                    container.append(copy.deepcopy(data))
                    return True
                else:
                    print("Scenario is not valid. Please check the scenario data.")
                    return False

            def __parse(self, container: list, data: ScenarioModel.Scenario | dict | None):
                match data:
                    case None:
                        return self.__something(container, self.model.scenario)
                    case ScenarioModel.Scenario():
                        return self.__something(container, data)
                    case dict():
                        try:
                            scenario = ScenarioModel.Scenario(**data)
                            return self.__something(container, scenario)
                        except Exception as e:
                            print("Data is not in correct format. Please check.")
                            return False

            def pool(self, data: ScenarioModel.Scenario | dict | None = None):
                return self.__parse(self.model.pool, data)

            def sequence(self, data: ScenarioModel.Scenario | dict | None = None):
                return self.__parse(self.model.sequence, data)

        return To(self)

