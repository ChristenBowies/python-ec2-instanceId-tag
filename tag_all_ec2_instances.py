import boto3
from argparse import ArgumentParser

#Args
parser = ArgumentParser(description='script to tag all ec2 instances with own instance id')
parser.add_argument('--region',
    action='store_true',
    required=True,
    help='region of ec2 instanes',
    default='us-east-1')
args = parser.parse_args()

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
