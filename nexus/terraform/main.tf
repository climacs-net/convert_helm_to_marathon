provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "nexus_demo" {
  ami               = "ami-04ffc9f7871904759" # Ubuntu Server 22.04 LTS (HVM)
  instance_type     = "t2.medium"
  availability_zone = "us-east-1b"
  key_name          = "terraform_aws_key"  # Use the name of your existing key pair

  root_block_device {
    volume_size = 50 # Size in GB
    volume_type = "gp2" # General Purpose SSD
  }

  tags = {
    Name = "nexus-demo"
  }
}

resource "aws_eip" "nexus_demo_eip" {
  instance = aws_instance.nexus_demo.id
}

resource "aws_route53_record" "nexus_demo" {
  zone_id = "Z3RUW5P7TDNES4"
  name    = "nexusdemo.climacs.net"
  type    = "A"
  ttl     = 300
  records = [aws_eip.nexus_demo_eip.public_ip]
}

output "instance_id" {
  value = aws_instance.nexus_demo.id
}

output "public_ip" {
  value = aws_eip.nexus_demo_eip.public_ip
}

output "dns_name" {
  value = aws_route53_record.nexus_demo.fqdn
}
