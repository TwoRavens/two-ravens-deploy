"""Mongo commands"""

collections = ['acled_africa', 'acled_asia', 'acled_middle_east',
               'cline_phoenix_fbis', 'cline_phoenix_nyt', 'cline_phoenix_swb',
               'cline_speed', 'icews']

cnt = 0
for cname in collections:
    cnt+=1
    cmd1 = f'db.{cname}.drop()'
    cmd2 = f'mongorestore -u AdminEvent --port 17231  --authenticationDatabase admin -d event_data -c {cname} /home/eventuser/dbs/{cname}.bson'
    print('-' * 40)
    print(f'({cnt}) {cname}')
    print('-' * 40)
    print(cmd1)
    print('')
    print(cmd2)


if __name__ == '__main__':
    show_cmds()
