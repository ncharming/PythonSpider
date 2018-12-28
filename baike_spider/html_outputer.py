class HtmlOutput(object):

    def __init__(self):
        self.datas = []

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)
    # 将收集好的数据输出到 html 文件中

    def output_html(self):
        fout = open('outpur.html', 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<a>')
        for data in self.datas:
            fout.write('<a href="%s">%s</a>' % (data['url'], data['title']))
            fout.write('<p>%s</p>' % data['summary'])

        fout.write('</a>')
        fout.write('</body>')
        fout.write('</html>')
        fout.close()
