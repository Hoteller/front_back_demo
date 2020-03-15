# README

### 写在前面

​	编写这个demo是为了分隔开前后端的开发，保证接口部分没有不确定的技术。

​	运行这个demo可以参考后文的运行准备，但是过程中基本不可能不遇到问题。如果遇到问题，可以耐心地根据报错提示搜索并解决问题，实在遇到困难也可以来找我（但是基本上也是我再去搜索）。

​	另外，我最推荐的使用这个demo的方法是按照demo的思路，查找资料，重新实现这个demo。实现的过程中可以参考demo中的实现方法。demo中重要的代码部分有后端的get_test.py、post_test.py和前端的App.js，参考时可以比对自动生成的代码和demo中的区别找出demo中代码的作用。

### DEMO内容

1. 使用React+Django的前后端分离实现
2. 前端发送GET请求
3. 前端发送带参数的POST请求
4. 后端解析GET和POST请求
5. 后端发送JSON类型的HttpResponse给前端

### 运行准备

**以下部分只是关键步骤，具体操作中遇到问题可以根据报错搜索*

安装python

https://www.liaoxuefeng.com/wiki/1016959663602400/1016959856222624

安装django

```
pip install django
```

安装Node.js

https://www.runoob.com/nodejs/nodejs-install-setup.html

安装MySQL

https://www.runoob.com/mysql/mysql-install.html

数据库准备

​	** 以下具体操作可以自己搜索*（关键词可以是“django mysql 配置”）

- 创建用户 root 密码123456（这些登录信息写在了后端配置代码中，不能错）
- 创建数据库HotelManage（同前）
- 切换到HotelManage
- 安装python包pymysql

### 代码运行

1. 在back_end\HotelManage路径下

   ```
   python manage.py runserver
   ```

2.   在front_end\hotelmanage路径下

   ```
   npm start
   ```

3. 此时会自动打开浏览器的127.0.0.1:3000，进入demo

### demo功能

​	**以下部分按照Google Chrome编写*

1. 在127.0.0.1:3000中，按F12进入开发者模式
2. 在输入框中填写房间号和现在的费用（具体值随意）
3. 点击“post”发送POST请求
4. 在console栏中依次可以看到：
   - 输入的内容
   - "POST RESPONSE"
   - 后端的回复，包含之前填写的RoomID，证明后端已经成功接收并解析
5. 在NetWork栏中，也可以找到刚才发送的POST请求，可以看到数据被装载在“payload”中
6. 点击“get”发送GET请求（不需要填写输入框）
7. 在console栏中依次可以看到：
   - "GET RESPONSE"
   - 后端返回的一个JSON，在data项目中可以看到具体的数据

### 开发提示

​	以下说明开发中部分可以参考的资料和实用的辅助工具

	##### 辅助工具

  1. 模拟后端接口

     https://jsonplaceholder.typicode.com/

     使用介绍：

     https://www.youtube.com/watch?v=NEYrSUM4Umw

  2. 模拟前端HTTP请求

     https://www.postman.com/

##### 参考资料

1. React、Django和Mysql安装和使用

   https://juejin.im/post/5e096b04518825497b41c093

2. HTTP访问控制CORS（在DEMO中已经配置为允许所有）

   https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Access_control_CORS

   配置方法：

   https://github.com/adamchainz/django-cors-headers#configuration

3. 使用React发送GET/POST请求

   https://malcoded.com/posts/react-http-requests-axios/

4. Django+MySQl配置

   https://blog.csdn.net/u011304490/article/details/80315185








