# abundance/utils/data_utils.py
def merge_data(data1, data2):
    """
    递归合并两个数据结构，这两个数据结构可以是字典或列表。
    当两个数据结构都是字典时，会递归合并相同键的值；当都是列表时，会将两个列表拼接起来；
    对于其他情况，直接返回第二个数据结构。

    :param data1: 第一个要合并的数据结构
    :param data2: 第二个要合并的数据结构
    :return: 合并后的数据结构
    """
    # 判断 data1 和 data2 是否都是字典类型
    if isinstance(data1, dict) and isinstance(data2, dict):
        # 复制 data1 到 result 中，避免修改原始的 data1
        result = data1.copy()
        # 遍历 data2 的键值对
        for key, value in data2.items():
            if key in result:
                # 如果键已经存在于 result 中，递归调用 merge_data 方法合并对应的值
                result[key] = merge_data(result[key], value)
            else:
                # 如果键不存在于 result 中，直接将该键值对添加到 result 中
                result[key] = value
        return result
    # 判断 data1 和 data2 是否都是列表类型
    elif isinstance(data1, list) and isinstance(data2, list):
        # 如果都是列表，将两个列表拼接起来并返回
        return data1 + data2
    # 对于其他情况，直接返回 data2
    return data2