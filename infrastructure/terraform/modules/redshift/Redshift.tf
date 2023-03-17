resource "aws_redshift_cluster" "example" {
  cluster_identifier = "tf-redshift-cluster"
  database_name      = "dev"
  master_username    = "wu1userredshift"
  master_password    = "Wu1passredshift"
  node_type          = "dc2.large"
  cluster_type       = "single-node"
  skip_final_snapshot  = true
  publicly_accessible  = true

  # iam_roles = ["arn:aws:iam::222498481656:role/service-role/AmazonRedshift-CommandsAccessRole-20230315T175615"]
}