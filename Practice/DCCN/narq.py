# import random
# import time

# TOTAL_FRAMES = 10
# WINDOW_SIZE = 4
# LOSS_PROBABILITY = 0.2


# def go_back_n():

#     base = 0
#     expected = 0

#     print("===== GO-BACK-N ARQ =====")

#     while base < TOTAL_FRAMES:

#         next_seq = base
#         window_end = min(base + WINDOW_SIZE, TOTAL_FRAMES)

#         # Send frames in the current window
#         while next_seq < window_end:

#             print(f"\nSending Frame {next_seq}")

#             if random.random() < LOSS_PROBABILITY:
#                 print(f"Frame {next_seq} LOST!")

#             elif next_seq == expected:
#                 print(f"Receiver accepted Frame {next_seq}")
#                 expected += 1
#                 base = expected
#                 print(f"Cumulative ACK {base} received")

#             else:
#                 print(f"Frame {next_seq} discarded (out of order)")
#                 print(f"Duplicate ACK {expected} received")

#             next_seq += 1
#             time.sleep(0.2)

#         # If some frames remain unacknowledged
#         if base < window_end:
#             print("\nTIMEOUT!")
#             print(f"Going back to Frame {base}")
#             print("Retransmitting outstanding frames...\n")

#         time.sleep(0.3)

#     print("\nAll frames transmitted successfully!")

import random
import time


TOTAL_FRAMES = 10
WINDOW_SIZE = 4
PROB = .2

def go_back_n():
    base = 0
    expected = 0
    
    while(base < TOTAL_FRAMES):
        next_seq = base
        window_end = min(base + WINDOW_SIZE,TOTAL_FRAMES)
        
        while(next_seq < window_end):
            
            print(f"SENDING FRAME {next_seq}")
            
            if random.random() < PROB:
                print(f"PACKET {next_seq} LOST")
                
            elif next_seq == expected:
                print(f"RECIEVED PACKET {next_seq}")
                expected += 1
                base = expected
                print(f"ACK FOR PACKET {base}")
            else:
                print(f"PACKET OUT OF ORDER {next_seq}")
                
            next_seq += 1
            time.sleep(0.2)
            
        if base < window_end:
            print("TIMEOUT...")
            print("ACK NOT RECIEVED")
            print(f"STARTING AGAIN FROM {base}")
        
        time.sleep(0.3)
        
    print("ALL PACKETS RECIEVED")
    
go_back_n()