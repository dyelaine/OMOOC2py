# OMOOC.py 周任务代码试作

## 3w

- 私人笔记:
    + 交互式日记：基于python中的socket模块实现，socket分为两种，基于TCP和基于UDP。TCP发送数据时，已建立好TCP连接，所以不需要指定地址。UDP是面向无连接的，每次发送要指定是发给谁。
    + UDP 网络服务
        *根据host和port，client可以访问server，并将client的输入推送到server上并保存，client端可以重复打印历史记录，也可以多次输入内容，直至用户输入q退出系统
    + 运行说明
        *下载week3_server.py和week3_client.py; 在第一个终端中cd 下载路径(此路径为server.py下载路径)，输入指令python week3_server.py即可启动服务器端，然后在第二个终端中cd 下载路径(此路径为client.py下载路径)第二个个终端中输入指令python week3_client.py即可输入记录及重复查看历史记录。可以多个客户端同时访问服务器。
    + 客户端可以和服务器进行交互，那客户端怎样才叫交互呢？继续研究......
