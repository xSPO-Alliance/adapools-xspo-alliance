#!/usr/bin/env bash

export BASEDIR="$(cd $(dirname ${BASH_SOURCE[0]}) >/dev/null 2>&1 && pwd)"

API="https://api.koios.rest/api/v0"
CURL_CMD="curl -sS -X POST \"${API}/pool_info\" -H \"Content-Type: application/json\" -d '{\"_pool_bech32_ids\":[\"'${pool_bech32_id}'\"]}'"

pool_hex_id=$(eval ${CURL_CMD} | jq -r '.[].pool_id_hex')

if [[ ! $(cat ${BASEDIR}/../xSPO-list-cexplorer.json | grep ${pool_bech32_id}) ]]; then
    if [[ $(eval ${CURL_CMD} | jq -r '.[].pool_status') == "registered" ]]; then
        _message="Pool is registered on Cardano mainnet"
        echo ${_message}
    else
        _message="Pool is not registered on Cardano mainnet"
        echo ${_message}
        exit -1
    fi

    pool_active_stake=$(eval ${CURL_CMD} | jq -r '.[].active_stake')

    if [[ ! $((pool_active_stake / 1000000 )) -gt 1000000 ]]; then
        
        pool_name=$(eval ${CURL_CMD} | jq -r '.[].meta_json.name')        
        pool_ticker=$(eval ${CURL_CMD} | jq -r '.[].meta_json.ticker')        
        m_count=$(($(tail -8 ${BASEDIR}/../xspo-alliance-members.json | head -1 | cut -d'"' -f2) + 1))
        m_since=$(date +%Y-%m-%d)

        _message="Adding the Pool to the xSPO-Alliance"
        echo ${_message}

        echo ${pool_name} | xargs -I {} jq '.adapools.members += {"'${m_count}'":{"pool_id": "'${pool_hex_id}'", "member_since": "'${m_since}'", "name": "'${pool_ticker}' ('{}')" }}' ${BASEDIR}/../xspo-alliance-members.json >> ${BASEDIR}/../_temp0.json
        mv ${BASEDIR}/../_temp0.json ${BASEDIR}/../xspo-alliance-members.json

        jq -r '. += ["'${pool_bech32_id}'"]' ${BASEDIR}/../xSPO-list-cexplorer.json >> ${BASEDIR}/../_temp.json
        mv ${BASEDIR}/../_temp.json ${BASEDIR}/../xSPO-list-cexplorer.json

    else
        _message="Pool does not meet xSPO-Alliance minimal requirement!"
        echo ${_message}
        exit -1
    fi
else
    _message="Pool is already added!\n\n"
    pool_json_already=$(jq -r --arg hex ${pool_hex_id} '.adapools.members[] | select(.pool_id == $hex)' xspo-alliance-members.json)
    _message+=${pool_json_already}
    echo -e ${_message}
    exit -1
fi