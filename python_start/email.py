emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
       'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
       'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff', ["jhjkhkh"]],
       'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
       'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
       'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
for i in emails:
    for j in emails[i]:
        if type(j).find('turple') != -1 or type(j).find('list') != -1:
            for k in j:
                print(f'{k}@{i}')
        else:
            print(f'{j}@{i}')