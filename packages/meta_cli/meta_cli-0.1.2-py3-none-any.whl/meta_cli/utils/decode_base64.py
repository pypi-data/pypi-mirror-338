import base64
import json
import sys

from loguru import logger


def decode_base64_fields(data):
    if isinstance(data, dict):
        return {k: decode_base64_fields(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [decode_base64_fields(item) for item in data]
    elif isinstance(data, str):
        try:
            decoded_bytes = base64.b64decode(data)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except (base64.binascii.Error, UnicodeDecodeError):
            return data
    else:
        return data


def test_base64():
    decoded_bytes = base64.b64decode("AAAAAAAAAAE=")
    decoded_str = decoded_bytes.decode('utf-8')
    decimal_value = int.from_bytes(decoded_bytes, byteorder="big", signed=False)
    logger.info(decoded_str)
    logger.info(decimal_value)


def main():
    # input_data = sys.stdin.read()
    # json_data = json.loads(input_data)
    json_data = [{'attributes': [{'index': True, 'key': 'ZmVl', 'value': ''}, {'index': True, 'key': 'ZmVlX3BheWVy',
                                                                               'value': 'bWUxdmN2cXc5dWZoZ2RwdTVudGh6eDNxZWM3Y3ZtOW0zODM5Z2hqM3c='}],
                  'type': 'tx'}, {'attributes': [{'index': True, 'key': 'YWNjX3NlcQ==',
                                                  'value': 'bWUxdmN2cXc5dWZoZ2RwdTVudGh6eDNxZWM3Y3ZtOW0zODM5Z2hqM3cvMTI='}],
                                  'type': 'tx'}, {'attributes': [{'index': True, 'key': 'c2lnbmF0dXJl',
                                                                  'value': 'M0sxK1lzQzQ5eCttam50VmFWTFdVTVJyVGVUNGpta3RISG5sQVR0bDh1Z2JkbjBOUGhJNHpvRGhLaEtzWVgrQld1cVdPTDFVMzlGV2g3ZnorMUs4ZXc9PQ=='}],
                                                  'type': 'tx'}, {'attributes': [
        {'index': True, 'key': 'YWN0aW9u', 'value': 'L2liYy5jb3JlLmNsaWVudC52MS5Nc2dVcGRhdGVDbGllbnQ='}],
                     'type': 'message'}, {
                     'attributes': [{'index': True, 'key': 'Y2xpZW50X2lk', 'value': 'MDctdGVuZGVybWludC0w'},
                                    {'index': True, 'key': 'Y2xpZW50X3R5cGU=', 'value': 'MDctdGVuZGVybWludA=='},
                                    {'index': True, 'key': 'Y29uc2Vuc3VzX2hlaWdodA==', 'value': 'MS01ODA='},
                                    {'index': True, 'key': 'aGVhZGVy',
                                     'value': 'MGEyNjJmNjk2MjYzMmU2YzY5Njc2ODc0NjM2YzY5NjU2ZTc0NzMyZTc0NjU2ZTY0NjU3MjZkNjk2ZTc0MmU3NjMxMmU0ODY1NjE2NDY1NzIxMmI2MGMwYWIzMDYwYTk0MDMwYTAyMDgwYjEyMGQ2ZDY1NjM2ODYxNjk2ZTVmMzEzMDMwMmQzMTE4YzQwNDIyMGMwOGI5ZjI5YWJlMDYxMGNhZTA4YWUzMDIyYTQ4MGEyMGI5ZTU2OTcxMzc2NWU4MjY0MTBhMDQ2ODJmMTNmZGVlNWZlNzRhZTFmNjUzNDljMzE0MDg0M2IyOTNhYTc2NjgxMjI0MDgwMTEyMjAzODU5OTU0NzEzZTdjZjQ5MDQ1YmY5ODkwZWFmNjI4YzAzNTYxYWZkMGU2YWY5YmEzY2E3MjRhZTE2NWIxZTBjMzIyMGE5ODMzOTVkOTNkZGRmM2FmOGQzMmQ0OWZlMzRlMjhiZDRlYzM2MzU0ZjA5NzVkZTdmODY4ZTYzOGVmMjQwNzQzYTIwZTNiMGM0NDI5OGZjMWMxNDlhZmJmNGM4OTk2ZmI5MjQyN2FlNDFlNDY0OWI5MzRjYTQ5NTk5MWI3ODUyYjg1NTQyMjBkNWFlOGNhYjVmN2Q1NzU2NTFmMTY4ODRmMGEzZDIwODZkODg2ZDQxZDQ4Nzk4NGRkYmUwNjc2MjA2ZWRjMTViNGEyMGQ1YWU4Y2FiNWY3ZDU3NTY1MWYxNjg4NGYwYTNkMjA4NmQ4ODZkNDFkNDg3OTg0ZGRiZTA2NzYyMDZlZGMxNWI1MjIwNjhlY2Q2ZjMzMzExOWNlNDM3NTFlY2U1ODNiOTgxZjIzNTA4YWVhZjQyMjFmZjU4MmIxYmIzM2JlNDJiY2VmYTVhMjA4MzhjZmM5ZjY2YzkwMWY0MDYzMjJjYjAwNTRhYWQ3YzdkZDIxMzU1NjhjOTg3MjFkMzc3NzRmYTQ1ZTI0ZDQ5NjIyMGI3YjRhZmJkYjJkOWYyMTBjODhjYjg2NmMyMjc1ZjNiYzFmYjY5ZmI4ZGI4MTIzMDY3ZWQwMDY2OGRkMTVjMzg2YTIwZTNiMGM0NDI5OGZjMWMxNDlhZmJmNGM4OTk2ZmI5MjQyN2FlNDFlNDY0OWI5MzRjYTQ5NTk5MWI3ODUyYjg1NTcyMTQ4Zjc1YzhmZTE3ZDA5YzBiOWZhN2FmZTdjNzk3YmIwYjI3NzhhZWE5MTI5OTAzMDhjNDA0MWE0ODBhMjAyNmM0MGEwN2JlMzlkZGI5MGI4ZGQ0Y2RmMzI2ZTJhYTE5YmQwMDJiNzg5YzZkN2I4Yzc1ZGExZjE0MzlkMTMzMTIyNDA4MDExMjIwYWJkMWMzMGZlYWQxNTM4MTE0MzI4YTM2NzUxYTI2MDMwNzQ1NjgzNDk1ODVkMDMxNTAwMzZlZTM5ZjBkYTA4NDIyNjcwODAyMTIxNDBmNzY1ZGMwMDg3MGYyZWE2ZWJlYTRjNmMyODhhM2YzMDJlYjY3MGMxYTBiMDhiZmYyOWFiZTA2MTA4N2M1OGM0NzIyNDBmNjNjMzdlMjg5ZWRiMjdjNzNhZmU0YmYwZTgyNzZjMmY2NzhkY2YwYzc2ODQxZTY0OTViYjRiMmZhZmU0ZTE4NDY5M2FmZjlhZGUzMjA3YzRlMGI5MTBiNzU3YTg4OGE0MTJlNjAzZTEyMzkyYTA1YThjMWY1MDYzNTQ5MDkwNzIyNjcwODAyMTIxNDc4YzRlMjE3ZTBlN2JkNGU1NDg0ZTEzOTZmMzMyYmExOGQxYjk0NzAxYTBiMDhiZmYyOWFiZTA2MTA4YmQyZjk0NjIyNDBjM2UyNWFlYTYxNDRiYzk0OTNlNWI5ZjZiOTFhNDUxOTM0ZWYyOWEzZmFiY2VkZGM1MjExZjE4MjY1YjExMDQ0ODNkMDM0ZGExZmIwZjU4ZjYzOWQ1Yzg3Y2NmNmQzM2U1Y2ViOWI1ZTMxNGE1YWE2MGI3NzBmOWY0MWJjNWMwNzIyNjcwODAyMTIxNDgxOWVmZTllYThmYTJkYTViOWNiMmQ0MjQ4MzljYTdjNzk5YjEyNzQxYTBiMDhiZmYyOWFiZTA2MTBjNGEyYmY3NjIyNDBiZGIwOTgwNWU0MjAxY2M4MDQyZDk1NmU4YTk0NmQzY2ZjY2MyMTQ3YmVjOWY0ODA0MDM0NTcyNmU0Y2MzZjhhYTRjYzI1NjA4ZmNjOWI3NzM2Y2YwMzE5NTc4NGQxMzdkN2IxNDBjNTIxMDY5ZGJiMDVmNDBjNDc0YjM2MGQwYTIyMGYwODAxMWEwYjA4ODA5MmI4YzM5OGZlZmZmZmZmMDExMmZjMDIwYTRiMGExNDBmNzY1ZGMwMDg3MGYyZWE2ZWJlYTRjNmMyODhhM2YzMDJlYjY3MGMxMjIyMGEyMDIzOTAyMTgwNzE3MGYzNzU0MDRiYzkzYzVkMjBkZjk3MzY0YjkxNDc3MTNkM2JiODZkZGZmYWMyNTNkYjQwMzQxODgwYzhhZmEwMjUyMDgwODdmYWFiZmJmZmZmZmZmZjAxMGE0YjBhMTQ3OGM0ZTIxN2UwZTdiZDRlNTQ4NGUxMzk2ZjMzMmJhMThkMWI5NDcwMTIyMjBhMjBjMzAyNmYzMmRlODllYjQ2NWYxODczZmVjM2E2ODQ3Y2ZiNzE5MzQ4NWZkZDY4N2RlYzIwODgwNDcxZjMyMGZmMTg4MGM4YWZhMDI1MjA4MDg3ZmFhYmZiZmZmZmZmZmYwMTBhNDYwYTE0ODE5ZWZlOWVhOGZhMmRhNWI5Y2IyZDQyNDgzOWNhN2M3OTliMTI3NDEyMjIwYTIwNWY5NDFhMDE1MDQ0ZDIxNjk1ZGE1ZDZjNmQyZDU0Yzk4YTMzODRjMTg1OTdjM2Q5ZDA4MmZkODQyYjMzODljYzE4ODBjOGFmYTAyNTIwODBlYjkxZmMwZDBhNGIwYTE0OGY3NWM4ZmUxN2QwOWMwYjlmYTdhZmU3Yzc5N2JiMGIyNzc4YWVhOTEyMjIwYTIwMGY1Y2FhOWZiZDlhMTBjMDBhNTFiMmI3ZjY2YmNiYmQ4YmYzYjg1M2I4MGQ1NTI3Mzk3OGU4ZWUyMDliZTljOTE4ODBjOGFmYTAyNTIwODA4N2ZhYWJmYmZmZmZmZmZmMDExMjRiMGExNDhmNzVjOGZlMTdkMDljMGI5ZmE3YWZlN2M3OTdiYjBiMjc3OGFlYTkxMjIyMGEyMDBmNWNhYTlmYmQ5YTEwYzAwYTUxYjJiN2Y2NmJjYmJkOGJmM2I4NTNiODBkNTUyNzM5NzhlOGVlMjA5YmU5YzkxODgwYzhhZmEwMjUyMDgwODdmYWFiZmJmZmZmZmZmZjAxMWEwNTA4MDExMGExMDMyMmY3MDIwYTRiMGExNDBmNzY1ZGMwMDg3MGYyZWE2ZWJlYTRjNmMyODhhM2YzMDJlYjY3MGMxMjIyMGEyMDIzOTAyMTgwNzE3MGYzNzU0MDRiYzkzYzVkMjBkZjk3MzY0YjkxNDc3MTNkM2JiODZkZGZmYWMyNTNkYjQwMzQxODgwYzhhZmEwMjUyMDgwZjc5YWViYjBmZmZmZmZmZjAxMGE0NjBhMTQ3OGM0ZTIxN2UwZTdiZDRlNTQ4NGUxMzk2ZjMzMmJhMThkMWI5NDcwMTIyMjBhMjBjMzAyNmYzMmRlODllYjQ2NWYxODczZmVjM2E2ODQ3Y2ZiNzE5MzQ4NWZkZDY4N2RlYzIwODgwNDcxZjMyMGZmMTg4MGM4YWZhMDI1MjA4MDk3ZDllYzQ1MGE0YjBhMTQ4MTllZmU5ZWE4ZmEyZGE1YjljYjJkNDI0ODM5Y2E3Yzc5OWIxMjc0MTIyMjBhMjA1Zjk0MWEwMTUwNDRkMjE2OTVkYTVkNmM2ZDJkNTRjOThhMzM4NGMxODU5N2MzZDlkMDgyZmQ4NDJiMzM4OWNjMTg4MGM4YWZhMDI1MjA4MGRiYjJiYmMzZmZmZmZmZmYwMTBhNDYwYTE0OGY3NWM4ZmUxN2QwOWMwYjlmYTdhZmU3Yzc5N2JiMGIyNzc4YWVhOTEyMjIwYTIwMGY1Y2FhOWZiZDlhMTBjMDBhNTFiMmI3ZjY2YmNiYmQ4YmYzYjg1M2I4MGQ1NTI3Mzk3OGU4ZWUyMDliZTljOTE4ODBjOGFmYTAyNTIwODA5N2Q5ZWM0NTEyNGIwYTE0MGY3NjVkYzAwODcwZjJlYTZlYmVhNGM2YzI4OGEzZjMwMmViNjcwYzEyMjIwYTIwMjM5MDIxODA3MTcwZjM3NTQwNGJjOTNjNWQyMGRmOTczNjRiOTE0NzcxM2QzYmI4NmRkZmZhYzI1M2RiNDAzNDE4ODBjOGFmYTAyNTIwODBmNzlhZWJiMGZmZmZmZmZmMDE='}],
                     'type': 'update_client'},
                 {'attributes': [{'index': True, 'key': 'bW9kdWxl', 'value': 'aWJjX2NsaWVudA=='}], 'type': 'message'}, {
                     'attributes': [{'index': True, 'key': 'YWN0aW9u',
                                     'value': 'L2liYy5jb3JlLmNoYW5uZWwudjEuTXNnQWNrbm93bGVkZ2VtZW50'}],
                     'type': 'message'}, {
                     'attributes': [{'index': True, 'key': 'cGFja2V0X3RpbWVvdXRfaGVpZ2h0', 'value': 'MS0xNjk3'},
                                    {'index': True, 'key': 'cGFja2V0X3RpbWVvdXRfdGltZXN0YW1w',
                                     'value': 'MTc0MTA3NzM2OTAwMDAwMDAwMA=='},
                                    {'index': True, 'key': 'cGFja2V0X3NlcXVlbmNl', 'value': 'NQ=='},
                                    {'index': True, 'key': 'cGFja2V0X3NyY19wb3J0', 'value': 'dHJhbnNmZXI='},
                                    {'index': True, 'key': 'cGFja2V0X3NyY19jaGFubmVs', 'value': 'Y2hhbm5lbC0w'},
                                    {'index': True, 'key': 'cGFja2V0X2RzdF9wb3J0', 'value': 'dHJhbnNmZXI='},
                                    {'index': True, 'key': 'cGFja2V0X2RzdF9jaGFubmVs', 'value': 'Y2hhbm5lbC0w'},
                                    {'index': True, 'key': 'cGFja2V0X2NoYW5uZWxfb3JkZXJpbmc=',
                                     'value': 'T1JERVJfVU5PUkRFUkVE'},
                                    {'index': True, 'key': 'cGFja2V0X2Nvbm5lY3Rpb24=', 'value': 'Y29ubmVjdGlvbi0w'}],
                     'type': 'acknowledge_packet'},
                 {'attributes': [{'index': True, 'key': 'bW9kdWxl', 'value': 'aWJjX2NoYW5uZWw='}], 'type': 'message'}, {
                     'attributes': [{'index': True, 'key': 'bW9kdWxl', 'value': 'dHJhbnNmZXI='},
                                    {'index': True, 'key': 'c2VuZGVy',
                                     'value': 'bWUxanJreGY5eGp1enJ1ZGN5d2wwa3d4cDVxNXF4eTQzeWVqcmRka2U='},
                                    {'index': True, 'key': 'cmVjZWl2ZXI=',
                                     'value': 'bWUxazMwbWc5c2tubHd1dmh0aHJqd20wcmFkN3hjajhheGZzZmRoaDU='},
                                    {'index': True, 'key': 'ZGVub20=', 'value': 'dHJhbnNmZXIvY2hhbm5lbC0wL3VtZWM='},
                                    {'index': True, 'key': 'YW1vdW50', 'value': 'MTAw'},
                                    {'index': True, 'key': 'bWVtbw==', 'value': ''},
                                    {'index': True, 'key': 'YWNrbm93bGVkZ2VtZW50', 'value': 'cmVzdWx0OiJcMDAxIiA='}],
                     'type': 'fungible_token_packet'},
                 {'attributes': [{'index': True, 'key': 'c3VjY2Vzcw==', 'value': 'AQ=='}],
                  'type': 'fungible_token_packet'}]

    json_data = {
        "jsonrpc": "2.0",
        "result": {
            "height": "7684",

            "begin_block_events": [
                {
                    "type": "coin_spent",
                    "attributes": [
                        {
                            "key": "c3BlbmRlcg==",
                            "value": "bWUxN3hwZnZha20yYW1nOTYyeWxzNmY4NHoza2VsbDhjNWxyMndmZjI=",
                            "index": True
                        },
                        {
                            "key": "YW1vdW50",
                            "value": None,
                            "index": True
                        }
                    ]
                },
                {
                    "type": "coin_received",
                    "attributes": [
                        {
                            "key": "cmVjZWl2ZXI=",
                            "value": "bWUxanY2NXMzZ3JxZjZ2NmpsM2RwNHQ2Yzl0OXJrOTljZDg1dmY0dGc=",
                            "index": True
                        },
                        {
                            "key": "YW1vdW50",
                            "value": None,
                            "index": True
                        }
                    ]
                },
                {
                    "type": "transfer",
                    "attributes": [
                        {
                            "key": "cmVjaXBpZW50",
                            "value": "bWUxanY2NXMzZ3JxZjZ2NmpsM2RwNHQ2Yzl0OXJrOTljZDg1dmY0dGc=",
                            "index": True
                        },
                        {
                            "key": "c2VuZGVy",
                            "value": "bWUxN3hwZnZha20yYW1nOTYyeWxzNmY4NHoza2VsbDhjNWxyMndmZjI=",
                            "index": True
                        },
                        {
                            "key": "YW1vdW50",
                            "value": None,
                            "index": True
                        }
                    ]
                },
                {
                    "type": "message",
                    "attributes": [
                        {
                            "key": "c2VuZGVy",
                            "value": "bWUxN3hwZnZha20yYW1nOTYyeWxzNmY4NHoza2VsbDhjNWxyMndmZjI=",
                            "index": True
                        }
                    ]
                },
                {
                    "type": "sequencer_rewards",
                    "attributes": [
                        {
                            "key": "YW1vdW50",
                            "value": None,
                            "index": True
                        },
                        {
                            "key": "c2VxdWVuY2Vy",
                            "value": "bWV2YWxvcGVyMTJxbmNnbDdweHh2ODRuNzJqZjRkNGF4dHhsNnFlbmRkdXVseHAy",
                            "index": True
                        }
                    ]
                },
                {
                    "type": "commission",
                    "attributes": [
                        {
                            "key": "YW1vdW50",
                            "value": None,
                            "index": True
                        },
                        {
                            "key": "dmFsaWRhdG9y",
                            "value": "bWV2YWxvcGVyMTJxbmNnbDdweHh2ODRuNzJqZjRkNGF4dHhsNnFlbmRkdXVseHAy",
                            "index": True
                        }
                    ]
                },
                {
                    "type": "rewards",
                    "attributes": [
                        {
                            "key": "YW1vdW50",
                            "value": None,
                            "index": True
                        },
                        {
                            "key": "dmFsaWRhdG9y",
                            "value": "bWV2YWxvcGVyMTJxbmNnbDdweHh2ODRuNzJqZjRkNGF4dHhsNnFlbmRkdXVseHAy",
                            "index": True
                        }
                    ]
                },
                {
                    "type": "epoch_end",
                    "attributes": [
                        {
                            "key": "ZXBvY2hfbnVtYmVy",
                            "value": "NjUy",
                            "index": True
                        }
                    ]
                },
                {
                    "type": "epoch_start",
                    "attributes": [
                        {
                            "key": "ZXBvY2hfbnVtYmVy",
                            "value": "NjUy",
                            "index": True
                        },
                        {
                            "key": "c3RhcnRfdGltZQ==",
                            "value": "MTc0MTE5OTM3Ng==",
                            "index": True
                        }
                    ]
                }
            ],
            "end_block_events": None,
            "validator_updates": None,
            "consensus_param_updates": {
                "block": {
                    "max_bytes": "22020096",
                    "max_gas": "-1"
                },
                "evidence": {
                    "max_age_num_blocks": "100000",
                    "max_age_duration": "172800000000000",
                    "max_bytes": "1048576"
                },
                "validator": {
                    "pub_key_types": [
                        "ed25519"
                    ]
                }
            }
        },
        "id": -1
    }
    import httpx

    resp = httpx.get(f"http://192.168.0.198:36657/block_results?height=8160")
    json_data = resp.json()["result"]
    decoded_data = decode_base64_fields(json_data)
    print(json.dumps(decoded_data, indent=2))


if __name__ == "__main__":
    main()
