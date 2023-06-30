# Pyserini 自建索引 查询 Demo
注意，以下环境为 Ubuntu 20.04 虚拟机

## 数据获取
编写脚本从 (https://daxue.hao86.com) 爬取一些大学名称及其基本描述，见 `./data/data_fetch.py`

同时进行将数据保存为 jsonl，见 `./data/clean_data/documents.jsonl` （数据为粗洗，并不完全 clean，仅为 demo 使用）

## 环境配置
### 安装 Anserini
安装 Java 11 和 maven 3.3+ （略）

```sh
git clone https://github.com/castorini/anserini.git --recurse-submodules
cd ./anserini/
mvn clean package appassembler:assemble
cd tools/eval && tar xvfz trec_eval.9.0.4.tar.gz && cd trec_eval.9.0.4 && make && cd ../../..
cd tools/eval/ndeval && make && cd ../../..
```

### 初始化 python 环境
```sh
cd ../
python3 -m venv ./venv/
source ./venv/bin/activate
pip install pyserini
pip install faiss-cpu
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### 建立 index
使用以下命令进行 index 的建立

```sh
python -m pyserini.index.lucene -collection JsonCollection -input data/clean_data -index indexed/demo_index_jsonl -generator DefaultLuceneDocumentGenerator -threads 1 -storeRaw -language zh
```

执行结束后，在 `./indexed/` 下可见生成的 index

### 查询 demo
启动查询 demo 开始查询。注意，使用中文查询效果较差

```sh
python demo.py
```

查询效果如：

![](/images/1.png)
