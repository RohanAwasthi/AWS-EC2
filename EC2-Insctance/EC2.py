import boto3

# Specify the AWS region
ec2 = boto3.client('ec2', region_name='us-west-2')

# Launch a new EC2 instance
instance = ec2.run_instances(
    ImageId='ami-0c55b159cbfafe1f0',  # Specify the appropriate AMI ID
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',  # Specify the instance type
    KeyName='your_key_pair_name',  # Specify the key pair name
    SecurityGroupIds=['your_security_group_id'],  # Specify the security group ID
    SubnetId='your_subnet_id'  # Specify the subnet ID
)

print(f"New instance created with ID: {instance['Instances'][0]['InstanceId']}")
