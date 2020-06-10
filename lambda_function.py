import boto3

client = boto3.client('lambda')


def toggle_event_state(function: str) -> None:
    """
    Toggles state of the Lambda function event

    :param function: ARN, Version/Alias ARN, Name
    """
    event = get_event(function)
    state = get_state(event['State'])

    response = client.update_event_source_mapping(
        UUID=event['UUID'],
        FunctionName=function,
        Enabled=not state,
    )
    print('EVENT TOGGLED FOR ', response['FunctionArn'])


def get_event(function: str) -> dict:
    """
    Checks for Lambda function trigger events

    :param function: ARN, Version/Alias ARN, Name
    :return: event
    """
    response = client.list_event_source_mappings(
        FunctionName=function,
    )
    return next(iter(response['EventSourceMappings']))


def get_state(state: str) -> bool:
    return True if state == 'Enabled' else False


def lambda_handler(event, context):
    func_names = ['scraper-tender-saver', 'scraper-mail-sender']
    for name in func_names:
        toggle_event_state(name)
