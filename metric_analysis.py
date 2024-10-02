def get_passing_accuracy(df, half):

    bad_passes = 0
    good_passes = 0

    for x in range(len(df['id'])):
        if (df['period'].iloc[x] == half):

            if any([df['pass.outcome.name'].iloc[x] == "Incomplete",
                    df['pass.outcome.name'].iloc[x] == "Unknown",
                    df['pass.outcome.name'].iloc[x] == 'Injury Clearance',
                    df['pass.outcome.name'].iloc[x] == 'Out',
                    df['pass.outcome.name'].iloc[x] == 'Pass Offside']):
                
                bad_passes += 1
            else:
                good_passes += 1

    return round((good_passes / (good_passes + bad_passes)) * 100) # successful pass percentage