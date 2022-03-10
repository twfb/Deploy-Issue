# DeployIssue

# 干啥的?
通过Issue自动生成/更新/删除博客文章

# 咋用?

1. `git clone https://github.com/twfb/DeployIssue.git`
2. 将`deploy_issue.py`放入自己的博客目录
3. 参考`example.yml`编辑 自己部署博客的yml文件
4. 添加Actions secrets
  - `TOKEN`: github token
5. 尝试写一个issue
  - title: 文件名, 将生成`title.md`文件
  - labels: `unpublished`: 删除, `published`:发布
6. 有问题提issue, 看到必解答, 回的慢不要骂我
