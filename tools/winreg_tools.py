import winreg

def set_registry_value(hive, path, name, value_type, value):
    """
    设置注册表值
    
    参数:
        hive: 注册表根键 (如 winreg.HKEY_CURRENT_USER)
        path: 注册表路径 (如 r"Software\MyTestApp")
        name: 值名称
        value_type: 值类型 (如 winreg.REG_SZ, winreg.REG_DWORD)
        value: 要设置的值
    """
    try:
        # 打开或创建注册表键
        key = winreg.CreateKey(hive, path)
        
        # 设置值
        winreg.SetValueEx(key, name, 0, value_type, value)
        
        # 关闭注册表键
        winreg.CloseKey(key)
        
        print(f"成功设置注册表值: {path}\\{name}")
        return True
        
    except WindowsError as e:
        print(f"设置注册表值时出错: {e}")
        return False

def get_registry_value(hive, path, name):
    """
    获取注册表值
    
    参数:
        hive: 注册表根键
        path: 注册表路径
        name: 值名称
    
    返回:
        (值, 类型) 的元组
    """
    try:
        # 打开注册表键
        key = winreg.OpenKey(hive, path, 0, winreg.KEY_READ)
        
        # 读取值
        value, value_type = winreg.QueryValueEx(key, name)
        
        # 关闭注册表键
        winreg.CloseKey(key)
        
        print(f"成功读取注册表值: {path}\\{name}")
        return value, value_type
        
    except WindowsError as e:
        print(f"读取注册表值时出错: {e}")
        return None, None

def delete_registry_value(hive, path, name):
    """
    删除注册表值
    
    参数:
        hive: 注册表根键
        path: 注册表路径
        name: 值名称
    """
    try:
        # 打开注册表键
        key = winreg.OpenKey(hive, path, 0, winreg.KEY_ALL_ACCESS)
        
        # 删除值
        winreg.DeleteValue(key, name)
        
        # 关闭注册表键
        winreg.CloseKey(key)
        
        print(f"成功删除注册表值: {path}\\{name}")
        return True
        
    except WindowsError as e:
        print(f"删除注册表值时出错: {e}")
        return False

def delete_registry_key(hive, path):
    """
    删除注册表键
    
    参数:
        hive: 注册表根键
        path: 注册表路径
    """
    try:
        # 删除键
        winreg.DeleteKey(hive, path)
        
        print(f"成功删除注册表键: {path}")
        return True
        
    except WindowsError as e:
        print(f"删除注册表键时出错: {e}")
        return False

def create_registry_key(hive, path):
    """
    创建注册表项
    
    参数:
        hive: 注册表根键 (如 winreg.HKEY_CURRENT_USER)
        path: 注册表路径 (如 r"Software\MyTestApp")
    
    返回:
        bool: 是否创建成功
    """
    try:
        # 创建注册表键
        key = winreg.CreateKey(hive, path)
        winreg.CloseKey(key)
        print(f"成功创建注册表项: {path}")
        return True
    except WindowsError as e:
        print(f"创建注册表项时出错: {e}")
        return False

def modify_registry_value(hive, path, name, value_type, value):
    """
    修改注册表键值
    
    参数:
        hive: 注册表根键
        path: 注册表路径
        name: 值名称
        value_type: 值类型
        value: 新值
    
    返回:
        bool: 是否修改成功
    """
    try:
        # 打开注册表键
        key = winreg.OpenKey(hive, path, 0, winreg.KEY_SET_VALUE)
        
        # 修改值
        winreg.SetValueEx(key, name, 0, value_type, value)
        
        # 关闭注册表键
        winreg.CloseKey(key)
        
        print(f"成功修改注册表值: {path}\\{name}")
        return True
        
    except WindowsError as e:
        print(f"修改注册表值时出错: {e}")
        return False