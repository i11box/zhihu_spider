import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "priority": "u=1, i",
    "referer": "https://www.zhihu.com/search?type=content&q=%E5%85%A8%E6%A0%88",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "x-api-version": "3.0.91",
    "x-app-za": "OS=Web",
    "x-requested-with": "fetch",
    "x-zse-93": "101_3_3.0",
    "x-zse-96": "2.0_fWCl=r6gulDtDVXN1tuBq2rFIUDmbpuUsIfXOrNaHkY88TMqgKbSGU4n0wrUAGpn",
    "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZGTY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPFHc9HBxCbgOCUrHMJqo_shV1CcCmIBSMrwx0xC28VBHBIwN82Ht1-GwKShSTvHCVgugMgUFKaUwyPCp8L9Y13gg1yhH1SMt8AG2M1uYLyrXGWwoYYcSY7wL_jvNq3wpsbHYGfvxywuVMDqxMBCY8mQL8DhUYHBFVChc9nwoYsD9_H9F9OqfzFGOfjCxfrbHO-bLOp9gGPqLGrGwMf9L9mbxfnbcY_wHmEve0K83f8Ue0EDHLFBL1mDN18rVOhDofpup9yvX1egwB-cNOqUC189gKLvoVVbLGQXeC-wFC"
}
cookies = {
    "_xsrf": "ncjieleHb1IWng0IvikQ2JY8kBnR9SOL",
    "_zap": "ff47db1e-7618-4908-96ed-c1ad4e772b9a",
    "d_c0": "APARLHx_AxmPTtN_2TVzgkHcYHvZPOeY434=|1722511475",
    "q_c1": "aaa48bd451bd4a56862382dc156c8888|1722862855000|1722862855000",
    "__zse_ck": "001_A205vVo8vFHafaFlcOHeWL8l99W9=BPItymbSiZKhyVuuXQwkK3/W/AIM04oUEtbeF/bbR/peFfaLc0ygft9+vB0gC/MYhb4pBfL9d=cFYp+W+2yIdRLTtSBeeLuC3LK",
    "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1722863085,1723427925,1724309916,1724377707",
    "HMACCOUNT": "5952A02A4A4BF0A4",
    "__snaker__id": "NBcFvuG8UeiiftNY",
    "SESSIONID": "e7E6IafenB3YVM9pEGgyEgeruioxYLeOucNISdlnz1i",
    "JOID": "UFoRC0_IrH2ZUtiZO8CaKVK1aZckrZ00ox25-VKg7kjMCJOgTeastfVU3pM7kpr2hhNlZMSwTJ2F_rDz9u7DcwY=",
    "osd": "Vl4dA0_OqHGRUt6dN8iaL1a5YZciqZE8oxu99Vqg6EzAAJOmSeqktfNQ0ps7lJ76jhNjYMi4TJuB8rjz8OrPewY=",
    "gdxidpyhxdE": "bIcyjJMra%5CMu%2F7d9wkZ8LDBaDZtSbjb1Guw30C%2B5dzr96PjLtWBGsKHKvnJCv65IMq2CBU1rZazUfhvtYRg2jibY%5C%5CpRphTNEkTgG8%2FDAJBz9dG2%5Clvd%5Cl9A49lJQhOurgXyysO%2Fwq42VBPbIS3Hmgbg%5CISZgV5N%5C1mgiMvzqe007fd1%3A1724397417401",
    "captcha_session_v2": "2|1:0|10:1724396861|18:captcha_session_v2|88:MGtOUXhWcXRRellQRWRuN3JGODlwemdSYmlWcElFeDFXMm5ZbG4vNGZJRm1RM0hId2JUa1FUbS8yRGFnN0VMdg==|870897c21fa53c0d5fe79a8e9722f3b7e5edc71b8368f41014bfa38f16f424d2",
    "captcha_ticket_v2": "2|1:0|10:1724396864|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfdWFwLkcwblFnY1FjY3RYRXdJUE1HY0tZaVJwQnlLKl9qNmhKYnlsc3ljeTgubzZYS0JIbldDY1k5WE1MeVpaem5sZ2JwV0FKbUVnaXh5b0M0YlU2QXMxZ0NIRnM4Ul82V1dBaUdtVnpycmZTMGFvM0k2R2JMdlE5OWtlbi5CUnFQaUJybFdGbkdVLkVuUmYqTV9IVVU2b1RnRjlIRzFEcUhWZUMxRUNwaEVRZkVTUEpKYzRiWkN4c2cubm5BcDBFSU9uVE9oZ2FtaWE2M3RGWmdkcTMyeGNGeGVPaGlyWXpFWUNyS0NQSUNLVjZxcDZTSnlka0E2QVFFV2dRa0c5MXpoVHFDaEpCNGdBRUFHOEtYY19EYXQ0SEE2R21rY1NOeXFZZmlfNmVGdlFfWU5vYXlRVnE0UmVIRllGcmNyRnZMUW9vbzlTTFBFWTNuZ2VBQmJ2UC53SHdIcmhkbTQ1TU5MUzZFUHFBRFpnUFN0WjBybzFmaG1fNElHYm13R2t4TXFDQUtNTHp4MFB4aEhxTUt5UmxxSmI2em1ET25MNDB1RmExMThyek1sY3Q0SDFRQUtpaDMxYnQ0OEZEMWV3YUFiNFZTZjNfY285cW1FOGpfSWRmSWMuOUpIX0dGUUdNWm0yYlBkSWhJeldHcE5fYVpyNHJnc2ZBQnlsWXkxNTU2LjMzYVg3N192X2lfMSJ9|bdd6794f0b82c59526d56b11a80e691a53d633fd8ede78689896852edbe68b93",
    "z_c0": "2|1:0|10:1724396864|4:z_c0|92:Mi4xQXA3bEJnQUFBQUFBOEJFc2ZIOERHU1lBQUFCZ0FsVk5RSU8xWndEbW5iQkNEQXh5OUFCV0pEWGs0WmNTQ3d1Z3lR|e8c977e6b179b404e32343c34bf8f75179574f482250fc9da28f10b6822d78e4",
    "tst": "r",
    "BEC": "738c6d0432e7aaf738ea36855cdce904",
    "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49": "1724426832"
}
url = "https://www.zhihu.com/api/v4/search_v3"
params = {
    "gk_version": "gz-gaokao",
    "t": "general",
    "q": "全栈",
    "correction": "1",
    "offset": "0",
    "limit": "20",
    "filter_fields": "",
    "lc_idx": "0",
    "show_all_topics": "0",
    "search_source": "Normal"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

with open("output.json", "w", encoding="utf-8") as f:
  f.write(response.text)
  
