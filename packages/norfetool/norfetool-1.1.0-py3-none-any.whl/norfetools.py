import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from PIL import Image

import os
import re
import numpy as np
import pickle

from contextlib import contextmanager
import warnings


try:
    plt.style.use(["science", "grid"])
except OSError:
    warnings.warn(f"Matplotlib style load failed: {e}. Using default style.", UserWarning)


# 默认的DPI设置，用于保存图像
DPI_SAVE = 800


@contextmanager
def Set_style(styles = ["science", "grid", "nature"]):
    with plt.style.context(styles):
        yield


def SaveFig(flag, path, filepath="figure/",):
    """
    保存绘制的图像到指定路径。

    参数:
    flag (bool): 决定是否保存图像。如果为True，则保存图像；如果为False，则不执行任何操作。
    path (str): 图像文件的名称，包括扩展名（例如 'image.png'）。
    filepath (str): 图像文件的保存路径，默认为 'figure/' 目录。

    返回:
    无

    功能:
    此函数检查是否需要保存图像（基于`flag`参数），并将其保存在指定路径。
    如果目标路径不存在，会自动创建该路径。
    使用matplotlib的savefig方法，确保边界紧凑并设置高DPI，以便图像质量更高。
    """
    # 保存图片
    if flag:
        # 如果目录不存在，则创建
        if not os.path.isdir(filepath):
            os.makedirs(filepath)
        # 保存图像
        plt.savefig(os.path.join(filepath, path), bbox_inches='tight', dpi=DPI_SAVE)
        plt.close()
    else:
        # 如果不保存图片，则显示图片
        plt.show()
        pass


def TestColorList(clist):
    """
    显示色卡和颜色在不同图形中的应用示例。
    
    参数:
    clist (list): 色卡列表，包含颜色定义。
    """
    num = len(clist)
    gs = GridSpec(3, num + int(num / 2), figure=plt.figure(figsize=(6, 4)))
    plt.subplots_adjust(wspace=0.3, hspace=0.2)

    # 显示色卡
    for i, color in enumerate(clist):
        if type(color) != str:
            color = tuple([int(i * 255) for i in color])
        img = Image.new('RGB', (10, 10), color)
        ax = plt.subplot(gs[0, i])
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis("off")
        ax.imshow(img)

    # 正弦波形
    ax = plt.subplot(gs[1:, :num])
    xvalue = np.arange(0, 2 * np.pi, 0.1)
    for i, color in enumerate(clist):
        ax.plot(xvalue, np.sin((i + 0.5) * xvalue), "-", color=color, label="%d" % i)
    ax.grid(":", alpha=0.3)
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.legend(loc=4)

    # 指数波形
    ax = plt.subplot(gs[:, num:])
    xvalue = np.arange(0, 0.5, 0.05)
    for i, color in enumerate(clist):
        ax.plot(xvalue, np.exp((i + 0.5) * xvalue), "s", color=color, markerfacecolor='none', label="%d" % i)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.legend(loc=2)
    plt.show()
    plt.close()


def SetColor(string, num_colors, extract_first_colors=False, ifshow=False):
    """
    根据给定的colormap名称生成颜色列表并显示。可以选择生成均匀分布的颜色列表
    或者提取colormap的前几个颜色。

    参数:
    string (str): colormap的名称。
    num_colors (int): 要生成或提取的颜色数量。
    extract_first_colors (bool): 如果为True，则仅提取colormap的前num_colors个颜色。
                                 如果为False，则根据num_colors在colormap中均匀分布生成颜色列表。

    返回:
    list: 生成的颜色列表。
    """
    if extract_first_colors:
        # 仅提取colormap的前num_colors个颜色
        color_list = [plt.cm.get_cmap(string)(i) for i in range(num_colors)]
    else:
        # 生成均匀分布的颜色列表
        array = np.linspace(0, 1, num_colors)
        color_list = plt.cm.get_cmap(string)(array)

    if ifshow:
        TestColorList(color_list)
    return color_list


def Set_axis_formatting(axis, nbins, decimals):
    from matplotlib.ticker import MaxNLocator, FormatStrFormatter
    """
    设置图表的轴格式。

    参数:
    axis (str): 指定要设置的轴。'x' 设置x轴，'y' 设置y轴，'both' 设置两者。
    nbins (int): 轴的主要刻度的数量。
    decimals (int): 轴刻度标签的小数位数。
    """
    formatter = FormatStrFormatter(f'%.{decimals}f')

    if axis == 'x' or axis == 'both':
        plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=nbins))
        plt.gca().xaxis.set_major_formatter(formatter)

    if axis == 'y' or axis == 'both':
        plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=nbins))
        plt.gca().yaxis.set_major_formatter(formatter)


#############################################
##################文件处理####################
#############################################


def Ensure_directory_exists(filename):
    """
    检查文件的目录是否存在，如果不存在，则创建。
    :param filename: 要检查的文件名或路径。
    """
    directory = os.path.dirname(filename)
    
    # 如果目录名不为空且目录不存在，则创建
    if directory and not os.path.exists(directory):
        os.makedirs(directory)


def Save_data(temp_data_list, filename='temp_data_list.pkl'):
    """
    保存 temp_data_list 到一个文件中。
    :param temp_data_list: 要保存的数据列表。
    :param filename: 保存数据的文件名，默认为 'temp_data_list.pkl'。
    """
    Ensure_directory_exists(filename)
    with open(filename, 'wb') as file:
        pickle.dump(temp_data_list, file)


def Load_data(filename='temp_data_list.pkl'):
    """
    从文件中加载 temp_data_list。
    :param filename: 包含数据的文件名，默认为 'temp_data_list.pkl'。
    :return: 返回加载的数据列表。
    """
    with open(filename, 'rb') as file:
        return pickle.load(file)


#############################################
#################字符串处理###################
#############################################
# 主要用于slurm的脚本批量提交


def Ensure_directory_exists(file_path):
    """
    检查文件路径的目录是否存在，如果不存在则创建。
    
    参数：
    - file_path: 文件的完整路径。
    """
    directory = os.path.dirname(file_path)

    # 检查文件是否存在，存在则删除
    if os.path.exists(file_path):
        os.remove(file_path)
        
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def Replace_strings_in_file(file_name, replace_dict, new_file_path):
    """
    将文件中的多个旧字符串替换为对应的新字符串，并保存到新路径。
    
    参数：
    - file_name: 原始文件路径。
    - replace_dict: 一个字典，键为旧字符串，值为新字符串。
    - new_file_path: 新文件保存路径，如果路径不存在会创建。
    """
    # 确保新文件路径存在，如果不存在则创建
    Ensure_directory_exists(new_file_path)
    
    # 读取文件内容
    with open(file_name, 'r') as file:
        file_contents = file.read()
    
    # 遍历字典并替换所有旧字符串
    new_contents = file_contents
    for old_string, new_string in replace_dict.items():
        new_contents = re.sub(re.escape(old_string), new_string, new_contents)
    
    # 将修改后的内容写入新的文件路径
    with open(new_file_path, 'w') as new_file:
        new_file.write(new_contents)
    
    print(f"File has been saved to {new_file_path} with the updated content.")