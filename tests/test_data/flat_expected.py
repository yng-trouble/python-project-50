expected_result = '''- proxy: 123.234.53.22
- follow: False
- timeout: 50
+ timeout: 20
+ verbose: True
host: hexlet.io
'''

parsed1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}

parsed2 = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}