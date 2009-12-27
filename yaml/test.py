import yaml

handler = open('test.yaml')

print yaml.load(handler.read())
