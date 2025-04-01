# dvatioff-audio

A general-purpose function library for Wwise-based game audio tool development.

---

## Introduction

This library is a collection of general-purpose utility functions specifically designed for developing game audio tools based on Wwise. It mainly consists of the following components:

- **WAAPI**
    
    - Wrappers for commonly used WAAPI interfaces
    - A multithreading class based on PySide6's QRunnable/Signal for real-time retrieval of WAAPI connection status and the selection status of Wwise Authoring objects
    - General utility functions, such as batch replacements of Originals files and complete silence filling for languages missing in multilingual projects
- **Voice**
    
    - Wrappers for Microsoft Azure's Text-to-Speech and Speech-to-Text (Whisper) interfaces
    - Text preprocessing, text distance, and word error rate calculations for four languages (Chinese, Japanese, English, and Korean)
    - Simple sine wave generation
- **GUI**
    
    - Wrappers for creating common GUI elements with PySide6
- **Utils**
    
    - System-level utility functions, including Retry decorators, JSON read/write utilities, file operations, path handling, spreadsheet processing, and common regular expressions for audio file naming
- **Examples**
    
    - example scripts, such as GUI Windows, build automation scripts and a NAS-based automatic update checker


---

## Installation

```bash

pip install dvatioff-audio
```

---

为基于 Wwise 的游戏音频工具开发准备的通用功能库。

## 介绍

本库是套专为基于 Wwise 的游戏音频工具开发设计的通用功能函数集合，主要由以下几个部分组成：

- **WAAPI**
	- 常用 WAAPI 接口的封装
	- 基于 Pyside6 QRunnerble/Signal 的多线程类，用于实时获取 WAAPI 连接状态以及 Wwise Authoring 对象选中状态
	- 通用功能函数，如 Originals 文件批量替换、多语言缺失语种的 Silence 全量填充等
- **Voice**
	- 基于 Microsoft Azure 的 Text2Speech 和 Speech2Text（Whisper）接口封装
	- 对四个语种（中、日、英、韩）的文本预处理，文本距离和词错误率计算等
	- 简单的正弦波生成
- **GUI**
	- 对 Pyside6 常用 GUI 元素创建的封装
- **Utils**
	- 系统级通用函数，如 Retry 装饰器、JSON 读取保存、文件操作、路径处理、表格处理、常用音频命名正则表达式等
- **示例**
	- 示例脚本，比如 GUI 窗口， build 自动化脚本，基于 NAS 的程序自动更新检测模块等

## 安装

```bash

pip install dvatioff-audio
```

---

## 工具集界面示例

![alt text](image.png)