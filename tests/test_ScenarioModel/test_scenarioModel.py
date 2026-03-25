import pytest
import datetime
import copy
import json
from mdc.model.scenarioModel import ScenarioModel,ProcessStep

class TestScenarioModel():
    model= ScenarioModel()
    def test_scenarioModel(self):
        datimeNow= datetime.datetime.now().astimezone().isoformat()

        self.model.scenario.id = "1"
        self.model.scenario.creation_timestamp = datimeNow
        self.model.scenario.name = "Test Scenario"
        self.model.scenario.primary_usecase = ProcessStep.VALIDATION
        self.model.scenario.description = "This is a test scenario."
        self.model.scenario.tags = ["test", "scenario"]
        self.model.scenario.specification = None
        self.model.scenario.facial_landmarks_mandatory = True

        # Test if the scenario is valid
        assert self.model.scenario.check_fillout == True

        # Test if the scenario can be added to the pool
        assert self.model.store_to.pool() == True

        # Test if the scenario can be added to the sequence
        assert self.model.store_to.sequence() == True
        assert self.model.scenario.as_json ==json.dumps({"id": "1", "creation_timestamp": datimeNow, "name": "Test Scenario", "primary_usecase": "validation", "description": "This is a test scenario.", "tags": ["test", "scenario"], "specification": None, "facial_landmarks_mandatory": True})