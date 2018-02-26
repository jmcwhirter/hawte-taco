# Overview

This project was put together in less than 12 hours to demonstrate some AWS services.

1. User calls 1-800 number provided by [Amazon Connect](https://aws.amazon.com/connect/)
2. Connect handles the incoming call and does some simple routing. The routing is handled via a drag-and-drop UI.
3. Connect hands off to [Amazon Lex](https://aws.amazon.com/lex/) where we have an intent defined. The intent contains two variables we have configured it to collect; a numeric rating and an experience word.
4. Lex calls an [AWS Lambda](https://aws.amazon.com/lambda/) function that parses the JSON to get the rating and word.
  1. Lambda creates a CSV file and sends it to S3.
  2. Lambda constructs a feedback message and delivers it to the caller via Lex.
5. [Amazon Simple Storage Service](https://aws.amazon.com/s3/) is used to store all data in this process.
6. Business users load data into [QuickSight](https://aws.amazon.com/quicksight/) for analysis and report generation.

![Architecture](documentation/hawte_taco_arch.png)

Files provided:

- [x] Draw.io [architecture diagram](documentation/hawte_taco_arch.xml)
- [x] [Lambda code](lambda_function.py)
- [ ] [CodeFormation](https://aws.amazon.com/cloudformation/) template
- [ ] Script to generate sample data
