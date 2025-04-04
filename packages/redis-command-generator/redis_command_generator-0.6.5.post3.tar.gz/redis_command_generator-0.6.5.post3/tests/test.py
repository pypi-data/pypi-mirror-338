import redis_command_generator as cg

gen_runner = cg.GenRunner(hosts=("192.168.122.190:6379",), max_cmd_cnt=100, pipe_every_x=10, logfile="/tmp/bla.txt", verbose=True, maxmemory_bytes=10000000, flush=True)
gen_runner.start()
print(gen_runner.join())