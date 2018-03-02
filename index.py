from __future__ import print_function
import json
import boto3
import logging
import time
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    #logger.info('Event: ' + str(event))
    #print('Received event: ' + json.dumps(event, indent=2))

    try:
        region = event['region']
        detail = event['detail']
        eventname = detail['eventName']
        arn = detail['userIdentity']['arn']
        principal = detail['userIdentity']['principalId']
        userType = detail['userIdentity']['type']
        eventTime = detail['eventTime']
        bucketACL = detail['requestParameters']
        s3BucketName = detail['requestParameters']['bucketName']

        if userType == 'IAMUser':
            user = detail['userIdentity']['userName']

        else:
            user = principal.split(':')[1]

        logger.info('detail: ' + str(detail))
        logger.info('principalId: ' + str(principal))
        logger.info('region: ' + str(region))
        logger.info('eventName: ' + str(eventname))  
        logger.info('bucketName: ' + str(s3BucketName))     
        logger.info('userName: ' + str(detail['userIdentity']['userName']))

        s3 = boto3.resource('s3')

        if eventname == 'CreateBucket':
            bucket = s3.Bucket(s3BucketName)
            bucket.Acl().put(ACL='private')
            logger.info('S3 bucket vaulted: ' + s3BucketName)
                        
        else:
            logger.warning('Not supported action')

        logger.info(' Remaining time (ms): ' + str(context.get_remaining_time_in_millis()) + '\n')
        return True
    except Exception as e:
        logger.error('Something went wrong: ' + str(e))
        return False