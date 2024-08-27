import re,json
import scrapy
from zhihu_spider.items import QuestionItem
from urllib.parse import urlparse, parse_qs,urlencode,urlunparse
from collections import OrderedDict

class ZhihuSearchSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    keyword = '全栈'
    custom_settings = {
        'ITEM_PIPELINES': {
            'zhihu_spider.pipelines.ZhihuSpiderPipeline': 300,
        },
        'DOWNLOAD_DELAY': 5,  # 延迟5秒再发送下一个请求
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 5,  # 初始延迟
        'AUTOTHROTTLE_MAX_DELAY': 15,  # 最大延迟时间
    }
    max_pages = 3  # 翻几页
    anwser_base_url =  ''
    search_base_url = 'https://www.zhihu.com/api/v4/search_v3?gk_version=gz-gaokao&t=general&q=%E5%85%A8%E6%A0%88&correction=1&offset=0&limit=20&filter_fields=&lc_idx=0&show_all_topics=0&search_source=Normal'
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "priority": "u=1, i",
        "referer": "https://www.zhihu.com/search?type=content&q=%E5%85%A8%E6%A0%88",
        "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "x-api-version": "3.0.91",
        "x-app-za": "OS=Web",
        "x-requested-with": "fetch",
        "x-zse-93": "101_3_3.0",
        "x-zse-96": "2.0_CQF7MrUV0aXayPAxsL3A3sXAr1zcTWlQlPuIdDNxuo6W+aptB0IdLd2k1gf3iv+a",
        "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZfTY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPFLeBwqcf9hg1Y9Lp0CLCMCYG0JUmcXSpSge9YGYmVJS_oCemUqCOGcN1YroTvAOY-G2ChgN9eiUfbX2M3BxfM9Y919SGrhcpJ_O94CpOVuN_-gpYHqxyFcfmrUH0ShLmnveYfRo9trXCPwXstwF_RcNMVqwfNCFBWvcV3bNM-Dr_V9F9OqfzK4LLSUuBEUHB_9tLy9YmfvoBWbSxDBO13GNB6vuM2hNKQXgfsBN9NrLfcvwmsgSq_wemZG_ONhLxUwt1YiC_k0VBQXF80qS8mrX0AgcmjDV8QXXBwrOC"
    }
    cookies = {
        "_xsrf": "ncjieleHb1IWng0IvikQ2JY8kBnR9SOL",
        "_zap": "ff47db1e-7618-4908-96ed-c1ad4e772b9a",
        "d_c0": "APARLHx_AxmPTtN_2TVzgkHcYHvZPOeY434=|1722511475",
        "q_c1": "aaa48bd451bd4a56862382dc156c8888|1722862855000|1722862855000",
        "__zse_ck": "001_A205vVo8vFHafaFlcOHeWL8l99W9=BPItymbSiZKhyVuuXQwkK3/W/AIM04oUEtbeF/bbR/peFfaLc0ygft9+vB0gC/MYhb4pBfL9d=cFYp+W+2yIdRLTtSBeeLuC3LK",
        "__snaker__id": "NBcFvuG8UeiiftNY",
        "gdxidpyhxdE": "bIcyjJMra%5CMu%2F7d9wkZ8LDBaDZtSbjb1Guw30C%2B5dzr96PjLtWBGsKHKvnJCv65IMq2CBU1rZazUfhvtYRg2jibY%5C%5CpRphTNEkTgG8%2FDAJBz9dG2%5Clvd%5Cl9A49lJQhOurgXyysO%2Fwq42VBPbIS3Hmgbg%5CISZgV5N%5C1mgiMvzqe007fd1%3A1724397417401",
        "captcha_session_v2": "2|1:0|10:1724396861|18:captcha_session_v2|88:MGtOUXhWcXRRellQRWRuN3JGODlwemdSYmlWcElFeDFXMm5ZbG4vNGZJRm1RM0hId2JUa1FUbS8yRGFnN0VMdg==|870897c21fa53c0d5fe79a8e9722f3b7e5edc71b8368f41014bfa38f16f424d2",
        "captcha_ticket_v2": "2|1:0|10:1724396864|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfdWFwLkcwblFnY1FjY3RYRXdJUE1HY0tZaVJwQnlLKl9qNmhKYnlsc3ljeTgubzZYS0JIbldDY1k5WE1MeVpaem5sZ2JwV0FKbUVnaXh5b0M0YlU2QXMxZ0NIRnM4Ul82V1dBaUdtVnpycmZTMGFvM0k2R2JMdlE5OWtlbi5CUnFQaUJybFdGbkdVLkVuUmYqTV9IVVU2b1RnRjlIRzFEcUhWZUMxRUNwaEVRZkVTUEpKYzRiWkN4c2cubm5BcDBFSU9uVE9oZ2FtaWE2M3RGWmdkcTMyeGNGeGVPaGlyWXpFWUNyS0NQSUNLVjZxcDZTSnlka0E2QVFFV2dRa0c5MXpoVHFDaEpCNGdBRUFHOEtYY19EYXQ0SEE2R21rY1NOeXFZZmlfNmVGdlFfWU5vYXlRVnE0UmVIRllGcmNyRnZMUW9vbzlTTFBFWTNuZ2VBQmJ2UC53SHdIcmhkbTQ1TU5MUzZFUHFBRFpnUFN0WjBybzFmaG1fNElHYm13R2t4TXFDQUtNTHp4MFB4aEhxTUt5UmxxSmI2em1ET25MNDB1RmExMThyek1sY3Q0SDFRQUtpaDMxYnQ0OEZEMWV3YUFiNFZTZjNfY285cW1FOGpfSWRmSWMuOUpIX0dGUUdNWm0yYlBkSWhJeldHcE5fYVpyNHJnc2ZBQnlsWXkxNTU2LjMzYVg3N192X2lfMSJ9|bdd6794f0b82c59526d56b11a80e691a53d633fd8ede78689896852edbe68b93",
        "z_c0": "2|1:0|10:1724396864|4:z_c0|92:Mi4xQXA3bEJnQUFBQUFBOEJFc2ZIOERHU1lBQUFCZ0FsVk5RSU8xWndEbW5iQkNEQXh5OUFCV0pEWGs0WmNTQ3d1Z3lR|e8c977e6b179b404e32343c34bf8f75179574f482250fc9da28f10b6822d78e4",
        "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1723427925,1724309916,1724377707,1724463826",
        "HMACCOUNT": "5952A02A4A4BF0A4",
        "SESSIONID": "diBQV26tAGpRa4Ao936WhEeWFbnJxweXlqvnuLjKd8c",
        "JOID": "VFgTA0kpmsr3k7xZGi2omDZwAVMDS_WOpMGIaWhs27yj8Iwec_mgB5eRvFke-ZJvyNVG5PTXgo97IkYGi8O-qgo=",
        "osd": "Vl4WC0ornM__kL5fHyWrmjB1CVABTfCGp8OObGBv2bqm-I8cdfyoBJWXuVEd-5RqwNZE4vHfgY19J04FicW7ogk=",
        "tst": "r",
        "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49": "1724485533",
        "BEC": "69a31c4b51f80d1feefe6d6caeac6056"
    }

    def start_requests(self):
        # 初始请求
        yield scrapy.Request(url=self.search_base_url, cookies=self.cookies, headers=self.headers, callback=self.parse, meta={'page': 1})
        
        self.logger.info('-----------开始工作-----------')

    def parse(self, response):
        # 解析 JSON 响应
        data = response.json()

        # 检查是否包含 `data` 字段
        if 'data' in data:
            for item in data['data']:
                if 'object' in item and 'type' in item and item['type'] == 'search_result':
                    question = item['object'].get('question')
                    if question:
                        question_id = question.get('id')
                        zhihu_question_item = QuestionItem()
                        zhihu_question_item['question_id'] = question.get('id')
                        zhihu_question_item['title'] = question.get('name')
                        self.logger.info(f"问题标题：{zhihu_question_item['title']}")
                        yield zhihu_question_item
                        
                        # 调用获取答案函数
                        self.headers = {
                            "accept": "*/*",
                            "accept-language": "zh-CN,zh;q=0.9",
                            "priority": "u=1, i",
                            "referer": f"https://www.zhihu.com/question/{question_id}",
                            "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
                            "sec-ch-ua-mobile": "?0",
                            "sec-ch-ua-platform": "\"Windows\"",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                            "x-requested-with": "fetch",
                            "x-zse-93": "101_3_3.0",
                            "x-zse-96": "2.0_9DBLPgcr86AdSMhzANX52uj6mHDBGpH4Q3VHOrfCrY0DBAdqSh5qQqafclj/IPd2",
                            "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZGTY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPF7VMUCtK2JwLxqoL8gtGwG2C6gH1DwFXbGOO-UL96gXYIuc8Zh3KGbLm6LSTveH8bQS9MM3BLJL_CDp_HgH00hNLBDCMAU28nDNfjCVGfgx08GcXYDcV79gmIugfUu3x2LcL1HgKwgVCe_SV0hXBqqc9hgUOjGtf1JLq69eqADr_LCH9Cqfz2UCZAqCM6wx9UwHOXDo8xUuLBCcBcRpmFgC8JquLcDxmYwY8v93LFUgO9bSXagHByu201cS11ckmtUCy7cffPDcGL9HX2iCZMrLOTvU_ucnLWhXCGwFC"
                        }
                        self.cookies = {
                            "_xsrf": "o8w2Np1l9VDY5SpTdYfXpHHqjSyicV76",
                            "__zse_ck": "001_5c0hwLk/RtV0V1q+xPlfsq9LpRqokpEQ/O5s5+pCTk9sAG=D/WKCcTqN6axFEaI8cvsbYLQHlhZggUJUGY/9/Jt/oY9SOQWL+5NLLkUhJF+=iDehdrCdH/=2m79IF3h6",
                            "_zap": "8b74c4c5-ad5d-4425-940a-ceb0dc523cc9",
                            "d_c0": "AiBS1x-YHxmPTl0cHhPxmOWR0UqRQNc8O6E=|1724396982",
                            "gdxidpyhxdE": "TfzCn%2FBtlLM3CeKqBeRQcd%2F4sKBKqCXYdygmoREqQfcK1Ns1PKE0U4xAKX7xfjVqId%5CdI6JEPMx%2F354JKP7puxnc%5Cds1P6zbvS4n6LgdIUAAZmIicr0gbPe0Vy%2F5Y2HHgBCc%2FEH4gOTqa0dWgCdd5IQEMcXkDsUvbEkWwryxreCie7Xa%3A1724465570927",
                            "captcha_session_v2": "2|1:0|10:1724464695|18:captcha_session_v2|88:QVlzelNnbmZxQjhYNmZycllyQVhzNUk4c2V3YUZRcGRHWktkdTRmc2hvNDBSbkswaW9HUGVFWW9NemVXWWpwZQ==|5f55f191ed7c936f435b23e40dde607b4fa53bdd68c7fdf36dcbf1823806442a",
                            "captcha_ticket_v2": "2|1:0|10:1724464704|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6Ik5BTlBfcXlhbktTSWV3ZXVMUnNjdUd5Wk1ZSE5oXzUxQ05mOWhxRi4xX0xxbU1ySlVlMDFjODYub3NTQkxTSm10WmhrSm5vT0pLZ25YTlhtNWNlS0lUeTE0QXk5KjFtOHZGYnlIcXRUZHBMKjhUWWN2YzNmc1pDM1JNc25kSExKMkp0SjM0SUNVWjEyZXdCRHVub1IwQUczYlBTY3VJRzJEOFdHY0NZRFdPaVhYMXdwaFk4LkpYZm50d3U5cFJ0VklQejhGdWlORXJsUUpKdjJvdktQb3ZoWnp5cHo5ekV2bVo5Kk1nc3A5VGNRNm5JYnJhQXhOZEFieDRxakpPSXFZc19VcFU1TjBuKmNjbFJob3lYVUpRQnRDOF9fUHlxUFlwQmFpbE9DRThWRVJqZW16KjJBbmlXb3lRY1NZVzZKNFByVmdXU3FSVEZTU3dmVU5ScjRfbGRleE9rb3VvVGZMVS5KY2h0VThQRC5HajNocnRrRDNlcjZIc0VfT3VsbDF2RHVlcF9VQXJEVGlGbU5qQzNCMVgzNmlyM1RKSyp2b21ubkxjS05IR2JYY05TX25mWkUwcGNkUURZWUxsWkoyWGVvajRxdmJhVjNOLlh2KnYyZmRkSzRNYW90SFdQME0xWHZSd0t0S0VGb2RmclJ6ZzFvbkZPNFRwUUI2NVZhdW0zQXQqTjNVdFg3N192X2lfMSJ9|b46a1d1065649f57d1d4e9b530a8d4e14930a9e498b6a90be04c3fe6a23e830c",
                            "z_c0": "2|1:0|10:1724464715|4:z_c0|92:Mi4xQXA3bEJnQUFBQUFDSUZMWEg1Z2ZHU1lBQUFCZ0FsVk5TNHkyWndDUUJPSjB4MXRSZWpnUmVLOV9TNWVuS2NWVWp3|9de38153a44082fe02f8b3821b724ab37fe3d4b3a54a05ecca1d9bf47d865222",
                            "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1724464766",
                            "q_c1": "711c903f49ae45279ff92535eb9e0059|1724554254000|1724554254000",
                            "tst": "r",
                            "BEC": "6bca8f185b99e85d761c7a0d8d692864"
                        }
                        answer_url = f"https://www.zhihu.com/question/{question_id}"
                        yield scrapy.Request(url=answer_url, cookies=self.cookies, headers=self.headers, callback=self.parse_answers, meta={'question_id': question_id})                        

        # 检查是否还有下一页
        paging = data.get('paging')
        current_page = response.meta.get('page')
        if paging and not paging.get('is_end'):
            # 处理下一页网址
            next_page_url = paging.get('next')
            next_page_url = re.sub(r'\\u0026', '&', next_page_url)
            
            # 解析url
            parsed_url = urlparse(next_page_url)
            base_url = "https://www.zhihu.com/api/v4/search_v3"
            params = parse_qs(parsed_url.query)

            # 确保参数格式正确
            for key, value in params.items():
                if isinstance(value, list):
                    params[key] = ",".join(value)
            
            # 添加或更新参数
            params['lc_idx'] = params['offset']
            params['search_hash_id'] = data.get('search_action_info', {}).get('search_hash_id', '')
            params['filter_fields'] = ""

            # 按照指定顺序排列参数
            order = [
                "gk_version", "t", "q", "correction", "offset", "limit", 
                "filter_fields", "lc_idx", "show_all_topics", "search_hash_id", "search_source"
            ]
            ordered_params = OrderedDict((key, params[key]) for key in order if key in params)
            next_page_url = base_url + "?" + urlencode(ordered_params)

            self.logger.info(f"下一页地址：{next_page_url}")
            if current_page <= self.max_pages:
                # 请求下一页
                yield scrapy.Request(url=next_page_url, cookies=self.cookies, headers=self.headers, callback=self.parse, meta={'page': current_page + 1})
            else:
                self.logger.info(f"已经达到最大页数 {self.max_pages} 页，停止翻页")
        else:
            self.logger.info('-----------搜索问题ID结束，翻页完毕-----------')
            

    def parse_answers(self, response):

        # 获取答案逻辑
        question_id = response.meta.get('question_id')

        # 获取初始数据
        initial_data_match = re.search(r'(?<=<script id="js-initialData" type="text/json">)(.*?)(?=</script>)', response.text)

        if not initial_data_match:
            self.logger.error("无法获取初始数据")
            return

        initial_data = json.loads(initial_data_match.group(1))
        next_url = initial_data["initialState"]["question"]["answers"].get(str(question_id)).get("next")

        if next_url:
            next_url = re.sub(r'\\u002F', '/', next_url)
            self.logger.info(f"获取到答案url：{next_url}")
            parsed_url = urlparse(next_url)
            # cursor = next_url_params.get("cursor", [""])[0]
            # session_id = next_url_params.get("session_id", [""])[0]

            # # 请求获取答案数据
            # answer_data_url = f"https://www.zhihu.com/api/v4/questions/{question_id}/feeds"
            # params = {
            #     "cursor": cursor,
            #     "limit": "20",
            #     "offset": "1",
            #     "order": "default",
            #     "platform": "desktop",
            #     "session_id": session_id
            # }
            # answer_data_url = answer_data_url + "?" + urlencode(params)
            # self.logger.info(f"请求答案数据：{answer_data_url}")
            
            # 获取查询参数并修改
            query_params = parse_qs(parsed_url.query)
            query_params['limit'] = ['20']  # 修改limit值为20

            # 重新编码查询参数
            new_query = urlencode(query_params, doseq=True)

            # 构造新的URL
            new_url = urlunparse(parsed_url._replace(query=new_query))
            
        else:
            self.logger.error("无法获取答案url")
        
        yield scrapy.Request(url=new_url, cookies=self.cookies, headers=self.headers, callback=self.extract_answers)
        
    def extract_answers(self, response):
        # 提取答案
        data = response.json().get("data")
        if data is None:
            self.logger.error("无法获取答案数据")
            return
        answers = [item.get("target").get("content") for item in data]

        # 保存答案
        cnt = 1
        with open("answers.txt", "a", encoding="utf-8") as f:
            for answer in answers:
                answer_cleaned = re.sub(r'<.*?>', '', answer)  # 去除HTML标签
                f.write(f"==========第{cnt}个回答===========\n")
                f.write(answer_cleaned + "\n")
                cnt += 1

        self.logger.info(f"获取了 {len(answers)} 个回答")