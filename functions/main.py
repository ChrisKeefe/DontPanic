from google.cloud import firestore


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
    postFlag = ""
    # TODO: sanitize inputs

    # get_json gets a json object if exists, else returns None
    request_json = request.get_json(silent=True)
    # args is a multidict, which can be indexed like request_args[key]
    request_args = request.args
    if request_json and 'messagePayload' in request_json:
        payload = request_json['messagePayload']
        postFlag = "POST"
    elif request_args and 'messagePayload' in request_args:
        payload = request_args['messagePayload']
        postFlag = "GET"
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
    return f"Request successful: Message added to DB via {postFlag}"


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
    postFlag = ""

    # get_json gets a json object if exists, else returns None
    request_json = request.get_json(silent=True)
    # args is a multidict, which can be indexed like request_args[key]
    request_args = request.args
    if request_json and 'profilePayload' in request_json:
        payload = request_json['profilePayload']
        postFlag = "POST"
    elif request_args and 'profilePayload' in request_args:
        payload = request_args['profilePayload']
        postFlag = "GET"
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
    return f"Request successful: Profile added to DB via {postFlag}"


def create_user(request):
    """ Adds/updates a User document to the messages collection in firestore
    Used to keep device tokens up-to-date
    Preconditions: receives a POST request of content-type 'application/json'
        format:
        {
          "userPayload":{
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
    postFlag = ""

    # get_json gets a json object if exists, else returns None
    request_json = request.get_json(silent=True)
    # args is a multidict, which can be indexed like request_args[key]
    request_args = request.args

    if request_json and 'userPayload' in request_json:
        payload = request_json['userPayload']
        postFlag = "POST"
    elif request_args and 'userPayload' in request_args:
        payload = request_args['userPayload']
        postFlag = "GET"
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
    return f"Request successful: User added to DB via {postFlag}"
