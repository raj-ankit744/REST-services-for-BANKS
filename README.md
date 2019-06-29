# REST-services-for-BANKS


# To create tables and to populate values : 

psql -h <host> -U <user> <database> < indian_banks.sql
                                                      
# Run Appication

waitress-serve --call 'REST:create_app'

# Create user

curl -d '{"username":"user", "password":"1234"}' -H "Content-Type: application/json" -X POST http://localhost:5000/auth/register

# Login with the created user to receive the access token

curl -d '{"username":"user", "password":"1234"}' -H "Content-Type: application/json" -X POST http://localhost:5000/auth/login


# Accessing API for getting bank details based on IFSC code

curl -H "Authorization: Bearer <jwt>" -X GET http://localhost:5000/api/getBankDetails/ABHY0065001

# Accessing API for getting branch details based on bank name and city
# The api also has limit and offset parameters

curl -H "Authorization: Bearer <jwt>" -X GET http://localhost:5000/api/getBranchDetails/ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED/MUMBAI/2/33
