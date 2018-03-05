#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
from datetime import datetime

from libs.excel import Excel
from service.admin import *
from service.business import BusinessService
from forms.admin import TrackingForm, OrderForm
from .base import BaseHandler, LoginRequireMixin


__all__ = ['AdminLoginHandler', 'OrderDetailHandler',
           'DonateDetailHandler', 'DonateListHandler',
           'EmailDetailHandler', 'EmailListHandler', 'OrderListHandler',
           'TrackingCodeListHandler', 'TrackingCodeDetailHandler',
           'TrackingCodeCreateHandler', 'OrderTrackingNoUploadHandler',
           'AdminLogoutHandler', 'OrderExportHandler',
           'SysConfigHandler']

# ======================================================
# AdminBase ============================================
# ======================================================


class AdminBaseHandler(BaseHandler):

    def get_current_user(self):
        return self.get_secure_cookie("user_id")

# ======================================================
# main handler =========================================
# ======================================================


class AdminLoginHandler(AdminBaseHandler):

    def get(self):
        self.render("admin/login.html", error_message=None)

    def post(self):
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")

        login_status = AdminService.login(self.db,
                                          username, password)
        if login_status['error'] != 0:
            return self.render("admin/login.html",
                               error_message=login_status['message'])
        else:
            self.set_secure_cookie("user_id",
                                   login_status['user_id'])
            # 登录成功，重定向
            self.redirect(self.reverse_url("admin:order:list"))


class EmailListHandler(LoginRequireMixin, AdminBaseHandler):

    def get(self):
        page_num = self.get_page_arg()
        object_list = EmailService.get_object_list(self.db,
                                                   page_num)
        pass


class EmailDetailHandler(LoginRequireMixin, AdminBaseHandler):

    def get(self, id_):
        obj = EmailService.get_object_by_id(self.db,
                                            id_)
        if obj is None:
            return self.write_error(404)

        # TODO: render


class DonateListHandler(LoginRequireMixin, AdminBaseHandler):

    def get(self):
        page_num = self.get_page_arg()
        object_list = DonateService.get_object_list(self.db,
                                                    page_num)
        # TODO: render

    def post(self):
        pass


class DonateDetailHandler(LoginRequireMixin, AdminBaseHandler):

    def get(self, id_):
        obj = DonateService.get_object_by_id(self.db,
                                             id_)
        if obj is None:
            return self.write_error(404)

        # TODO: render

    def post(self, id_):
        pass


class OrderListHandler(LoginRequireMixin, AdminBaseHandler):

    def get(self):
        start_date = self.get_query_argument('start_date', '')
        end_date = self.get_query_argument("end_date", "")
        if start_date:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        if end_date:
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        filter_ = {
            'start_date': start_date,
            'end_date': end_date,
            'status': self.get_query_argument('status', ''),
            'filtered': False
        }
        if self._is_filtered(filter_):
            filter_['filtered'] = True
        page_num = self.get_page_arg()

        object_list = OrderService.get_object_list(self.db, page_num, filter_)
        self.render("admin/order/list.html",
                    object_list=object_list,
                    page_num=page_num,
                    filter=filter_)

    def put(self):
        """这个接口用于修改订单状态"""
        data = json.loads(self.request.body)
        BusinessService.change_order_status(self.db,
                                    order_id=data['id'],
                                    status=data['status'],
                                    user_id=self.get_secure_cookie('user_id'))

    def _is_filtered(self, filter_):
        """根据filter参数判断是否存在筛选参数"""
        for value in filter_.values():
            if value:
                return True
        return False


class OrderDetailHandler(LoginRequireMixin, AdminBaseHandler):
    error_message = None

    def get(self, id_):
        obj = OrderService.get_object_by_id(self.db,
                                            obj_id=id_)
        if obj is None:
            return self.write_error(404)
        form = OrderForm(data=obj.__dict__)
        self.render("admin/order/detail.html",
                    obj=obj,
                    form=form,
                    error_message=self.error_message)

    def post(self, id_):
        # 获取对象
        obj = OrderService.get_object_by_id(self.db,
                                            obj_id=id_)
        if obj is None:
            return self.write_error(404)

        # 表单验证
        form = OrderForm(self.request.body_arguments)
        if not form:
            error_message = form.errors
            return self.render("admin/order/detail.html",
                               form=form,
                               obj=obj,
                               error_message=error_message)

        # 更新对象
        update_info = OrderService.update(self.db, obj, **form.data)
        if update_info['error'] != 0:
            return self.render("admin/order/detail.html",
                               error_message=update_info['message'])
        self.redirect(self.reverse_url("admin:order:list"))

    def delete(self, id_):
        # 获取对象
        obj = OrderService.get_object_by_id(self.db,
                                            obj_id=id_)
        if obj is None:
            return self.write_error(404)
        delete_info = OrderService.delete(self.db, obj,
                                          self.get_secure_cookie('user_id'))
        if delete_info['error'] != 0:
            return self.write_error(500, reason=delete_info['message'])


class OrderTrackingNoUploadHandler(LoginRequireMixin, AdminBaseHandler):
    """处理上传快递单号文件(.xls)"""

    def post(self):
        """接收上传的excel文件

        上传的excel文件应该具有两列: order_no和tracking_no.
        根据order_no找到订单，然后更新tracking_no字段.
        更新成功以后修改订单状态: processing(处理中) -> shipped(已发货)
        并且发送通知邮件(event事件处理)
        """
        file = self.request.files['excel'][0]
        if not '.xls' in file['content_type'] and \
                not '.xlsx' in file['content_type']:
            return self.write_error(400, message='文件格式不合法,'
                                                 '只支持excel文件')
        xls = Excel(file_contents=file['body'])
        try:
            dct_list = xls.rows_to_dicts(
                header_format=Excel._col_name_underscore_fmt
            )
            if not dct_list:
                raise KeyError
            for dct in dct_list:
                BusinessService.order_deliver_upload(
                    self.db,
                    self.get_secure_cookie('user_id'),
                    order_no=dct['order_no'],
                    tracking_no=dct['tracking_no']
                )
        except KeyError:
            self.write_error(400, message='excel文件必须包含'
                                          'order_no和tracking_no这两个列名')
        else:
            self.write("文件上传成功")


class OrderExportHandler(LoginRequireMixin, AdminBaseHandler):

    def get(self):
        """接受订单筛选参数，返回一个excel文件
        
        另外，如果订单处于‘已支付’状态，再导出以后状态将会自动变为‘处理中’
        :param start_date: ‘起始日期’，格式为'YYYY-MM-DD'的字符串
        :param end_date: ‘结束日期’, 格式为'YYYY-MM-DD'的字符串
        :param status:　‘状态’, 订单状态
        :return: 
        """
        start_date = self.get_query_argument('start_date', '')
        end_date = self.get_query_argument('end_date', '')
        status = self.get_query_argument('status', '')
        if start_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        if end_date:
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

        object_list = BusinessService.order_data_export(
            self.db,
            start_date=start_date,
            end_date=end_date,
            status=status,
            user_id=self.get_secure_cookie('user_id')
        )
        header = ['fullname', 'address', 'zip-code', 'city', 'state/province',
                  'country', 'phone', 'email', 'pstyle', 'order_no', 'num']
        data = [
            (
                obj.fullname(),
                obj.address,
                obj.zipcode,
                obj.city,
                obj.state,
                obj.country,
                obj.phone,
                obj.email,
                "color: {0} size: {1}".format('black', obj.size),
                obj.order_no,
                obj.quantity
            )
            for obj in object_list
        ]

        # 以excel格式导出
        self.set_header('Content-Type', 'application/x-xls')
        self.set_header('Content-Disposition',
                        'attachment; filename=export.xls')
        io_data = Excel.write_to_file(header, data)
        self.write(io_data)


class TrackingCodeListHandler(LoginRequireMixin, AdminBaseHandler):

    def get(self):
        page_num = self.get_page_arg()
        object_list = TrackingService.get_object_list(self.db,
                                                      page_num)
        self.render("admin/tracking/list.html",
                    object_list=object_list,
                    page_num=page_num)


class TrackingCodeCreateHandler(LoginRequireMixin, AdminBaseHandler):
    error_message = None

    def get(self):
        form = TrackingForm(data={
            "code": TrackingService.gen_unique_code(self.db)
        })
        self.render("admin/tracking/create.html",
                    form=form,
                    error_message=self.error_message)

    def post(self):
        form = TrackingForm(self.request.body_arguments)
        if not form.validate():
            error_message = form.errors
            return self.render("admin/tracking/create.html",
                               form=form,
                               error_message=error_message)
        create_info = TrackingService.create(self.db, **form.data)
        if create_info['error'] != 0:
            return self.render("admin/tracking/create.html",
                               form=form,
                               error_message=create_info['message'])
        self.redirect(self.reverse_url("admin:tracking:list"))


class TrackingCodeDetailHandler(LoginRequireMixin, AdminBaseHandler):
    error_message = None

    def get(self, id_):
        obj = TrackingService.get_object_by_id(self.db,
                                               id_)
        if obj is None:
            return self.write_error(404)

        form = TrackingForm(data=obj.__dict__)
        self.render("admin/tracking/detail.html",
                    form=form,
                    obj=obj,
                    error_message=self.error_message)

    def post(self, id_):
        obj = TrackingService.get_object_by_id(self.db,
                                               obj_id=id_)
        if obj is None:
            return self.write_error(404)

        form = TrackingForm(self.request.body_arguments)
        if not form.validate():
            error_message = form.errors
            return self.render("admin/tracking/detail.html",
                               form=form,
                               obj=obj,
                               error_message=error_message)

        # 更新对象
        update_info = TrackingService.update(self.db, obj, **form.data)
        if update_info['error'] != 0:
            error_message = update_info['message']
            return self.render("admin/tracking/detail.html",
                               form=form,
                               obj_id=id_,
                               error_message=error_message)
        # 成功更新
        self.redirect(self.reverse_url("admin:tracking:list"))

    def delete(self, id_):
        # 获取对象
        obj = TrackingService.get_object_by_id(self.db,
                                               obj_id=id_)
        if obj is None:
            return self.write_error(404)
        delete_info = TrackingService.delete(self.db, obj)
        if delete_info['error'] != 0:
            return self.write_error(500, reason=delete_info['message'])


class AdminLogoutHandler(LoginRequireMixin, AdminBaseHandler):

    def get(self, *args, **kwargs):
        self.clear_cookie("user_id")
        self.redirect(self.reverse_url("admin:logout"))


class SysConfigHandler(LoginRequireMixin, AdminBaseHandler):

    def get(self, *args, **kwargs):
        success = False
        if self.get_query_argument('s', None):
            success = True
        template_dir = SysConfig.template_dir()
        email_dir = SysConfig.email_dir()
        self.render(
            'admin/sys_config/index.html',
            template_dir=template_dir,
            email_dir=email_dir,
            success=success
        )

    def post(self, *args, **kwargs):
        template_dir = self.get_body_argument('template_dir')
        SysConfig.set_template_dir(template_dir)

        email_dir = self.get_body_argument('email_dir')
        SysConfig.set_email_dir(email_dir)

        self.redirect(self.reverse_url('admin:sys-config') + '?s=1')

