import csv
import os
import nexmo

def send_msg_batch(sms_from, targets):
    API_KEY = os.environ.get('NEXMO_API_KEY')
    API_SECRET = os.environ.get('NEXMO_API_SECRET')
    client = nexmo.Client(key=API_KEY, secret=API_SECRET)

    for target in targets:
        result = client.send_message({
            'from': sms_from,
            'to': target['number'],
            'text': target['text'],
        })
        print(result)


def load_target_numbers():
    with open('targets.csv', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        targets = [{ 'number': row['number'], 'text': row['text'] } for row in rows]
    return targets

if __name__ == '__main__':
    SMS_FROM = os.environ.get('SMS_FROM')
    targets = load_target_numbers()
    print('The first 10 targets...')
    print('\n'.join(str(t) for t in targets[:10]))
    ans = input('Sure? Enter "y" to proceed. ')
    if ans == 'y':
        print('Sending...')
        send_msg_batch(SMS_FROM, targets)
    else:
        print('Cancel.')
