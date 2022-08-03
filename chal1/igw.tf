# Creating Internet Gateway 
resource "aws_internet_gateway" "chal1gateway" {
  vpc_id = "${aws_vpc.chal1vpc.id}"
}