# Elastic Search 文档

### 介绍

Elastic Search是一个基于开源Lucence的搜索引擎。它提供了一个具有HTTP web接口和无架构的JSON文档的分布式的，多租户能力的全文搜索能力。并且官方提供了Java，Python等客户端。

Elastisearch能够被用来搜索任何类型的文档。它提供了接近实时搜索的可扩展的搜索，以及支持多租户。每一个搜索引擎可以划分为分片的索引，每个分片可以有多个副本。每个Elasticsearch节点可以有一个或多个分片，其引擎可以同时作为协调器，将操作转发给正确的分片。

Elasticsearch的主要特性:

* 分布式搜索
* 多租户
* 查询统计分析
* 分组和聚合 


### Demo

[Elasticsearch Demo](https://github.com/dyljqq/elastic-search-demo)


### 与Solr的对比

1. 数据源

	* solr可以来自不同来源的数据，如xml，csv等，我们现在采用的方法就是通过csv格式导入数据，来更新索引。
	* Elasticsearch还支持其他来源的数据。例如ActiveMQ，JDBC, git等。最主要的还是通过json。

2. 搜索

	* solr专注于文本搜索
	* Elasticsearch则常用于查询，过滤和分组分析统计。

3. 索引

	两者都支持使用停用词和同义词来匹配文档。

	在solr中，索引间进行join必须是单个分片和其他节点上的副本集进行关联来搜索文档间关系（例如SQL连接）。而Elasticsearch提供更高效的has_children和top_children查询来检索这样的相关文档。
	
4. 可扩展性和分布式

	搜索引擎需要处理数以百万级的文档，基于此搜索引擎应该是可复制的，模块化的和可扩展的，支持集群和分布式架构。

5. 专为云而设计

	Elasticsearch非常易于扩展，拥有足够多的需要大集群的使用案例。而且内置了ZooKeeper。
	
6. 分片拆分和再平衡

	shards是luence索引的分区单元，solr和elasticsearch均使用。你可以通过在集群中的不同计算机上运行shard来分发索引。随着	SolrCloud的引入，Solr开始支持shard拆分，这允许您通过拆分现有shard来添加更多shard。相比之下，ElasticSearch仍然不支持	这一点，事实上，实际上阻止了这种做法。ES通过向设置中添加更多计算机，可以使用自动碎片平衡功能。相比之下，Solr允许添加分片	（使用隐式路由时）或分割（使用复合ID时），但不能删除分片。它允许您增加副本。在Elasticsearch中，默认情况下每个索引具有五个	分片。它不允许您更改主分片的数量，但它允许您增加副本的数量。分片再平衡对于水平扩容非常有用。当添加新机器时，它将自动重新平衡	不同机器中可用的分片。
	
### 目前的设想

首先准备尝试替换掉熊猫优选运营后台的搜索服务，看看Elasticsearch的效果如何。因为考虑到，如果直接替换到前端的搜索的话，可能会有一定的风险。

### 目前的进度

目前的话，将商品数据更新到Elastic已经完成走通，后面会写搜索需要的逻辑吧。进度的话，会更新在这篇文档上。