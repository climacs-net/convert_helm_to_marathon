provider "aws" {
  region = "us-east-1"
}

resource "aws_key_pair" "deployer" {
  key_name   = "terraform_aws_key"
  public_key = file("~/.ssh/id_ed25519.pub")
}

resource "aws_instance" "bamboo_demo" {
  ami               = "ami-04ffc9f7871904759" # Ubuntu Server 22.04 LTS (HVM)
  instance_type     = "t3.large"
  availability_zone = "us-east-1b"
  key_name          = aws_key_pair.deployer.key_name

  root_block_device {
    volume_size = 50 # Size in GB
    volume_type = "gp2" # General Purpose SSD
  }

  tags = {
    Name = "bamboo-demo"
  }
}

resource "aws_eip" "bamboo_demo_eip" {
  instance = aws_instance.bamboo_demo.id
}

resource "aws_route53_record" "bamboo_demo" {
  zone_id = "Z3RUW5P7TDNES4" # Replace with your actual Route 53 zone ID
  name    = "bamboodemo.climacs.net" # Corrected domain name without underscore
  type    = "A"
  ttl     = 300
  records = [aws_eip.bamboo_demo_eip.public_ip]
}

output "instance_id" {
  value = aws_instance.bamboo_demo.id
}

output "public_ip" {
  value = aws_eip.bamboo_demo_eip.public_ip
}

output "dns_name" {
  value = aws_route53_record.bamboo_demo.fqdn
}
