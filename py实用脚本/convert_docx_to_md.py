import docx
import pypandoc
# 注意改脚本仅支持后缀为.docx的文件若原来的文件为.doc请在word中另存为.docx文件
def get_heading_level(paragraph):
    # 获取段落的样式名
    style_name = paragraph.style.name
    # 根据样式名判断标题的层级
    if style_name.startswith('Heading 1'):
        return 1
    elif style_name.startswith('Heading 2'):
        return 2
    elif style_name.startswith('Heading 3'):
        return 3
    elif style_name.startswith('Heading 4'):
        return 4
    elif style_name.startswith('Heading 5'):
        return 5
    # 可根据需要添加更多层级的判断条件
    else:
        return None

def convert_docx_to_md(input_file, output_file):
    # 读取Word文档
    doc = docx.Document(input_file)

    # 遍历文档中的所有段落
    markdown_content = ''
    for para in doc.paragraphs:
        heading_level = get_heading_level(para)
        if heading_level is not None:
            # 添加相应数量的#，构成Markdown格式的标题
            heading_text = para.text.strip()
            markdown_content += f"{'#' * heading_level} {heading_text}\n\n"
        else:
            # 将普通文本直接添加到Markdown内容中
            markdown_content += para.text + '\n\n'

    # 将Markdown内容写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

if __name__ == '__main__':
    input_file_path = 'D:/考研/西哲史背诵-赵敦华_.doc'
    output_file_path = 'D:/考研/西哲史背诵.md'
    convert_docx_to_md(input_file_path, output_file_path)

