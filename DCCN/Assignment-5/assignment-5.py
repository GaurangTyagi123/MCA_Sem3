
import random

# ============================================================
# CONFIGURATION
# ============================================================

FRAME_LOSS_PROB = 0.7
TOTAL_FRAMES = 100


# ============================================================
# COMMUNICATION CHANNEL
# ============================================================

class Channel:

    def transmit(self, frame_id):
        """
        Simulates transmission of a frame.

        Returns True if transmission succeeds,
        otherwise returns False.
        """

        is_success = random.random() >= FRAME_LOSS_PROB

        if not is_success:
            print(f"{frame_id},", end="")

        return is_success


# ============================================================
# STOP-AND-WAIT PROTOCOL
# ============================================================

def stop_and_wait(ch):

    total_count = 0
    success_count = 0
    failed_count = 0

    print("\nFailed attempts (Frame IDs): ", end="")

    for frame_id in range(1, TOTAL_FRAMES + 1):

        total_count += 1

        if ch.transmit(frame_id):
            success_count += 1
        else:
            failed_count += 1

    print("\n")

    result = {
        "total transmitted": total_count,
        "successful": success_count,
        "failed": failed_count,
        "re-transmitted": 0,
        "loss-rate": (failed_count * 100) / total_count,
        "delivery-rate": (success_count * 100) / total_count
    }

    return result


# ============================================================
# STOP-AND-WAIT ARQ PROTOCOL
# ============================================================

def stop_and_wait_arq(ch):

    total_count = 0
    success_count = 0
    failed_count = 0
    retransmitted = 0

    print("\nFailed attempts (Frame IDs): ", end="")

    for frame_id in range(1, TOTAL_FRAMES + 1):

        while True:

            total_count += 1

            if ch.transmit(frame_id):
                success_count += 1
                break

            else:
                retransmitted += 1

    print("\n")

    result = {
        "total transmitted": total_count,
        "successful": success_count,
        "failed": failed_count,
        "re-transmitted": retransmitted,
        "loss-rate": (retransmitted * 100) / total_count,
        "delivery-rate": (success_count * 100) / total_count
    }

    return result


# ============================================================
# DISPLAY RESULTS
# ============================================================

def display_results(result):

    for key, value in result.items():

        if "rate" in key:
            print(f"{key} : {value:.2f}%")
        else:
            print(f"{key} : {value}")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    ch = Channel()

    print("---------------- Stop and Wait ----------------")

    snw_result = stop_and_wait(ch)
    display_results(snw_result)

    print("\n-------------- Stop and Wait ARQ --------------")

    snw_arq_result = stop_and_wait_arq(ch)
    display_results(snw_arq_result)
