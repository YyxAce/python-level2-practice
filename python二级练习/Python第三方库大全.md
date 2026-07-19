# Python 第三方库大全

## 一、什么是 Python 第三方库

Python 中的库大致分为三类：

| 类型 | 是否需要安装 | 示例 |
|---|---:|---|
| 内置函数 | 不需要导入 | `print()`、`len()`、`range()` |
| 标准库 | 不需要额外安装 | `math`、`random`、`time`、`os` |
| 第三方库 | 通常需要自行安装 | `numpy`、`pandas`、`requests` |

第三方库由 Python 社区、企业或个人开发，通常发布在 **PyPI（Python Package Index）**。

由于 PyPI 中的项目数量非常多，不可能逐个列出全部第三方库。更实用的方法是按照用途分类掌握常见库。

---

## 二、第三方库的安装与管理

### 1. Windows 推荐安装命令

在 CMD、PowerShell 或 Windows Terminal 中运行：

```bash
py -m pip install 库名
```

例如：

```bash
py -m pip install requests
```

也可以使用：

```bash
python -m pip install requests
```

相比直接写 `pip install requests`，`py -m pip` 或 `python -m pip` 更容易确保第三方库安装到了指定 Python 解释器中。

### 2. IDLE 用户特别注意

IDLE 使用哪个 Python，第三方库就必须安装到哪个 Python 中。

先在 IDLE 中运行：

```python
import sys

print(sys.executable)
```

可能得到：

```text
C:\Users\用户名\AppData\Local\Programs\Python\Python314\pythonw.exe
```

安装时可以找到同目录下的 `python.exe`，然后执行：

```bash
"C:\Users\用户名\AppData\Local\Programs\Python\Python314\python.exe" -m pip install requests
```

安装完成后，重新启动 IDLE。

不要直接在 IDLE 的 `>>>` 后面输入：

```python
pip install requests
```

因为这是终端命令，不是 Python 语句。

### 3. 常用 pip 命令

```bash
# 安装库
py -m pip install requests

# 安装多个库
py -m pip install numpy pandas matplotlib

# 安装指定版本
py -m pip install numpy==2.3.0

# 升级库
py -m pip install --upgrade numpy

# 卸载库
py -m pip uninstall numpy

# 查看已安装的库
py -m pip list

# 查看某个库的信息
py -m pip show numpy

# 检查依赖关系是否冲突
py -m pip check

# 导出当前环境的库
py -m pip freeze > requirements.txt

# 按照文件安装全部依赖
py -m pip install -r requirements.txt
```

### 4. 虚拟环境

虚拟环境可以让不同项目使用不同版本的第三方库，避免版本冲突。

创建虚拟环境：

```bash
py -m venv .venv
```

Windows 激活：

```bash
.venv\Scripts\activate
```

激活后安装：

```bash
python -m pip install numpy pandas
```

退出虚拟环境：

```bash
deactivate
```

---

## 三、安装名和导入名可能不同

| 安装命令中的名称 | Python 中的导入名称 |
|---|---|
| `scikit-learn` | `sklearn` |
| `opencv-python` | `cv2` |
| `beautifulsoup4` | `bs4` |
| `pillow` | `PIL` |
| `python-docx` | `docx` |
| `python-pptx` | `pptx` |
| `pyserial` | `serial` |
| `pyyaml` | `yaml` |
| `pymupdf` | `fitz` |

例如：

```bash
py -m pip install scikit-learn
```

代码中却写：

```python
import sklearn
```

---

## 四、科学计算与数学库

| 库 | 主要用途 |
|---|---|
| `numpy` | 多维数组、矩阵、数值计算 |
| `scipy` | 积分、优化、插值、信号处理、统计计算 |
| `sympy` | 符号运算、解方程、求导、积分 |
| `mpmath` | 高精度浮点数计算 |
| `decimalfp` | 十进制数值计算 |
| `numba` | JIT 编译，加速数值计算 |
| `cupy` | 使用 NVIDIA GPU 进行类似 NumPy 的计算 |
| `jax` | 自动微分、GPU/TPU 数值计算 |

### NumPy 示例

```bash
py -m pip install numpy
```

```python
import numpy as np

a = np.array([1, 2, 3, 4])

print(a * 2)
print(np.mean(a))
```

输出：

```text
[2 4 6 8]
2.5
```

### SciPy 示例

```python
from scipy.integrate import quad

result, error = quad(lambda x: x**2, 0, 1)
print(result)
```

### SymPy 示例

```python
import sympy as sp

x = sp.symbols("x")

print(sp.diff(x**3, x))
print(sp.integrate(x**2, x))
print(sp.solve(x**2 - 4, x))
```

---

## 五、数据分析与数据处理库

| 库 | 主要用途 |
|---|---|
| `pandas` | 表格数据分析与清洗 |
| `polars` | 高性能 DataFrame 数据处理 |
| `dask` | 大规模并行数据处理 |
| `modin` | 并行加速 pandas |
| `pyarrow` | Arrow、Parquet 数据格式 |
| `duckdb` | 嵌入式分析型数据库 |
| `petl` | ETL 数据清洗 |
| `vaex` | 大型表格数据处理 |
| `datatable` | 高性能二维表格处理 |

### Pandas 示例

```bash
py -m pip install pandas
```

```python
import pandas as pd

data = {
    "姓名": ["小明", "小红", "小刚"],
    "成绩": [85, 92, 78]
}

df = pd.DataFrame(data)

print(df)
print(df["成绩"].mean())
```

常见读取方法：

```python
pd.read_csv("data.csv")
pd.read_excel("data.xlsx")
pd.read_json("data.json")
pd.read_sql("SELECT * FROM student", connection)
```

---

## 六、数据可视化库

| 库 | 特点 |
|---|---|
| `matplotlib` | 最基础、最灵活的绘图库 |
| `seaborn` | 统计图表，建立在 Matplotlib 上 |
| `plotly` | 交互式图表 |
| `pyecharts` | ECharts 图表，中文资料较多 |
| `bokeh` | 浏览器交互式可视化 |
| `altair` | 声明式统计可视化 |
| `holoviews` | 高层数据可视化接口 |
| `wordcloud` | 词云 |
| `graphviz` | 流程图、树形图 |
| `folium` | 交互式地图 |

### Matplotlib 示例

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 15, 13, 20]

plt.plot(x, y, marker="o")
plt.xlabel("x")
plt.ylabel("y")
plt.title("折线图")
plt.show()
```

### Seaborn 示例

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.show()
```

---

## 七、Excel、Word、PPT 和 PDF

### 1. Excel

| 库 | 用途 |
|---|---|
| `openpyxl` | 读写 `.xlsx` |
| `xlsxwriter` | 创建格式丰富的 Excel 文件 |
| `xlrd` | 读取旧版 `.xls` |
| `xlwt` | 写入旧版 `.xls` |
| `pyxlsb` | 读取 `.xlsb` |
| `pandas` | 表格数据批量处理 |

```python
from openpyxl import Workbook

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "姓名"
sheet["B1"] = "成绩"
sheet.append(["小明", 90])

workbook.save("成绩表.xlsx")
```

### 2. Word

```bash
py -m pip install python-docx
```

```python
from docx import Document

document = Document()
document.add_heading("Python 学习笔记", level=1)
document.add_paragraph("这是正文。")
document.save("笔记.docx")
```

### 3. PowerPoint

```bash
py -m pip install python-pptx
```

```python
from pptx import Presentation

presentation = Presentation()
slide = presentation.slides.add_slide(presentation.slide_layouts[1])

slide.shapes.title.text = "Python"
slide.placeholders[1].text = "Python 第三方库"

presentation.save("Python.pptx")
```

### 4. PDF

| 库 | 用途 |
|---|---|
| `pypdf` | 合并、拆分、读取 PDF |
| `pymupdf` | PDF 页面、文字和图片处理 |
| `pdfplumber` | 提取 PDF 文字和表格 |
| `reportlab` | 创建 PDF |
| `weasyprint` | HTML 转 PDF |
| `camelot-py` | 提取表格型 PDF |
| `tabula-py` | 调用 Tabula 提取表格 |

---

## 八、网络请求和 API

| 库 | 主要用途 |
|---|---|
| `requests` | 同步 HTTP 请求 |
| `httpx` | 同步和异步 HTTP 请求 |
| `aiohttp` | 异步网络请求和服务器 |
| `websocket-client` | WebSocket 客户端 |
| `urllib3` | 底层 HTTP 连接池 |
| `paramiko` | SSH 连接 |

### Requests 示例

```python
import requests

response = requests.get(
    "https://httpbin.org/get",
    timeout=10
)

print(response.status_code)
print(response.json())
```

POST 请求：

```python
data = {
    "username": "Jok",
    "password": "123456"
}

response = requests.post(
    "https://httpbin.org/post",
    json=data,
    timeout=10
)

print(response.json())
```

---

## 九、爬虫与网页自动化

| 库 | 主要用途 |
|---|---|
| `beautifulsoup4` | 解析 HTML |
| `lxml` | 高性能 HTML、XML 解析 |
| `scrapy` | 大型爬虫框架 |
| `selenium` | 操作真实浏览器 |
| `playwright` | 现代浏览器自动化 |
| `parsel` | XPath、CSS 选择器解析 |
| `selectolax` | 高性能 HTML 解析 |
| `fake-useragent` | 生成 User-Agent |
| `requests-html` | 请求和 HTML 解析 |
| `pyquery` | 类似 jQuery 的网页解析方式 |

```bash
py -m pip install beautifulsoup4
```

```python
from bs4 import BeautifulSoup

html = """
<html>
    <body>
        <h1>Python</h1>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup.h1.text)
```

---

## 十、机器学习库

| 库 | 主要用途 |
|---|---|
| `scikit-learn` | 传统机器学习 |
| `xgboost` | 梯度提升树 |
| `lightgbm` | 高性能梯度提升树 |
| `catboost` | 类别特征处理较强 |
| `imbalanced-learn` | 不平衡数据处理 |
| `optuna` | 超参数优化 |
| `shap` | 模型解释 |
| `lime` | 局部模型解释 |
| `mlxtend` | 机器学习扩展工具 |
| `yellowbrick` | 机器学习可视化 |
| `joblib` | 模型保存和并行计算 |

安装：

```bash
py -m pip install scikit-learn
```

示例：

```python
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(x, y)

print(model.predict([[5]]))
```

---

## 十一、统计分析与数学建模

| 库 | 用途 |
|---|---|
| `statsmodels` | 回归、时间序列、统计检验 |
| `scipy.stats` | 概率分布和统计检验 |
| `pymc` | 贝叶斯建模 |
| `pingouin` | 常见统计检验 |
| `lifelines` | 生存分析 |
| `arch` | 金融时间序列、ARCH/GARCH |
| `prophet` | 时间序列预测 |
| `pmdarima` | 自动 ARIMA |
| `linearmodels` | 面板数据、计量经济学 |
| `pulp` | 线性规划 |
| `ortools` | 运筹优化 |
| `gurobipy` | Gurobi 优化器接口 |
| `cvxpy` | 凸优化 |
| `gekko` | 动态优化和工程建模 |

数学建模常见组合：

```text
NumPy
Pandas
SciPy
Matplotlib
Seaborn
Scikit-learn
Statsmodels
PuLP
```

---

## 十二、深度学习与人工智能

| 库 | 主要用途 |
|---|---|
| `torch` | PyTorch 深度学习 |
| `tensorflow` | TensorFlow 深度学习 |
| `keras` | 高层神经网络接口 |
| `jax` | 自动微分和高性能计算 |
| `transformers` | 预训练大模型 |
| `datasets` | 机器学习数据集处理 |
| `accelerate` | 多设备训练 |
| `peft` | 参数高效微调 |
| `diffusers` | 扩散模型 |
| `onnx` | 跨框架模型格式 |
| `onnxruntime` | ONNX 模型推理 |
| `tensorboard` | 训练过程可视化 |

推荐学习顺序：

```text
NumPy
  ↓
Pandas
  ↓
Matplotlib
  ↓
Scikit-learn
  ↓
PyTorch / TensorFlow
```

---

## 十三、自然语言处理

| 库 | 用途 |
|---|---|
| `jieba` | 中文分词 |
| `nltk` | 英文自然语言处理 |
| `spacy` | 工业级 NLP |
| `transformers` | 预训练语言模型 |
| `sentence-transformers` | 文本向量 |
| `gensim` | Word2Vec、主题模型 |
| `textblob` | 简单文本处理 |
| `snownlp` | 中文情感分析 |
| `hanlp` | 中文自然语言处理 |
| `opencc` | 简繁体转换 |
| `langdetect` | 语言检测 |

```python
import jieba

words = jieba.lcut("我正在学习Python第三方库")
print(words)
```

---

## 十四、计算机视觉与图像处理

| 库 | 用途 |
|---|---|
| `pillow` | 图片读取、缩放、裁剪 |
| `opencv-python` | 计算机视觉和视频处理 |
| `scikit-image` | 图像处理算法 |
| `imageio` | 图片和视频读写 |
| `albumentations` | 图像数据增强 |
| `ultralytics` | YOLO 目标检测 |
| `mediapipe` | 人脸、手势、姿态识别 |
| `pytesseract` | OCR 接口 |
| `easyocr` | 深度学习 OCR |
| `rembg` | 图片去背景 |

### Pillow

```bash
py -m pip install pillow
```

```python
from PIL import Image

image = Image.open("photo.jpg")
image = image.resize((800, 600))
image.save("new_photo.jpg")
```

### OpenCV

```bash
py -m pip install opencv-python
```

```python
import cv2

image = cv2.imread("photo.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.jpg", gray)
```

---

## 十五、Web 开发

| 库或框架 | 特点 |
|---|---|
| `flask` | 轻量级 Web 框架 |
| `django` | 功能完整的大型 Web 框架 |
| `fastapi` | API 开发，支持类型提示 |
| `tornado` | 异步网络框架 |
| `sanic` | 异步 Web 框架 |
| `starlette` | 轻量级 ASGI 框架 |
| `uvicorn` | ASGI 服务器 |
| `gunicorn` | WSGI 服务器 |
| `jinja2` | HTML 模板引擎 |
| `streamlit` | 快速创建数据应用 |
| `gradio` | 快速创建 AI 演示界面 |
| `dash` | 数据仪表盘 |

Flask 示例：

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask!"

app.run(debug=True)
```

---

## 十六、数据库操作

| 库 | 数据库 |
|---|---|
| `sqlite3` | SQLite，属于标准库 |
| `sqlalchemy` | ORM 和 SQL 工具包 |
| `pymysql` | MySQL |
| `mysql-connector-python` | MySQL 官方连接器 |
| `psycopg` | PostgreSQL |
| `pymongo` | MongoDB |
| `redis` | Redis |
| `peewee` | 轻量级 ORM |
| `tortoise-orm` | 异步 ORM |
| `alembic` | 数据库迁移 |

```python
import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score REAL
)
""")

connection.commit()
connection.close()
```

---

## 十七、桌面图形界面 GUI

| 库 | 特点 |
|---|---|
| `tkinter` | Python 标准库自带 |
| `customtkinter` | 现代化 Tkinter |
| `PyQt6` | 功能完整的 Qt 框架 |
| `PySide6` | Qt 官方 Python 绑定 |
| `wxPython` | 原生桌面界面 |
| `kivy` | 跨平台、移动端 |
| `flet` | 使用 Python 构建跨平台应用 |
| `dearpygui` | 高性能 GUI |
| `ttkbootstrap` | 美化 Tkinter |
| `pywebview` | HTML 桌面界面 |

推荐顺序：

```text
Tkinter
   ↓
CustomTkinter
   ↓
PySide6
```

---

## 十八、自动化操作

| 库 | 用途 |
|---|---|
| `pyautogui` | 控制鼠标和键盘 |
| `keyboard` | 监听和模拟键盘 |
| `mouse` | 鼠标控制 |
| `pyperclip` | 剪贴板 |
| `schedule` | 定时任务 |
| `apscheduler` | 高级任务调度 |
| `watchdog` | 监控文件变化 |
| `psutil` | 系统进程和硬件信息 |
| `pygetwindow` | 管理窗口 |
| `pywinauto` | Windows 界面自动化 |
| `uiautomation` | Windows UI 自动化 |

```python
import pyautogui

pyautogui.FAILSAFE = True
pyautogui.moveTo(500, 300, duration=1)
pyautogui.click()
pyautogui.write("Hello Python")
```

把鼠标快速移动到屏幕左上角，可以触发 `FAILSAFE` 并停止程序。

---

## 十九、串口、单片机与电子信息工程

| 库 | 用途 |
|---|---|
| `pyserial` | 串口通信 |
| `pymodbus` | Modbus 通信 |
| `pyvisa` | 控制示波器、信号发生器等仪器 |
| `minimalmodbus` | 简化 Modbus 仪器通信 |
| `smbus2` | I²C/SMBus 通信 |
| `spidev` | SPI 通信 |
| `gpiozero` | 树莓派 GPIO |
| `RPi.GPIO` | 树莓派 GPIO |
| `bleak` | 蓝牙 BLE |
| `paho-mqtt` | MQTT 通信 |
| `python-can` | CAN 总线 |
| `control` | 自动控制系统分析 |
| `schemdraw` | 绘制电路图 |
| `scikit-rf` | 射频和微波工程 |

安装：

```bash
py -m pip install pyserial
```

示例：

```python
import serial

port = serial.Serial(
    port="COM3",
    baudrate=115200,
    timeout=1
)

port.write(b"Hello STM32\r\n")

data = port.readline()
print(data)

port.close()
```

注意：安装名是 `pyserial`，导入名是 `serial`。

---

## 二十、音频与视频处理

| 库 | 用途 |
|---|---|
| `pydub` | 音频剪切、合并、格式转换 |
| `librosa` | 音频特征分析 |
| `sounddevice` | 录音和播放 |
| `soundfile` | 音频文件读写 |
| `pygame` | 简单音频播放 |
| `moviepy` | 视频剪辑 |
| `ffmpeg-python` | 调用 FFmpeg |
| `opencv-python` | 视频帧处理 |
| `imageio-ffmpeg` | FFmpeg 视频支持 |
| `whisper` | 语音识别模型 |

---

## 二十一、游戏开发

| 库 | 用途 |
|---|---|
| `pygame` | 2D 游戏开发 |
| `arcade` | 现代 2D 游戏框架 |
| `pyglet` | 多媒体和窗口 |
| `panda3d` | 3D 游戏引擎 |
| `ursina` | 简单 3D 游戏开发 |
| `pymunk` | 2D 物理引擎 |
| `moderngl` | OpenGL 图形编程 |

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Python 游戏")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```

---

## 二十二、地理信息与地图

| 库 | 用途 |
|---|---|
| `geopandas` | 地理表格数据 |
| `shapely` | 几何对象计算 |
| `folium` | 交互式地图 |
| `rasterio` | 栅格地理数据 |
| `fiona` | 地理矢量文件 |
| `pyproj` | 坐标系转换 |
| `geopy` | 地理编码和距离计算 |
| `osmnx` | OpenStreetMap 路网分析 |
| `cartopy` | 地图绘图 |

---

## 二十三、网络、服务器与安全

| 库 | 用途 |
|---|---|
| `paramiko` | SSH |
| `fabric` | 远程服务器自动化 |
| `cryptography` | 加密与证书 |
| `pycryptodome` | 密码学算法 |
| `scapy` | 网络数据包分析 |
| `dnspython` | DNS 查询 |
| `netifaces` | 网络接口信息 |
| `websockets` | WebSocket |
| `twisted` | 异步网络框架 |

> 网络安全工具只能用于自己拥有或明确获准测试的设备、网络和系统。

---

## 二十四、测试、调试和代码质量

| 库 | 用途 |
|---|---|
| `pytest` | 单元测试 |
| `hypothesis` | 属性测试、自动生成测试数据 |
| `coverage` | 测试覆盖率 |
| `tox` | 多环境测试 |
| `black` | 自动格式化代码 |
| `ruff` | 高速代码检查和格式化 |
| `pylint` | 代码质量检查 |
| `flake8` | 代码规范检查 |
| `mypy` | 静态类型检查 |
| `isort` | 自动整理 import |
| `pre-commit` | 提交前自动检查 |
| `debugpy` | Python 调试器 |

```python
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
```

运行：

```bash
pytest
```

---

## 二十五、命令行和终端美化

| 库 | 用途 |
|---|---|
| `rich` | 彩色终端、表格、进度条 |
| `tqdm` | 进度条 |
| `click` | 创建命令行程序 |
| `typer` | 基于类型提示创建 CLI |
| `argparse` | 标准库命令行解析 |
| `questionary` | 交互式终端菜单 |
| `prompt-toolkit` | 高级命令行输入 |
| `colorama` | 跨平台彩色文字 |
| `tabulate` | 终端表格 |

```python
from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.02)
```

---

## 二十六、配置、日志和数据校验

| 库 | 用途 |
|---|---|
| `pydantic` | 类型校验和数据模型 |
| `pyyaml` | YAML 文件 |
| `python-dotenv` | 读取 `.env` 环境变量 |
| `loguru` | 简化日志记录 |
| `toml` | TOML 配置文件 |
| `marshmallow` | 数据序列化和校验 |
| `attrs` | 简化类定义 |
| `dacite` | 字典转换为数据类 |
| `jsonschema` | JSON Schema 校验 |

```python
from pydantic import BaseModel


class Student(BaseModel):
    name: str
    score: float


student = Student(name="小明", score=90)
print(student)
```

---

## 二十七、并发、异步和任务队列

| 库 | 用途 |
|---|---|
| `asyncio` | 异步编程，属于标准库 |
| `aiohttp` | 异步 HTTP |
| `httpx` | 同步和异步 HTTP |
| `celery` | 分布式任务队列 |
| `rq` | Redis 任务队列 |
| `joblib` | 并行计算 |
| `ray` | 分布式计算 |
| `gevent` | 协程并发 |
| `greenlet` | 轻量级协程 |
| `anyio` | 统一异步接口 |

---

## 二十八、项目打包和环境管理

| 工具 | 用途 |
|---|---|
| `pip` | 安装第三方包 |
| `venv` | 创建虚拟环境，属于标准库 |
| `virtualenv` | 第三方虚拟环境工具 |
| `setuptools` | 项目构建和打包 |
| `wheel` | Wheel 包格式 |
| `build` | 构建 Python 包 |
| `twine` | 上传软件包到 PyPI |
| `poetry` | 依赖和项目管理 |
| `pipenv` | 虚拟环境和依赖管理 |
| `uv` | 高性能 Python 包和环境管理 |
| `pipx` | 隔离安装命令行程序 |
| `conda` | 环境和软件包管理 |

---

## 二十九、Jupyter 与交互式开发

| 库或工具 | 用途 |
|---|---|
| `jupyter` | Jupyter 工具集合 |
| `jupyterlab` | JupyterLab 开发环境 |
| `notebook` | 经典 Notebook |
| `ipython` | 增强型交互式 Python |
| `ipykernel` | Jupyter Python 内核 |
| `ipywidgets` | Notebook 交互控件 |
| `voila` | Notebook 转 Web 应用 |
| `nbconvert` | Notebook 格式转换 |

---

## 三十、常见安装错误

### 1. `ModuleNotFoundError`

```text
ModuleNotFoundError: No module named 'requests'
```

原因通常有三种：

1. 没有安装。
2. 安装到了另一个 Python 环境。
3. 安装名和导入名不同。

检查当前解释器：

```python
import sys

print(sys.executable)
```

检查安装位置：

```bash
py -m pip show requests
```

### 2. pip 找不到

```text
'pip' 不是内部或外部命令
```

改用：

```bash
py -m pip install requests
```

或者：

```bash
python -m pip install requests
```

### 3. 文件名与第三方库重名

不要把自己的程序命名为：

```text
numpy.py
pandas.py
requests.py
serial.py
matplotlib.py
random.py
time.py
```

否则可能导入自己的文件，而不是正确的库。

同目录中的这些文件也要删除：

```text
numpy.pyc
__pycache__
```

### 4. 安装成功但 IDLE 无法导入

很可能是 IDLE 和 pip 对应的不是同一个 Python。

在 IDLE 中查看：

```python
import sys

print(sys.executable)
```

然后使用这个解释器对应的 `python.exe` 安装。

### 5. 安装编译失败

先升级安装工具：

```bash
py -m pip install --upgrade pip setuptools wheel
```

然后再次安装：

```bash
py -m pip install 库名
```

---

## 三十一、适合当前阶段的库

当前学习 Python 基础、数学建模、数据分析，同时涉及电子信息和单片机，可以按下面顺序学习。

### 第一阶段：必须掌握

```text
requests
numpy
pandas
matplotlib
openpyxl
```

对应能力：

```text
网络请求
数组和矩阵
表格数据分析
数据绘图
Excel 操作
```

### 第二阶段：数据分析与数学建模

```text
scipy
seaborn
scikit-learn
statsmodels
sympy
pyecharts
```

### 第三阶段：自动化和工程应用

```text
beautifulsoup4
lxml
selenium
python-docx
python-pptx
pypdf
pyserial
```

### 第四阶段：进阶方向

| 方向 | 学习库 |
|---|---|
| 深度学习 | `torch` |
| Web 后端 | `flask`、`fastapi` |
| 桌面软件 | `PySide6` |
| 爬虫 | `scrapy`、`playwright` |
| 计算机视觉 | `opencv-python` |
| 数据应用 | `streamlit` |
| 单片机上位机 | `pyserial`、`PySide6` |

---

## 三十二、推荐安装组合

### Python 基础与常用工具

```bash
py -m pip install requests pillow rich tqdm
```

### 数据分析与数学建模

```bash
py -m pip install numpy pandas scipy matplotlib seaborn scikit-learn openpyxl statsmodels sympy
```

### 爬虫学习

```bash
py -m pip install requests beautifulsoup4 lxml selenium
```

### Office 自动化

```bash
py -m pip install openpyxl python-docx python-pptx pypdf pymupdf
```

### 单片机串口通信

```bash
py -m pip install pyserial
```

不建议一次安装所有第三方库。最合理的原则是：

> 项目需要什么，就安装什么。

当前最值得优先掌握的核心链条是：

```text
Python 基础
   ↓
NumPy
   ↓
Pandas
   ↓
Matplotlib / Seaborn
   ↓
SciPy / Scikit-learn
   ↓
数学建模与数据分析项目
```
