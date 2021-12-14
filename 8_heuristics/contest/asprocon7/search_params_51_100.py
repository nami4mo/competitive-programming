import optuna
import os
import subprocess


def objective(trial):
    # temp_start = trial.suggest_float("temp_start", 1e-3, 1., log=True)
    # temp_end = trial.suggest_float("temp_end", 1e-7, 1e-4, log=True)
    # square = trial.suggest_int("square", 0, 1024)
    # shrink = trial.suggest_int("shrink", 0, 1024)

    mini_part = trial.suggest_int("mini_part", 10, 100)
    temp_start = trial.suggest_float("temp_start", 10., 500., log=True)
    temp_end = trial.suggest_float("temp_end", 1., 50., log=True)
    mini_rate = trial.suggest_float("first_mini_rate", 0.5, 0.99, log=False)

    args = ['sh', 'test_params.sh', '51', '100', str(mini_part), str(temp_start), str(temp_end), str(mini_rate)]
    res = subprocess.check_output(args)
    return int(res)

study = optuna.create_study(
    study_name="asprocon7_0811_51_100_v3",
    storage="sqlite:///db.sqlite3",
    load_if_exists=True,
    direction="maximize"
)
study.optimize(objective, n_trials=100)