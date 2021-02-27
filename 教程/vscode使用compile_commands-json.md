# 背景
vscode+cmake可以实现C/C++项目开发和构建。可以在vscode上装以下几个插件：

![插件](https://upload-images.jianshu.io/upload_images/6411513-2f1e454cca809257.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

`CMake Tools插件`能够给`C/C++插件`提供信息，实现IntelliSense、代码补全、注释浏览、文件转跳等功能。一般在第一次使用`CMake Tools插件`时会出现如下提示：

![提示](https://upload-images.jianshu.io/upload_images/6411513-c43fa9a699a800bc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Allow之后会在当前工作目录的`.vscode/settings.json`文件（即当前工作目录的设置文件，会覆盖用户设置文件）中添加：
```json
{
    "C_Cpp.default.configurationProvider": "ms-vscode.cmake-tools"
}
```
当然，也可以在`C/C++插件`的配置文件`.vscode/c_cpp_properties.json`中手动指定`configurationProvider`：
```json
{
    "configurations": [
        {
            "name": "Linux",
            "includePath": [],
            "defines": [],
            "compilerPath": "/usr/bin/gcc",
            "cStandard": "gnu11",
            "cppStandard": "gnu++14",
            "intelliSenseMode": "gcc-x64",
            "configurationProvider": "ms-vscode.cmake-tools"
        }
    ],
    "version": 4
}
```
这样`C/C++插件`就能正常工作了，不用自己指定`.vscode/c_cpp_properties.json`的`includePath`和`defines`。
除了以上两种方式以外，还有另一种方式：
# 指定compile_commands.json
1. 让cmake生成`compile_commands.json`，需要在运行`cmake`时添加参数`-DCMAKE_EXPORT_COMPILE_COMMANDS=True`或者在CMakeLists.txt中添加`set(CMAKE_EXPORT_COMPILE_COMMANDS True)`。例子：假设在`~`目录下有一个hello的项目
```shell
$ cd ~/hello
$ mkdir build
$ cd build
$ cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=True ..
```
会在`~/hello/build`下生成`compile_commands.json`。
2. 在vscode中打开`~/hello`目录，配置`.vscode/c_cpp_properties.json`。指定`compileCommands`为上一步的`~/hello/build/compile_commands.json`：
```json
{
    "configurations": [
        {
            "name": "Linux",
            "includePath": [],
            "defines": [],
            "compilerPath": "/usr/bin/g++",
            "cStandard": "gnu11",
            "cppStandard": "gnu++14",
            "intelliSenseMode": "gcc-x64",
            "compileCommands": "~/hello/build/compile_commands.json"
        }
    ],
    "version": 4
}
```
这样和指定`configurationProvider`是一样的效果。

# 原理
1. `configurationProvider`：
> The ID of a VS Code extension that can provide IntelliSense configuration information for source files. For example, use the VS Code extension ID ms-vscode.cmake-tools to provide configuration information from the CMake Tools extension.
2. `compileCommands`：
> The full path to the compile_commands.json file for the workspace. The include paths and defines discovered in this file will be used instead of the values set for includePath and defines settings. If the compile commands database does not contain an entry for the translation unit that corresponds to the file you opened in the editor, then a warning message will appear and the extension will use the includePath and defines settings instead.



> 参考：
> https://cmake.org/cmake/help/latest/variable/CMAKE_EXPORT_COMPILE_COMMANDS.html
> https://code.visualstudio.com/docs/languages/cpp
> https://code.visualstudio.com/docs/cpp/cmake-linux
> https://code.visualstudio.com/docs/cpp/c-cpp-properties-schema-reference
> https://code.visualstudio.com/docs/cpp/customize-default-settings-cpp
> https://code.visualstudio.com/docs/cpp/configure-intellisense-crosscompilation
> https://clang.llvm.org/docs/JSONCompilationDatabase.html
