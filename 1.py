import json

print('hello')
print('a')


with open('C:\KockpitStudio\ETLJobs\test.json') as f:
  data = json.load(f)

# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)