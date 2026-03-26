import json
import copy
from typing import Optional, List
from dataclasses import dataclass, field, asdict

from data_model.location import Location,continents,countries_ISO3166


class LocationModel():
    pool = []
    sequence = []

    @dataclass(frozen=False)
    class Location():
        continent: continents = None
        country: countries_ISO3166 = None
        city: str = None
        state: Optional[str] = None

        @property
        def check_fillout(self) -> bool:
            """Check if all mandatory fields are filled out"""
            _continent: bool = True if self.continent in list(continents) else False
            _country: bool = True if self.country in list(countries_ISO3166) else False
            _city: bool = True if self.city not in [None, ""] else False

            match _continent:
                case False: print("continent has invalid value or is not filled out")
            match _country:
                case False: print("country has invalid value or is not filled out")
            match _city:
                case False: print("city is not filled out")

            return all([_continent, _country, _city])

        @property
        def as_dict(self) -> dict:
            """Get Location as dictionary format"""
            return asdict(self)

        @property
        def as_json(self) -> json:
            """Get Location as json format"""
            return json.dumps(self.as_dict)

        def is_valid(self) -> bool:
            try:
                return True,LocationModel.Location(**Location(**self.as_dict).dict())
            except Exception as e:
                print(f"Error validating Location: {e}")
                return False,None

    def __init__(self):
        self.reset()

    def reset(self):
        self.location = self.Location()

    @property
    def store_to(self):
        class To():
            def __init__(self, locModel: LocationModel):
                self.model = locModel

            def __store(self, container: list, data: LocationModel.Location) -> bool:
                """Handle store process"""
                isValid,_ = data.is_valid()
                if isValid:
                    if not container:
                        container.append(copy.deepcopy(data))
                        print(f"Location '{data.city}, {data.country.value}' added to container")
                        return True
                    for idx,loc in enumerate(container):
                        if loc.city == data.city and loc.country == data.country:
                            container[idx] = copy.deepcopy(data)
                            print(f"Location '{data.city}, {data.country.value}' updated in container")
                            return True
                    container.append(copy.deepcopy(data))
                    print(f"Location '{data.city}, {data.country.value}' added to container")
                    return True
                print(f"Location '{data}' is not valid. Please check the location data.")
                return False

            def __parse(self, container: list, data: LocationModel.Location | dict | None):
                match data:
                    case None:
                        return self.__store(container, self.model.location)
                    case LocationModel.Location():
                        return self.__store(container, data)
                    case dict():
                        try:
                            loc = LocationModel.Location(**data)
                            return self.__store(container, loc)
                        except Exception as e:
                            print(f"Data is not in correct format. Please check. \nError: {e}")
                            return False

            def pool(self, data: LocationModel.Location | dict | None = None):
                """Handle store process"""
                return self.__parse(self.model.pool, data)

            def sequence(self, data: LocationModel.Location | dict | None = None):
                """Handle store process"""
                return self.__parse(self.model.sequence, data)

        return To(self)

if __name__ == "__main__":
    loc1= LocationModel()
    loc2 = LocationModel()
    loc1.location.continent = continents.EU
    loc1.location.country = countries_ISO3166.DE
    loc1.location.city = "Munich"

    loc2.location.continent = "asd"
    loc2.location.country = 'qwe'
    loc2.location.city = "Hamburg"

    print(loc1.location.check_fillout)
    print(loc2.location.check_fillout)

    loc1.store_to.pool()
    loc2.store_to.pool()

    print("Pool:", [loc for loc in loc1.pool])