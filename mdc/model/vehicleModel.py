import json
import copy
from typing import List,Optional
from dataclasses import dataclass, field, asdict
from typing import Optional
from data_model.common import NIRColors
from data_model.environment import Vehicle,SeatOrientation


class VehicleModel():
    pool = []
    sequence = []

    @dataclass(frozen=False)
    class Vehicle():
        id: str = None
        vin: Optional[str] = None
        number_plates: List[str] = field(default_factory=list)
        vin: Optional[str] = None
        number_plates: List[str] = field(default_factory=list)
        brand: Optional[str] = None
        model: Optional[str] = None
        nickname: Optional[str] = None
        seat_count: int = 0
        seat_config: List[List[SeatOrientation]] = field(default_factory=list)
        right_hand_drive: bool = False
        seatbelt_NIR_color: Optional[NIRColors] = None

        def as_dict(self) -> dict:
            return asdict(self)

        def as_json(self) -> str:
            return json.dumps(self.as_dict())

        def is_valid(self) -> bool:
            try:
                return True,VehicleModel.Vehicle(**Vehicle(**self.as_dict()).dict())
            except Exception as e:
                print(f"Error validating Vehicle: {e}")
                return False,None

    def __init__(self):
        self.reset()

    def reset(self):
        self.vehicle = self.Vehicle()

    @property
    def store_to(self):
        class To():
            def __init__(self, model: VehicleModel):
                self.model = model

            def __store(self, container: list, data: VehicleModel.Vehicle) -> bool:
                isValid,_ = data.is_valid()
                if isValid:
                    if not container:
                        container.append(copy.deepcopy(data))
                        print(f"Vehicle '{data.id}' added to container")
                        return True
                    for idx,veh in enumerate(container):
                        if veh.id == data.id:
                            container[idx] = copy.deepcopy(data)
                            print(f"Vehicle '{data.id}' updated in container")
                            return True
                    container.append(copy.deepcopy(data))
                    print(f"Vehicle '{data.id}' added to container")
                    return True
                print(f"Vehicle '{data.id}' is not valid. Please check the vehicle data.")
                return False

            def __parse(self, container: list, data: VehicleModel.Vehicle | dict | None):
                match data:
                    case None:
                        return self.__store(container, self.model.vehicle)
                    case VehicleModel.Vehicle():
                        return self.__store(container, data)
                    case dict():
                        try:
                            vehicle = VehicleModel.Vehicle(**data)
                            return self.__store(container, vehicle)
                        except Exception as e:
                            print("Data is not in correct format. Please check.")
                            return False

            def pool(self, data: VehicleModel.Vehicle | dict | None = None):
                return self.__parse(self.model.pool, data)

            def sequence(self, data: VehicleModel.Vehicle | dict | None = None):
                return self.__parse(self.model.sequence, data)

        return To(self)
