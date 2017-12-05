import psutil

for pidIndex in psutil.pids():
    p = psutil.Process(pidIndex)
    print(p.name(), pidIndex)