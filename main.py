import fileinput
import re
from pathlib import Path
import time


class ResBytesCounter:
    def __init__(self, file_name: str = " "):
        self.file_name = file_name
        self.period = []
        self.sum_size_of_images = 0

    def ok_img(self):
        pattern_request_ok_jpg = r'(GET|POST)+(.*(jpg).* 200 )'
        pattern_request_ok_png = r'(GET|POST)+(.*(png).* 200 )'
        list_of_request_ok_jpg = []
        list_of_request_ok_png = []
        for line in self.period:
            if re.findall(pattern_request_ok_jpg, str(line)):
                list_of_request_ok_jpg.append(line)
            elif re.findall(pattern_request_ok_png, str(line)):
                list_of_request_ok_png.append(line)
        return list_of_request_ok_jpg, list_of_request_ok_png

    def calc_size_resource_of_request(self, list_of_request):
        pattern_size_request = r'\s\d{4}\d*\s'
        count = 0
        for line in list_of_request:
            count += int(str(re.findall(pattern_size_request,
                                        str(line))).replace(" ", "").replace("[", "").replace("]", "").replace("'", ""))
        print(f"Size of images: {count}")

    def sort_by_date_and_time(self):
        lines = list(fileinput.input(self.file_name))
        file = open(f"copyof{self.file_name}", mode='w')
        for line in sorted(lines, key=lambda l: re.findall(r'\d+/\w+/\d+:\d+:\d+:\d+', str(l))):
            file.write(line)
        file.close()

    def __is_date(self, start_date: str = " ", end_date: str = " "):
        file = open(f"copyof{self.file_name}", mode='r')
        lines = file.read().splitlines()
        file.close()
        if re.search(start_date, str(lines)):
            if re.search(end_date, str(lines)):
                return True
        else:
            return False

    def search_period(self, start_date: str = " ", end_date: str = " "):
        pattern_of_time = r'\d+/\w+/\d+:\d+:\d+:\d+'
        if Path(self.file_name).is_file():
            print(f"\u001b[32mFile exist")
        else:
            print("\u001b[31mFile not exist")
            raise IOError

        try:
            is_period = False
            self.sort_by_date_and_time()
            file = open(f"copyof{self.file_name}", mode='r')
            lines = file.read().splitlines()
            file.close()
            if not self.__is_date(start_date, end_date):
                print("\u001b[31mThere is no such period of time")
                raise IOError

            for line in lines:
                found_start_time = re.findall(pattern_of_time, str(line))

                if is_period == True:
                    break
                for i in found_start_time:
                    if i > f"{end_date}":
                        is_period = True
                        break
                    else:
                        pass
                    if i >= f"{start_date}":
                        self.period.append(line)
        except IOError as e:
            print(e)


if __name__ == '__main__':
    start_time = time.time()
    counter = ResBytesCounter("apache_logs")
    counter.search_period("17/May/2015:10:05:03", "17/May/2015:10:05:43")
    a, b = counter.ok_img()
    counter.calc_size_resource_of_request(a)
    counter.calc_size_resource_of_request(b)
    print("\u001b[35mProcessing time: %.2f" % (time.time() - start_time))

