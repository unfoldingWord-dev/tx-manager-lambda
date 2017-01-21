# Method for handling the starting of jobs that have been queued in the tx-job table

from __future__ import print_function

from tx_manager.tx_manager import TxManager

def handle(event, context):
    print("------------PROCESSING DB STREAM---------------------")
    for record in event['Records']:
        try:
            if record['eventName'] == 'INSERT' and 'job_id' in record['dynamodb']['Keys']:
                print(record['eventID'])
                print(record['eventName'])
                job_id = record['dynamodb']['Keys']['job_id']['S']
                TxManager().start_job(job_id)
        except Exception as e:
            print("Failed for record:")
            print(record)
            print("Error:")
            print(e)
    print("------------END PROCESSING DB STREAM---------------------")
