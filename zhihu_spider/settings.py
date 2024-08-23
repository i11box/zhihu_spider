# Scrapy settings for zhihu_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "zhihu_spider"
DOWNLOADER_MIDDLEWARES = {
    'zhihu_spider.middlewares.RandomDelayMiddleware': 543
}
SPIDER_MODULES = ["zhihu_spider.spiders"]
NEWSPIDER_MODULE = "zhihu_spider.spiders"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
ITEM_PIPELINES = {
    'zhihu_spider.pipelines.ZhihuSpiderPipeline': 300
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "zhihu_spider (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "^cookie": "_xsrf=ncjieleHb1IWng0IvikQ2JY8kBnR9SOL; _zap=ff47db1e-7618-4908-96ed-c1ad4e772b9a; d_c0=APARLHx_AxmPTtN_2TVzgkHcYHvZPOeY434=^|1722511475; q_c1=aaa48bd451bd4a56862382dc156c8888^|1722862855000^|1722862855000; __zse_ck=001_A205vVo8vFHafaFlcOHeWL8l99W9=BPItymbSiZKhyVuuXQwkK3/W/AIM04oUEtbeF/bbR/peFfaLc0ygft9+vB0gC/MYhb4pBfL9d=cFYp+W+2yIdRLTtSBeeLuC3LK; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1722863085,1723427925,1724309916,1724377707; HMACCOUNT=5952A02A4A4BF0A4; __snaker__id=NBcFvuG8UeiiftNY; SESSIONID=e7E6IafenB3YVM9pEGgyEgeruioxYLeOucNISdlnz1i; JOID=UFoRC0_IrH2ZUtiZO8CaKVK1aZckrZ00ox25-VKg7kjMCJOgTeastfVU3pM7kpr2hhNlZMSwTJ2F_rDz9u7DcwY=; osd=Vl4dA0_OqHGRUt6dN8iaL1a5YZciqZE8oxu99Vqg6EzAAJOmSeqktfNQ0ps7lJ76jhNjYMi4TJuB8rjz8OrPewY=; gdxidpyhxdE=bIcyjJMra^%^5CMu^%^2F7d9wkZ8LDBaDZtSbjb1Guw30C^%^2B5dzr96PjLtWBGsKHKvnJCv65IMq2CBU1rZazUfhvtYRg2jibY^%^5C^%^5CpRphTNEkTgG8^%^2FDAJBz9dG2^%^5Clvd^%^5Cl9A49lJQhOurgXyysO^%^2Fwq42VBPbIS3Hmgbg^%^5CISZgV5N^%^5C1mgiMvzqe007fd1^%^3A1724397417401; captcha_session_v2=2^|1:0^|10:1724396861^|18:captcha_session_v2^|88:MGtOUXhWcXRRellQRWRuN3JGODlwemdSYmlWcElFeDFXMm5ZbG4vNGZJRm1RM0hId2JUa1FUbS8yRGFnN0VMdg==^|870897c21fa53c0d5fe79a8e9722f3b7e5edc71b8368f41014bfa38f16f424d2; captcha_ticket_v2=2^|1:0^|10:1724396864^|17:captcha_ticket_v2^|728:eyJ2YWxpZGF0ZSI6IkNOMzFfdWFwLkcwblFnY1FjY3RYRXdJUE1HY0tZaVJwQnlLKl9qNmhKYnlsc3ljeTgubzZYS0JIbldDY1k5WE1MeVpaem5sZ2JwV0FKbUVnaXh5b0M0YlU2QXMxZ0NIRnM4Ul82V1dBaUdtVnpycmZTMGFvM0k2R2JMdlE5OWtlbi5CUnFQaUJybFdGbkdVLkVuUmYqTV9IVVU2b1RnRjlIRzFEcUhWZUMxRUNwaEVRZkVTUEpKYzRiWkN4c2cubm5BcDBFSU9uVE9oZ2FtaWE2M3RGWmdkcTMyeGNGeGVPaGlyWXpFWUNyS0NQSUNLVjZxcDZTSnlka0E2QVFFV2dRa0c5MXpoVHFDaEpCNGdBRUFHOEtYY19EYXQ0SEE2R21rY1NOeXFZZmlfNmVGdlFfWU5vYXlRVnE0UmVIRllGcmNyRnZMUW9vbzlTTFBFWTNuZ2VBQmJ2UC53SHdIcmhkbTQ1TU5MUzZFUHFBRFpnUFN0WjBybzFmaG1fNElHYm13R2t4TXFDQUtNTHp4MFB4aEhxTUt5UmxxSmI2em1ET25MNDB1RmExMThyek1sY3Q0SDFRQUtpaDMxYnQ0OEZEMWV3YUFiNFZTZjNfY285cW1FOGpfSWRmSWMuOUpIX0dGUUdNWm0yYlBkSWhJeldHcE5fYVpyNHJnc2ZBQnlsWXkxNTU2LjMzYVg3N192X2lfMSJ9^|bdd6794f0b82c59526d56b11a80e691a53d633fd8ede78689896852edbe68b93; z_c0=2^|1:0^|10:1724396864^|4:z_c0^|92:Mi4xQXA3bEJnQUFBQUFBOEJFc2ZIOERHU1lBQUFCZ0FsVk5RSU8xWndEbW5iQkNEQXh5OUFCV0pEWGs0WmNTQ3d1Z3lR^|e8c977e6b179b404e32343c34bf8f75179574f482250fc9da28f10b6822d78e4; tst=r; BEC=8b4a1b0a664dd5d88434ef53342ae417; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1724397235^",
    "priority": "u=1, i",
    "^referer": "https://www.zhihu.com/search?type=content&q=^%^E5^%^85^%^A8^%^E6^%^A0^%^88^",
    "^sec-ch-ua": "^\\^Not)A;Brand^^;v=^\\^99^^, ^\\^Microsoft",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^\\^Windows^^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "x-api-version": "3.0.91",
    "x-app-za": "OS=Web",
    "x-requested-with": "fetch",
    "x-zse-93": "101_3_3.0",
    "x-zse-96": "2.0_xQt=WLyvRKmlKKSY0yLW0n7ad9tb7LSl9PwGZCsyhp1VQTv=jjT8KK1=85MqYq1a",
    "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZGTY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPFLgMWgNffqV9n93VIhF9vwOqcqe069pVgUO90hY8_cwOAuFMnvOO3qCqZcoTvHCVgugMgUFKaUwyPCp8L9Y13gg1yhH1SMt8AG2M1uYLyrXGWwoYYcSY7wL_jvNq3wpsbHYGfvxywuVMDqxMBCY8mQL8DhUYHBFVChc9nwoYsD9_H9F9Oqfz2uFCQheCVwLOP9cqvgxy6QSLhqYpCwNYhBLy9DCLn9OGiBp1YULfSHCK3woswhYYBi38TvpMLGYfS7Vf1wC06wH8Iho_SMc_hGc0oJr0JDO8WwXO-rSC"
}

MAX_PAGE = 5

DATA_URI = 'data_file'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "zhihu_spider.middlewares.ZhihuSpiderSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "zhihu_spider.middlewares.ZhihuSpiderDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "zhihu_spider.pipelines.ZhihuSpiderPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
