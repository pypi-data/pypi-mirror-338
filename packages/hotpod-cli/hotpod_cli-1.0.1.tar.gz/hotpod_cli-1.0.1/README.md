# HotPod CLI

京东云GPU云服务命令行工具，用于管理JD Cloud GCS（Global Container Storage）实例。

## 安装

```bash
pip install hotpod
```

## 配置

在使用该工具之前，需要设置京东云API凭证。

1. 设置以下环境变量：

```bash
export JDCLOUD_AK=your_access_key
export JDCLOUD_SK=your_secret_key
```

## 使用方法

### 基本信息

显示关于HotPod CLI的信息：

```bash
hotpod info
```

### 实例管理

列出所有GCS实例：

```bash
hotpod instance list
```

创建新的GCS实例（默认：1个）：

```bash
hotpod instance create
```

交互式选择镜像和SKU创建实例：

```bash
hotpod instance create
```

使用指定的镜像ID和SKU创建实例：

```bash
hotpod instance create --imageid <镜像ID> --sku <SKU ID>
```

删除GCS实例：

```bash
hotpod instance delete --id <实例ID>
```

显示GCS实例的详细信息：

```bash
hotpod instance show --id <实例ID>
```

### 文件操作

上传文件到GCS实例：

```bash
hotpod file upload --instance <实例ID> --local <本地文件路径> --remote <远程目录路径>
```

在GCS实例上执行命令：

```bash
hotpod file exec --instance <实例ID> --cmd <命令>
```

列出GCS实例上的文件和目录：

```bash
hotpod file list --instance <实例ID> --path <远程目录路径>
```

从GCS实例下载文件：

```bash
hotpod file download --instance <实例ID> --remote <远程文件路径> --local <本地保存路径>
```

### ComfyUI任务

运行ComfyUI任务：

```bash
hotpod comfyui runtask --task <任务配置文件路径>
```

使用指定实例运行ComfyUI任务：

```bash
hotpod comfyui runtask --instance <实例ID> --task <任务配置文件路径>
```

等待任务完成：

```bash
hotpod comfyui runtask --task <任务配置文件路径> --wait
```

### LLM任务

运行LLM任务，直接返回模型访问URL：

```bash
hotpod llm runtask
```

使用指定模型创建实例：

```bash
hotpod llm runtask --model deepseek
```

向特定实例的模型发送提示词：

```bash
hotpod llm runtask --instance <实例ID> --prompt "你好，请介绍一下自己"
```

## 开发

1. 克隆仓库
2. 创建虚拟环境
3. 安装开发依赖：
   ```bash
   pip install -e .
   ```

## 许可证

MIT
