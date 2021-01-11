import boto3

def uploadPicture(photoPath):
    bucket_name = "shigeoka"
    s3 = boto3.resource('s3')

    s3.Bucket(bucket_name).upload_file(photoPath,photoPath)


def detect_labels(photo, bucket):

    client=boto3.client('rekognition')

    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
        MaxLabels=10)

    print('Detected labels for ' + photo) 
    print()
    for label in response['Labels']:
        print ("Label: " + label['Name'])
        print ("Confidence: " + str(label['Confidence']))
        print ("Instances:")
        for instance in label['Instances']:
            print ("  Bounding box")
            print ("    Top: " + str(instance['BoundingBox']['Top']))
            print ("    Left: " + str(instance['BoundingBox']['Left']))
            print ("    Width: " +  str(instance['BoundingBox']['Width']))
            print ("    Height: " +  str(instance['BoundingBox']['Height']))
            print ("  Confidence: " + str(instance['Confidence']))
            print()

        print ("Parents:")
        for parent in label['Parents']:
            print ("   " + parent['Name'])
        print ("----------")
        print ()
    return len(response['Labels'])

def getlavels(path):
    uploadPicture('app/static/uploads/'+path)
    client=boto3.client('rekognition')
    response = client.detect_labels(Image={'S3Object':{'Bucket':'shigeoka','Name':path}},
        MaxLabels=5)
    return response['lavels']

if __name__ == "__main__":
    uploadPicture('app/static/images/pancake.jpg')
    label_count=detect_labels('server.jpg','shigeoka')
    print("Labels detected: " + str(label_count))
    #app.run(debug=True)