#!/usr/bin/env python3
import os
import shutil


def main():
    benises = {
        'default': {
            'music_src': 'https://www.youtube.com/watch?v=zkmB-oKL1d0',
        },
        '8bit': {
            'music_src': 'https://www.youtube.com/watch?v=IQflTntEPEM',
        }
    }

    with open('template.html') as f:
        template = f.read()

    os.makedirs('output', exist_ok=True)

    for i, (benis_name, benis) in enumerate(benises.items(), start=1):
        html = template
        html = html.replace('%benis%', benis_name)
        html = html.replace('%music_src%', benis['music_src'])

        if i == 1:
            filename = 'index.html'
        else:
            filename = f'{i}.html'

        filepath = os.path.join('output', filename)

        with open(filepath, 'w') as f:
            f.write(html)

        print(f"wrote {filepath}")

    print("copying assets")
    shutil.copy('style.css', 'output/style.css')
    shutil.copytree('img', 'output/img', dirs_exist_ok=True)
    shutil.copytree('mus', 'output/mus', dirs_exist_ok=True)


if __name__ == '__main__':
    main()
