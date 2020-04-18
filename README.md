This project uses python 3.7.0

The html templates used in this project are the free MD Bootstrap 
ecommerce template files

some part of the code is taken from this link
https://github.com/justdjango/django-ecommerce

The uploaded image files are stored in AWS s3 bucket.

So you need the following AWS keys

AWS_ACCESS_KEY_ID = 'your AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'your AWS_SECRET_ACCESS_KEY'
AWS_STORAGE_BUCKET_NAME = 'your AWS_STORAGE_BUCKET_NAME'

#set your region
AWS_S3_REGION_NAME = 'ap-south-1'
AWS_S3_SIGNATURE_VERSION = 's3v4'

You also need Stripe keys to test stripe payment integration

STRIPE_SECRET_KEY= "your STRIPE_SECRET_KEY"
STRIPE_PUBLISHABLE_KEY= "your STRIPE_PUBLISHABLE_KEY"

To test on live server change the allowed hosts in production.py
ALLOWED_HOSTS =['your web url']