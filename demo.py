from pyserini.search.lucene import LuceneSearcher

searcher = LuceneSearcher('indexed/demo_index_jsonl')
searcher.set_language('zh')

while True:
    print("请输入要查询的内容：")
    content = input()
    hits = searcher.search(str(content), k=15)
    print("结果如下：")
    for i in range(len(hits)):
        print(f'{i+1:2} {hits[i].docid:4} {hits[i].score:.5f}')
    print("-------------------------")