import datetime
from dataclasses import dataclass, field
from typing import List, Optional, Union

from data_model.reference import MongoDBRef
from data_model.dbgui_input import DbGuiInput
from data_model.common import Comment, Supervisor
from data_model.scenario import Scenario
from data_model.recording_campaign import RecordingCampaign
from data_model.occupant import Occupant
from data_model.seatbelt import Seatbelt
from data_model.crs import CRSInfo
from data_model.sensor_system import SensorSystem
from data_model.object import ObjectInVehicle
from data_model.custom_data import CustomData
from data_model.environment import Environment, EmptySeatClassification

from mdc.model.supervisorModel import SupervisorModel

@dataclass(frozen=False)
class SequenceModel:
    revision: int = 0
    schema_version: str = None
    dbgui_config_ref: Optional[MongoDBRef[DbGuiInput]] = None
    name: str = None
    timestamp_start_utc: Optional[datetime.datetime] = None
    comments: Optional[List[Comment]] = None
    duration_seconds: Optional[Union[float, datetime.timedelta]] = None
    scenario: Scenario = None
    supervisor: Optional[List[SupervisorModel]] = None
    recording_campaign: RecordingCampaign = None
    environment: Optional[List[Environment]] = None
    seat_occupancy: Optional[List[List[bool]]] = None
    empty_seat_classification: Optional[List[EmptySeatClassification]] = None
    occupants: Optional[List[Occupant]] = None
    seatbelt: Optional[List[Seatbelt]] = None
    crs: Optional[List[CRSInfo]] = None
    sensor_systems: Optional[List[SensorSystem]] = None
    objects: Optional[List[ObjectInVehicle]] = None
    custom_structured_data = None
    custom_data: Optional[CustomData] = None

    def __init__(self,name,schema_version,duration_sec=None,comments = None):
        self.name: str = name
        self.schema_version = schema_version
        self.timestamp_start_utc = datetime.datetime.strptime(name, "%Y%m%dT%H%M%S").astimezone().isoformat()
        self.comments = comments
        self.duration_seconds = duration_sec
        self.supervisor: Optional[List[SupervisorModel]] = SupervisorModel.sequence if SupervisorModel.sequence else None
        self.scenario = None
        self.recording_campaign: RecordingCampaign = None
        self.environment: Optional[List[Environment]] = None
        self.seat_occupancy: Optional[List[List[bool]]] = None
        self.empty_seat_classification: Optional[List[EmptySeatClassification]] = None
        self.occupants: Optional[List[Occupant]] = None
        self.seatbelt: Optional[List[Seatbelt]] = None
        self.crs: Optional[List[CRSInfo]] = None
        self.sensor_systems: Optional[List[SensorSystem]] = None
        self.objects: Optional[List[ObjectInVehicle]] = None
        self.custom_data: Optional[CustomData] = None




