# Created by: Izram Khan
# Date Created: 27-Nov-2025
# Feel free to use and copy where you want. It's all yours
#____________________________________________________________________________________________________
import markdown
import os

def converter(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
            html_content = markdown.markdown(md_content)

            with open(output_file, 'w', encoding='utf-8') as html_file:
                html_file.write(html_content)

            print(f'Markdown file [{input_file}] converted to HTML file successfully!')

    except FileNotFoundError:
        print('\n❌ Error: File path does not exist')
    except Exception as e:
        print(f'\n❌ Error: {str(e)}')

if __name__ == '__main__':
    
    md_name = input('\nEnter the name of your MD file: ')
    md_file = os.path.abspath(md_name)

    html_name = input('\nEnter the name of your HTML file: ')
    html_file = os.path.abspath(html_name)

    converter(md_file, html_file)

#____________________________________________________________________________________________________