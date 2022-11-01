### trojan搭建：

1.  利用官方一键搭建脚本搭建trojan：

+ 安装
```bash
source <(curl -sL https://git.io/trojan-install)  \\搭建
```
+ 卸载
```bash
source <(curl -sL https://git.io/trojan-install) --remove \\卸载
```
2. 利用以下脚本更改web页面端口，部署伪装网站，伪装软件用nginx搭建
```bash
wget -N --no-check-certificate "https://raw.githubusercontent.com/V2RaySSR/Trojan_panel_web/master/trojan-web-panel.sh" && chmod +x trojan-web-panel.sh && ./trojan-web-panel.sh

```
对于oracle的vps, 还需要运行 `iptables -F` 命令开放端口，否则会出错。


### 修改trojan-web端口：
修改 `/etc/systemd/system/trojan-web.service` 配置文件，在 `/usr/local/bin/trojan web` 后面添加 `-p port`。然后运行：
```bash
systemctl daemon-reload
systemctl restart trojan-web
```