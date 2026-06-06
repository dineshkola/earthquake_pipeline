# earth_quake_pipeline
this pipeline connects the publish API to collect the last 24 hours earthquake information , transforms and writes into an s3 bucket

Phase 1 Task Breakdown
Create a logger object.
Set the logging level to DEBUG.
Add a stream handler to output logs to the terminal (a formatter is optional for the initial version).
Encapsulate the logging logic within a custom class or function.
Save the implementation in a standalone file named dk_logging.py.
Commit the file to the Git repository under the common/ directory.
Update extract.py to import dk_logging.py, initialize logging, and configure the pipeline to save logs locally or to the repository.
Integrate logging into transform.py and enable DEBUG-level logging.
Execute the pipeline (e.g., via Airflow) and verify output in Amazon Athena, ensuring the Athena external schema aligns with the S3 Parquet file structure.
Run the pipeline multiple times to confirm consistent log capture.
