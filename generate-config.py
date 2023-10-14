import json
import tomlkit
import datetime
import sys
import os


def generate(meta_path, destination):
  with open(meta_path, 'r') as f:
    data = json.load(f)

  doc = tomlkit.document()

  doc['enabled'] = True
  doc['include'] = ['.']
  doc['dll'] = data.get('binaries')

  doc.add(tomlkit.nl())

  doc['name'] = data.get('name', 'My Mod')
  doc['description'] = data.get('description', '')

  version_data = list(map(str, data.get('version', [1, 0, 0])))
  doc['version'] = '.'.join(version_data[:3]) + ('-' if len(version_data) > 3 else '') + '-'.join(version_data[3:])

  doc['date'] = datetime.date.today().strftime("%d.%m.%Y")
  doc['author'] = ', '.join(data.get('authors'))

  with open(destination, 'w') as f:
    f.write(doc.as_string())


if __name__ == '__main__':
  meta_path = sys.argv[1] if len(sys.argv) > 1 else 'meta.json'
  config_path = sys.argv[2] if len(sys.argv) > 2 else 'config.toml'
  generate(meta_path, config_path)
