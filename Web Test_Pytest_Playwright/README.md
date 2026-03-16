怎么把代码变成 Playwright 能懂的“地址”？
B站的登录页面很有代表性，你会发现它通常有这几种“地址”写法：

1. 通过 ID 定位（最稳、首选）
如果你看到代码里有 id="login-username" 这样的字样：

写法： page.fill("#login-username", "你的账号")

规则： ID 前面要加个 # 号。

2. 通过 Placeholder 定位（最直观）
B站的框里通常写着“请输入手机号或邮箱”：

写法： page.get_by_placeholder("请输入手机号或邮箱")

优点： 就像真人操作一样，看着什么填什么。

3. 通过 Class 定位（备选）
如果你看到 class="input-box"：

写法： page.fill(".input-box", "你的账号")

规则： Class 前面要加个 . 号。