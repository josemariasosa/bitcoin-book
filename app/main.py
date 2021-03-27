#!/usr/bin/env python
# coding=utf-8

# Programming Bitcoin
# ------------------------------------------------------------------------------
# josemariasosa 🦡

"""
PLEASE TRY TO SOLVE THIS PROBLEM, THIS IS A REQUIREMENT TO BE CONSIDERED.

You are given a bunch of Bitcoin UTXOs of varying amounts that you are
able to spend from your Bitcoin wallet. They are given to you sorted by
amount. You want to pay someone 0.05 BTC with a fee of less than 1000
sats AND not generate any change. Write a function to determine if your
UTXOs will allow for this specific transaction.

Remember, you may use more than 1 input! (Solving for the 2 input case
is good, solving for the 3 input case amazing and the 4+ input
case extraordrinary)
"""


def select_optimized_utxos(utxos, target, fee, minimum_fee=0):
    goal = target + fee
    values = [d['value'] for d in utxos]

    upper_limit = ''.join([str(int(v <= goal)) for v in values])
    upper_value = int(upper_limit, 2)

    sumres = 0
    lower_limit = ''
    for value in values[::-1]:
        sumres += value
        if sumres < target:
            lower_limit += '1'
        else:
            break
    lower_value = int(lower_limit, 2)

    response = {'is_valid': False}
    if upper_value > lower_value:
        results = []
        for ix in range(lower_value, upper_value+1):
            b = "{0:b}".format(ix).zfill(len(values))
            total = sum([(t[0] * t[1]) for t in zip(values, [int(i) for i in b])])
            if (((target + fee) >= total > target)
                    and (total > (target + minimum_fee))):
                results.append({
                    'bin': b,
                    'total': int(total)
                })

        if len(results) > 0:
            winner = max(results, key=lambda d: d['total'])
            response.update({
                'is_valid': True,
                'txs': [
                    tx[0] for tx in 
                    zip([d['tx_hash'] for d in utxos], [int(i) for i in winner['bin']])
                    if bool(tx[1])
                ],
                'total': winner['total'],
                'fee': winner['total'] - target
            })
    
    return response


def main():
    utxos = [
        {'value': 5500014, 'tx_hash': 'tx01a'},
        {'value': 5000991, 'tx_hash': 'tx01b'},
        {'value': 5000000, 'tx_hash': 'tx01c'},
        {'value': 2155143, 'tx_hash': 'tx02'},
        {'value': 1430921, 'tx_hash': 'tx03'},
        {'value': 1015435, 'tx_hash': 'tx04'},
        {'value': 1000191, 'tx_hash': 'tx05'},
        {'value': 99997, 'tx_hash': 'tx06'},
        {'value': 998, 'tx_hash': 'tx07'}
    ]
    utxos = sorted(utxos, key=lambda d: d['value'], reverse=True)
    fee = 1000
    target = 5000000

    valid_utxos = select_optimized_utxos(utxos, target, fee, 900)

    print(valid_utxos)


if __name__ == '__main__':
    main()

