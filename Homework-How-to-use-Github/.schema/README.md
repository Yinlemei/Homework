# How to use Github

这次作业主要目的是让大家熟悉一下提交作业的流程;

## 流程
1. 将 `.schema` 目录复制为以自己名字命名的目录 :
`cp -r .schema your-name` ;
2. 新建一个名为 `test.txt` 的文件, 并且内容为 `Hello world!` :
`echo "Hello world!" >> test.txt` ;
此时目录结构应该像下面:
```bash
.
├── .git
│   └── ...
├── .gitignore
├── Homework-How-to-use-Github
│   ├── .schema
│   │   └── README.md
│   └── VEct0r
│       ├── README.md
│       └── test.txt
└── README.md
```
3. 保存自己的改动, 并且推送到远程仓库此次作业的分支 :
`git add * && git commit -m 'Your commit here.' && git push origin How-to-use-Github` ;
4. 向原仓库提交 pr ; 