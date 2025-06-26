# coding:utf-8
from rename_ import Ui_Dialog6
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox

import os
import re


class CustomOutputRedirector:
    def __init__(self, text_edit):
        self.text_edit = text_edit

    def write(self, message):
        # 将消息追加到 QTextEdit 组件
        self.text_edit.append(message.strip())

    def flush(self):
        pass  # 不需要实现 flush 方法 *input会卡住


class DueFiles:
    @staticmethod
    def re_name_prefix(old_prefix, new_prefix):
        print('--' * 23)
        list_img_name = os.listdir(os.getcwd())  # 继承目录
        for i, old_name in enumerate(list_img_name):
            # 标准图片格式：liaNXI详情_7.jpg
            if old_name.startswith(old_prefix):  # 过滤其他文件
                del_old = re.sub(old_prefix, f"{new_prefix}", old_name, count=1)  # 新字符+"_"替换旧字符,后缀不变
                os.renames(old_name, f"{del_old}")
            else:
                print(
                    f'<h3 style="color:red;display: inline;margin: 0;padding: 0;>输入的前缀不吻合,没有执行重命名</h3>')
        print('<h3 style="color:green;">批量重命名-前缀替换-任务已完成！</h3>')
        print('--' * 23)

    # 后缀修改函数
    @staticmethod
    def re_name_suffix(old_suffix, new_suffix):
        print('--' * 23)
        list_img_name = os.listdir(os.getcwd())  # 继承目录
        for i, old_name in enumerate(list_img_name):
            if old_name.endswith(old_suffix):  # 过滤不同后缀‘g’可匹配png，jpg，jpeg
                del_old = re.sub(f"{old_name.split('.')[1]}", f"{new_suffix.replace('.', '')}",
                                 old_name)  # 新字符+"_"替换旧字符,前缀不变
                os.renames(old_name, f"{del_old}")
        print('<h3 style="color:green;display: inline;margin: 0;padding: 0;">批量重命名-后缀替换-任务已完成！</h3>')
        print('--' * 23)

    @staticmethod
    def rename_match(old_prefix, new_prefix):
        list_img_name = os.listdir(os.getcwd())  # 继承目录
        for i, old_name in enumerate(list_img_name):
            if old_prefix in old_name:
                del_old = re.sub(old_prefix, f"{new_prefix}", old_name)  # 新字符+"_"替换旧字符,后缀不变
                os.renames(old_name, f"{del_old}")

        print('<h3 style="color:green;display: inline;margin: 0;padding: 0;">批量重命名-任意替换-任务已完成！</h3>')
        print('--' * 23)


class ReNamePS(QDialog, Ui_Dialog6, DueFiles):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.init_ui()  # print重定向
        self.flag = ''
        print(
            '简易脚本：该脚本是由@饼饼开发的非商用版本，仅作为学习使用，可试用7天》使用建议先点击...指定到文件所在目录，不点击默认是执行当前软件目录，\n确认后按下-圆点-执行对应功能！ ')
        self.toolButton.clicked.connect(self.dictionary_choose)  # ...按钮
        self.buttonBox.accepted.connect(self.act_rename)
        self.buttonBox.rejected.connect(self.act_clear)
        self.pushButton.clicked.connect(self.act_clear2)

    def init_ui(self):
        # 重定向标准输出
        sys.stdout = CustomOutputRedirector(self.textEdit)
        # print('原始显示')  # 这接管了print

    def dictionary_choose(self):
        # print('--输入快捷命令后清空，再次输入统一的图片前缀名--')
        dir_path = QFileDialog.getExistingDirectory(self)
        if not dir_path:
            print(
                f'<h3 style="color:blue;display: inline;margin: 0;padding: 0;">没有指定文件夹，当前执行{os.getcwd()}</h3>')
            os.chdir(os.getcwd())
            QMessageBox.information(self, '警告', '未指定文件夹，执行最近目录！')
        else:
            os.chdir(dir_path)
            self.lineEdit_3.setText(dir_path)
            print(f'<h3 style="color:green;display: inline;margin: 0;padding: 0;">新选中工作目录已变为：{dir_path}</h3>')

    def act_rename(self):
        if QMessageBox.question(self, '提示', '确认执行吗？',
                                QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel) != QMessageBox.StandardButton.Ok:
            return
        # 用户点了 OK，继续执行下一行代码
        if self.radioButton.isChecked():  # 前缀修改
            print('<h3 style="color:red;display: inline;margin: 0;padding: 0;">执行修改前缀,请谨慎操作不可逆!!</h3>')
            old_prefix = self.lineEdit.text()
            new_prefix = self.lineEdit_2.text()
            print(
                f'<h3 style="color:grey;display: inline;margin: 0;padding: 0;">旧名:{old_prefix} \n 新名：{new_prefix} </h3>')
            self.re_name_prefix(old_prefix, new_prefix)
            self.textEdit.append('<h3 style="color:blue;display: inline;margin: 0;padding: 0;">执行修改前缀完成</h3>')
        elif self.radioButton_2.isChecked():
            print('<h3 style="color:red;">执行修改后缀,不用输入【.】,请谨慎操作不可逆!!</h3>')
            old_prefix = self.lineEdit.text()
            new_prefix = self.lineEdit_2.text()
            print(
                f'<h3 style="color:red;display: inline;margin: 0;padding: 0;">旧后缀:{old_prefix}\n新后缀：{new_prefix} </h3>')
            self.re_name_suffix(old_suffix=old_prefix, new_suffix=new_prefix)
            self.textEdit.append('<h3 style="color:blue;">执行修改后缀完成</h3>')
        elif self.radioButton_3.isChecked():
            print('<h3 style="color:red;">执行重命名替换,请谨慎操作不可逆!!</h3>')
            old_prefix = self.lineEdit.text()
            new_prefix = self.lineEdit_2.text()
            print(
                f'<h3 style="color:red;display: inline;margin: 0;padding: 0;">原旧名:{old_prefix}\n新名：{new_prefix} </h3>')

            self.rename_match(old_prefix, new_prefix)
            self.textEdit.append('<h3 style="color:blue;">执行任意替换完成</h3>')

    def act_clear(self):
        QMessageBox.information(self, '提示', '仅清屏输入内容')

    def act_clear2(self):
        self.lineEdit_3.setText('警告：未确认文件夹！')


if __name__ == '__main__':
    # enable dpi scale
    app = QApplication(sys.argv)
    window = ReNamePS()
    window.show()
    app.exec()
