
# Task Description

JSON REST API with CRUD operations for 
Provider (name, email, phone number, language and currency) and
ServiceArea (name, price, geojson information)

developing a specific endpoint that takes a latitude and longitude pair as arguments and return a list of all polygons that include the given latitude and longitude.


## Installation

Install my-project with pip

```bash
  pip install -r requirements.txt
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY=DGDFKLGJFLGDFGJGJDFN`



## Running Tests

To run tests, run the following command

```bash
  pytest
```


## API Reference

#### Get all Polygons that include the given latitude and longitude

```http
  POST  /service/area/polygon/
```
INPUT

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `latitude` | `string` | **Required**.  |
| `longitude` | `string` | **Required**.  |

OUTPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Id`      | `string` | **Required**.  |
| `name`      | `string` | **Required**.  |
| `price`      | `string` | **Required**.  |
| `provider`      | `string` | **Required**.  |



#### Get Provider Item

```http
  GET /provider/${id}/
```
INPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

OUTPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**.  |
| `email`      | `string` | **Required**.  |
| `phone`      | `string` | **Required**.  |
| `language`      | `string` | **Required**.  |
| `currency`      | `string` | **Required**.  |


#### Create Provider Item

```http
  POST /provider/
```
INPUT
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**.  |
| `email`      | `string` | **Required**.  |
| `phone`      | `string` | **Required**.  |
| `language`      | `string` | **Required**.  |
| `currency`      | `string` | **Required**.  |

OUTPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**.  |
| `email`      | `string` | **Required**.  |
| `phone`      | `string` | **Required**.  |
| `language`      | `string` | **Required**.  |
| `currency`      | `string` | **Required**.  |

#### Update Provider Item

```http
  PUT /provider/${id}/
```
INPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**.  |
| `email`      | `string` | **Required**.  |
| `phone`      | `string` | **Required**.  |
| `language`      | `string` | **Required**.  |
| `currency`      | `string` | **Required**.  |
OUTPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**.  |
| `email`      | `string` | **Required**.  |
| `phone`      | `string` | **Required**.  |
| `language`      | `string` | **Required**.  |
| `currency`      | `string` | **Required**.  |


#### Partially Update Provider Item

```http
  PATCH /provider/${id}/
```
INPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Not Required**.  |
| `email`      | `string` | **Not Required**.  |
| `phone`      | `string` | **Not Required**.  |
| `language`      | `string` | **Not Required**.  |
| `currency`      | `string` | **Not Required**.  |

OUTPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**.  |
| `email`      | `string` | **Required**.  |
| `phone`      | `string` | **Required**.  |
| `language`      | `string` | **Required**.  |
| `currency`      | `string` | **Required**.  |

#### DELETE Provider Item

```http
  DELETE /provider/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


| ----------------- | -----------------------| --------------------------------------------------------------- | --------------------------

##### Create Service Area Item

```http
  POST /service/area/
```
INPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | ** Required**.  |
| `price`      | `string` | ** Required**.  |
| `provider`      | `string` | ** Required**.  |
| `geo_json`      | `string` | ** Required**. |

geo_json  will cover all types of shapes like Polygon , multiPolygon, multiStringLine, Point, StringLine 

OUTPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | ** Required**.  |
| `name`      | `string` | ** Required**.  |
| `price`      | `string` | ** Required**.  |
| `provider`      | `string` | ** Required**.  |
| `geo_json`      | `string` | ** Required**.  |

#### Partially Update Service Area Item

```http
  PATCH /service/area/${id}/
```
INPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Not Required**.  |
| `price`      | `string` | **Not Required**.  |
| `provider`      | `string` | **Not Required**.  |
| `geo_json`      | `string` | **Not Required**.  |

OUTPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Not Required**.  |
| `name`      | `string` | **Not Required**.  |
| `price`      | `string` | **Not Required**.  |
| `provider`      | `string` | **Not Required**.  |
| `geo_json`      | `string` | **Not Required**.  |


##### Update Service Area Item

```http
  PUT /service/area/${id}/
```
INPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Not Required**.  |
| `price`      | `string` | **Not Required**.  |
| `provider`      | `string` | **Not Required**.  |
| `geo_json`      | `string` | **Not Required**.  |

OUTPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Not Required**.  |
| `name`      | `string` | **Not Required**.  |
| `price`      | `string` | **Not Required**.  |
| `provider`      | `string` | **Not Required**.  |
| `geo_json`      | `string` | **Not Required**.  |


#### Get Service Area Item      


```http
  GET /service/area/${id}/
```
INPUT

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |


#### DELETE Service Area Item

```http
  DELETE /service/area/${id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

## 🔗 Links

[![portfolio](https://img.shields.io/badge/hosting_server_address-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://mozio-webapp.herokuapp.com/)

[![linkedin](https://img.shields.io/badge/Github-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://github.com/sarakvn1/mozio.git
)
