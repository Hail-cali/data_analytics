from key.login import serverKey
from com.Dbsys import DBsysyem
import matplotlib.pyplot as plt
plt.style.use('seaborn')

if __name__ == '__main__':

    key = serverKey('mimic')
    system = DBsysyem(db_name='mimiciv', login=key.login)

    comd = 'select * from d_items'
    comd2 = '''select *   from icustays
                where subject_id in (
                    select admissions.subject_id from admissions
                    where (deathtime is not null)
                    and (dischtime-admissions.admittime)<=3
            );'''

    df = system.run(comd2)
    print(df)
    dm = system.run(comd)


