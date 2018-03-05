下面的这一段代码竟然能够正常运行？甚至能够发出邮件？有时间可以重演一下看看是什么原因:

```python
class MailClient(object):
    """邮件发送客户端"""

    @staticmethod
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    @classmethod
    def _message_create(cls, from_, to, subject, content, type='html'):
        """

        :param from_: 寄信人
        :param to: 收件者
        :param subject: 标题
        :param content: 内容
        :param type: 邮件的mimetype, 默认为"html"
        :return: MIMEText对象
        """
        from_ = "{0} <{1}>".format(Config.EMAIL_SENDER, from_)
        msg = MIMEText(content, type, "utf-8")
        msg['From'] = cls._format_addr(from_)
        msg['To'] = Header(to, 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8').encode()
        return msg

    @classmethod
    def _mail_send(cls, from_addr, to_addr, msg,
                  smtp_server, smtp_port, password):
        """

        :param from_addr: 发件人的邮箱地址
        :param to_addr: 收信人(多人)的邮箱地址(可迭代对象)
        :param msg: 一个email.MIMEText对象
        :param smtp_port: smtp端口
        :param smtp_server: smtp服务器
        :return:
        """

        # 建立和smtp服务器的连接并登录
        server = smtplib.SMTP(smtp_server, smtp_port)
        # server.set_debuglevel(1)
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()

    def send_mail(to, subject, content):        # 诡异之处，这里忘了加@classmethod
                                                # 但是可以在不实例化MailClient的情况调用这个方法
                                                # 比如Client.send_mail(some_mail, title, content)
        # 创建邮件msg对象                         # 竟然仍然能传入3个参数？to可以当做参数是使用
        from_ = Config.SMTP_USERNAME
        msg_obj = MailClient._message_create(from_,
                                            to,
                                            subject,
                                            content)
        # 发送邮件
        MailClient._mail_send(from_, [to], msg_obj,
                              Config.SMTP_SERVER,
                              Config.SMTP_PORT,
                              Config.SMTP_PASSWORD)

# ===============================================================
# Celery任务 =====================================================
# ===============================================================


@celery_client.task
def send_greet_mail(email_obj_id):
    """发送欢迎邮件"""
    with context_session() as session:
        try:
            email_obj = session.query(EmailModel).get(email_obj_id)
            with open(os.path.join(BASE_PATH,
                                   'templates',
                                   "email",
                                   "1.html"), "r") as f:
                content = f.read()
            MailClient.send_mail(email_obj.email,
                                 "Thank you for your concern",
                                 content)
        except:
            raise
        else:
            obj = EmailInformRecord(email_id=email_obj_id)
            obj.add_record("1.html")
            session.add(obj)


```