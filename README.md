# 右键菜单添加工具

这是一个用于在 Windows 系统中添加右键菜单项的工具，可以方便地将常用程序添加到右键菜单中。

## 功能特点

- 支持添加打开文件夹选项
- 支持添加空白处打开选项

## 使用方法

### 基本用法

```bash
run.bat -p "程序路径" -n "菜单名称" [-d] [-b]
```

### 参数说明

| 参数 | 说明 | 是否必需 |
|------|------|----------|
| `-p` 或 `--path` | 程序路径 | 是 |
| `-n` 或 `--name` | 菜单名称 | 是 |
| `-d` 或 `--directory` | 添加打开文件夹选项 | 否 |
| `-b` 或 `--background` | 添加空白处打开选项 | 否 |

### 使用示例

1. 基本使用：
```bash
run.bat -p "C:\Program Files\app.exe" -n "MyApp"
```

2. 添加打开文件夹选项：
```bash
run.bat -p "C:\Program Files\app.exe" -n "MyApp" -d
```

3. 添加空白处打开选项：
```bash
run.bat -p "C:\Program Files\app.exe" -n "MyApp" -b
```

4. 同时添加两种选项：
```bash
run.bat -p "C:\Program Files\app.exe" -n "MyApp" -d -b
```

## 注意事项

1. 程序需要管理员权限才能修改注册表
2. 请确保提供的程序路径正确
3. 菜单名称建议使用英文，避免乱码

## 文件说明

- `regedit_example.py`：主程序文件
- `run.bat`：启动脚本
- `tools/`：工具函数目录

## 依赖要求

- Python 3.x
- Windows 操作系统
- 管理员权限
