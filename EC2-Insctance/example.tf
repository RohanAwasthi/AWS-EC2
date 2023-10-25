provider "aws" {
  region = "us-west-2" # Specify the appropriate region
}

resource "aws_instance" "example" {
  ami                    = "ami-0c55b159cbfafe1f0"  # Specify the appropriate AMI ID
  instance_type          = "t2.micro"  # Specify the instance type
  key_name               = "your_key_pair_name"  # Specify the key pair name
  security_groups        = ["your_security_group_id"]  # Specify the security group ID
  subnet_id              = "your_subnet_id"  # Specify the subnet ID
}
