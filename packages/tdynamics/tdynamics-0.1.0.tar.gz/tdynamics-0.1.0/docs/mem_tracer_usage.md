# 内存跟踪器(MemTracer)使用文档

## 简介

[`MemTracer`]类是 [`tdynamics`]包中的一个工具，用于跟踪 PyTorch 模型训练过程中的 GPU 内存使用情况。它记录模型执行不同阶段（前向传播、反向传播、优化器步骤）的内存统计数据，帮助识别内存瓶颈并优化内存使用。

## 安装

内存跟踪器是 `tdynamics` 包的一部分，除了安装该包本身外，不需要额外的安装步骤。

## 基本用法

```python
import torch
from tdynamics.tracer import MemTracer, install_hooks

# 创建模型和优化器
model = torch.nn.Linear(10, 10)
optimizer = torch.optim.Adam(model.parameters())

# 创建内存跟踪器
tracer = MemTracer()

# 在模型和优化器上安装钩子
install_hooks(m=model, opt=optimizer, tracer=tracer)

# 训练循环
inputs = torch.randn(32, 10)
target = torch.randn(32, 10)
for epoch in range(10):
    # 前向传播
    output = model(inputs)
    loss = torch.nn.functional.mse_loss(output, target)
    
    # 反向传播
    optimizer.zero_grad()
    loss.backward()
    
    # 优化器步骤
    optimizer.step()
```

## 高级特性

### 自定义日志文件

默认情况下，内存使用日志写入名为 `mem_trace_rank_{rank}.log` 的文件。您可以指定自定义日志文件：

```python
# 使用特定文件
tracer = MemTracer(logfile=open("custom_memtrace.log", "w"))

# 或传递文件路径
import io
tracer = MemTracer(logfile=io.open("custom_memtrace.log", "w"))
```

### 记录时间戳

启用日志中的时间信息：

```python
tracer = MemTracer(logtime=True)
```

### Python 异常跟踪

启用 Python 异常跟踪：

```python
tracer = MemTracer(tracepy=True)
```

## API 参考

### [`MemTracer`](../src/tdynamics/tracer/mem_tracer.py)

```python
class MemTracer(BaseTracer):
    def __init__(self, logfile=None, tracepy=False, logtime=False):
        # 初始化内存跟踪器
        # 参数:
        #   logfile: 文件对象或 None（默认创建 mem_trace_rank_{rank}.log）
        #   tracepy: 是否跟踪 Python 异常（默认: False）
        #   logtime: 是否在日志中包含时间戳（默认: False）
```

### [`install_hooks`](../src/tdynamics/tracer/__init__.py)

```python
def install_hooks(m: torch.nn.Module = None, opt: torch.optim.Optimizer = None, tracer: BaseTracer = None):
    # 在模型模块和优化器上安装钩子
    # 参数:
    #   m: 要跟踪的 PyTorch 模块
    #   opt: 要跟踪的 PyTorch 优化器
    #   tracer: 跟踪器实例（例如 MemTracer）
```

## 内存跟踪输出格式

跟踪器以以下格式记录信息：

```
{'step': 0, 'module': 'Linear', 'stage': 'pre forward', 'mem': {'allocated': 0.0, 'cached': 512.0, 'max_allocated': 0.0, 'max_cached': 512.0}}
```

每个日志条目包含：
- `step`: 当前步骤编号
- `module`: 正在执行的模块名称
- `stage`: 执行阶段（pre forward, post forward, pre backward, post backward, pre step, post step）
- `mem`: 内存统计数据（单位：MB）
  - `allocated`: 当前已分配内存
  - `cached`: 当前预留内存
  - `max_allocated`: 最大分配内存
  - `max_cached`: 最大预留内存
- `time`: （可选）启用日志记录时的时间戳

## 最佳实践

1. 始终同时跟踪模型和优化器，以获得完整的内存分析
2. 在内存测量前使用 `torch.cuda.synchronize()`（当 CUDA 可用时自动执行）
3. 通过将内存峰值与特定模块和阶段关联来分析内存使用情况
4. 使用完毕后关闭日志文件，确保所有数据都被写入
