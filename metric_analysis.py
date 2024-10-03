def get_passing_accuracy(df, half = 0):

    bad_passes = 0
    good_passes = 0
    total_passes = 0

    for x in range(len(df['id'])):
        if half != 0:

            if (df['period'].iloc[x] == half):

                if any([df['pass.outcome.name'].iloc[x] == "Incomplete",
                        df['pass.outcome.name'].iloc[x] == "Unknown",
                        df['pass.outcome.name'].iloc[x] == 'Injury Clearance',
                        df['pass.outcome.name'].iloc[x] == 'Out',
                        df['pass.outcome.name'].iloc[x] == 'Pass Offside']):
                    
                    bad_passes += 1
                else:
                    good_passes += 1
        else:

            if any([df['pass.outcome.name'].iloc[x] == "Incomplete",
                    df['pass.outcome.name'].iloc[x] == "Unknown",
                    df['pass.outcome.name'].iloc[x] == 'Injury Clearance',
                    df['pass.outcome.name'].iloc[x] == 'Out',
                    df['pass.outcome.name'].iloc[x] == 'Pass Offside']):
                    
                bad_passes += 1
            else:
                good_passes += 1

    total_passes = good_passes + bad_passes

    return round((good_passes / (good_passes + bad_passes)) * 100), total_passes, good_passes


def get_xg(df,half=0):
    xg = 0.0
    for x in range(len(df['id'])):
         
        if half == 0:
            if df['period'].iloc[x] != 5:
                xg += df['shot.statsbomb_xg'].iloc[x] # not including penalty shootout

        else:
            if df['period'].iloc[x] == half and half != 5: 
                xg += df['shot.statsbomb_xg'].iloc[x]

    return round(xg,2)

def get_shot_accuracy(df,half=0):
    num_shots = 0
    on_target = 0
    off_target = 0

    for x in range(len(df['id'])):

        if half == 0:
            if df['period'].iloc[x] != 5:
                num_shots += 1
                if df['shot.outcome.name'].iloc[x] == "Saved" or df['shot.outcome.name'].iloc[x] == "Goal":
                    on_target += 1
                else:
                    off_target += 1
        else:
            if df['period'].iloc[x] == half and half != 5: # not including the penalty shootout
                num_shots += 1
                if df['shot.outcome.name'].iloc[x] == "Saved" or df['shot.outcome.name'].iloc[x] == "Goal":
                    on_target += 1
                else:
                    off_target += 1
    return round((on_target / num_shots) * 100), num_shots, on_target, off_target
