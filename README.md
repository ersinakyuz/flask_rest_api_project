
# Project flask_rest_api_project

This project provides basic REST API functions on Python3

Default Flask libraries has been used for the application. 


## 🔗 Link to Repository
[[Flask Rest API Project]](https://github.com/ersinakyuz/flask_rest_api_project/)

Ersin Akyüz
ersinakyuz.de@gmail.com
## API Reference

#### To GET JWT Authentication Header

```http
POST /auth
```

| Parameter  | Type     | Description                    |
| :--------- | :------- | :----------------------------- |
| `username` | `string` | **Required**. initially (admin)|
| `password` | `string` | **Required**. initially (admin)|

#### Add Customer

```http
PUT /customer/${id}
```

| Parameter  | Type     | Description                                      |
| :--------  | :------- | :----------------------------------------------- |
| `name`     | `string` | **Required**. Customer Name and Surname          |
| `is_active`| `string` | **Optional**. Is it an active account? Default 1 |
| `bills`    | `string` | **Optional**. Bills of the customer              |

| Header Key      | Type     | Description                                 |
| :-------------  | :------- | :------------------------------------------ |
| `Authorization` | `string` | **Required**. JWT Authorization Header      |

#### Changing Customer Information

```http
PUT /customer/${id}
```

| Parameter   | Type     | Description                                       |
| :---------- | :------- | :------------------------------------------------ |
| `name`      | `string` | **Required**. Customer Name and Surname           |
| `is_active` | `string` | **Optional**. Is it an active account? Default 1  |
| `bills`     | `string` | **Optional**. Bills of the customer               |

| Header Key      | Type     | Description                                 |
| :-------------  | :------- | :------------------------------------------ |
| `Authorization` | `string` | **Required**. JWT Authorization Header      |

#### Get Customers

```http
GET /customers/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

| Header Key      | Type     | Description                                 |
| :-------------  | :------- | :------------------------------------------ |
| `Authorization` | `string` | **Required**. JWT Authorization Header      |




## Running Tests

To run tests, run the following command

```bash
test_with_curl.sh
```


## Deployment & Run Locally

Clone the project

```bash
  git clone git@github.com:ersinakyuz/flask_rest_api_project.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  ./install.sh
```

Start the server

```bash
  python main
```

