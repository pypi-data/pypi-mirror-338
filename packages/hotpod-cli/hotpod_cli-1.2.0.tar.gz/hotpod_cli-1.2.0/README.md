# HotPod CLI

Hotpod命令行工具，用于管理GCS实例。

## 安装

```bash
pip install hotpod-cli
```

## 配置

在使用该工具之前，需要设置京东云API凭证。

1. 设置以下环境变量：

```bash
export JDCLOUD_AK=your_access_key
export JDCLOUD_SK=your_secret_key
```

或者在.env文件中配置JDCLOUD_AK和JDCLOUD_SK

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

列出GCS实例上的文件和目录：

```bash
hotpod file list --instance <实例ID> --path <远程目录路径>
```

### ComfyUI任务

使用指定实例运行ComfyUI任务：

```bash
hotpod comfyui runtask --instance <实例ID> --task <任务配置文件路径>
```

使用指定集群运行ComfyUI任务：

```bash
hotpod comfyui runtask --cluster <集群名称> --task <任务配置文件路径>
```

### LLM任务


向特定实例上的模型对话，model包括qwq和deepseek

```bash
hotpod llm runtask --instance <实例ID> --model <model> --prompt "你好，请介绍一下自己"
```

向指定集群上的模型对话

```bash
hotpod llm runtask --cluster <集群名称> --model <model> --prompt "你好，请介绍一下自己"
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
