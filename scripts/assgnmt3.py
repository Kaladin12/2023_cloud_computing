# Import for the libraries and modules to use in the script
# boto3 is the library that allows to communicate with AWS, while sys allows to handle command
# line arguments from the terminal
import boto3
import sys


class ASSIGNMENT3:
    # Didn;t wanted to instantiate the session as a global variable, so created a class from which the methods can call it
    def __init__(self):
        # This constructor creates a boto3 session, which is just a way to define a connection with AWS, with a set of configuration values. 
        # Since I don't have my default profile configured with the key-pair for this class, I pass the profile with this configuration
        # in the profile_name paramater
        self.session = boto3.Session(profile_name='kaladin12')
        # Then, define a client that passes 'dynamodb' as parameter, namely, I'm using the session configuration to create
        # a client that will allow me to communictae with dynamodb
        self.dynamodbClient = self.session.client('dynamodb')

    def get_item_by_id(
            self,
            student_id:str, 
            ) -> list:
        # In order to get an item from the Students database, create this method which receives the student id
        # Then define a list of the fields I want the user to see when returning the record searched
        fields_to_return:list=['id', 'full_name', 'personal_website']
        # Then, checked whether the values provided for the paramaters match the values needed to send to the DB
        # student_id has to be of type string
        # If any of these asserts fails, an error will be raised and the function will no send the data to the db
        # This just allows to catch possible errors before sending the data
        assert type(student_id) == str
        # Then, we call the get_item method for the dynamo client, it receives the name of the Table, which is
        # Students, as well as the key to search, which needs to specify the structure of it, namely
        # "name":{ "type": value }, where name is the name of the field, type is S for string
        # and the value is the id passed by the user that we want to search
        # This method also has the option to indicate the AttributesToGet, which
        # tells dynamoDB which fields we want to get for the record that matches the query, for it we pass
        # the fields_to_return list
        res = self.dynamodbClient.get_item(
            TableName = 'Students',
            Key =  {
                "id": {
                    "S":student_id,
                }
            },
            AttributesToGet=fields_to_return
        )
        # The query return its value into the res variable
        # Next, we need to handle the response, if the code is not a 200 (successfull) or the Item attribute
        # is empty (it can happen that the query is successfull but no item was found), we raise a KeyError
        # which indicates the value provided was not found
        # The response has the attribute ResponseMetadata, which in turns has the HTTPStatusCode value
        # for the request sent by the client
        if res['ResponseMetadata']['HTTPStatusCode'] != 200 or 'Item' not in res:
            raise KeyError(student_id)
        # else, we return the value by passing the content in the Item attribute of the response json
        return res['Item']

    def create_or_update(
            self,
            student_data:str
            ) -> str:
        # To create or update a record in the database, we receive the student_data parameter
        # which has to be a str since its a JSON object taken from the terminal (as string)
        # Then import the json module to convert strs to objects easily
        # I import it here because I don't need it in the other methods, and don't want to have it in memory
        # if isn't used
        import json
        # Then, try to convert the string into a proper JSON object by converting it with the json module
        # if isn't successful (wrong json format passed ) a type error will be raised to inform the user 
        # its mistake
        try:
            student_data = json.loads(student_data)
        except:
            raise TypeError('Wrong Format!!!')

        # Then, after the json object exists, just check whether it has the appropiate attributes to send 
        # to the database, namely id, full_name and personal_website
        assert 'id' in student_data
        assert 'full_name' in student_data
        assert 'personal_website' in student_data
        # If all the fields are in the object, call the put_item method from the dynamodb client
        # which allows to create or update a record with the same parameters
        # It receives the table name as well as the Item parameter, which is an object
        # that asks to define the structure of the fields in the databse and the values to be sent
        # for this, just define the following:
        # "name":{ "type": value }, where name is the name of the field, type is S for string
        # and the value is parameter passed by the user, namely full_name, id and personal_website
        res = self.dynamodbClient.put_item(
            TableName = 'Students',
            Item={
                "full_name":{
                    "S":student_data['full_name']
                },
                "id": {
                    "S":student_data['id']
                },
                "personal_website":{
                    "S":student_data['personal_website']
                }
            }
        )
        # This gives us a response, if its status code is not successfull (200)
        # then raise a key error and tell the user it did not work
        if res['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise KeyError("DIDN'T WORKED")
        # else, tell the user its action was successful
        return 'SUCCESS'

    def delete_item_by_id(
            self, 
            student_id:str
            ) -> str:
        # To delete an item, receive a student id as a parameter in order to be able to 
        # look for a record based on this value
        # then, assert whether it has the proper type
        assert type(student_id) == str
        # After asserting this, call the delete_item method of the dynamodb client
        # passing the table anme, as well as the key to search for
        # which defines the field name, its type and the value to look for, which is the
        # student id passed by the user
        res = self.dynamodbClient.delete_item(
            TableName = 'Students',
            Key =  {
                "id": {
                    "S":student_id,
                }
            }
        )
        # Then check the response if it isn't successfull (200) raise an error
        if res['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise KeyError(student_id)
        # else, tell the user it was successful
        return 'DELETED'

# Used to check whether the module is run directly or as an import in another module
if __name__ == '__main__':
    # create the instance for the class that contains all the methods
    assgn = ASSIGNMENT3()
    # Since I decided to test my knwoledge in command line manipulation, defined a series of 
    # options to be sent from the terminal by the user in order to call each of the methods
    # here I just map each option with the proper reference (the method name with no ())
    mappings= {
        '--get-item-by-id': assgn.get_item_by_id,
        '--create-or-update': assgn.create_or_update,
        '--delete-item-by-id': assgn.delete_item_by_id
    }
    # Then, read the arguments from the command line by using the sys.argv (variable arguments)
    # and filtering them by those that start with -- (the method to call) or nor (arguments)
    # within a list comprehension
    # this has the pitfall of only allowingone argument, but sisnce its for practice, its ok
    calls = [arg for arg in sys.argv[1:] if arg.startswith('--')]
    args = [arg for arg in sys.argv[1:] if not arg.startswith('--')]
    # then, couple the methods and arguments to pass to them with a zip (joins by tuples)
    # and pass them to the proper function by calling mappins with the call (the function selected)
    # and the argument
    for call, arg in zip(calls, args):
        print(mappings[call](arg))
    
