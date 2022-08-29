import subprocess
import json
import requests
from config import *
from time import sleep


def get_tip():
    """
    Get the tip info about the latest block seen by chain
    """
    url = API_BASE_URL + '/tip'
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_genesis():
    """
    Get the Genesis parameters used to start specific era on chain
    """
    url = API_BASE_URL + '/genesis'
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_totals(epoch=0):
    """
    Get the circulating utxo, treasury, rewards, supply and reserves in lovelace for specified epoch,
    or for all epochs if epoch is empty.
    """
    url = API_BASE_URL + '/totals'
    if isinstance(epoch, int) and epoch > 0:
        url += '?_epoch_no=%d' % epoch
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_epoch_info(epoch=0):
    """
    Get the epoch information, all epochs if no epoch specified
    """
    url = API_BASE_URL + '/epoch_info'
    if isinstance(epoch, int) and epoch > 0:
        url += '?_epoch_no=%d' % epoch
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_epoch_params(epoch=0):
    """
    Get the protocol parameters for specific epoch, returns information about all epochs if no epoch specified
    """
    url = API_BASE_URL + '/epoch_params'
    if isinstance(epoch, int) and epoch > 0:
        url += '?_epoch_no=%d' % epoch
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_blocks(limit=1000):
    """
    Block List
    """
    url = API_BASE_URL + '/blocks?limit=%d' % limit
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_block_info(blocks):
    """
    Blocks Information
    """
    url = API_BASE_URL + '/block_info'
    block_hashes = {}
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    block_hashes['_block_hashes'] = blocks
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(block_hashes)).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_block_txs(block):
    """
    Block Transactions
    """
    url = API_BASE_URL + '/block_txs?_block_hash=%s' % block
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_tx_info(txs):
    """
    Transaction Information
    """
    url = API_BASE_URL + '/tx_info'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    tx_hashes = {'_tx_hashes': txs}
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(tx_hashes)).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_tx_utxos(txs):
    """
    Transaction UTxOs
    """
    url = API_BASE_URL + '/tx_utxos'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    tx_hashes = {'_tx_hashes': txs}
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(tx_hashes)).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_tx_metadata(txs):
    """
    Get metadata information (if any) for given transaction(s)
    """
    url = API_BASE_URL + '/tx_metadata'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    tx_hashes = {'_tx_hashes': txs}
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(tx_hashes)).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_tx_metalabels():
    """
    Get a list of all transaction metadata labels
    """
    url = API_BASE_URL + '/tx_metalabels'
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_tx_status(txs):
    """
    Transaction Status (Block Confirmations)
    """
    url = API_BASE_URL + '/tx_status'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    tx_hashes = {'_tx_hashes': txs}
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(tx_hashes)).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_address_info(addr):
    """
    Address Information
    """
    url = API_BASE_URL + '/address_info?_address=%s' % addr
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_address_txs(addr):
    """
    Address Transactions
    """
    url = API_BASE_URL + '/address_txs'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    addresses = {'_addresses': addr}
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(addresses)).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_account_info(addr):
    """
    Account Information
    """
    url = API_BASE_URL + '/account_info?_address=%s' % addr
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_account_history(addr):
    """
    Account history
    """
    url = API_BASE_URL + '/account_history?_address=%s' % addr
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_account_addresses(addr):
    """
    Stake Address Payment Addresses
    """
    url = API_BASE_URL + '/account_addresses?_address=%s' % addr
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_account_assets(addr):
    """
    Stake Address (account) Assets
    """
    url = API_BASE_URL + '/account_assets?_address=%s' % addr
    assets = []
    offset = 0
    while True:
        paginated_url = url + '&offset=%d' % offset
        while True:
            try:
                resp = json.loads(requests.get(paginated_url).text)
                break
            except Exception as e:
                print(e)
                sleep(1)
                print('retrying...')
        assets += resp
        if len(resp) < 1000:
            break
        else:
            offset += len(resp)
    return assets


def get_pools_list():
    """
    # Get the list of stake pools
    :return: pool_list
    """
    url = API_BASE_URL + '/pool_list'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    pools_list = []
    offset = 0
    while True:
        paginated_url = url + '?offset=%d' % offset
        while True:
            try:
                resp = json.loads(requests.get(paginated_url, headers=headers).text)
                break
            except Exception as e:
                print(e)
                sleep(1)
                print('retrying...')
        pools_list += resp
        if len(resp) < 1000:
            break
        else:
            offset += len(resp)
    return pools_list


def get_pool_info(pool_id):
    """
    # Get the stake pool information
    :param pool_id:
    :return: pool_info
    """
    url = API_BASE_URL + '/pool_info'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    pool_ids = {'_pool_bech32_ids': [pool_id]}
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(pool_ids)).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_pool_history(pool_id):
    """
    # Get the stake pool history information
    :param pool_id:
    :return: pool_history
    """
    url = API_BASE_URL + '/pool_history?_pool_bech32=%s' % pool_id
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_pool_delegators(pool_id, epoch=0):
    """
    Get the stake pool delegators list
    """
    url = API_BASE_URL + '/pool_delegators?_pool_bech32=%s' % pool_id
    if epoch != 0:
        url += '&_epoch_no=' + str(epoch)

    delegators = []
    offset = 0
    while True:
        paginated_url = url + '&offset=%d' % offset
        while True:
            try:
                resp = json.loads(requests.get(paginated_url).text)
                break
            except Exception as e:
                print(e)
                sleep(1)
                print('retrying...')
        delegators += resp
        if len(resp) < 1000:
            break
        else:
            offset += len(resp)
    return delegators


def get_asset_list(policy):
    """
    :param policy: Asset Policy
    :return: List of assets with the specified policy
    """
    url = API_BASE_URL + '/asset_list?policy_id=eq.%s' % policy
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    asses_names_hex = []
    while True:
        try:
            resp = json.loads(requests.get(url, headers=headers).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    for item in resp[0]['asset_names']['hex']:
        asses_names_hex.append(item)
    return asses_names_hex


def get_asset_address_list(policy, name):
    """
    :param policy: Asset Policy
    :param name: Asset Name
    :return: List of wallets holding the asset and the amount of assets per wallet
    """
    url = API_BASE_URL + '/asset_address_list?_asset_policy=%s&_asset_name=%s' % (policy, name)
    wallets = []
    offset = 0
    while True:
        paginated_url = url + '&offset=%d' % offset
        while True:
            try:
                resp = json.loads(requests.get(paginated_url).text)
                break
            except Exception as e:
                print(e)
                sleep(1)
                print('offset: %d, retrying...' % offset)
        wallets += resp
        if len(resp) < 1000:
            break
        else:
            offset += len(resp)
    return wallets


def get_pool_metadata(pool_id):
    """
    # Get the stake pool metadata
    :param pool_id:
    :return: pool_metadata
    """
    url = API_BASE_URL + '/pool_metadata'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    pool_ids = {'_pool_bech32_ids': [pool_id]}
    data = json.dumps(pool_ids)
    print(data)
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(data)).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_retiring_pools():
    """
    # Get the retiring stake pools list
    :return: retiring_pools
    """
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    url = API_BASE_URL + '/pool_updates?pool_status=eq.retiring'
    while True:
        try:
            resp = json.loads(requests.get(url, headers=headers).text)
            break
        except Exception as e:
            print(e)
            sleep(1)
            print('retrying...')
    return resp


def get_stake_address(wallet_addr):
    """
    :param wallet_addr: wallet address
    :return: stake address
    """
    valid_stake_address = check_if_staking_wallet(wallet_addr)
    if valid_stake_address:
        decoded = decode_wallet_addr(wallet_addr)
        stake_key = create_stake_key(decoded)
    else:
        stake_key = ''
    return stake_key


def check_if_staking_wallet(wallet_addr):
    """
    :param wallet_addr: wallet address
    :return: True if the wallet is staked, False otherwise
    """
    valid_stake_address = False
    if len(wallet_addr) > 63:
        valid_stake_address = True
    else:
        print('This is not a staking wallet')
    return valid_stake_address


def decode_wallet_addr(wallet_addr):
    """
    :param wallet_addr: wallet address
    :return: hex encoded wallet address
    """
    args = '/usr/local/bin/bech32 <<< ' + wallet_addr
    result = subprocess.check_output(args, shell=True, executable='/bin/bash')
    result = result.decode("utf-8")
    decoded = result.replace('\n', '')
    return decoded


def decode_pool_id(hex_id):
    """
    :param hex_id: hex stake pool id
    :return: bech32 stake pool id
    """
    args = '/usr/local/bin/bech32 pool <<< ' + hex_id
    result = subprocess.check_output(args, shell=True, executable='/bin/bash')
    result = result.decode("utf-8")
    decoded = result.replace('\n', '')
    return decoded


def create_stake_key(decoded):
    """
    :param decoded: hex stake address
    :return: bech32 stake address
    """
    last_chars = decoded[-56:]
    if CARDANO_NET == '--mainnet':
        main_net_stake_hex = ('e1' + last_chars)
        args = '/usr/local/bin/bech32 stake <<< ' + main_net_stake_hex
    else:
        test_net_stake_hex = ('e0' + last_chars)
        args = '/usr/local/bin/bech32 stake_test <<< ' + test_net_stake_hex
    result = subprocess.check_output(args, shell=True, executable='/bin/bash')
    result = result.decode("utf-8")
    stake_key = result.replace('\n', '')
    return stake_key
