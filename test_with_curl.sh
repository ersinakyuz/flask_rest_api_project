# Get JWT Authorization Header
curl --location --request POST 'http://127.0.0.1:5000/auth' \
--header 'Content-Type: application/json' \
--data-raw '{
	"username" : "admin",
	"password" : "admin"
}'

# Add First Customer
curl --location --request PUT 'http://127.0.0.1:5000/customer/1' \
--header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTM4NjE5OTMsImlhdCI6MTY1Mzg2MTY5MywibmJmIjoxNjUzODYxNjkzLCJpZGVudGl0eSI6MX0.7L3Dg12RFWRNQyIqDIimUPYEC0sNwp3rlNFsuKbv9o8' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name":"Ersin Akyuz"
}'

# Add Second Customer
curl --location --request PUT 'http://127.0.0.1:5000/customer/2' \
--header 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTM4NjIxNTgsImlhdCI6MTY1Mzg2MTg1OCwibmJmIjoxNjUzODYxODU4LCJpZGVudGl0eSI6MX0.JOThpp2ILsFq7ae43ms5cHIJhEEUwWDDEGZfdlfwG6c' \
--header 'Content-Type: application/json' \
--data-raw '{
	"name":"John Doe",
    "is_active" : 1
}'