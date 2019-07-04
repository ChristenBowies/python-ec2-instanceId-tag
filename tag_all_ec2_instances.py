import boto3
import sys

def main():
    
    #init
    ec2_client = boto3.client('ec2')

    #Get EC2 instances per region
    instances = ec2_client.describe_instances()

    #tag all instances
    for i in instances.Reservations.Instances:
        ec2_client.create_tags(
            Resources=[
                i.InstanceId
            ],
            Tags=[
                {
                    'Key': 'instanceid',
                    'Value': i.InstanceId
                }
            ]
        )
if __name__ == '__main__':
    main()
