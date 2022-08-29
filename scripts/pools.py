#!/usr/bin/env python3


from library import *
from requests.exceptions import HTTPError


if __name__ == '__main__':
    """
    Try to open the file "xspo_pools.json" from the disk.
    If not found, open the file from the Github repository 
    and get the data for every stake pool from the Koios API.
    """
    try:
        with open('xspo_pools.json', 'r') as f:
            xspo_pools = json.loads(f.read())
    except FileNotFoundError as err:
        print(err)
        print('Opening the file from the Github repository')
        members = {}
        try:
            response = requests.get(JSON_URL)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            exit(1)
        except Exception as err:
            print(f'Other error occurred: {err}')
            exit(1)
        else:
            print('Success!')
            members = json.loads(response.content)['adapools']['members']

        xspo_pools = {}
        for item in members.keys():
            # fill the stake pool data
            member = members[item]
            pool = {}
            pool['pool_id'] = member['pool_id']
            pool['pool_id_bech32'] = decode_pool_id(member['pool_id'])
            pool['name'] = member['name']
            print(pool['name'])
            pool_info = get_pool_info(pool['pool_id_bech32'])[0]
            pool['metadata'] = pool_info['meta_json']
            if pool['metadata'] and 'ticker' in pool['metadata']:
                pool['ticker'] = pool_info['meta_json']['ticker']
            else:
                pool['ticker'] = ''
            pool['status'] = pool_info['pool_status']
            # add the stake pool to the xspo_pools dictionary
            # by the "status" key
            if pool['status'] not in xspo_pools:
                xspo_pools[pool['status']] = []
            xspo_pools[pool['status']].append(pool)

        with open('xspo_pools.json', 'w') as f:
            f.write(json.dumps(xspo_pools, indent=2))

    active_pools = []
    active_pools_bech32 = []
    for pool_status in xspo_pools.keys():
        print('%d %s pools' % (len(xspo_pools[pool_status]), pool_status))
        with open('xspo_' + pool_status + '_pools.json', 'w') as f:
            f.write(json.dumps(xspo_pools[pool_status], indent=2))
        if pool_status == 'registered':
            for pool in xspo_pools[pool_status]:
                active_pools.append(pool['pool_id'])
                active_pools_bech32.append(pool['pool_id_bech32'])

    """
    Generate the "xSPO-list-cexplorer.json" file for cexplorer.io
    """
    with open('xSPO-list-cexplorer.json', 'w') as f:
        f.write(json.dumps(active_pools_bech32, indent=0))

    """
    """
    try:
        with open('xspo-alliance-members.json', 'r') as f:
            xspo_members = json.loads(f.read())
    except FileNotFoundError as err:
        print(err)
        print('Opening the file from the Github repository')
        xspo_members = {}
        try:
            response = requests.get(JSON_URL)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            exit(1)
        except Exception as err:
            print(f'Other error occurred: {err}')
            exit(1)
        else:
            print('Success!')
            xspo_members = json.loads(response.content)

    active_xspo_members = {}
    for item in xspo_members['adapools']['members'].keys():
        if xspo_members['adapools']['members'][item]['pool_id'] in active_pools:
            active_xspo_members[item] = xspo_members['adapools']['members'][item]
    xspo_members['adapools']['members'] = active_xspo_members
    """
    Generate the "xspo-alliance-members.json" file
    """
    with open('xspo-alliance-members.json', 'w') as f:
        f.write(json.dumps(xspo_members, indent=2))
