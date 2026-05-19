#!/usr/bin/env python3
"""
add_edit_buttons.py
Inyecta <script src="/edit-btn.js"></script> en todos los cancion/{slug}/index.html
del web repo de aleguitarra.

Uso:
    python3 add_edit_buttons.py /ruta/al/web-repo

El script es idempotente: si ya tiene el script, no lo agrega de nuevo.
"""

import os, sys

SNIPPET = '<script src="/edit-btn.js"></script>'

def process(web_root):
    cancion_dir = os.path.join(web_root, 'cancion')
    if not os.path.isdir(cancion_dir):
        print(f"ERROR: no se encuentra {cancion_dir}")
        sys.exit(1)

    modified = 0
    skipped = 0
    errors = 0

    for slug in os.listdir(cancion_dir):
        html_path = os.path.join(cancion_dir, slug, 'index.html')
        if not os.path.isfile(html_path):
            continue
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if SNIPPET in content:
                skipped += 1
                continue

            # Inject before </body>
            if '</body>' in content:
                new_content = content.replace('</body>', f'{SNIPPET}\n</body>', 1)
            elif '</html>' in content:
                new_content = content.replace('</html>', f'{SNIPPET}\n</html>', 1)
            else:
                new_content = content + '\n' + SNIPPET

            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            modified += 1

        except Exception as e:
            print(f"  ERROR {slug}: {e}")
            errors += 1

    print(f"Done: {modified} modificados, {skipped} ya tenían el botón, {errors} errores")

if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    process(root)
