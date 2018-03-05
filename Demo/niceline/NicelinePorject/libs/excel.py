#! /usr/bin/env python
# -*- coding: utf-8 -*-
from io import BytesIO
import re
import xlrd
import xlwt


COLNAME_SUB_PATTERN = re.compile(r"[-_ ]")


class Excel(object):

    @classmethod
    def write_to_file(cls, headers, data):
        """将数据写入并生成文件内容"""
        workbook = xlwt.Workbook()
        workbook.encoding = 'gbk'
        sheet = workbook.add_sheet('sheet1')
        rowx = 0
        for colx, value in enumerate(headers):
            sheet.write(rowx, colx, value)

        for row in data:
            rowx += 1
            for colx, value in enumerate(row):
                sheet.write(rowx, colx, value)
        bio = BytesIO()
        workbook.save(bio)
        return bio.getvalue()


    def __init__(self, filename=None, file_contents=None):
        """接受一个excel文件名和或者excel文件内容
        """
        if filename is not None and file_contents is not None:
            raise ValueError("Only one of 'filename', 'file_contents'"
                             "can be pass to __init__")
        if filename:
            self.workbook = xlrd.open_workbook(filename)
        elif file_contents:
            self.workbook = xlrd.open_workbook(file_contents=file_contents)
        else:
            raise ValueError("Not pass any argument")
        # 默认使用index=0的sheet
        self.sheet = self.workbook.sheet_by_index(0)

    def sheet_by_index(self, index):
        """根据索引重新选择使用的sheet"""
        self.sheet = self.workbook.sheet_by_index(index)

    def rows_to_dicts(self, header_format=None):
        """将excel的文件内容转换为Python的数据格式

        :param: header_format是一个可选的列名格式化函数
        :return: 返回一个列表，列表中的每个元素都是一个dict，代表excel中的一个row
        """
        result = []
        headers = []
        for index, row in enumerate(self.sheet.get_rows()):
            if index == 0:  # 获取列名
                for cell in row:
                    if header_format is None:
                        headers.append(cell.value.strip())
                    else:
                        headers.append(header_format(cell.value))
            else:
                row_dict = {}
                for cell_index, cell in enumerate(row):
                    row_dict[headers[cell_index]] = str(cell.value).strip()
                result.append(row_dict)
        return result

    @staticmethod
    def _col_name_underscore_fmt(value):
        """列名格式化函数"""
        return COLNAME_SUB_PATTERN.sub("_", value).strip()


if __name__ == '__main__':
    xls = Excel("订单信息171020发货后.xls")
    result = xls.row_to_dict(header_format=Excel._col_name_underscore_fmt)
    print(result)
    '40f8cc9bdfd8'