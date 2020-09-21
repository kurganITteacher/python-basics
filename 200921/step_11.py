# scrapy
row_record = '217.168.17.5 - - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"'
correct_result = '217.168.17.5'
# correct_result = ['217.168.17.5', '- - [17/May/2015:08:05:12 +0000] "GET /downloads/product_2 HTTP/1.1" 200 3316 "-" "-"']
# [<remote_IP_address>, '']
result = row_record.split()[0]
print(result)

assert result == correct_result
