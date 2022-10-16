### git 介绍

1. 首先配置用户名和邮箱：

```sh
git config --global user.name "name" 
git config --global user.email "email"
```
2. 生成公钥和私钥，测试，并将公钥粘贴到github账号中
```sh
ssh-keygen -t rsa -C 'user.email or name'
ssh -T git@github.com
```
### 常用的命令

```sh
git pull                     //将远程仓库中的新的内容拉到本地
git push                     //将本地仓库中的内容提交到远程仓库
git add .                    //将所有改动都添加到临时仓库中
git commit -m 'string'       //将改动提交，并添加提交说明
```
### git 冲突
对于同一个文件，当本次更改前的文件和远程仓库中的信息不相同时，会产生冲突。

解决办法：

1.找到冲突文件，修改后commit并再次提交。 


### 退回到某一个commit 上

```sh 
git reset --hard commitID
```

### git合并commit

假如有提交记录：

- cm5
- cm4
- cm3
- cm2
- cm1

其中cm1的提交记录最早，如果我们要合并记录cm2,cm4,cm5,此时做以下操作：

1. ```git rebase -i cm1 ``` #cm1 是要合并的所有记录最早的前一个

2. 然后会自动打开一个文件，显示：

   ```shell
   pick id cm2
   pick id cm3
   pick id cm4
   pick id cm5
   ```

把保留的id前面的pick保持不变，要被合并的pick改为s（不能合并不连续的commit，否则会出错）

v2ray:

```shell
bash <(curl -sL https://raw.githubusercontent.com/daveleung/hijkpw-scripts-mod/main/v2ray_mod1.sh)
```