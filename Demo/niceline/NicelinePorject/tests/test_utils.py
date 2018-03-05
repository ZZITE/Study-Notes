#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

from tornado.testing import AsyncTestCase
import xlrd

from libs.excel import Excel

__all__ = ['ExcelUtilsTestCase']

# constants
TEST_DIR = os.path.dirname(__file__)


class ExcelUtilsTestCase(AsyncTestCase):

    def test_read_xls_file(self):
        xls = Excel(os.path.join(TEST_DIR, "fixtures/read_1.xls"))
        self.assertIsInstance(xls.workbook,
                              xlrd.book.Book)
        self.assertIsInstance(xls.sheet,
                              xlrd.sheet.Sheet)

    def test_read_xls_file_to_dict(self):
        xls = Excel(os.path.join(TEST_DIR, "fixtures/read_1.xls"))
        data = xls.rows_to_dicts(header_format=Excel._col_name_underscore_fmt)

        self.assertIsInstance(data[0], dict)
        self.assertIn('order_no', data[0])
        self.assertEqual(len(data), 2)





