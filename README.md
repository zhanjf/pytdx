# pytdx_backup
1. 看到原作者rainx把它的pytdx代码archived了，为了让他的代码继续发光发热，开一个远程库备份一下。
2. 原作者的说明文档在这里：https://rainx.gitbooks.io/pytdx/content/
3. 备份说明文档在这里：https://counsel-chai.gitbook.io/pytdx-1/
4. 原作者代码地址：https://github.com/rainx/pytdx
5. 原readme文档地址：https://github.com/rainx/pytdx/commit/14b1ad3534593952d1d698ffa706f4f13a4ed156#diff-04c6e90faac2675aa89e2176d2eec7d8


## 独立维护与安装

此仓库可以独立克隆，与SignalX同级维护。源码目录本身就是pytdx包；
pyproject.toml显式声明包映射，支持editable安装，不需要手工设置PYTHONPATH。

```sh
python -m pip install -e /path/to/pytdx
python -c "import pytdx; print(pytdx.__file__)"
```

当前维护改动：HQ握手仅发送SetupCmd1与SetupCmd2；对非空两字节K线桩响应明确报错。
前复权、市场路由和CSV导出等SignalX业务逻辑保留在SignalX中。

独立仓库测试：`python -m unittest discover -s tests -v`。
