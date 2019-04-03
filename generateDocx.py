from docx import Document
from docx.shared import Inches, RGBColor, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
import database

document = Document()

# heading = document.add_heading(level=0)
heading = document.add_paragraph()
h1 = heading.add_run('\n\n露天采场矿岩与品位信息报告\n\n\n')
h1.font.color.rgb = RGBColor(0, 0, 0)  # 黑色
h1.font.size = Pt(24)  # 一号字体
h1.bold = True

# https://www.cnblogs.com/apple2016/p/9635061.html
# https://blog.csdn.net/wuxiyue238/article/details/81085137
h1.font.name = u'宋体'
h1._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
document.styles['Normal'].font.name = u'宋体'  # 修改正文的中文字体类型
document.styles['Normal'].font.size = Pt(14)  # 修改正文的中文字体类型
document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
heading.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER  # 居中
# heading.paragraph_format.left_indent = Inches(0) # 左缩进
heading.paragraph_format.space_before = Pt(0)  # 上行间距
# heading.paragraph_format.space_after = Pt(0) # 下行间距
heading.paragraph_format.line_spacing = 1  # 单倍行距

p1 = document.add_paragraph()
p1.add_run('使用单位：').font.size = Pt(14)
p1.add_run('          '+'haha'+'         .').font.underline = True
p1.paragraph_format.first_line_indent = Inches(1)
# p1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
# p1.paragraph_format.space_after = Pt(0) # 下行间距

p2 = document.add_paragraph()
p2.add_run('设备名称：').font.size = Pt(14)
p2.add_run('          '+'沈抚支线管道1'+'         .').font.underline = True
p2.paragraph_format.first_line_indent = Inches(1)

p3 = document.add_paragraph()
p3.add_run('设备类别：').font.size = Pt(14)
p3.add_run('          '+'长输管道'+'         .').font.underline = True
p3.paragraph_format.first_line_indent = Inches(1)

p4 = document.add_paragraph()
p4.add_run('设备品种：').font.size = Pt(14)
p4.add_run('          '+'天然气管道'+'         .').font.underline = True
p4.paragraph_format.first_line_indent = Inches(1)

p5 = document.add_paragraph()
p5.add_run('压力管道代码：').font.size = Pt(14)
p5.add_run('          '+'81201'+'         .').font.underline = True
p5.paragraph_format.first_line_indent = Inches(1)

p6 = document.add_paragraph()
p6.add_run('检验日期：').font.size = Pt(14)
p6.add_run('          '+'2019.04.03'+'         .').font.underline = True
p6.paragraph_format.first_line_indent = Inches(1)

p7 = document.add_paragraph('\n\n\n\n\n')

p8 = document.add_paragraph()
p8.add_run('东北大学软件学院').font.size = Pt(14)
p8.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER  # 居中

document.save('/Users/skye/Desktop/demo1.docx')