from common.base import Base


class RegisterPage(Base):

    email_loc = ("id", "id_email")
    password_loc = ("id", "id_password")
    btn_loc = ("id", "jsEmailRegBtn")

    back_index_loc = ("class name", "index-font")
    login_link_loc = ("css selector", ".form-p>a")

    # 注册成功
    success_loc = ("css selector", "body>h1")

    def input_email(self, text):
        '''输入邮箱'''
        self.send(self.email_loc, text)

    def input_password(self, text):
        '''输入密码'''
        self.send(self.password_loc, text)

    def click_register_btn(self):
        '''点注册按钮'''
        self.click(self.btn_loc)

    def register_success_text(self):
        '''获取注册成功的文本'''
        return self.get_text(self.success_loc)



