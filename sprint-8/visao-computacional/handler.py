import json
import boto3
import botocore
import datetime

def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v1_description(event, context):
    body = {
        "message": "VISION api version 1."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v2_description(event, context):
    body = {
        "message": "VISION api version 2."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
    
def v1Label(event, context):
    # Extract bucket name and image name from the POST request body
    try:
        body = json.loads(event['body'])
        bucket_name = body['bucket']
        image_name = body['imageName']
    except KeyError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Missing required field: {e}'})
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Invalid JSON payload'})
        }
    
    try:
        # S3 connection
        s3_client = boto3.client('s3')
        # Create an Amazon Rekognition client
        rekognition = boto3.client("rekognition")
        
        # Call Amazon Rekognition to detect labels in the image
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket_name, 'Name': image_name}},
            MaxLabels=4  # Change this value for more or fewer labels
        )

        # Extract the detected labels from the response
        labels = [{'confidence': label['Confidence'], 'Name': label['Name']} for label in response["Labels"]]
        
        # Get the metadata of the image object
        response = s3_client.head_object(Bucket=bucket_name, Key=image_name)
        image_url = f"https://{bucket_name}.s3.amazonaws.com/{image_name}"
        creation_time = response['LastModified'].strftime('%d-%m-%Y %H:%M:%S')
        
        # Create a dictionary representing the JSON body
        response_body = {
            "url_to_image": image_url,
            "created_image": creation_time,
            "labels": labels
        }

        # Convert the dictionary to a JSON string
        response_json = json.dumps(response_body)
        
        # Print logs to CloudWatch
        print(response_json)

        # Return the JSON string as the response body of the Lambda function
        return {
            'statusCode': 200,
            'body': response_json
        }
        
    except botocore.exceptions.ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
    
def v2Emotion(event, context):
    
    # Extract name and image name from the POST request body
    try:
        body = json.loads(event['body'])
        bucket_name = body['bucket']
        image_name = body['imageName']

    except KeyError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Missing required field: {e}'})
        }

    except json.JSONDecodeError:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Invalid JSON payload.'})
        }

    # Connection configs
    try:
        # S3 connection
        s3_client = boto3.client('s3')
        # Create an Amazon Rekognition client
        rekognition = boto3.client('rekognition')
    
        response = rekognition.detect_faces(
            Image={'S3Object': {'Bucket': bucket_name, 'Name': image_name}},
            Attributes=['ALL']
        )

        # Get the metadata of the image object
        response_metadata = s3_client.head_object(Bucket=bucket_name, Key=image_name)
        url_to_image = f"https://{bucket_name}.s3.amazonaws.com/{image_name}"
        created_image = response_metadata['LastModified'].strftime('%d-%m-%Y %H:%M:%S')

        # List comprehension that loops to DetectFaces in the response
        faces = [
            {
                "position": {
                    "Height": float(faceDetail["BoundingBox"]["Height"]),
                    "Left": float(faceDetail["BoundingBox"]["Left"]),
                    "Top": float(faceDetail["BoundingBox"]["Top"]),
                    "Width": float(faceDetail["BoundingBox"]["Width"])
                },
                "classified_emotion": faceDetail["Emotions"][0]["Type"],
                "classified_emotion_confidence": float(faceDetail["Emotions"][0]["Confidence"])
            }
            for faceDetail in response['FaceDetails']
        ]

        # This checks if the 'faces' object is empty, if so, returns "Null"
        if (faces == []):
            faces = [
                {
                    "position": {
                        "Height": None,
                        "Left": None,
                        "Top": None,
                        "Width":  None
                    },
                    "classified_emotion": None,
                    "classified_emotion_confidence": None
                }
            ]
            # IF any null values in the repsonse
            response_body = {
                "url_to_image": url_to_image,
                "created_image": created_image,
                "faces": faces
            }

            # Convert the dictionary to a JSON string
            response_json = json.dumps(response_body)

            # Print logs to CloudWatch
            print(response_body)

            return {
                'statusCode': 500,
                'body': response_json
            }
        
        # Constructs the response body
        response_body = {
            "url_to_image": url_to_image,
            "created_image": created_image,
            "faces": faces
        }
        
        # Convert the dictionary to a JSON string
        response_json = json.dumps(response_body)
            
        # Print logs to CloudWatch
        print(response_json)

        return {
            'statusCode': 200,
            'body': response_json
        }

    except botocore.exceptions.ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }