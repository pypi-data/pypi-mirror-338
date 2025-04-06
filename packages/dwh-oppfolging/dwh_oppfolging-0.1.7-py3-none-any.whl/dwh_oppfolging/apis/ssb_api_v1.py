"ssb api"

import logging
from datetime import datetime
import requests # type: ignore
from dwh_oppfolging.apis.ssb_api_v1_types import (
    Version, VersionHeader,
    Correspondence, CorrespondenceHeader,
    Classification,
    CodeChangeList
)

API_VERSION = 1
API_NAME = "SSB"
SEKTOR_ID = 39
NAERING_ID = 6
YRKESKATALOG_ID = 145
YRKESKLASSIFISERING_ID = 7
YRKESKATALOG_TO_YRKESKLASSIFISERING_ID = 426
ORGANISASJONSFORM_ID = 35

_BASE_URL = (
    f"https://data.ssb.no/api/klass/v{API_VERSION}"  # classifications/{0}/changes"
)
_HEADERS = {"Accept": "application/json;charset=UTF-8"}


def get_classification(classification_id: int, include_future: bool = False):
    """
    Makes a get request to SSB Klass API and builds a Classification from the JSON response

    params:
        - classification_id: int
        - include_future: bool = False
            > If this is set then classification versions which become valid
            in the *future* are made available in the versions list.
    returns:
        Classification
    """
    url = _BASE_URL + f"/classifications/{classification_id}"
    params = {"includeFuture": include_future}
    response = requests.get(url, headers=_HEADERS, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return Classification.from_json(data)


def get_classification_version(classification_id: int, version_id: int):
    """
    Makes a get request to SSB Klass API and builds a Version from the JSON response

    params:
        classification_id: int
        version_id: int
    returns:
        Version
    """
    url = _BASE_URL + f"/versions/{version_id}"
    response = requests.get(url, headers=_HEADERS, timeout=10)
    response.raise_for_status()
    data = response.json()
    return Version.from_json(data, classification_id)


def get_correspondence(source_classification_id: int, target_classification_id: int, correspondence_id: int):
    """
    Makes a get request to SSB Klass API and builds a Correspondence from the JSON response

    params:
        - source_classification_id: int
        - target_classification_id: int
        - correspondence_id: int
            > Note: It is not checked if the returned Correspondence is actually between the provided classifications.
            To validate this, check if Correspondence.source_version_id and Correspondence.target_version_id
            are in the source and target Classifications.versions list respectively.
            Alternatively, check if the correspondence_id is in the source and target Version.correspondence_tables,
            since correspondences are between specific versions of classifications.
    returns:
        Correspondence
    """
    url = _BASE_URL + f"/correspondencetables/{correspondence_id}"
    response = requests.get(url, headers=_HEADERS, timeout=10)
    response.raise_for_status()
    data = response.json()
    return Correspondence.from_json(data, source_classification_id, target_classification_id)


def get_classification_changes(classification_id: int):
    """
    Makes a get request to SSB Klass API and builds CodeChangeList from the JSON response.
    
    Note: if there is no change table available then inter-version changes may have been lost
    """
    url = _BASE_URL + f"/classifications/{classification_id}/changes"

    classification = get_classification(classification_id)
    version_dates = sorted((v.valid_from for v in classification.versions))
    for from_date in version_dates:
        params = {"from": from_date.date().isoformat()}
        response = requests.get(url, headers=_HEADERS, params=params, timeout=10)
        try:
            response.raise_for_status()
        except requests.HTTPError as e:
            logging.warning(response.text)
            continue
        data = response.json()
        return CodeChangeList.from_json(data, classification_id)
    return []