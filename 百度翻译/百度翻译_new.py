#! -*-conding=: UTF-8 -*-
# 2024/4/18 11:31

# 百度翻译新版接口，sse

import json

import requests

cookies = {
    'BAIDUID': '2075799560CB805468E46C062291C3CA:FG=1',
    'PSTM': '1710310886',
    'H_WISE_SIDS': '40009_40207_40212_40216_40223_40294_40291_40289_40286_40317_40079_40365_40351_40380_40369_40358_40410_40416',
    'BIDUPSID': 'B15467B23371BD127587BB726566C72B',
    'BDUSS': 'mVBN2kzSFZ4OERFQ3hod3BXamk2bjl6YkhUT35jZnI5UERTaH5nS3p6MEgwU0JtRVFBQUFBJCQAAAAAAAAAAAEAAAD1-B2zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdE-WUHRPllU',
    'BDUSS_BFESS': 'mVBN2kzSFZ4OERFQ3hod3BXamk2bjl6YkhUT35jZnI5UERTaH5nS3p6MEgwU0JtRVFBQUFBJCQAAAAAAAAAAAEAAAD1-B2zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdE-WUHRPllU',
    'H_WISE_SIDS_BFESS': '40009_40207_40212_40216_40223_40294_40291_40289_40286_40317_40079_40365_40351_40380_40369_40358_40410_40416',
    'newlogin': '1',
    'BDSFRCVID': 'jukOJexroG3Kp_otXXu4UmHEg9NbUdrTDYrEjGc3VtzSGYLVYWf0EG0Pts1-dEub6j30ogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
    'H_BDCLCKID_SF': 'tbC8VCDKJKD3qbjkq45HMt00qxby26nBbC39aJ5y-J7nhpvxBPnMWhk0jboLBUQMfmoa-Rb-QpbZql5FQP-53R0h0PJkWp5kQKFjKl0MLPb5hj6gQJoDj4TyDMnMBMPe52OnaIbx3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj5vLjNrP',
    'BAIDUID_BFESS': '2075799560CB805468E46C062291C3CA:FG=1',
    'BDSFRCVID_BFESS': 'jukOJexroG3Kp_otXXu4UmHEg9NbUdrTDYrEjGc3VtzSGYLVYWf0EG0Pts1-dEub6j30ogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5',
    'H_BDCLCKID_SF_BFESS': 'tbC8VCDKJKD3qbjkq45HMt00qxby26nBbC39aJ5y-J7nhpvxBPnMWhk0jboLBUQMfmoa-Rb-QpbZql5FQP-53R0h0PJkWp5kQKFjKl0MLPb5hj6gQJoDj4TyDMnMBMPe52OnaIbx3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj5vLjNrP',
    'ZFY': 'XOAnHNRrDQvsBgbbRdLGSHEXnegxeyvSwaDRW4Zw9OQ:C',
    'PSINO': '6',
    'delPer': '0',
    'H_PS_PSSID': '40380_40369_40416_40304_40458_40480_60042_60024_60030_60048_60057_40510_40080',
    'BA_HECTOR': '0l818l0la420ag84al2k0ga543hq2c1j1urkp1t',
    'BDORZ': 'FFFB88E999055A3F8A630C64834BD6D0',
    'BDRCVFR[r5ISJbddYbD]': 'CxlIKiaG4umuAwsTZb8mvqV',
    'ab_sr': '1.0.1_MGMyNzJjYzgyMDUyYmMyNzIyY2U1MWRlYTNjNmY5NTgwYjRiNjVhMzBhZTc5Y2RmNTU2Y2E1ZTBjYzFiOTc1OGVkZmEzYmFjYmRmMjc5ZWZjNGVkOTc4Y2NiZWI1ZWVhNDdhZTE0ODA1YWViZGFlMTAzM2FkYTkwNjg0ZTllMjYwNGJmNTQ1ZTlhZmMyNmQ1YmJjN2E2ZDRkNmIwZGNiOQ==',
    'RT': '"z=1&dm=baidu.com&si=2877dd4d-868d-4b92-bd34-e444008016ba&ss=lv4onn7x&sl=14&tt=beb&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=4ultq"',
}

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Acs-Token': '1713355270682_1713419123474_kZvi+CHFTi89fKLk/UJ84VAyonvEOyxebomu95N+kIs/NPV6RNDy5BTnKWNnkozuXXYuBVcEnNqZHtcluxIciDs+2OlKciTeBwJY2F8PnGuBOfr1CaKORLQXIRubEV3Z6wONbiu9emTAiERul5qDPFAeFSYu+qXWF+aQii0B2o4sG5SoBywzLxxiCxTVcy5iJLmuLo0ZPrcjTo8jDJSFZVznW7HBoeUV7b0xSwfuNzjXTAUkOdMIRPGaY/RDvPgNUoFHwfagoqnV/Tu9DyTMgCcQs4K4Hp7woaBcx6IddshDwNgpWp6qaJKFEUdz98pB/A6llkpkqLgw5EiVzCSzmKnlEvDPXBrqG4EmJ9PvVY4w0wxbNG0h0AFP3+9Un7PbK3xyENIUvdqKSAa2LX3miDi0VWCASwjlaIg31izb6vYCIaIoaj4GWixqH6uZtvGQsSRhcHLIamowPTxsd7p+EWZo2H7dZYBy+cKgRSjCPd0=',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'BAIDUID=2075799560CB805468E46C062291C3CA:FG=1; PSTM=1710310886; H_WISE_SIDS=40009_40207_40212_40216_40223_40294_40291_40289_40286_40317_40079_40365_40351_40380_40369_40358_40410_40416; BIDUPSID=B15467B23371BD127587BB726566C72B; BDUSS=mVBN2kzSFZ4OERFQ3hod3BXamk2bjl6YkhUT35jZnI5UERTaH5nS3p6MEgwU0JtRVFBQUFBJCQAAAAAAAAAAAEAAAD1-B2zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdE-WUHRPllU; BDUSS_BFESS=mVBN2kzSFZ4OERFQ3hod3BXamk2bjl6YkhUT35jZnI5UERTaH5nS3p6MEgwU0JtRVFBQUFBJCQAAAAAAAAAAAEAAAD1-B2zAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdE-WUHRPllU; H_WISE_SIDS_BFESS=40009_40207_40212_40216_40223_40294_40291_40289_40286_40317_40079_40365_40351_40380_40369_40358_40410_40416; newlogin=1; BDSFRCVID=jukOJexroG3Kp_otXXu4UmHEg9NbUdrTDYrEjGc3VtzSGYLVYWf0EG0Pts1-dEub6j30ogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tbC8VCDKJKD3qbjkq45HMt00qxby26nBbC39aJ5y-J7nhpvxBPnMWhk0jboLBUQMfmoa-Rb-QpbZql5FQP-53R0h0PJkWp5kQKFjKl0MLPb5hj6gQJoDj4TyDMnMBMPe52OnaIbx3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj5vLjNrP; BAIDUID_BFESS=2075799560CB805468E46C062291C3CA:FG=1; BDSFRCVID_BFESS=jukOJexroG3Kp_otXXu4UmHEg9NbUdrTDYrEjGc3VtzSGYLVYWf0EG0Pts1-dEub6j30ogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbC8VCDKJKD3qbjkq45HMt00qxby26nBbC39aJ5y-J7nhpvxBPnMWhk0jboLBUQMfmoa-Rb-QpbZql5FQP-53R0h0PJkWp5kQKFjKl0MLPb5hj6gQJoDj4TyDMnMBMPe52OnaIbx3fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-Xj5vLjNrP; ZFY=XOAnHNRrDQvsBgbbRdLGSHEXnegxeyvSwaDRW4Zw9OQ:C; PSINO=6; delPer=0; H_PS_PSSID=40380_40369_40416_40304_40458_40480_60042_60024_60030_60048_60057_40510_40080; BA_HECTOR=0l818l0la420ag84al2k0ga543hq2c1j1urkp1t; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[r5ISJbddYbD]=CxlIKiaG4umuAwsTZb8mvqV; ab_sr=1.0.1_MGMyNzJjYzgyMDUyYmMyNzIyY2U1MWRlYTNjNmY5NTgwYjRiNjVhMzBhZTc5Y2RmNTU2Y2E1ZTBjYzFiOTc1OGVkZmEzYmFjYmRmMjc5ZWZjNGVkOTc4Y2NiZWI1ZWVhNDdhZTE0ODA1YWViZGFlMTAzM2FkYTkwNjg0ZTllMjYwNGJmNTQ1ZTlhZmMyNmQ1YmJjN2E2ZDRkNmIwZGNiOQ==; RT="z=1&dm=baidu.com&si=2877dd4d-868d-4b92-bd34-e444008016ba&ss=lv4onn7x&sl=14&tt=beb&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=4ultq"',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/mtpe-individual/multimodal?query=hello&lang=en2zh',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'accept': 'text/event-stream',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'query': 'student',
    'from': 'en',
    'to': 'zh',
    'reference': '',
    'corpusIds': [],
    'qcSettings': [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
    ],
    'needPhonetic': False,
    'domain': 'common',
    'milliTimestamp': 1713420885594,
}

response = requests.post('https://fanyi.baidu.com/ait/text/translate', cookies={}, headers=headers, json=json_data,
                         stream=True)
print(response.status_code)

for line in response.iter_lines(decode_unicode=True):
    if line:
        # 处理其他行，比如id, retry等
        if line.startswith("data: "):
            data = json.loads(line[len("data: "):])
            # print("数据是:", data)
            if data.get("data", {}).get("message") == "翻译中":
                print(f'翻译结果是：{data.get("data", {}).get("list")[0].get("dst")}')


