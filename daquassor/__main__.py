#!/usr/bin/env python

"Main executable file"

if __name__ == '__main__':
    msg_components = [
        '',
        'Hello user.',
        '',
        'I ran and did nothing.',
        'At least I loaded fine :).',
        '',
        'Have a good day.',
        '',
    ]
    msg = '\n'.join(msg_components)
    print(msg)
