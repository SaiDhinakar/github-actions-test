with open('https://github.com/SaiDhinakar/github-actions-test/blob/main/logs.txt', 'a') as f:
    f.write('[INFO] Someone pushed their code on the repo\n')
f.close()
print("Log entries added successfully.")