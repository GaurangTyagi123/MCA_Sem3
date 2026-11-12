# import random
# import time

# TOTAL_FRAMES = 10
# WINDOW_SIZE = 4
# LOSS_PROBABILITY = 0.2


# def selective_repeat():

#     base = 0
#     received = set()

#     print("===== SELECTIVE REPEAT ARQ =====")

#     while base < TOTAL_FRAMES:

#         window_end = min(base + WINDOW_SIZE, TOTAL_FRAMES)

#         # Send only frames that have not been acknowledged
#         for frame in range(base, window_end):

#             if frame in received:
#                 continue

#             print(f"\nSending Frame {frame}")

#             if random.random() < LOSS_PROBABILITY:
#                 print(f"Frame {frame} LOST!")
#                 continue

#             print(f"Receiver accepted Frame {frame}")
#             received.add(frame)

#             print(f"Individual ACK {frame} received")

#             time.sleep(0.2)

#         # Move base over consecutively received frames
#         while base in received:
#             base += 1

#         # Identify missing frames
#         missing = [
#             frame for frame in range(base, window_end)
#             if frame not in received
#         ]

#         if missing:
#             print("\nTIMEOUT!")
#             print(f"Retransmitting only lost frames: {missing}")

#         time.sleep(0.3)

#     print("\nAll frames transmitted successfully!")


import random
import time

TOTAL_FRAMES = 10
LOSS_PROB = 0.2
WINDOW_SIZE = 4

def selective_repeat():
    base = 0
    received = list()
    
    while base < TOTAL_FRAMES:
        window_end = min(base + WINDOW_SIZE,TOTAL_FRAMES)
        for frame in range(base,window_end):
            if frame  in received:
                continue
            
            print(f"SENDING FRAME {frame}")
            if random.random() < LOSS_PROB:
                print(f"LOST FRAME {frame}")
                continue
            print(f"FRAME RECEIVED {frame}")
            received.append(frame)
            
        while base in received:
            base += 1
        
        missing = [
            frame for frame in range(base,window_end) if frame not in received
        ]
        
        if missing:
            print("TIMEOUT")
            print(f"RETRANSMITTING MISSING FRAME : {missing}")
            

selective_repeat()