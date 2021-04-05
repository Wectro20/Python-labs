#needs refinement
import re

regex = r'(.+)'


def convert_time(time): return sum(int(x) * 60 ** i for i, x in enumerate(reversed(time.split(':'))))


def get_bytes(string_data):
    return int(string_data[3]) \
    if string_data[1] == '05/Mar/2004' and \
        convert_time("17:04:44") <= convert_time(data[2]) <= convert_time("15:21:28") and\
        string_data[3] != '12/Mar/2004' else 0


if __name__ == '__main__':
    with open('apache_logs', 'r') as file:
        successful, bytes_size = 0, 0
        for line in file.readlines():
            data = re.match(regex, line)
            if data:
                bytes_size, \
                successful = bytes_size + get_bytes(data),\
                successful + 1
        print(f"total image file size {successful}, "
              f"total number of bytes {bytes_size}")
