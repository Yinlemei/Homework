# 作业提交系统

每次提交的作业摘要: [Homework Summary](https://github.com/zmhab/Homework/blob/master/Homework%20Summary.md)

每次布置的作业会提交到这个仓库中.
每次作业对应一个目录, 大家在对应作业目录下, 创建一个以自己名字命名的文件夹, 作业放在里面.
比如:
```bash
.
├── Homework-How-to-use-github
│   ├── alice
│   │   ├── main.py
│   │   └── README.md
│   └── bob
│       ├── main.py
│       └── README.md
└── README.md
```
提交作业以提交 `pull request` 的方式来进行;

* 注意
    
    * 如你所见, 这个仓库是 `公开` 的, 个人隐私相关的信息不要上传;
    * 所有改动仅在 `当前作业目录/个人目录` 下, 否则提交不会被通过;
    * 多次作业的个人目录名请 `保持相同` , 方便后续评估;

## 流程
* 如何开始
    1. fork 这个仓库;
    2. 将你自己的仓库 clone 到本地 
    `git clone git@github.com:yourname/Homework.git` ;
    3. 在当前作业目录下, 创建一个自己专有的文件夹
    `cp -r homework-name/.schema homework-name/your-name/`;
    4. 在自己专有的目录下完成作业;
    5. 将所有的改动保存, 推送到远程仓库
    `git add * && git commit -m 'Your commit here.' && git push origin master`;
    6. 在作业截止日期之前向这个仓库提交 pull request;

在截止日期到达之后, 会接受所有合格的 pr , 然后大家就可以互相看看同学的作业互相交流一下;

## Q & A
* 为什么我提交的 pr 没有同意?
```
    提交的 pr 没有通过的话, 说明有一些地方格式不对;
    提交的作业有误不会影响 pr 审核.
```
* Github 我不会使用, 应该从哪里学起?
```
    首先应该学习 git 的使用:

        * 安装
            https://git-scm.com/download/win
        * 文档
            * https://git-scm.com/book/en/v2
            如果阅读英文吃力的话, 有对应的中文翻译版:
            * https://git-scm.com/book/zh/v2
            * https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000
    然后就是 Github 的相关
        * fork
        * pull request
        * issue
        * wiki
        * etc
```