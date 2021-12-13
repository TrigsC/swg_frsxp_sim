import logging
from os import kill
import numpy as np
import pandas as pd
import random
import string


frsExperienceValues = [
	['nonjedi_win', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	['nonjedi_lose', 1000, 1250, 1759, 2250, 3000, 3750, 4750, 5500, 6750, 7750, 8750, 10000],
	['bh_win', 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],
	['bh_lose', 1000, 1250, 1759, 2250, 3000, 3750, 4750, 5500, 6750, 7750, 8750, 10000],
	['padawan_win', 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
	['padawan_lose', 500, 650, 1000, 1250, 1750, 2250, 2750, 2350, 4000, 4500, 5000, 6000],
	['rank0_win', 750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750, 750],
	['rank0_lose', 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 3750, 4250, 5000, 5750],
	['rank1_win', 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900, 900],
	['rank1_lose', 100, 250, 500, 900, 1300, 1750, 2250, 2750, 3500, 4150, 4750, 5500],
	['rank2_win', 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250, 1250],
	['rank2_lose', 100, 250, 500, 900, 1300, 1750, 2250, 2750, 3500, 4150, 4750, 5500],
	['rank3_win', 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250, 2250],
	['rank3_lose', 100, 250, 500, 900, 1300, 1750, 2250, 2750, 3500, 4150, 4750, 5500],
	['rank4_win', 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000],
	['rank4_lose', 100, 250, 500, 900, 1300, 1750, 2250, 2750, 3500, 4150, 4750, 5500],
	['rank5_win', 3750, 3750, 3750, 3750, 3750, 3750, 3750, 3750, 3750, 3750, 3750, 3750],
	['rank5_lose', 100, 250, 500, 900, 1300, 1750, 2250, 2750, 3500, 4150, 4750, 5500],
	['rank6_win', 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500, 4500],
	['rank6_lose', 100, 250, 500, 900, 1300, 1750, 2250, 2750, 3500, 4150, 4750, 5500],
	['rank7_win', 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500, 5500],
	['rank7_lose', 100, 250, 500, 900, 1300, 1750, 2250, 2750, 3500, 4150, 4750, 5500],
	['rank8_win', 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500, 6500],
	['rank8_lose', 100, 250, 500, 900, 1300, 1750, 2250, 2750, 3500, 4150, 4750, 5500],
	['rank9_win', 7500, 7500, 7500, 7500, 7500, 7500, 7500, 7500, 7500, 7500, 7500, 7500],
	['rank9_lose', 100, 250, 500, 900, 1300, 1750, 2250, 2750, 3500, 4150, 4750, 5500],
	['rank10_win', 8750, 8750, 8750, 8750, 8750, 8750, 8750, 8750, 8750, 8750, 8750, 8750],
	['rank10_lose', 100, 250, 500, 900, 1300, 1750, 2250, 2750, 3500, 4150, 4750, 5500],
	['rank11_win', 9750, 9750, 9750, 9750, 9750, 9750, 9750, 9750, 9750, 9750, 9750, 9750],
	['rank11_lose', 100, 250, 500, 900, 1300, 1750, 2250, 2750, 3500, 4150, 4750, 5500]
]

frsRanks = [
    ['rm',0,0,0],
    ['s1',1,10000,100],
    ['s2',2,20000,200],
    ['s3',3,30000,300],
    ['s4',4,40000,400],
    ['c1',5,60000,500],
    ['c2',6,80000,600],
    ['c3',7,100000,700],
    ['a1',8,150000,800],
    ['a2',9,200000,900],
    ['cm',10,300000,1000],
    ['cl',11,500000,1100]
]

fieldnames=['name','isjedi','isnormie','isbh','winrate','rank','frsxp','faction','groupkills','solokills','deaths']
df = pd.DataFrame(columns=fieldnames)

FRS_XP_SPLIT = False

logging.basicConfig(filename='frsxp_audit.log', filemode='w', level=logging.DEBUG)


def generate_data(imperial_percent,rebel_percent,normies,jedi,bh_num):
    print('\nGenerating random player data...')
    imp_normies_num = round((int(imperial_percent) / 100) * normies)
    imp_jedi_num = round((int(imperial_percent) / 100) * jedi)
    reb_normies_num = round((int(rebel_percent) / 100) * normies)
    reb_jedi_num = round((int(rebel_percent) / 100) * jedi)

    letters = string.ascii_lowercase
    global df

    for ij in range(0, imp_jedi_num):
        df2 = {'name': ''.join(random.choice(letters) for i in range(10)), 'isjedi': 1, 'isnormie': 0, 'isbh': 0, 'winrate': random.randint(60,90),'rank': 0,'frsxp':0,'faction':1,'groupkills':0,'solokills':0,'deaths':0}
        df = df.append(df2, ignore_index = True)
    for i in range(0, imp_normies_num):
        df2 = {'name': ''.join(random.choice(letters) for i in range(10)), 'isjedi': 0, 'isnormie': 1, 'isbh': 0, 'winrate': random.randint(30,70),'rank': 0,'frsxp':0,'faction':1,'groupkills':0,'solokills':0,'deaths':0}
        df = df.append(df2, ignore_index = True)
    for rj in range(0, reb_jedi_num):
        df2 = {'name': ''.join(random.choice(letters) for i in range(10)), 'isjedi': 1, 'isnormie': 0, 'isbh': 0, 'winrate': random.randint(60,90),'rank': 0,'frsxp':0,'faction':2,'groupkills':0,'solokills':0,'deaths':0}
        df = df.append(df2, ignore_index = True)
    for r in range(0, reb_normies_num):
        df2 = {'name': ''.join(random.choice(letters) for i in range(10)), 'isjedi': 0, 'isnormie': 1, 'isbh': 0, 'winrate': random.randint(30,70),'rank': 0,'frsxp':0,'faction':2,'groupkills':0,'solokills':0,'deaths':0}
        df = df.append(df2, ignore_index = True)
    for b in range(0, bh_num):
        df2 = {'name': ''.join(random.choice(letters) for i in range(10)), 'isjedi': 0, 'isnormie': 0, 'isbh': 1, 'winrate': random.randint(40,80),'rank': 0,'frsxp':0,'faction':0,'groupkills':0,'solokills':0,'deaths':0}
        df = df.append(df2, ignore_index = True)

    reb_normies = df.loc[(df['faction'] == 2) & (df['isnormie'] == 1)]
    imp_normies = df.loc[(df['faction'] == 1) & (df['isnormie'] == 1)]
    all_bh = df.loc[df['isbh'] == 1]
    reb_jedi = df.loc[(df['faction'] == 2) & (df['isjedi'] == 1)]
    imp_jedi = df.loc[(df['faction'] == 1) & (df['isjedi'] == 1)]
    print('Player Data Generated!\n')
    return imp_jedi_num,imp_jedi,imp_normies_num,imp_normies,reb_jedi_num,reb_jedi,reb_normies_num,reb_normies,all_bh

def get_1v1(imp_jedi_num,imp_jedi,reb_jedi_num,reb_jedi):
    imp_won = False
    reb_won = False
    killtype = 'solo'
    imp_num = random.randint(1, imp_jedi_num)
    chosen_1_imp_idx = np.random.choice(imp_num)

    imp_1 = imp_jedi.iloc[lambda imp_jedi: [chosen_1_imp_idx], :]

    reb_num = random.randint(1, reb_jedi_num)
    chosen_1_reb_idx = np.random.choice(reb_num)
    reb_1 = reb_jedi.iloc[lambda reb_jedi: [chosen_1_reb_idx], :]

    imp_rate = imp_1.iloc[0]['winrate']
    reb_rate = reb_1.iloc[0]['winrate']
    if random.randint(0,100) < imp_rate:
        imp_won = True
    if random.randint(0,100) < reb_rate:
        reb_won = True
    
    if imp_won == True & reb_won == True:
        pass
    elif imp_won == True:
        decrease_jedi_xp(reb_1,imp_1)
        increase_jedi_xp(imp_1,reb_1,killtype)
    elif reb_won == True:
        decrease_jedi_xp(imp_1,reb_1)
        increase_jedi_xp(reb_1,imp_1,killtype)
    else:
        pass
    pass

def bh_fight(imp_jedi,reb_jedi,all_bh):
    jedi_won = False
    bh_won = False
    killtype = 'bh'
    jedi = imp_jedi.append(reb_jedi, ignore_index = True)
    amt_jedi = len(jedi.index)
    amt_bh = len(all_bh.index)
    jedi_num = random.randint(1, amt_jedi)
    chosen_1_jedi_idx = np.random.choice(jedi_num)

    jedi_1 = jedi.iloc[lambda jedi: [chosen_1_jedi_idx], :]

    bh_num = random.randint(1, amt_bh)
    chosen_1_bh_idx = np.random.choice(bh_num)
    bh_1 = all_bh.iloc[lambda all_bh: [chosen_1_bh_idx], :]

    jedi_rate = jedi_1.iloc[0]['winrate']
    bh_rate = bh_1.iloc[0]['winrate']
    if random.randint(0,100) < jedi_rate:
        jedi_won = True
    if random.randint(0,100) < bh_rate:
        bh_won = True
    
    if jedi_won == True & bh_won == True:
        pass
    elif jedi_won == True:
        increase_jedi_xp(jedi_1,bh_1,killtype)
    elif bh_won == True:
        decrease_jedi_xp(jedi_1,bh_1)
    else:
        pass
    pass

def get_groups(imp_jedi_num,imp_jedi,imp_normies_num,imp_normies,reb_jedi_num,reb_jedi,reb_normies_num,reb_normies):
    imp_jedi_active = random.randint(1, imp_jedi_num)
    chosen_imp_jedi_idx = np.random.choice(imp_jedi_num, replace=False, size=imp_jedi_active)
    imp_jedi_trimmed = imp_jedi.iloc[chosen_imp_jedi_idx]

    reb_jedi_active = random.randint(1, reb_jedi_num)
    chosen_reb_jedi_idx = np.random.choice(reb_jedi_num, replace=False, size=reb_jedi_active)
    reb_jedi_trimmed = reb_jedi.iloc[chosen_reb_jedi_idx]

    if imp_normies_num > 0:
        imp_normies_active = random.randint(1, imp_normies_num)
        chosen_imp_normies_idx = np.random.choice(imp_normies_num, replace=False, size=imp_normies_active)
        imp_normies_trimmed = imp_normies.iloc[chosen_imp_normies_idx]
        
    else:
        imp_normies_trimmed = pd.DataFrame(columns = fieldnames)
        imp_normies_active = 0
    total_active_imp = imp_jedi_active + imp_normies_active

    if reb_normies_num > 0:
        reb_normies_active = random.randint(1, reb_normies_num)
        chosen_reb_normies_idx = np.random.choice(reb_normies_num, replace=False, size=reb_normies_active)
        reb_normies_trimmed = reb_normies.iloc[chosen_reb_normies_idx]
    else:
        reb_normies_trimmed = pd.DataFrame(columns = fieldnames)
        reb_normies_active = 0
    total_active_reb = reb_jedi_active + reb_normies_active

    return imp_jedi_trimmed, imp_normies_trimmed, reb_jedi_trimmed, reb_normies_trimmed, total_active_imp, total_active_reb

def pick_fighters(imp_jedi_trimmed, imp_normies_trimmed, reb_jedi_trimmed, reb_normies_trimmed,total_active_imp,total_active_reb):

    imps = imp_jedi_trimmed.append(imp_normies_trimmed, ignore_index = True)
    imps_infight_num = random.randint(1, total_active_imp)
    chosen_imp_idx = np.random.choice(total_active_imp, replace=False, size=imps_infight_num)
    imp_trimmed = imps.iloc[chosen_imp_idx]

    rebs = reb_jedi_trimmed.append(reb_normies_trimmed, ignore_index = True)
    rebs_infight_num = random.randint(1, total_active_reb)
    chosen_reb_idx = np.random.choice(total_active_reb, replace=False, size=rebs_infight_num)
    reb_trimmed = rebs.iloc[chosen_reb_idx]
    return imps_infight_num,imp_trimmed,rebs_infight_num,reb_trimmed

def run_fight(imps_infight_num,imp_trimmed,rebs_infight_num,reb_trimmed):
    killtype = 'group'
    imp_fighters_winrate = imp_trimmed['winrate'].sum()
    reb_fighters_winrate = reb_trimmed['winrate'].sum()

    if imp_fighters_winrate > reb_fighters_winrate:
        imp_won = True
        reb_num = random.randint(1, rebs_infight_num)
        chosen_1_reb_idx = np.random.choice(reb_num)
        reb_1_dead = reb_trimmed.iloc[lambda reb_trimmed: [chosen_1_reb_idx], :]

        reb_dead_name = reb_1_dead.iloc[0]['name']
        imp_num = random.randint(1, imps_infight_num)
        chosen_1_imp_idx = np.random.choice(imp_num)
        imp_1_winner = imp_trimmed.iloc[lambda imp_trimmed: [chosen_1_imp_idx], :]
        imp_jedi_winners = imp_trimmed.loc[imp_trimmed['isjedi'] == 1]
        if reb_1_dead.iloc[0]['isjedi'] == 1:
            decrease_jedi_xp(reb_1_dead,imp_1_winner)
            if len(imp_jedi_winners.index) >= 1:
                increase_jedi_xp(imp_jedi_winners,reb_1_dead,killtype)
            reb_trimmed = reb_trimmed.loc[reb_trimmed["name"] != reb_dead_name]
        else:
            reb_trimmed = reb_trimmed.loc[reb_trimmed["name"] != reb_dead_name]
        rebs_infight_num -= 1
    else:
        reb_won = True
        imp_num = random.randint(1, imps_infight_num)
        chosen_1_imp_idx = np.random.choice(imp_num)
        imp_1_dead = imp_trimmed.iloc[lambda imp_trimmed: [chosen_1_imp_idx], :]
        imp_dead_name = imp_1_dead.iloc[0]['name']
        reb_num = random.randint(1, rebs_infight_num)
        chosen_1_reb_idx = np.random.choice(reb_num)
        reb_1_winner = reb_trimmed.iloc[lambda reb_trimmed: [chosen_1_reb_idx], :]
        reb_jedi_winners = reb_trimmed.loc[reb_trimmed['isjedi'] == 1]
        if imp_1_dead.iloc[0]['isjedi'] == 1:
            decrease_jedi_xp(imp_1_dead,reb_1_winner)
            if len(reb_jedi_winners.index) >= 1:
                increase_jedi_xp(reb_jedi_winners,imp_1_dead,killtype)
            imp_trimmed = imp_trimmed.loc[imp_trimmed["name"] != imp_dead_name]
        else:
            imp_trimmed = imp_trimmed.loc[imp_trimmed["name"] != imp_dead_name]
        imps_infight_num -= 1
    return imps_infight_num,imp_trimmed,rebs_infight_num,reb_trimmed

def increase_jedi_xp(jedi_winners,dead_jedi,killtype):
    global FRS_XP_SPLIT
    global df
    dead_jedi_name = dead_jedi.iloc[0]['name']
    if killtype == 'bh':
        dead_jedi_rank = 'bh_win'
    else:
        dead_jedi_rank_num = df.loc[df['name'] == dead_jedi_name, 'rank'].iloc[0]
        dead_jedi_rank = 'rank' + str(dead_jedi_rank_num) + '_win'
    num_winners = len(jedi_winners.index)
    for winner in jedi_winners.itertuples():
        winner_name = winner.name
        winner_old_frsxp = df.loc[df['name'] == winner_name, 'frsxp'].iloc[0]
        winner_rank_num = df.loc[df['name'] == winner_name, 'rank'].iloc[0]
        check_rank(winner_name, winner_old_frsxp, winner_rank_num)
        winner_rank = winner_rank_num + 1
        
        for ranks in frsExperienceValues:
                if ranks[0] == dead_jedi_rank:
                    winner_xp_gain = ranks[winner_rank]
                    break
        if FRS_XP_SPLIT == True:
            winner_frsxp = (winner_xp_gain / num_winners) + winner_old_frsxp
        else:
            winner_frsxp = winner_xp_gain + winner_old_frsxp
        df.loc[df['name'] == winner_name, 'frsxp'] = winner_frsxp
        if killtype == 'solo':
            logging.info('SOLO KILL: {} (Rank {}) killed {} (Rank {}). Old XP {}, Gained XP {}, Current XP {}'.format(winner_name,winner_rank_num,dead_jedi_name,dead_jedi_rank_num,winner_old_frsxp,winner_xp_gain,winner_frsxp))
            df.loc[df['name'] == winner_name, 'solokills'] = df.loc[df['name'] == winner_name, 'solokills'] + 1
        elif killtype == 'bh':
            logging.info('BH KILLED: {} (Rank {}) killed {} (a BH). Old XP {}, Gained XP {}, Current XP {}'.format(winner_name,winner_rank_num,dead_jedi_name,winner_old_frsxp,winner_xp_gain,winner_frsxp))
            df.loc[df['name'] == winner_name, 'solokills'] = df.loc[df['name'] == winner_name, 'solokills'] + 1
        else:
            if FRS_XP_SPLIT == True:
                logging.info('GROUP KILL: {} (Rank {}) helped kill {} (Rank {}). Old XP {}, Gained {}, New XP {}'.format(winner_name,winner_rank_num,dead_jedi_name,dead_jedi_rank_num,winner_old_frsxp,(winner_xp_gain / num_winners),winner_frsxp))
            else:
                logging.info('GROUP KILL: {} (Rank {}) helped kill {} (Rank {}). Old XP {}, Gained {}, New XP {}'.format(winner_name,winner_rank_num,dead_jedi_name,dead_jedi_rank_num,winner_old_frsxp,winner_xp_gain,winner_frsxp))
            df.loc[df['name'] == winner_name, 'groupkills'] = df.loc[df['name'] == winner_name, 'groupkills'] + 1

def check_rank(winner_name, winner_frsxp, winner_rank):
    next_rank = winner_rank + 1
    if next_rank == 12:
        next_rank = 11
    for rank_amt in frsRanks:
        if rank_amt[1] == next_rank:
            if rank_amt[2] < winner_frsxp:
                df.loc[df['name'] == winner_name, 'rank'] = next_rank
            else:
                break


def decrease_jedi_xp(loser,winner):
    global df
    loser_xp_loss = 0
    loser_name = loser.iloc[0]['name']
    loser_old_frsxp = df.loc[df['name'] == loser_name, 'frsxp'].iloc[0]
    loser_rank_num = df.loc[df['name'] == loser_name, 'rank'].iloc[0]
    loser_rank = loser_rank_num + 1
    winner_name = winner.iloc[0]['name']

    isnormie = winner.iloc[0]['isnormie']
    isbh = winner.iloc[0]['isbh']
    isjedi = winner.iloc[0]['isjedi']
    
    if isnormie == 1:
        winner_rank = 'nonjedi_lose'
        deathby = 'a Non-Jedi'
    elif isjedi == 1:
        winner_rank = df.loc[df['name'] == winner_name, 'rank'].iloc[0]
        deathby = 'Rank {}'.format(winner_rank)
        winner_rank = 'rank' + str(winner_rank) + '_lose'
    elif isbh == 1:
        deathby = 'a BH'
        winner_rank = 'bh_lose'
    else: pass
    for ranks in frsExperienceValues:
            if ranks[0] == winner_rank:
                loser_xp_loss = ranks[loser_rank]
                break
    if loser_xp_loss > loser_old_frsxp:
        loser_frsxp = 0
    else:
        loser_frsxp = loser_old_frsxp - loser_xp_loss
    logging.info('DEATH: {} ({}) DB\'ed {} (Rank {}). Old XP {}, Lost XP {}, Current XP {}'.format(winner_name,deathby,loser_name,loser_rank_num,loser_old_frsxp,loser_xp_loss,loser_frsxp))
    df.loc[df['name'] == loser_name, 'frsxp'] = loser_frsxp
    df.loc[df['name'] == loser_name, 'deaths'] = df.loc[df['name'] == loser_name, 'deaths'] + 1
    
    pass

def get_battle_ratio(total_active_reb,total_active_imp):
    if total_active_reb == 0 or total_active_imp == 0:
        return True
    if total_active_reb > total_active_imp:
        #more_rebs = True
        battle_ratio = total_active_reb / total_active_imp
    else:
        #more_imps = True
        battle_ratio = total_active_imp / total_active_reb
    
    rand_rate = random.randint(0,100)

    ## Disengage battle ratio
    if battle_ratio >= 4.0:
        if rand_rate < 95:
            return True
    elif battle_ratio >= 3.0:
        if rand_rate < 85:
            return True
    elif battle_ratio >= 2.0:
        if rand_rate < 60:
            return True
    elif battle_ratio >= 1.5:
        if rand_rate < 30:
            return True
    else:
        return False

def run_battle(imp_jedi_trimmed, imp_normies_trimmed, reb_jedi_trimmed, reb_normies_trimmed,total_active_imp, total_active_reb):
    run_from_battle = False
    run_from_fight = False
    imps_infight_num = total_active_imp
    rebs_infight_num = total_active_reb
    while run_from_battle == False:
        total_active_imp = total_active_imp - (total_active_imp - imps_infight_num)
        total_active_reb = total_active_reb - (total_active_reb - rebs_infight_num)
        run_from_battle = get_battle_ratio(total_active_imp,total_active_reb)
        if run_from_battle == True or run_from_battle == None:
            # decides to run from fight
            break
        run_from_fight = False
        imps_infight_num,imp_trimmed,rebs_infight_num,reb_trimmed = pick_fighters(imp_jedi_trimmed, imp_normies_trimmed, reb_jedi_trimmed, reb_normies_trimmed,total_active_imp,total_active_reb)
        while run_from_fight == False:
            
            run_from_fight = False
            run_from_fight = get_battle_ratio(rebs_infight_num,imps_infight_num)
            if run_from_fight == True or run_from_fight == None:
                # decides to run from fight
                continue
        #Fighting
            imps_infight_num,imp_trimmed,rebs_infight_num,reb_trimmed = run_fight(imps_infight_num,imp_trimmed,rebs_infight_num,reb_trimmed)

def frs_xp_decision(split_xp):
    split_xp.lower()
    if split_xp == 'no' or split_xp == 'false' or split_xp == 'f':
        FRS_XP_SPLIT = False
        return FRS_XP_SPLIT
    else:
        FRS_XP_SPLIT = True
        return FRS_XP_SPLIT

# Print iterations progress
def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iterable    - Required  : iterable object (Iterable)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    # Print New Line on Complete
    print()

def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Must be a whole number! Try again.\n")
       continue
    else:
       return userInput 
       break

if __name__=="__main__":
    
    print('Let\'s start out with some information about our scenario.\n')
    jedi = inputNumber('How many Ranked Jedi are there? ')
    normies = inputNumber('How many Non-Jedi PVP players are there? ')
    bh = inputNumber('How many Bounty Hunters are there? ')
    split_xp = input('Do you want to split frsxp? ')
    FRS_XP_SPLIT = frs_xp_decision(split_xp)
    jedi = int(jedi)
    normies = int(normies)
    bh_num = int(bh)
    total_players = jedi + normies + bh_num
    imperial_percent = inputNumber('What percent are Imperial? ')
    rebel_percent = 100 - int(imperial_percent)

    simulated_battles = inputNumber('How many battles would you like to run? ')
    simulated_battles = int(simulated_battles)

    imp_jedi_num,imp_jedi,imp_normies_num,imp_normies,reb_jedi_num,reb_jedi,reb_normies_num,reb_normies,all_bh = generate_data(imperial_percent,rebel_percent,normies,jedi,bh_num)
    i = 0
    items = list(range(i,simulated_battles))
    print('Simulating...\n')
    for item in progressBar(items, prefix = 'Progress:', suffix = 'Complete', length = 50):
        if i % 3 == 0:
            logging.info('NEW 1V1:')
            get_1v1(imp_jedi_num,imp_jedi,reb_jedi_num,reb_jedi)
        elif i % 5 == 0:
            logging.info('NEW BH FIGHT:')
            bh_fight(imp_jedi,reb_jedi,all_bh)
        else:
            logging.info('NEW GROUP FIGH:')
            imp_jedi_trimmed, imp_normies_trimmed, reb_jedi_trimmed, reb_normies_trimmed, total_active_imp, total_active_reb = get_groups(
                imp_jedi_num,imp_jedi,imp_normies_num,imp_normies,reb_jedi_num,reb_jedi,reb_normies_num,reb_normies)

            run_battle(imp_jedi_trimmed, imp_normies_trimmed, reb_jedi_trimmed, reb_normies_trimmed, total_active_imp, total_active_reb)
        i += 1
    print('\nCreating battle_data.csv')
    df.to_csv('frsxp_data.csv', sep=',', encoding='utf-8', index=False, header=True, columns=fieldnames)
    print('Simulation Complete!')
