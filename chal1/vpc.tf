# Creating VPC
resource "aws_vpc" "chal1vpc" {
  cidr_block       = "${var.vpc_cidr}"
  instance_tenancy = "default"

  tags = {
    Name = "Chal1 VPC"
  }
}
