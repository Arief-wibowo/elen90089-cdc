import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """MAC Controller: Allows transmission only when PU is idle (control = 0)"""

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='MAC Controller',
            in_sig=[np.complex64, np.float32],
            out_sig=[np.complex64]
        )

    def work(self, input_items, output_items):
        su_data = input_items[0]       # Secondary user data stream
        control_signal = input_items[1]  # Energy detection (0 = idle, 1 = busy)
        output = output_items[0]

        # Basic MAC logic: if all control samples = 0, allow SU transmission
        if np.all(control_signal == 0.0):
            output[:] = su_data
        else:
            output[:] = np.zeros(len(su_data), dtype=np.complex64)

        return len(output)

