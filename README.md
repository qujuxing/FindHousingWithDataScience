# FindHousingWithDataScienc

重构了Stephen Hsu的[Speeding up the Housing Search in San Francisco with Data Science](https://towardsdatascience.com/how-to-find-housing-in-san-francisco-with-data-science-2991ff503602)

碰到了不少问题，查资料安装了python3,selenium,BeautifulSoup,Jupyter,pip3，对照作者的思路和源码从头学习语法调试框架，对照错误提示，修正原文的语法错误。这里感谢Google翻译，原文翻译的很精确，对照原文错误很少。也感谢崔庆才老师，他的[《Python3网络爬虫开发实战》](https://germey.gitbooks.io/python3webspider/)让我对基础有系统的理解。

其中python3中不能解析加密链接的问题，在上下文排查了很久，才发现是urllib库中的导入ssl库来处理，感谢StackOverFlow，找到了正确的解决方法。

还有一部分问题未解决：
* pandas和numpy库的用法 
* 怎么使用Jupyter库将最终结果显示在浏览器中，现在结果还只能在终端显示 
 --- 想复杂了，只要在终端输入 jupyter notebook打开notebook，在file中新建一个python3程序，将craig_list.py的源码输入运行就可以生成原作者所见的表。
