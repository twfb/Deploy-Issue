# DeployIssue

# 干啥的?

通过脚本在现有的博客中添加, Issue自动生成/更新/删除博客文章功能

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

- 写了个通过get发送post请求, 可以直接在markdown里执行action, 不过会暴露token,私人仓库用还不错, 后来想了想好处也就是不用登录直接调用, 没卵用
