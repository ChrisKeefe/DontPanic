from google.cloud import firestore
from firebase_admin import messaging
from flask import escape

# ################### Public-Facing API functions ###########################


def create_message(request):
    """ Adds a new Message document to the messages collection in firestore
    Preconditions: receives a POST request of content-type 'application/json'
        format:
        {
          "messagePayload":{
              "messageContent":"STR",
              "resourceURL":"STR",
              "category":"STR",
              "urgency":"INT",
              "tags":[
              "STR1",
              "STR2",
              "STRn"
              ]
            }
          }
    Postconditions: uniquely identified db document written to firestore
    """
    import uuid
    db = firestore.Client()
    # TODO: sanitize inputs

    # get_json gets a json object if exists, else returns None
    request_json = request.get_json(silent=True)
    # args is a multidict, which can be indexed like request_args[key]
    request_args = request.args
    if request_json and 'messagePayload' in request_json:
        payload = request_json['messagePayload']
    elif request_args and 'messagePayload' in request_args:
        payload = request_args['messagePayload']
    else:
        return "Failure: invalid payload"

    messageContent = payload['messageContent']
    resourceURL = payload['resourceURL']
    category = payload['category']
    urgency = payload['urgency']
    tags = payload['tags']

    data = {
        u'messageContent': str(messageContent),
        u'resourceURL': str(resourceURL),
        u'category': str(category),
        u'tags': tags,
        u'urgency': int(urgency)
    }

    # generate a unique id for db documents to prevent namespace collisions
    message_ID = uuid.uuid4()
    # Add a new doc in collection 'messages' with randomly-generated ID
    db.collection(u'messages').document(str(message_ID)).set(data)


def create_profile(request):
    """ Adds a new Profile document to the profiles collection in firestore
    Preconditions: Must have a user ID and other profile data delivered by as a
    POST request of content-type 'application/json', with format:
        {
          "profilePayload":{
              "userID":"INT",
              "receiveSMSflag":"BOOL",
              "receivePushFlag":"BOOL",
              "messageFrequency":"INT",
              "isProfileActive":"BOOL",
              "preferredTags":[
              "STR1",
              "STR2",
              "STRn"
              ]
            }
          }
    Postconditions: uniquely identified db document written to firestore
    TODO: add user device ID
    TODO: add a message scheduler to this
    TODO: sanitize inputs
    """
    import uuid
    db = firestore.Client()

    # get_json gets a json object if exists, else returns None
    request_json = request.get_json(silent=True)
    # args is a multidict, which can be indexed like request_args[key]
    request_args = request.args
    if request_json and 'profilePayload' in request_json:
        payload = request_json['profilePayload']
    elif request_args and 'profilePayload' in request_args:
        payload = request_args['profilePayload']
    else:
        return "Failure: invalid payload"

    userID = payload['userID']
    receiveSMSflag = payload['receiveSMSflag']
    receivePushFlag = payload['receivePushFlag']
    messageFrequency = payload['messageFrequency']
    isProfileActive = payload['isProfileActive']
    preferredTags = payload['preferredTags']

    data = {
        u'userID': int(userID),
        u'receiveSMSflag': bool(receiveSMSflag),
        u'receivePushFlag': bool(receivePushFlag),
        u'messageFrequency': int(messageFrequency),
        u'isProfileActive': bool(isProfileActive),
        u'preferredTags': preferredTags
    }

    # generate a unique id for db documents to prevent namespace collisions
    profile_ID = uuid.uuid4()
    # Add a new doc in collection 'messages' with randomly-generated ID
    db.collection(u'profiles').document(str(profile_ID)).set(data)


def create_user(request):
    """ Adds/updates a User document to the messages collection in firestore
    Used to keep device tokens up-to-date
    Preconditions: receives a POST request of content-type 'application/json'
        format:
        {
          "messagePayload":{
              "userID":"STR",
              "userName":"STR",
              "phoneNum":"INT",
              "profiles":[
              "profileID1",
              "profileID2",
              "profileIDn"
              ]
            }
          }
    Postconditions: uniquely identified db document written to firestore
    TODO: get existing user profiles, append them to this req for idempotence
    """
    db = firestore.Client()

    # get_json gets a json object if exists, else returns None
    request_json = request.get_json(silent=True)
    # args is a multidict, which can be indexed like request_args[key]
    request_args = request.args
    if request_json and 'messagePayload' in request_json:
        payload = request_json['messagePayload']
    elif request_args and 'messagePayload' in request_args:
        payload = request_args['messagePayload']
    else:
        return "Failure: invalid payload"

    userID = payload['userID']
    userName = payload['userName']
    phoneNum = payload['phoneNum']
    profiles = payload['profiles']

    data = {
        u'userName': str(userName),
        u'phoneNum': str(phoneNum),
        u'profiles': profiles,
    }
    # Add a new doc in collection 'users' with userID as doc name
    db.collection(u'users').document(str(userID)).set(data)


def send_message_to_one_user(request):
    # This registration token comes from the client FCM SDKs.
    registration_token = 'd5ITFKJ6Tm6KvoaIJ8IVQf:APA91bFizkGRIeA3OGKNHS6LK3nhTllG46voqXR0NtBtXlGvV6AAkZZMwkgqW7ZrXHBxORLzTBZRWRoFJ17ciLBU_AWoWRY2AoNlgcwSXQwR64BIcEjYrgG4eV5c16ksz-p8sGBqxM6v'

    # See documentation on defining a message payload.
    message = messaging.Message(
        notification={
            'title': 'A message...',
            'body': 'Wooohoooooo!',
        },
        token=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)



# ####################### TO-DO List ######################################
# TODO: Updating messages or profiles will require us to get the record,
# get existing tags, set() those tags, add the new ones, and then create the
# record passing the recordID explicitly

# TODO: Mason - create a function that sends a simple text message to our app

# TODO: create a function that listens to the firestore db and
# modifies the LA document once it's been created

# TODO: create a function that listens to the firestore db
# and calls add_from_dict with data so that it creates a new document for NYC


# ##################### SAMPLE FUNCTIONS ####################################
# HTTP functions like this must have (request) as a parameter, as they are
# triggered by HTTP get/post/etc requests. In this example, the branching logic
# allows this function to handle JSON inputs through POST, GET requests that
# that offer a "name" argument, and requests with no argument


def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <http://flask.pocoo.org/docs/1.0/api/#flask.Request>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>.
    Usage: passing a name as follows will yield Hello Name!
    https://GCP_REGION-PROJECT_ID.cloudfunctions.net/hello_http?name=NAME
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(escape(name))


# we can use publishers and subscribers to chain multiple cloud functions
# e.g. one function publishes to a channel. other functions which subscribe to
# that channel run in turn
# see: https://cloud.google.com/functions/docs/calling/pubsub
# and: https://cloud.google.com/functions/docs/tutorials/pubsub


def hello_pubsub(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict):  The dictionary with data specific to this type of
         event. The `data` field contains the PubsubMessage message. The
         `attributes` field will contain custom attributes if there are any.
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata. The `event_id` field contains the Pub/Sub message ID. The
         `timestamp` field contains the publish time.
    """
    import base64

    print("""This Function was triggered by messageId {} published at {}
    """.format(context.event_id, context.timestamp))

    if 'data' in event:
        name = base64.b64decode(event['data']).decode('utf-8')
    else:
        name = 'World'
    print('Hello {}!'.format(name))
