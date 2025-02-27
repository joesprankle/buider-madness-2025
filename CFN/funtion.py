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
        
        # Get vehicle information
        vehicle_info = body.get('vehicleInfo', {})
        logger.info(f"Vehicle information received: {vehicle_info}")
        
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
        
        # Upload to S3 
        try:
            # Add vehicle info as metadata if provided
            metadata = {}
            if vehicle_info:
                if 'brand' in vehicle_info and vehicle_info['brand']:
                    metadata['brand'] = vehicle_info['brand']
                if 'model' in vehicle_info and vehicle_info['model']:
                    metadata['model'] = vehicle_info['model']
                if 'year' in vehicle_info and vehicle_info['year']:
                    metadata['year'] = vehicle_info['year']
            
            response = s3.put_object(
                Bucket=bucket_name,
                Key=filename,
                Body=image_data,
                ContentType=content_type,
                ContentDisposition='inline',
                Metadata=metadata
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
        
        # Generate dummy data payload based on the CSV
        dummy_data = [
            {
                "part_id": "P123456",
                "alternative_parts": [
                    {"S": "P987654"},
                    {"S": "P654321"}
                ],
                "car_make": vehicle_info.get('brand', 'Toyota'),
                "car_model_year_part": f"{vehicle_info.get('model', 'Camry')}#{vehicle_info.get('year', '2021')}#Brake Pad",
                "category": "Brakes",
                "location": "Aisle 3, Shelf B",
                "part_name": "Brake Pad",
                "price": "49.99",
                "provider": "Bosch"
            },
            {
                "part_id": "P234567",
                "alternative_parts": [
                    {"S": "P876543"},
                    {"S": "P765432"}
                ],
                "car_make": vehicle_info.get('brand', 'Honda'),
                "car_model_year_part": f"{vehicle_info.get('model', 'Civic')}#{vehicle_info.get('year', '2022')}#Oil Filter",
                "category": "Engine",
                "location": "Aisle 1, Shelf C",
                "part_name": "Oil Filter",
                "price": "12.99",
                "provider": "Fram"
            },
            {
                "part_id": "P345678",
                "alternative_parts": [
                    {"S": "P765432"},
                    {"S": "P543219"}
                ],
                "car_make": vehicle_info.get('brand', 'Ford'),
                "car_model_year_part": f"{vehicle_info.get('model', 'F-150')}#{vehicle_info.get('year', '2020')}#Air Filter",
                "category": "Engine",
                "location": "Aisle 2, Shelf A",
                "part_name": "Air Filter",
                "price": "24.50",
                "provider": "K&N"
            },
            {
                "part_id": "P456789",
                "alternative_parts": [
                    {"S": "P654321"},
                    {"S": "P432198"}
                ],
                "car_make": vehicle_info.get('brand', 'Chevrolet'),
                "car_model_year_part": f"{vehicle_info.get('model', 'Silverado')}#{vehicle_info.get('year', '2019')}#Spark Plug",
                "category": "Ignition",
                "location": "Aisle 4, Shelf D",
                "part_name": "Spark Plug",
                "price": "8.75",
                "provider": "NGK"
            },
            {
                "part_id": "P567890",
                "alternative_parts": [
                    {"S": "P543210"},
                    {"S": "P321098"}
                ],
                "car_make": vehicle_info.get('brand', 'Nissan'),
                "car_model_year_part": f"{vehicle_info.get('model', 'Altima')}#{vehicle_info.get('year', '2023')}#Wiper Blade",
                "category": "Exterior",
                "location": "Aisle 5, Shelf E",
                "part_name": "Wiper Blade",
                "price": "19.99",
                "provider": "Rain-X"
            }
        ]
        
        # Return success response with dummy data
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({
                'message': 'Image uploaded successfully',
                'imageUrl': image_url,
                'filename': filename,
                'vehicleInfo': vehicle_info,  # Return the vehicle info in the response
                'data': dummy_data
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