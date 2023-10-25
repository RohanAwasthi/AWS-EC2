# EC2 Instance Creation with Boto3 and Terraform

This repository contains Python and Terraform scripts for creating an EC2 instance on AWS using the Boto3 library and Terraform, respectively.

## EC2.py

The `EC2.py` file is a Python script that utilizes the Boto3 library to launch a new EC2 instance on AWS. The script includes the following parameters:

- AWS region: us-west-2
- AMI ID: ami-0c55b159cbfafe1f0
- Instance type: t2.micro
- Key pair name: your_key_pair_name
- Security group ID: your_security_group_id
- Subnet ID: your_subnet_id

## example.tf

The `example.tf` file is a Terraform script that achieves the same task as the Python script. It creates an AWS EC2 instance with the following specifications:

- AWS region: us-west-2
- AMI ID: ami-0c55b159cbfafe1f0
- Instance type: t2.micro
- Key pair name: your_key_pair_name
- Security group ID: your_security_group_id
- Subnet ID: your_subnet_id

Feel free to use these scripts as a starting point for your own AWS EC2 instance creation. Make sure to replace the placeholder values with your actual AWS parameters.

## Prerequisites

- Python 3.x
- Boto3 library
- Terraform

## Usage

You can run the `EC2.py` script using Python, and the `example.tf` script using Terraform. Follow the comments within the scripts for any necessary modifications.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
