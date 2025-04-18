@echo off
if "%1"=="" (
    echo 使用方法:
    echo run.bat -p "程序路径" -n "菜单名称" [-d] [-b]
    echo.
    echo 参数说明:
    echo   -p 或 --path    程序路径（必需）
    echo   -n 或 --name    菜单名称（必需）
    echo   -d 或 --directory  添加打开文件夹选项（可选）
    echo   -b 或 --background 添加空白处打开选项（可选）
    echo.
    echo 示例:
    echo run.bat -p "C:\Program Files\app.exe" -n "MyApp" -d -b
    pause
    exit /b 1
)

python regedit_example.py %*
pause
