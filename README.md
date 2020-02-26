# goudan_plugins

这个项目是 [Goudan](https://github.com/daoye/goudan) 的插件。

这些插件用于向狗蛋提供可用的代理地址。

spiders目录下的每一个.py文件都是一个插件，这些插件从不同的网页上获取可用的代理IP，并提供给狗蛋，随后狗蛋就可以用这些代理IP来提供隧道代理服务。


# 用法

打开狗蛋根目录下的配置文件： `setting.py`， 并在`plugins`变量中添加配置，比如像下面这样:

    plugins = [
        # "C:\\Projects\\goudan_plugins\\src\\example.py",
        # "C:\\Projects\\goudan_plugins\\src\\spiders\\data5uSpider.py",
        # "C:\\Projects\\goudan_plugins\\src\\spiders\\freeHTTPSpider.py",
        # "C:\\Projects\\goudan_plugins\\src\\spiders\\freeHTTPSSpider.py",
        # "C:\\Projects\\goudan_plugins\\src\\spiders\\kuaidailiSpider.py",
        # "C:\\Projects\\goudan_plugins\\src\\spiders\\spysoneSpider.py",
        # "C:\\Projects\\goudan_plugins\\src\\spiders\\xiciSpider.py"
        "https://raw.githubusercontent.com/daoye/goudan_plugins/master/src/spiders/data5uSpider.py",
        "https://raw.githubusercontent.com/daoye/goudan_plugins/master/src/spiders/freeHTTPSpider.py",
        "https://raw.githubusercontent.com/daoye/goudan_plugins/master/src/spiders/kuaidailiSpider.py",
        "https://raw.githubusercontent.com/daoye/goudan_plugins/master/src/spiders/spysoneSpider.py",
        "https://raw.githubusercontent.com/daoye/goudan_plugins/master/src/spiders/xiciSpider.py"
    ]

这个名叫 `plugins` 的变量是一个字符串类型的数组，数组中的每一项都指定了一个插件的路径，路径可以是远程路径或者是本地路径。远程路径必须以`http或https`开头，本地路径则必须是完整的全路径。

狗蛋每次启动时只会加载列表中指定的插件，如果是远程地址，狗蛋会自动将该插件下载到本地插件目录中；如果是本地路径，狗蛋会将该插件拷贝到插件目录。

插件目录名为`plugins`，由狗蛋启动时自动创建。

## 如何更新插件？

1. 直接删除plugins目录，然后重启狗蛋。

2. 修改插件文件名称，如果是远程地址，可以在地址后面添加参数比如：?ver=xxx.xx；如果是本地地址，则需要修改文件名。


# 如何编写自定义的插件

首先你要会python。其次，你要搞清楚下面这段描述。

1. 插件必须是一个单独的.py文件（其实也可以是多个文件，但这样加载起来忒麻烦，我不推荐）。
2. 该.py文件中必须定义一个名为Plugin的类，该类中必须定义一个名为start的方法，该方法必须接收两个参数。
3. 插件中可以直接导入aiohttp、lxml、urllib3、pony、requests这些三方库，和python3.7自带的各种库。（如果需要其它的库，则需要在狗蛋的运行环境中预先手动安装。）
4. 插件会不断的被重复执行，执行间隔为：最少每隔15分钟。但不一定是15分钟，具体取决于其他插件的执行时间，因为狗蛋会循环执行每个插件，这个过程是顺序的而不是并行的，所有插件都运行一遍后，会休息15分钟。
5. 狗蛋提供了一个专门用于爬虫类插件的基类，可以这样导入`from extension.baseSpider import BaseSpider`，具体用法参考spiders目录下的插件。
6. 如果不是爬虫，但是又要给狗蛋提供代理地址的话，则需要自行操作数据库，例：example.py。
7. 代理地址都存储在sqlite数据库中，pony对应的实体对象为：core.data.ProxyItem

### 插件定义的示例

    class Plugin():
        def start(self, hosting):
            # 插件将从这里开始运行
            pass


### ProxyItem 的定义

    class ProxyItem(db.Entity):
        id = PrimaryKey(int, auto=True)
        host = Required(str)
        port = Required(int)
        protocol = Required(str) # This proxy's protocol, example: http,https,socks4,socks5
        supportProtocol = Required(str) # This proxy support's protocol, example: http,https,socks4,socks5,http/https,socks4/socks5
        expired = Required(int) # This proxy's expired time.
        usr = Optional(str) # This proxy's username.
        pwd = Optional(str) # This proxy's password.
        location = Optional(str) # This proxy's location.
        isok = Required(bool) # Is this proxy checked success.
        validCount = Required(int) # checked failed's count
        failedCount = Required(int) # connected failed' count

# License

MIT