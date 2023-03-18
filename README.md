# 1.Data Engineer Natuzzi - Study Case

## Natuzzi
This project is a study case of data engineering for Natuzzi, a furniture company. The goal is to create an end-to-end data pipeline to transform and process the transactional data generated by the company. This pipeline will support further analysis and visualization of the data.

### Data Pipeline Steps
1. Terraform was used to provision the cloud infrastructure required for the pipeline.
2. GitHub Actions served as a CI/CD platform for the Terraform infrastructure.
3. Python was used to generate dummy data for modeling a transactional database based on the business context.
4. The generated data was stored in an AWS RDS instance, simulating a transactional database.
5. AWS DMS was employed to transfer the data from RDS to an S3 Landing Zone.
6. The data from the S3 landing was processed using AWS Glue Job Spark, transforming it into parquet format.
7. The processed parquet data was stored in an S3 Data Lake Processed Zone.
8. The data was loaded into an AWS Redshift Data Warehouse for analytical purposes.
9. DBT was utilized to transform the Redshift tables into a single denormalized table.
10. The resulting denormalized table was stored in a Data Lake Curated Zone.
11. Finally, the entire pipeline was orchestrated using Apache Airflow, deployed on a Kubernetes cluster.

### Pipeline Diagram
![alt text](https://github.com/makima0499/1.Data-Engineer/blob/main/1.DataPipeline.png)

### Data Engineer Tools
* Python
* Airflow
* Terraform
* Github Actions
* K8S
* DBT
* AWS RDS
* AWS DMS 
* AWS S3
* AWS Glue Job
* AWS Redshift

### Note
This repository is provided for study purposes only, focusing on data engineering pipelines.

## License

[MIT](https://choosealicense.com/licenses/mit/)
