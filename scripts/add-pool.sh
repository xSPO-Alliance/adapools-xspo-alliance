#!/usr/bin/env bash

export BASEDIR="$(cd $(dirname ${BASH_SOURCE[0]}) >/dev/null 2>&1 && pwd)"

API="https://api.koios.rest/api/v0"

if [[ ! $(cat ${BASEDIR}/../xSPO-list-cexplorer.json | grep ${pool_bech32_id}) ]]; then
    if [[ $(curl -sS -X POST "${API}/pool_info" \
                    -H "Content-Type: application/json" \
                    -d '{"_pool_bech32_ids":["'${pool_bech32_id}'"]}' \
                    | jq -r '.[].pool_status') == "registered" ]]; then
        
        echo "Pool is registered on Cardano mainnet"
    else
        echo "Pool is not registered on Cardano mainnet"
        exit -1
    fi

    pool_active_stake=$(curl -sS -X POST "${API}/pool_info" \
                        -H "Content-Type: application/json" \
                        -d '{"_pool_bech32_ids":["'${pool_bech32_id}'"]}' \
                        | jq -r '.[].active_stake')

    if [[ ! $((pool_active_stake / 1000000 )) -gt 1000000 ]]; then
        pool_hex_id=$(curl -sS -X POST "${API}/pool_info" \
                        -H "Content-Type: application/json" \
                        -d '{"_pool_bech32_ids":["'${pool_bech32_id}'"]}' \
                        | jq -r '.[].pool_id_hex')
        
        pool_name=$(curl -sS -X POST "${API}/pool_info" \
                        -H "Content-Type: application/json" \
                        -d '{"_pool_bech32_ids":["'${pool_bech32_id}'"]}' \
                        | jq -r '.[].meta_json.name')
        
        pool_ticker=$(curl -sS -X POST "${API}/pool_info" \
                        -H "Content-Type: application/json" \
                        -d '{"_pool_bech32_ids":["'${pool_bech32_id}'"]}' \
                        | jq -r '.[].meta_json.ticker')
        
        m_count=$(($(tail -8 ${BASEDIR}/../xspo-alliance-members.json | head -1 | cut -d'"' -f2) + 1))
        m_since=$(date +%Y-%m-%d)

        echo "Adding the Pool to the xSPO-Alliance"

        echo ${pool_name} | xargs -I {} jq '.adapools.members += {"'${m_count}'":{"pool_id": "'${pool_hex_id}'", "member_since": "'${m_since}'", "name": "'${pool_ticker}' ('{}')" }}' ${BASEDIR}/../xspo-alliance-members.json >> ${BASEDIR}/../_temp0.json
        mv ${BASEDIR}/../_temp0.json ${BASEDIR}/../xspo-alliance-members.json

        jq -r '. += ["'${pool_bech32_id}'"]' ${BASEDIR}/../xSPO-list-cexplorer.json >> ${BASEDIR}/../_temp.json
        mv ${BASEDIR}/../_temp.json ${BASEDIR}/../xSPO-list-cexplorer.json

    else
        echo "Pool does not meet xSPO-Alliance minimal requirement!"
        exit -1
    fi
else
    echo "Pool is already added in json!"
    exit -1
fi