import config
import math
def current_speed(current_loop):
    lam = (1 / config.config.target_loops) * math.log(config.config.max_speed/ config.config.min_speed)
    return config.config.max_speed* math.exp(-lam * current_loop)

