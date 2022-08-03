# Creating External LoadBalancer
resource "aws_lb" "external-alb" {
  name               = "External-LB"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.chal1sg.id]
  subnets            = [aws_subnet.public-subnet-1.id, aws_subnet.public-subnet-2.id]
}

resource "aws_lb_target_group" "target-elb" {
  name     = "ALB-TG"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.chal1vpc.id
}


resource "aws_lb_listener" "external-elb-listener" {
  load_balancer_arn = aws_lb.external-alb.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.target-elb.arn
  }
}


resource "aws_autoscaling_attachment" "autoscale-attach" {
  autoscaling_group_name = aws_autoscaling_group.chal-asg.id
  alb_target_group_arn   = aws_lb_target_group.target-elb.arn
}
