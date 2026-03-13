# 文件系统对象模型

```mermaid
---
title: File System Object Model
---

classDiagram
class Element{
    string summary
}
style Element fill:lime

class File{
    +string title
    +Path path
    +List~Section~ sections
}
Element <|-- File
Element <|-- Section
Section *-- File


class Folder{
    +string title
    +Path path
    +List~File~ files
    +List~Folder~ subfolders
    +init(Markdown md)
}
Element <|-- Folder
File *-- Folder
style Folder fill:fuchsia

```

# 文件对象模型

```mermaid
---
title: Document Object Model
---

classDiagram
class Element{
    string summary
}
class Figure~Element~{
    base64 rawdata
}
style Element fill:lime
style Figure fill:lightblue
Element <|-- Figure
class Cell {
    string c
}
class Column {
    List~Cell~ cells
}
class Row {
    List~Column~ cols
}
class Table~Element~ {
    List~Row~ rows
}
Cell *-- Column
Column *-- Row
Row *-- Table
Element <|-- Table
style Table fill:lightblue

class Markdown
style Markdown fill:yellow

class Section{
    +string title
    +Path path
    +List~string~ paragraphs
    +List~Figure~ figures
    +List~Table~ tables
    +List~Section~ subsections
    +init(Markdown md)
}
Element <|-- Section
style Section fill:fuchsia


Table *-- Section 
Figure *-- Section 
```

# 统一文件对象模型

```mermaid
---
title: Document Object Model
---

classDiagram
class Element{
    string summary
}
style Element fill:lime


class Figure~Element~{
    base64 rawdata
}
style Element fill:lime
style Figure fill:lightblue
Element <|-- Figure
class Cell {
    string c
}
class Column {
    List~Cell~ cells
}
class Row {
    List~Column~ cols
}
class Table~Element~ {
    List~Row~ rows
}
Cell *-- Column
Column *-- Row
Row *-- Table
Element <|-- Table
style Table fill:lightblue


class Paragraph~Element~{
    string text
}
style Paragraph fill:lightblue
Element <|-- Paragraph

class Markdown
style Markdown fill:yellow

class Section~Element~{
    +string title
    +Path path
    +List~Paragraph~ paragraphs
    +List~Figure~ figures
    +List~Table~ tables
    +List~Section~ subsections
    +init(Markdown md)
}
Element <|-- Section
style Section fill:fuchsia


Table *-- Section 
Figure *-- Section 
Paragraph *-- Section 
Section *-- Section 


class File~Element~{
    +string title
    +Path path
    +List~Section~ sections
}
Element <|-- File
Section *-- File


class Folder~Element~{
    +string title
    +Path path
    +List~File~ files
    +List~Folder~ subfolders
    +init(Markdown md)
}
Element <|-- Folder
File *-- Folder
Folder *-- Folder
style Folder fill:Coral

```

# 数据存储模型

```mermaid

---
title: 数据存储模型
---

graph LR;
    subgraph 计算语义
                text(文本) --> 内嵌
    end
        内嵌 --> 语义树
    subgraph 检索
        语义树 --> 摘要 --> 对象树
    end

    text --> raw[(原始文件)]
    语义树 --> embedding[(向量数据库)]
    对象树 --> markdown[(内容对象数据库)]
```

# 自然语言接口

- 利用小语言模型(SLM)深度思索模式进行文本的高质量总结
- 利用多模态小语言模型对图像进行分析和总结
- 利用OCR进行图像内容分析
- 利用多模态大语言模型(LLM)进行图像分析和总结

# 文件系统和内容管理系统

文件模型：

- 文件系统树
- 文件对象树
- 版本树

# Markdown转录

- Marker
- MarkitDown
- Pandoc

# 强化学习改进

## MCTS

例子：multihop question: 哪个型号的六轴机器人需要对磨抛死锁后触发的紧急按钮进行复位？

多路径推理和综合
推理时结合搜索算法是小型LM RAG的关键
Inference-time scaling 推理时计算扩展

## DPO在线强化学习训练

利用用户评价构造在线强化学习改进Agent

# 智能体系统，MCP和工具使用

- 公司自有工具
- 数据库分析工具
- 机器人专有工具
- 提示词
- 多轮交互Agent

外部数据源，工具，环境，粘合不同的AI系统

# RAG

```mermaid
flowchart TB
    subgraph retrieval["检索增强生成"]
        direction LR
        ref_docs@{shape: docs, label: "应用文件集"} 
        subgraph text_understanding["文本理解(原始文本)"]
            direction LR
            summary_text_local["deepseek r1<br>本地思考模型"]
            summary_text_api["qwen3<br>云端文本模型"]
        end
        subgraph image_understanding["OCR图像理解(pdf/图片)"]
            direction LR
            summary_image_local["gemma3<br>本地图像模型"]
            summary_image_api["gemini3<br>云端图像模型"]
        end
        ref_docs --> summary_text_local
        ref_docs --> summary_text_api
        ref_docs --> summary_image_local
        ref_docs --> summary_image_api
        text_understanding --> llm_embed@{ shape: hex, label: "LLM<br>embedder"}
        image_understanding --> llm_embed
        %% link 0,1,2,3,4,5
        subgraph embedding_models["内嵌模型"]
            direction LR
            embed_bge["bge-m3<br>本地"]
            embed_qwen["qwen3<br>云端api"]
        end
        embedding_models --> vector_db@{ shape: cyl, label: "内嵌向量\n(向量数据库)"}
        llm_embed --> embed_bge 
        llm_embed --> embed_qwen 
        embedding_models --> query_vector@{ shape: lean-l, label: "查询向量"}
        query_vector --> find_docs[查找相关文档<br>相似度排序]
        vector_db --> find_docs
        find_docs --> context_chunks@{shape: rounded, label: "排序的上下文:\n<段落1>,\n<段落2>,\n<段落3>"}
        %% link 6,7,8,9,10,11,12
    end
    user_query@{shape: rounded, label: "用户查询:<br><用户问题>"} 
    user_query --> llm_embed
    aug_query@{shape: rounded, color: red, label: "提示模板：\n请基于给定的上下文:\n<段落1>,\n<段落2>,\n<段落3>\n回答用户的问题:\n<用户问题>\n"}
    aug_query --> llm_gen@{shape: hex, label: "LLM<br>答案生成"}
    context_chunks --> aug_query
    user_query --> aug_query
    %% link 13,14,15,16
    subgraph gen_models["生成模型"]
        direction LR
        gen_local["deepseek-r1<br>本地部署"]
        gen_api["qwen3<br>云端api"]
    end
    llm_gen --> gen_local
    llm_gen --> gen_api
    gen_models --> thinking@{shape: rounded, label: "思考:\n<思考过程>"}
    gen_models --> response@{shape: rounded, label: "响应:\n<答案文本>"}
    %% link 17,18,19,20

    style aug_query fill:darkkhaki
    style ref_docs fill:indianred
    style summary_text_local fill:lightblue
    style summary_text_api fill:pink
    style summary_image_local fill:lightblue
    style summary_image_api fill:pink
    style embed_bge fill:lightblue
    style embed_qwen fill:pink
    style gen_local fill:lightblue
    style gen_api fill:pink

    linkStyle 0,2,7 stroke:blue
    linkStyle 1,3,8 stroke:red
    linkStyle 4,5 stroke:brown,stroke-width:6px
    linkStyle 13 stroke:lime,stroke-width:2px
    %%linkStyle 5 stroke:blue
```


# 需求

```plantuml
@startmindmap
* 企业大模型知识库框架
left side
** 文档处理
*** 文档清洗
*** 跨平台文件转换
*** 文件对象化转录(Markdown转录)
*** 文件向量化(大语言模型摘要及向量化)
** 文档建模(文件模型抽象)
*** 文件系统树
*** 内容对象树
*** 语义树
*** 版本树
right side
** 应用框架搭建
*** 数据库搭建
**** 内容对象数据库
**** 向量数据库
*** HMI前端（Streamlit, Gradio）
*** RAG框架集成
*** 模型上下文协议(MCP)
*** 智能体(Agent)
** 检索增强生成(RAG)
*** 基于文本相似度检索(内嵌向量)
*** 基于搜索算法检索

@endmindmap
```