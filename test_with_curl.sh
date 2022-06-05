echo Get JWT Authorization Header

curl --location --request POST 'http://127.0.0.1:5000/auth' \
--header 'Content-Type: application/json' \
--data-raw '{
	"username" : "admin",
	"password" : "admin"
}'



TOKEN=$(curl --location --request POST 'http://127.0.0.1:5000/auth' \
--header 'Content-Type: application/json' \
--data-raw '{
	"username" : "admin",
	"password" : "admin"
}'| jq -r '.access_token'  )
#echo Token: $TOKEN


echo Adding the first customer

curl --location --request PUT 'http://127.0.0.1:5000/customer/1' \
--header "Authorization: JWT ${TOKEN}" --header 'Content-Type: application/json' \
--data-raw '{
	"name":"Ersin Akyuz"
}'


echo Adding the second customer
curl --location --request PUT 'http://127.0.0.1:5000/customer/2' \
--header "Authorization: JWT ${TOKEN}" --header 'Content-Type: application/json' \
--data-raw '{
	"name":"John Doe",
    "is_active" : 1
}'

echo Adding the second customer in order to test duplication check
curl --location --request PUT 'http://127.0.0.1:5000/customer/2' \
--header "Authorization: JWT ${TOKEN}" --header 'Content-Type: application/json' \
--data-raw '{
	"name":"John Doe",
    "is_active" : 1
}'

echo Billing the first customer 20 $
curl --location --request PATCH 'http://127.0.0.1:5000/customer/1' \
--header "Authorization: JWT ${TOKEN}" --header 'Content-Type: application/json' \
--data-raw '{
	"name":"Ersin Akyuz",
 	"is_active": 1, 
 	"bills": 20
}'

echo Deactivating the first customer
curl --location --request PATCH 'http://127.0.0.1:5000/customer/1' \
--header "Authorization: JWT ${TOKEN}" --header 'Content-Type: application/json' \
--data-raw '{
	"name":"Ersin Akyuz",
	"is_active": 0, 
 	"bills": 20
}'

echo Changing the customer name
curl --location --request PATCH 'http://127.0.0.1:5000/customer/1' \
--header "Authorization: JWT ${TOKEN}" --header 'Content-Type: application/json' \
--data-raw '{
	"name":"Ersin Akyuez",
 	"is_active": 0
}'

echo Billing the first customer 100 $
curl --location --request PATCH 'http://127.0.0.1:5000/customer/1' \
--header "Authorization: JWT ${TOKEN}" --header 'Content-Type: application/json' \
--data-raw '{
	"name":"Ersin Akyuz",
 	"is_active": 0, 
 	"bills": 100
}'

echo Getting details of first customer 
curl --location --request GET 'http://127.0.0.1:5000/customer/1' \
--header "Authorization: JWT ${TOKEN}" --header 'Content-Type: application/json' \
--data-raw '{
	"name":"Ersin Akyuz",
 	"is_active": 0, 
 	"bills": 20
}'