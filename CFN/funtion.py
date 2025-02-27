import json
import base64
import boto3
import os
import logging
from datetime import datetime

# Set up logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Log the event for debugging
        logger.info(f"Received event: {event}")
        
        # Get environment variables
        bucket_name = os.environ.get('BUCKET_NAME')
        logger.info(f"Using bucket: {bucket_name}")
        
        # Parse the request body
        try:
            if 'body' in event:
                body = json.loads(event['body'])
            else:
                logger.error("No body in event")
                body = {}
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing error: {str(e)}")
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Invalid JSON in request body'})
            }
        
        # Get image data
        base64_image = body.get('image')
        if not base64_image:
            logger.error("No image data in request")
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'No image data provided'})
            }
        
        filename = body.get('filename', f"image-{int(datetime.now().timestamp())}")
        content_type = body.get('contentType', 'image/jpeg')
        logger.info(f"Processing image with filename: {filename}, content_type: {content_type}")
        
        # Remove data URL prefix if present (e.g., data:image/jpeg;base64,)
        try:
            if ',' in base64_image:
                base64_image = base64_image.split(',', 1)[1]
        except Exception as e:
            logger.error(f"Error processing data URL: {str(e)}")
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Invalid image data format'})
            }
        
        # Decode base64 image
        try:
            image_data = base64.b64decode(base64_image)
            logger.info(f"Successfully decoded image, size: {len(image_data)} bytes")
        except Exception as e:
            logger.error(f"Base64 decoding error: {str(e)}")
            return {
                'statusCode': 400,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': 'Invalid base64 encoding'})
            }
        
        # Upload to S3 WITHOUT ACL parameter
        try:
            response = s3.put_object(
                Bucket=bucket_name,
                Key=filename,
                Body=image_data,
                ContentType=content_type,
                ContentDisposition='inline'
                # Removed ACL='public-read' parameter
            )
            logger.info(f"S3 upload successful: {response}")
        except Exception as e:
            logger.error(f"S3 upload error: {str(e)}")
            return {
                'statusCode': 500,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({
                    'error': 'Failed to upload to S3',
                    'details': str(e)
                })
            }
        
        # Generate URL for the uploaded image
        image_url = f"https://{bucket_name}.s3.amazonaws.com/{filename}"
        logger.info(f"Image URL: {image_url}")
        
        # Return success response
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'message': 'Image uploaded successfully',
                'imageUrl': image_url,
                'filename': filename
            })
        }
        
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        
        # Return error response
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'error': 'Failed to process image upload',
                'details': str(e)
            })
        }