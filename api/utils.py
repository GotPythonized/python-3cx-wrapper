import json

def make_payload(ObjectId=None, PropertyPath=None, propertyValue=None):
    array = []
    payload = {"Path":{"ObjectId":'',"PropertyPath":[]},"PropertyValue":''}
    if not isinstance(PropertyPath, list):
        PropertyPath = [PropertyPath]
    for path in PropertyPath:
        array.append({"Name":path})
    
    payload['Path']['ObjectId'] = ObjectId
    payload['Path']['PropertyPath'] = array
    payload['PropertyValue'] = propertyValue
    return json.dumps(payload)