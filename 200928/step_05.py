# settings
src_data_file = 'nginx_logs_head.txt'
parsed_data_file = 'nginx_logs_parsed.csv'

# init
parsed_data = []


def row_parse(item):
    remote_IP_address, row_tail = item.split(maxsplit=1)
    _, _request_datetime = row_tail.split('[', maxsplit=1)
    request_datetime, row_tail = _request_datetime.split(']', maxsplit=1)

    _, _request_method, row_tail = row_tail.split('"', maxsplit=2)
    request_method, requested_resource, _ = _request_method.split(maxsplit=2)

    # prepare result
    parsed_row = [remote_IP_address, request_datetime, request_method, requested_resource]
    return list(map(str.strip, parsed_row))


# result = row_parse(
#     '93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" '
#     '"Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.21)"'
# )
# assert result == ['93.180.71.3', '17/May/2015:08:05:32 +0000', 'GET', '/downloads/product_1']

# parse
with open(src_data_file, 'r', encoding='utf-8') as f:
    for row in f.read().splitlines():
        # validation
        if not row:
            continue
        # row parse
        parsed_row = row_parse(row)  # call the function row_parse with arg: row
        # append result
        parsed_data.append(parsed_row)

# print(parsed_data[2])
# save
with open(parsed_data_file, 'w', encoding='utf-8') as f:
    for row in parsed_data:
        f.write(f"{', '.join(row)}\n")
