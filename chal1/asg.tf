resource "aws_launch_configuration" "chal-asg-lc" {
  name   = "chal1-asg-config"
  image_id      = "ami-090fa75af13c156b4"
  instance_type = "t2.micro"
  security_groups      = ["${aws_security_group.chal1sg.id}"]
  associate_public_ip_address = true
  user_data                   = "${file("user-data.sh")}"
  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "chal-asg" {
  name = "chal-asg-instances"
  vpc_zone_identifier = [aws_subnet.public-subnet-1.id, aws_subnet.public-subnet-2.id]
  desired_capacity   = 2
  max_size           = 2
  min_size           = 2
  tag {
    key = "Name"
    value = "asg-web-server"
    propagate_at_launch = true
  } 

  launch_configuration = aws_launch_configuration.chal-asg-lc.name 
  lifecycle {
    create_before_destroy = true
  }
}
