import json
import boto3
import uuid
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    #logger.info(json.dumps(event))
    #print(json.dumps(event))

    foodScore = event['currentIntent']['slots']['foodScore']
    experienceWord = event['currentIntent']['slots']['experienceWord']

    AWS_BUCKET_NAME = 'd1-feedback-raw'
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(AWS_BUCKET_NAME)
    seed = str(uuid.uuid4())
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S")

    data = json.dumps(event)
    path = seed+'-taco.json'
    bucket.put_object(
        ACL='public-read',
        ContentType='application/json',
        Key=path,
        Body=data,
    )

    data = 'food score,experience word\n"'+foodScore+'","'+experienceWord+'"'
    #data = 'food score,experience word,current time\n"'+foodScore+'","'+experienceWord+'",'+currentTime
    path = seed+'-taco.csv'
    bucket.put_object(
        ACL='public-read',
        ContentType='text/csv',
        Key=path,
        Body=data,
    )

    responseMessages = {
        '1': 'I am very sorry the experience we provided did not meet your expectations. Use code C U R D on your next purchase for a free taco meal.',
        '2': 'I am sorry the experience we provided did not meet your expectations. Use code H O T on your next purchase for a free taco.',
        '3': 'We appreciate your feedback. If you have any suggestions on ways we can improve, please e-mail curd at oktank dot com.',
        '4': 'Thank you for your feedback. On behalf of your CEO, Curd Zeckm I ster, have a hot taco day!',
        '5': 'Thank you for your feedback. On behalf of your CEO, Curd Zeckm I ster, have a hot taco day!'
    }

    response = {
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': {
                'contentType': 'PlainText',
                'content': responseMessages.get(foodScore, 'Thank you for your feedback.')
            }
        }
    }
    return response
