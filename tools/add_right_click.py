from tools.winreg_tools import *
import winreg

def add_open_directory(exe_file_path,exe_name):
    regedit_path = r'Directory\shell' '\\'+ exe_name
    # 新建cursor子项
    create_registry_key(
        winreg.HKEY_CLASSES_ROOT,
        regedit_path
    )
    # 设置cursor的默认值
    set_registry_value(
        winreg.HKEY_CLASSES_ROOT,
        regedit_path,
        '',
        winreg.REG_SZ,
        '用cursor打开'
    )
    # 创建 command 子项
    command_path = regedit_path + r'\command'
    create_registry_key(
        winreg.HKEY_CLASSES_ROOT,
        command_path
    )
    #设置command的默认值
    set_registry_value(
        winreg.HKEY_CLASSES_ROOT,
        command_path,
        '',
        winreg.REG_SZ,
        '\"' + exe_file_path + "\"" + "  " "\"" + '%1' + "\""
    )
    #设置图标
    set_registry_value(
        winreg.HKEY_CLASSES_ROOT,
        regedit_path,
        'Icon',
        winreg.REG_EXPAND_SZ,
        exe_file_path
    )

def add_open_background(exe_file_path,exe_name):
    regedit_path = r'Directory\Background\shell' + '\\ '+ exe_name
    #新建cursor子项
    create_registry_key(
        winreg.HKEY_CLASSES_ROOT,
        regedit_path
    )
    #设置cursor的默认值
    set_registry_value(
        winreg.HKEY_CLASSES_ROOT,
        regedit_path,
        '',
        winreg.REG_SZ,
        '用cursor打开'
    )
    # 创建 command 子项
    command_path = regedit_path + r'\command'
    create_registry_key(
        winreg.HKEY_CLASSES_ROOT,
        command_path
    )
    #设置command的默认值
    set_registry_value(
        winreg.HKEY_CLASSES_ROOT,
        command_path,
        '',
        winreg.REG_SZ,
        '\"' + exe_file_path + "\"" + "  " "\"" + '%V' + "\""
    )
    #设置图标
    set_registry_value(
        winreg.HKEY_CLASSES_ROOT,
        regedit_path,
        'Icon',
        winreg.REG_EXPAND_SZ,
        '\"' + exe_file_path + "\""
    )