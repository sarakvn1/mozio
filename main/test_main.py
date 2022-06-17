from django.test import TestCase

# Create your tests here.
import json

import pytest
from model_bakery import baker
from django.urls import reverse
from rest_framework.test import APIClient

from loguru import logger


@pytest.mark.django_db
def test_create_provider_should_pass():
    client = APIClient()
    data = {
        "name": "sara3",
        "email": "sarakvn@gmail.com",
        "phone": "09100785091",
        "language": "persian",
        "currency": "IR"
    }

    response = client.post('/provider/', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 201


@pytest.mark.django_db
def test_retrieve_provider_should_pass():
    baker.make('Provider', id=1)
    client = APIClient()
    response = client.get('/provider/1/', content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_provider_should_pass():
    baker.make('Provider', id=1)
    client = APIClient()
    response = client.delete('/provider/1/', content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 204


@pytest.mark.django_db
def test_list_of_all_providers_should_pass():
    baker.make('Provider', id=1)
    client = APIClient()
    response = client.get('/provider/', content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_update_provider_should_pass():
    baker.make('Provider', id=1)
    client = APIClient()
    data = {
        "name": "sara3",
        "email": "sarakvn@gmail.com",
        "phone": "09100785091",
        "language": "persian",
        "currency": "IR"
    }

    response = client.put('/provider/1/', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_partially_update_provider_should_pass():
    baker.make('Provider', id=1)
    client = APIClient()
    data = {
        "email": "sarakvn@gmail.com",
        "phone": "09100785091",
        "language": "persian",
        "currency": "IR"
    }

    response = client.patch('/provider/1/', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_service_area_should_pass():
    baker.make('Provider', id=1)
    client = APIClient()
    data = {
        "name": "atlanta",
        "price": 100,
        "provider": 1,
        "geo_json": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "type": "MultiLineString",
                        "coordinates": [
                            [
                                [
                                    100.0,
                                    0.0
                                ],
                                [
                                    101.0,
                                    1.0
                                ]
                            ],
                            [
                                [
                                    102.0,
                                    2.0
                                ],
                                [
                                    103.0,
                                    3.0
                                ]
                            ]
                        ]
                    }
                },
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "type": "MultiPoint",
                        "coordinates": [
                            [
                                100.0,
                                0.0
                            ],
                            [
                                101.0,
                                1.0
                            ]
                        ]
                    }
                },
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "type": "MultiPolygon",
                        "coordinates": [
                            [
                                [
                                    [
                                        102.0,
                                        2.0
                                    ],
                                    [
                                        103.0,
                                        2.0
                                    ],
                                    [
                                        103.0,
                                        3.0
                                    ],
                                    [
                                        102.0,
                                        3.0
                                    ],
                                    [
                                        102.0,
                                        2.0
                                    ]
                                ]
                            ],
                            [
                                [
                                    [
                                        100.0,
                                        0.0
                                    ],
                                    [
                                        101.0,
                                        0.0
                                    ],
                                    [
                                        101.0,
                                        1.0
                                    ],
                                    [
                                        100.0,
                                        1.0
                                    ],
                                    [
                                        100.0,
                                        0.0
                                    ]
                                ],
                                [
                                    [
                                        100.2,
                                        0.2
                                    ],
                                    [
                                        100.8,
                                        0.2
                                    ],
                                    [
                                        100.8,
                                        0.8
                                    ],
                                    [
                                        100.2,
                                        0.8
                                    ],
                                    [
                                        100.2,
                                        0.2
                                    ]
                                ]
                            ]
                        ]
                    }
                }
            ]
        }
    }
    response = client.post('/service/area/', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 201


@pytest.mark.django_db
def test_list_of_service_area_should_pass():
    baker.make('Provider', id=1)
    client = APIClient()
    response = client.get('/service/area/', content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_service_area_should_pass():
    baker.make('Provider', id=1)
    baker.make('ServiceArea', id=1)
    client = APIClient()
    response = client.delete('/service/area/1/', content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 204


@pytest.mark.django_db
def test_update_service_area_should_pass():
    baker.make('Provider', id=2)
    baker.make('ServiceArea', id=2)
    client = APIClient()
    data = {
        "id": 1,
        "provider": 2,
        "name": "atlanta",
        "geo_json": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [
                            [
                                -30.234375,
                                69.77895177646761
                            ],
                            [
                                5.625,
                                47.27922900257082
                            ],
                            [
                                -48.515625,
                                69.77895177646761
                            ],
                            [
                                -31.640625,
                                70.02058730174062
                            ]
                        ]
                    }
                }
            ]
        }
    }

    response = client.put('/service/area/2/', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_partially_update_service_area_should_pass():
    baker.make('Provider', id=2)
    baker.make('ServiceArea', id=2)
    client = APIClient()
    data = {
        "name": "atlanta",
        "geo_json": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {},
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [
                            [
                                -30.234375,
                                69.77895177646761
                            ],
                            [
                                5.625,
                                47.27922900257082
                            ],
                            [
                                -48.515625,
                                69.77895177646761
                            ],
                            [
                                -31.640625,
                                70.02058730174062
                            ]
                        ]
                    }
                }
            ]
        }
    }

    response = client.patch('/service/area/2/', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_list_of_all_polygon_should_pass():
    baker.make('Provider', id=2, name='sara')
    baker.make('ServiceArea', id=2, provider_id=2)
    client = APIClient()
    data = {"geo_json": {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -48.8671875,
                                73.12494524712693
                            ],
                            [
                                -23.90625,
                                73.12494524712693
                            ],
                            [
                                -23.90625,
                                78.83606545333527
                            ],
                            [
                                -48.8671875,
                                78.83606545333527
                            ],
                            [
                                -48.8671875,
                                73.12494524712693
                            ]
                        ]
                    ]
                }
            }
        ]
    }}

    response = client.patch('/service/area/2/', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200
    data = {
        "longitude": "-37.6171875",
        "latitude": "76.3518964311259"
    }
    response = client.post('/service/area/polygon/', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200
    assert json.loads(response.content)[0].get('provider') == 'sara'
    assert len(json.loads(response.content)) == 1


@pytest.mark.django_db
def test_get_list_of_all_polygon_with_wrong_latitude_should_fail():
    baker.make('Provider', id=2, name='sara')
    baker.make('ServiceArea', id=2, provider_id=2)
    client = APIClient()
    data = {"geo_json": {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [
                                -48.8671875,
                                73.12494524712693
                            ],
                            [
                                -23.90625,
                                73.12494524712693
                            ],
                            [
                                -23.90625,
                                78.83606545333527
                            ],
                            [
                                -48.8671875,
                                78.83606545333527
                            ],
                            [
                                -48.8671875,
                                73.12494524712693
                            ]
                        ]
                    ]
                }
            }
        ]
    }}

    response = client.patch('/service/area/2/', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200
    data = {
        "latitude": "-37.6171875",
        "longitude": "76.3518964311259"
    }
    response = client.post('/service/area/polygon/', data=json.dumps(data), content_type='application/json')
    logger.info(response.content)
    assert response.status_code == 200
    assert len(json.loads(response.content)) == 0
