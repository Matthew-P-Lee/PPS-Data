import boto
import os

# Fill these in - you get them when you sign up for S3
AWS_ACCESS_KEY_ID = 'AKIAIUHMTMNCIAHE5V6Q'
AWS_SECRET_ACCESS_KEY = '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'

bucket_name = AWS_ACCESS_KEY_ID.lower() + '-vistaseeker.com'

source_directory = os.path.dirname(os.path.abspath(__file__))+'/source-data/'
filename = "Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG_.csv"

conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
            AWS_SECRET_ACCESS_KEY)

bucket = conn.create_bucket(bucket_name,
        location=boto.s3.connection.Location.DEFAULT)

print 'Uploading %s to Amazon S3 bucket %s' % \
       (filename, bucket_name)

import sys
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

from boto.s3.key import Key

key_name = 'IPPS-data.csv'
path = '/IPPS-data'
full_key_name = os.path.join(path, key_name)
k = bucket.new_key(full_key_name)

k.set_contents_from_filename(source_directory+filename,
        cb=percent_cb, num_cb=10)