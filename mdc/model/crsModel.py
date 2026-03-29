import json
import copy
from dataclasses import dataclass, field, asdict
from typing import List, Optional

from data_model.common import NIRColors
from data_model.environment import Seat
from data_model.crs import CRS,CRSInfo, MarketRegion,ECER4404Category,ISizeCategory,CRSType,ColorDesigns,RestraintTypes,InstallMethods
from data_model.crs import CrsStrapState,SuncoverState,CRSOccupancyEnum,InstallationStateEnum,ConditionEnum,CRSRotation

class CRSModel:
    pool = []
    sequence = []

    @dataclass(frozen=False)
    class CRS():
        crs_id: str = None
        brand: Optional[str] = None
        model: Optional[str] = None
        crs_type: Optional[CRSType] = None
        market_region: List[Optional[MarketRegion]] = field(default_factory=list)
        market_introduction_year: Optional[int] = None
        ECE_R44_04_category: Optional[ECER4404Category] = ECER4404Category.UNKNOWN
        ECE_R129_i_size_category: Optional[ISizeCategory] = None
        installation_method: Optional[InstallMethods] = None
        child_restraint_method: Optional[RestraintTypes] = None
        has_suncover: Optional[bool] = None
        has_impact_cushion_shield: Optional[bool] = None
        has_handle_bar: Optional[bool] = None
        supports_base_station: Optional[bool] = None
        has_support_leg: Optional[bool] = None
        seat_reflectance_NIR: Optional[NIRColors] = None
        seat_color_design: Optional[ColorDesigns] = None

        def as_dict(self) -> dict:
            return asdict(self)

        def as_json(self) -> str:
            return json.dumps(self.as_dict())

        def is_valid(self) -> bool:
            try:
                return True,CRSModel.CRS(**CRS(**self.as_dict()).dict())
            except Exception as e:
                print(f"Error validating CRS: {e}")
                return False,None

    @dataclass(frozen=False)
    class CRSInfo(CRS):
        seat_position: Seat = field(default_factory=lambda: Seat(row=0, column=0))
        occupied: Optional[CRSOccupancyEnum] = None
        crs_strap_state: Optional[CrsStrapState] = None
        suncover_state: Optional[SuncoverState] = None
        seat_reducer_installed: Optional[bool] = None
        impact_cushion_shield_state: Optional[InstallationStateEnum] = None
        has_aftermarket_accessories: Optional[bool] = None
        base_station_is_present: Optional[bool] = None
        condition: Optional[ConditionEnum] = None
        rotation: Optional[CRSRotation] = None
        orientation_front_back_on_axis_10deg: Optional[bool] = None

        def as_dict(self) -> dict:
            return asdict(self)

        def as_json(self) -> str:
            return json.dumps(self.as_dict())

        def is_valid(self) -> bool:
            try:
                return True,CRSModel.CRSInfo(**CRSInfo(**self.as_dict()).dict())
            except Exception as e:
                print(f"Error validating CRS: {e}")
                return False,None

    def __init__(self):
        self.reset()

    def reset(self):
        self.crs = self.CRS()
        self.crs_info = self.CRSInfo()

    @property
    def store_CRS_to(self):
        class To():
            def __init__(self, model: CRSModel):
                self.model = model

            def __store(self, container: list, data: CRSModel.CRS) -> bool:
                isValid,_ = data.is_valid()
                if isValid:
                    if not container:
                        container.append(copy.deepcopy(data))
                        print(f"CRS '{data.crs_id}' added to container")
                        return True
                    for idx,crs in enumerate(container):
                        if crs.crs_id == data.crs_id:
                            container[idx] = copy.deepcopy(data)
                            print(f"CRS '{data.crs_id}' updated in container")
                            return True
                    container.append(copy.deepcopy(data))
                    print(f"CRS '{data.crs_id}' added to container")
                    return True
                print(f"CRS '{data.crs_id}' is not valid. Please check the CRS data.")
                return False

            def __parse(self, container: list, data: CRSModel.CRS | dict | None):
                match data:
                    case None:
                        return self.__store(container, self.model.crs)
                    case CRSModel.CRS():
                        return self.__store(container, data)
                    case dict():
                        try:
                            crs = CRSModel.CRS(**data)
                            return self.__store(container, crs)
                        except Exception as e:
                            print(f"Error parsing CRS from dict: {e}")
                            return False
        return To(self)