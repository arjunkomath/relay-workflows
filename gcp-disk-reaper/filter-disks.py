#!/usr/bin/env python
from nebula_sdk import Interface, Dynamic as D

relay = Interface()

if __name__ == '__main__':
    to_terminate = []

    disks = relay.get(D.disks)
    for disk in disks:
        if "users" not in disk.keys():
            to_terminate.append(disk)

    print('Found {} disks that are unattached'.format(len(to_terminate)))
    print('Setting output `disks` to list of {} disks to terminate'.format(len(to_terminate)))

    relay.outputs.set('disks', to_terminate)
