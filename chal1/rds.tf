# Creating RDS Instance
resource "aws_db_subnet_group" "rds-subnet-grp" {
  name       = "main"
  subnet_ids = [aws_subnet.database-subnet-1.id, aws_subnet.database-subnet-2.id]

  tags = {
    Name = "DB subnet group"
  }
}

resource "aws_db_instance" "default" {
  allocated_storage      = 10
  db_subnet_group_name   = aws_db_subnet_group.rds-subnet-grp.id
  engine                 = "mysql"
  engine_version         = "8.0.20"
  instance_class         = "db.t2.micro"
  multi_az               = false
  name                   = "chal1db"
  username               = "chal1"
  password               = "FaceYourFears"
  skip_final_snapshot    = true
  vpc_security_group_ids = [aws_security_group.database-sg.id]
}