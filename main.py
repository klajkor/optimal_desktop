import time
import win32api
import ctypes


def move_a_bit():
    dif = 20
    exc = False
    while True:
        try:
            pos = win32api.GetCursorPos()
            time.sleep(30)
            cur_pos = win32api.GetCursorPos()

            if pos == cur_pos:
                new_pos = (cur_pos[0] + dif, cur_pos[1] + dif)
                print("Let's move to %s from %s" % (new_pos, pos))
                dif *= -1
                win32api.SetCursorPos(new_pos)
            exc = False
        except Exception as e:
            print("Error:", e.__str__())
            if not exc:
                print("Something bad happened.. But never mind.")
                exc = True


if __name__ == "__main__":
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    input('{Press enter to exit}')
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)

