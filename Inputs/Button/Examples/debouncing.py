from PiicoDev_Switch import PiicoDev_Switch
from PiicoDev_Unified import sleep_ms

button = PiicoDev_Switch(ema_parameter=73, ema_period=30)  # Initialise the module with 30ms poll period and EMA parameter = 73.0/255.0 => 0.286