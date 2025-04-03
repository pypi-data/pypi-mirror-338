# FFmpeg Converter

基于 FFmpeg 的音视频格式转换工具，支持异步操作和进度监控。

[![CI Status](https://github.com/ospoon/ffmpeg-converter/workflows/CI/badge.svg)](https://github.com/ospoon/ffmpeg-converter/actions)
[![Coverage](https://codecov.io/gh/ospoon/ffmpeg-converter/branch/main/graph/badge.svg)](https://codecov.io/gh/ospoon/ffmpeg-converter)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## 功能特点

### 音频转换
- 支持多种音频格式转换（mp3, wav, ogg 等）
- 可自定义采样率和声道数
- 实时转换进度显示
- 预估剩余时间计算

### 视频转换
- 支持多种视频格式转换（mp4, mkv, avi 等）
- 可自定义视频编解码器（h264, h265, vp9）
- 可调整视频比特率和分辨率
- 可设置帧率（FPS）
- 支持音频参数调整
- 支持编码预设选项
- 实时显示转换进度、速度和当前帧信息

## 环境要求

- Python >= 3.11
- FFmpeg（需要预先安装）
- UV（Python 包管理工具）

## 快速开始

### 安装

1. 安装 FFmpeg
   ```bash
   # Windows (使用 scoop)
   scoop install ffmpeg

   # Windows (使用 chocolatey)
   choco install ffmpeg

   # Linux (Ubuntu/Debian)
   sudo apt-get update && sudo apt-get install ffmpeg
   ```

2. 克隆仓库并安装依赖
   ```bash
   git clone https://github.com/ospoon/ffmpeg-converter.git
   cd ffmpeg-converter
   pip install uv
   uv venv
   uv sync
   ```

### 使用示例

#### 音频转换
```python
import asyncio
from audio import AudioConverter

async def main():
    converter = AudioConverter()
    
    def progress_callback(progress, time_remaining, info):
        print(f"进度: {progress:.2f}%, 剩余时间: {time_remaining}, 详细信息: {info}")
    
    success = await converter.convert(
        input_file="input.mp3",
        output_file="output",
        output_format="wav",
        sample_rate=44100,
        channels=2,
        progress_callback=progress_callback,
    )
    
    if success:
        print("转换完成")
    else:
        print("转换失败")

if __name__ == "__main__":
    asyncio.run(main())
```

#### 视频转换
```python
import asyncio
from video import VideoConverter

async def main():
    converter = VideoConverter()
    success = await converter.convert(
        input_file="input.mp4",
        output_file="output",
        output_format="mkv",
        video_codec="h264",
        video_bitrate="5M",
        resolution="1920x1080",
        fps=30,
        audio_codec="aac",
        audio_bitrate="192k",
        preset="medium",
        crf=23
    )
    print("转换完成" if success else "转换失败")

asyncio.run(main())
```

#### 进度回调示例
```python
def print_progress(progress: float, time_remaining: str, info: dict = None):
    if info:
        print(f"\r进度: {progress:.1f}% - 剩余时间: {time_remaining} - "
              f"速度: {info.get('conversion_speed', 'N/A')} - "
              f"当前帧: {info.get('current_frame', 'N/A')}", end="")
    else:
        print(f"\r进度: {progress:.1f}% - 剩余时间: {time_remaining}", end="")
```

## 开发指南

### 环境配置

1. 同步项目依赖
   ```bash
   uv sync
   ```

2. 安装 pre-commit hooks
   ```bash
   pre-commit install
   ```

### 开发流程

1. 创建新分支
   ```bash
   git checkout -b feature/your-feature
   ```

2. 代码格式化和检查
   ```bash
   ruff check --fix .
   ruff format .
   ```

3. 类型检查
   ```bash
   mypy .
   ```

4. 运行测试
   ```bash
   pytest
   ```

### 代码提交规范

提交信息格式：
```
<type>(<scope>): <subject>

<body>
```

类型（type）：
- feat: 新功能
- fix: 修复bug
- docs: 文档更新
- style: 代码格式（不影响代码运行的变动）
- refactor: 重构
- test: 测试相关
- chore: 构建过程或辅助工具的变动

### 代码质量要求

- 所有代码必须通过 ruff 检查
- 所有代码必须通过 mypy 类型检查
- 测试覆盖率要求达到 80% 以上
- 遵循 PEP 8 编码规范

## 注意事项

- 确保系统已正确安装 FFmpeg 并添加到环境变量
- 支持的具体格式取决于 FFmpeg 的编译选项
- 建议在转换大文件时使用进度回调功能
- 视频转换时注意选择合适的编码参数以平衡质量和性能

## 许可证

[MIT License](LICENSE)

## 贡献指南

欢迎提交 Issue 和 Pull Request。在提交 PR 之前，请确保：

1. 更新测试用例
2. 更新相关文档
3. 遵循代码规范
4. 所有测试通过

## 问题反馈

如果您在使用过程中遇到任何问题，请：

1. 查看是否是 [已知问题](https://github.com/ospoon/ffmpeg-converter/issues)
2. 如果是新问题，请创建一个新的 Issue，并提供：
   - 问题描述
   - 复现步骤
   - 期望行为
   - 实际行为
   - 环境信息（操作系统、Python版本、FFmpeg版本等）
