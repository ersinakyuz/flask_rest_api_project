
# Project flask_rest_api_project

This project provides basic REST API functions on Python3

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
## Deployment

To deploy this project run

```bash
git clone git@github.com:ersinakyuz/flask_rest_api_project.git  
./install.sh
python3 main.py
```


## Running Tests

To run tests, run the following command

```bash
test_with_curl.sh
```


## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  npm install
```

Start the server

```bash
  npm run start
```


## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```

