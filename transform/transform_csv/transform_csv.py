import csv
import string

def transform():
    filename = raw_input( 'Enter file name: ' )
    filename_txt = filename + '.txt'
    filename_csv = filename + '.csv'
    f = open( filename_txt, 'r' )
    context = f.readline()
    rowSet = context.split('"rowSet"', 1)

    items = rowSet[1].split(',')
    with open(filename_csv, 'wb') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        attribut = ["SEASON_ID","TEAM_ID","TEAM_ABBREVIATION","TEAM_NAME","GAME_ID","GAME_DATE","MATCHUP","WL","MIN","FGM","FGA","FG_PCT","FG3M","FG3A","FG3_PCT","FTM","FTA","FT_PCT","OREB","DREB","REB","AST","STL","BLK","TOV","PF","PTS","PLUS_MINUS","VIDEO_AVAILABLE"]

        writer.writerow(attribut)
        cnt, lst = 0, []
        for item in items:
            item = string.replace(item, '[', '')
            item = string.replace(item, ']', '')
            item = string.replace(item, ':', '')
            item = string.replace(item, '"', '')
            #print item
            lst = lst + [item]
            cnt += 1
            if cnt == 29:
                writer.writerow(lst)
                cnt, lst = 0, []

'''
i, j = 1984, 85
while i < 2015:
    filename = 'PlayersGameLogs_'
    if j == 100:
        i, j = 2009, 10
    time1, time2 = str(i), str(j)

    filename = filename + time1 + '-' + time2
    #print filename
    i += 1
    j += 1

    transform(filename)
'''
transform()