## What is it?
This small serverless application is an example of how to deal with additional costs made by SQS trigger for 
Lambda functions at AWS.

If you have SQS queue with trigger for Lambda function and you are not sending messages to queue the Lambda is still 
polling for messages (using long-polling). It causes the metric **NumberOfEmptyReceives** to grow.

It makes:
- 15 requests per minute,
- 900 requests per hour,
- 21.600 requests per day,
- 669.600 requests per month. 

An application is set of services: Event Bridge rule with Lambda trigger based on event pattern.

## How it works?
1. Event Bridge rule is triggering the function.
2. Lambda gets the event of desired Lambda (using **list_event_source_mapping**).
3. It extracts a status of an event and converts it (string -> bool).
4. Using **update_event_source_mapping** it toggles the event state.

## How to use it? (*SAM CLI*)
1. Change event pattern in **template.yaml**
2. `sam build` or (if doesn't work) `sam build --use-container` (it uses Docker)
3. `sam deploy -g`