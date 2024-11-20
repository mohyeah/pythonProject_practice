import wx

# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
    def __init__(self):
        try:
            super().__init__(None, title="first wxpython exe!", size=(400, 300), pos=(100, 100))
            self.init_ui()
        except Exception as e:
            raise

    def init_ui(self):
        # 创建一个面板
        panel = wx.Panel(parent=self)
        # 使用布局管理器
        sizer = wx.BoxSizer(wx.VERTICAL)
        # 创建静态文本
        self.static_text = wx.StaticText(parent=panel, label="hello world")
        sizer.Add(self.static_text, 0, wx.ALL, 10)

        # 创建一个按钮
        b = wx.Button(parent=panel, label="click me")
        b.Bind(wx.EVT_BUTTON, self.on_click)
        sizer.Add(b, 0, wx.ALL, 10)

        # 设置面板的布局
        panel.SetSizer(sizer)

    def on_click(self, event):
        self.static_text.SetLabel("Button clicked!")

    def OnClose(self, event):
        # 释放资源
        self.Destroy()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
