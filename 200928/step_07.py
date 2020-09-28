from log_parse import file_parse, save_parsed_data

parsed_data = file_parse('nginx_logs_head.txt')
save_parsed_data('logs_parsed.csv', parsed_data)
