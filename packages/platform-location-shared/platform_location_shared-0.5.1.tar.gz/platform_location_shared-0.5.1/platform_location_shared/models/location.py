from typing import Dict, Union

from platform_location_shared.models.mixins.serialise import Serialisable
from platform_location_shared.validations.postcode import postcode_field, Postcode


class InitialInputLocation(Serialisable):
    post_code: Postcode = postcode_field


class GooglePlacesLocation(InitialInputLocation):
    latitude: float
    longitude: float
    street_address: str
    city: str
    province: str
    province_code: str
    state: str
    state_code: str
    country: str
    country_code: str


class ONSLocation(InitialInputLocation):
    lsoa: str


class FullLocation(GooglePlacesLocation, ONSLocation):
    # [ ] TODO: Add the other fields
    nuts: str
    future: str
    sub_sub_region: str
    sub_region: str
    region: str


BatchGooglePlacesLocation = Dict[str, Union[GooglePlacesLocation, None]]
