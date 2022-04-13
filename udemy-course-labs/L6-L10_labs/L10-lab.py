projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

for projectName, leaderName in (zip(projects, leaders)):
    print('The leader of {} project is {}'.format(projectName, leaderName))

print()
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

prInfo = list(zip(projects,leaders, dates))
for projectName, leaderName, date in zip(projects, leaders, dates):
    print('The leader of {} project which was created on {} is {}'.format(projectName, date, leaderName))

for n, (projectName, leaderName, date) in list(enumerate(zip(projects, leaders, dates))):
    print('{} - The leader of {} project which was created on {} is {}'.format(n + 1, projectName, date, leaderName))