## 1. c++和python混合编程
分为两种方法，分别是python中调用C++以及C++中调用python。

1. **python中调用C++**：利用动态链接库，c++生成动态链接库文件.dll，然后在python导入ctypes模块，调用dll中的函数，该函数和python中的函数的用法一样。

   ```python
   import ctypes
   lib=ctypes.CDLL('name') #name:dll文件的名字
   a=lib.sum(3,2) #假设c++中sum函数的功能为输入两个变量，输出他们之和。
   ```

2. **c++ 中调用python**：还未知道。
3. xray搭建命令
   ```sh
bash <(curl -sL https://cdn.jsdelivr.net/gh/Misaka-blog/Xray-script@master/xray.sh)
   ```

